from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Literal, Protocol


SplitName = Literal["train", "test", "ood"]
ModeName = Literal["improve", "repair", "complete", "action", "repair_action", "verify"]


@dataclass(frozen=True)
class Span:
    line: int
    token_start: int
    token_end: int


@dataclass(frozen=True)
class VerificationResult:
    valid: bool
    error_code: str | None = None
    message: str = ""
    error_span: Span | None = None

    def target_lines(self) -> list[str]:
        if self.valid:
            return ["VALID"]
        return [f"INVALID {self.error_code or 'UNKNOWN'}"]


@dataclass(frozen=True)
class ProblemSpec:
    family: str
    problem_lines: list[str]
    canonical_states: list[list[str]]
    meta: dict[str, Any]
    fingerprint: str

    @property
    def final_state(self) -> list[str]:
        return self.canonical_states[-1]


@dataclass(frozen=True)
class Example:
    id: str
    split: str
    family: str
    mode: str
    problem_lines: list[str]
    state_lines: list[str]
    target_lines: list[str]
    meta: dict[str, Any]

    def source_lines(self) -> list[str]:
        lines = [f"MODE {self.mode}", "PROBLEM", *self.problem_lines, "STATE"]
        lines.extend(self.state_lines if self.state_lines else ["EMPTY"])
        return lines

    def source_text(self) -> str:
        return "\n".join(self.source_lines())

    def target_text(self) -> str:
        return "\n".join(self.target_lines)

    def to_json(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "split": self.split,
            "family": self.family,
            "mode": self.mode,
            "problem_lines": self.problem_lines,
            "state_lines": self.state_lines,
            "target_lines": self.target_lines,
            "source_text": self.source_text(),
            "target_text": self.target_text(),
            "meta": self.meta,
        }


class Generator(Protocol):
    family: str

    def generate(self, seed: int, difficulty: dict[str, Any]) -> ProblemSpec:
        ...

    def verify(self, problem: ProblemSpec, state_lines: list[str]) -> VerificationResult:
        ...

    def corrupt(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        ...


def int_param(rng, config: dict[str, Any], name: str, default: int) -> int:
    if name in config:
        return int(config[name])
    lo_key = f"{name}_min"
    hi_key = f"{name}_max"
    if lo_key in config or hi_key in config:
        lo = int(config.get(lo_key, default))
        hi = int(config.get(hi_key, lo))
        if hi < lo:
            raise ValueError(f"{hi_key} must be >= {lo_key}")
        return rng.randint(lo, hi)
    return default


def build_examples_for_problem(
    *,
    generator: Generator,
    problem: ProblemSpec,
    split: str,
    problem_index: int,
    seed: int,
    modes: list[str],
    relation_action_format: str = "follow",
    tree_repair_action_format: str = "index",
    repair_action_format: str = "index",
    verify_corruption_strategy: str = "default",
) -> list[Example]:
    examples: list[Example] = []
    states = problem.canonical_states
    group_id = f"{split}:{generator.family}:{problem_index}"
    base_meta = {
        "seed": seed,
        "split": split,
        "family": generator.family,
        "problem_id": group_id,
        "fingerprint": problem.fingerprint,
        **problem.meta,
    }

    def add(mode: str, suffix: str, state: list[str], target: list[str], extra: dict[str, Any] | None = None) -> None:
        examples.append(
            Example(
                id=f"{group_id}:{mode}:{suffix}",
                split=split,
                family=generator.family,
                mode=mode,
                problem_lines=problem.problem_lines,
                state_lines=state,
                target_lines=target,
                meta={**base_meta, "mode": mode, **(extra or {})},
            )
        )

    if "improve" in modes:
        for step in range(len(states) - 1):
            add("improve", str(step), states[step], states[step + 1], {"step": step, "target_step": step + 1})

    if "complete" in modes:
        for step in range(len(states) - 1):
            add("complete", str(step), states[step], problem.final_state, {"step": step, "target_step": len(states) - 1})

    if "action" in modes:
        for step in range(len(states) - 1):
            add(
                "action",
                str(step),
                states[step],
                _action_target_lines(
                    generator.family,
                    problem.problem_lines,
                    states[step],
                    states[step + 1],
                    relation_action_format=relation_action_format,
                ),
                {
                    "step": step,
                    "target_step": step + 1,
                    "next_state_lines": states[step + 1],
                    "final_state_lines": problem.final_state,
                },
            )

    if "repair" in modes:
        for step in range(1, len(states)):
            corrupted = generator.corrupt(seed + 7919 + step, problem, states[step])
            add("repair", str(step), corrupted, states[step], {"step": step, "target_step": step})

    if "repair_action" in modes:
        for step in range(1, len(states)):
            corrupted = generator.corrupt(seed + 7919 + step, problem, states[step])
            add(
                "repair_action",
                str(step),
                corrupted,
                _repair_action_target_lines(
                    generator.family,
                    corrupted,
                    states[step],
                    repair_action_format=repair_action_format,
                    tree_repair_action_format=tree_repair_action_format,
                ),
                {
                    "step": step,
                    "target_step": step,
                    "repaired_state_lines": states[step],
                },
            )

    if "verify" in modes:
        valid = generator.verify(problem, problem.final_state)
        add("verify", "valid", problem.final_state, valid.target_lines(), {"verification": asdict(valid)})
        corrupted = _verify_corruption(
            generator,
            seed + 104729,
            problem,
            problem.final_state,
            verify_corruption_strategy,
        )
        invalid = generator.verify(problem, corrupted)
        add("verify", "invalid", corrupted, invalid.target_lines(), {"verification": asdict(invalid)})

    return examples


def _verify_corruption(
    generator: Generator,
    seed: int,
    problem: ProblemSpec,
    state_lines: list[str],
    strategy: str,
) -> list[str]:
    if strategy == "default":
        return generator.corrupt(seed, problem, state_lines)
    if strategy != "single_error":
        raise ValueError(f"Unsupported verify_corruption_strategy: {strategy}")
    single_error_corrupt = getattr(generator, "corrupt_for_verify", None)
    if single_error_corrupt is None:
        return generator.corrupt(seed, problem, state_lines)
    return single_error_corrupt(seed, problem, state_lines)


def _action_target_lines(
    family: str,
    problem_lines: list[str],
    current: list[str],
    next_state: list[str],
    *,
    relation_action_format: str = "follow",
) -> list[str]:
    if family == "graph_reachability":
        current_nodes = _graph_state_nodes(current)
        next_nodes = _graph_state_nodes(next_state)
        if len(next_nodes) != len(current_nodes) + 1 or next_nodes[: len(current_nodes)] != current_nodes:
            raise ValueError("Graph action target requires a one-node path extension")
        return [f"APPEND {next_nodes[-1]}"]

    if family == "tree_ancestry":
        current_nodes = _lineage_state_nodes(current)
        next_nodes = _lineage_state_nodes(next_state)
        if len(next_nodes) != len(current_nodes) + 1 or next_nodes[: len(current_nodes)] != current_nodes:
            raise ValueError("Tree action target requires a one-node lineage extension")
        return [f"DESCEND {next_nodes[-1]}"]

    if family == "term_rewriting":
        if len(next_state) == len(current) + 1 and next_state[: len(current)] == current and next_state[-1] == "HALT":
            return ["HALT"]
        if len(next_state) == len(current) + 2 and next_state[: len(current)] == current:
            action_line = next_state[-2]
            term_line = next_state[-1]
            if action_line.startswith("RW ") and term_line.startswith("TERM "):
                return [action_line]
        raise ValueError("Term rewriting action target requires one rewrite transition or HALT")

    if len(next_state) != len(current) + 1 or next_state[: len(current)] != current:
        raise ValueError(f"{family} action target requires one appended derivation line")
    next_line = next_state[-1]
    tokens = next_line.split()

    if family == "implication_chains":
        if not ((len(tokens) == 4 or len(tokens) == 6) and tokens[0] == "DERIVE" and tokens[2] == "BY"):
            raise ValueError("Implication action target requires a derivation line")
        return [f"APPLY {tokens[3]}"]

    if family == "relation_composition":
        if len(tokens) != 6 or tokens[0] != "DERIVE" or tokens[4] != "VIA":
            raise ValueError("Relation action target requires a derivation line")
        rules = _relation_rules(problem_lines)
        rel, left_entity, right_entity, via = tokens[1], tokens[2], tokens[3], tokens[5]
        if rel not in rules:
            raise ValueError(f"Relation action target has unknown derived relation: {rel}")
        left_rel, right_rel = rules[rel]
        if relation_action_format == "compose":
            return [f"COMPOSE {left_rel} {left_entity} {right_rel} {right_entity} VIA {via}"]
        if relation_action_format == "follow_left":
            return [f"FOLLOW {left_entity} {right_entity} VIA {via}"]
        if relation_action_format != "follow":
            raise ValueError(f"Unsupported relation_action_format: {relation_action_format}")
        return [f"FOLLOW {right_entity} VIA {via}"]

    raise ValueError(f"Unsupported action family: {family}")


def _repair_action_target_lines(
    family: str,
    corrupted: list[str],
    target: list[str],
    *,
    repair_action_format: str = "index",
    tree_repair_action_format: str = "index",
) -> list[str]:
    if family == "graph_reachability":
        corrupted_nodes = _graph_state_nodes(corrupted)
        target_nodes = _graph_state_nodes(target)
        if len(corrupted_nodes) != len(target_nodes):
            raise ValueError("Graph repair action requires equal-length paths")
        diffs = [idx for idx, (left, right) in enumerate(zip(corrupted_nodes, target_nodes)) if left != right]
        if len(diffs) != 1:
            raise ValueError("Graph repair action requires exactly one node replacement")
        idx = diffs[0]
        if repair_action_format == "local":
            if idx == 0:
                return [f"REPLACE ROOT WITH {target_nodes[idx]}"]
            return [f"REPLACE AFTER {target_nodes[idx - 1]} WITH {target_nodes[idx]}"]
        if repair_action_format != "index":
            raise ValueError(f"Unsupported repair_action_format: {repair_action_format}")
        return [f"REPLACE NODE {idx} WITH {target_nodes[idx]}"]

    if family == "tree_ancestry":
        corrupted_nodes = _lineage_state_nodes(corrupted)
        target_nodes = _lineage_state_nodes(target)
        if len(corrupted_nodes) != len(target_nodes):
            raise ValueError("Tree repair action requires equal-length lineages")
        diffs = [idx for idx, (left, right) in enumerate(zip(corrupted_nodes, target_nodes)) if left != right]
        if len(diffs) != 1:
            raise ValueError("Tree repair action requires exactly one node replacement")
        idx = diffs[0]
        tree_format = "after" if repair_action_format == "local" else tree_repair_action_format
        if tree_format == "after":
            if idx == 0:
                return [f"REPLACE ROOT WITH {target_nodes[idx]}"]
            return [f"REPLACE AFTER {target_nodes[idx - 1]} WITH {target_nodes[idx]}"]
        if tree_format != "index":
            raise ValueError(f"Unsupported tree_repair_action_format: {tree_format}")
        return [f"REPLACE NODE {idx} WITH {target_nodes[idx]}"]

    if family == "implication_chains":
        if len(corrupted) != len(target):
            raise ValueError("Implication repair action requires equal line counts")
        diffs = [idx for idx, (left, right) in enumerate(zip(corrupted, target)) if left != right]
        if len(diffs) != 1:
            raise ValueError("Implication repair action requires exactly one line replacement")
        idx = diffs[0]
        corrupted_tokens = corrupted[idx].split()
        target_tokens = target[idx].split()
        if len(corrupted_tokens) != len(target_tokens):
            raise ValueError("Implication repair action requires equal token counts")
        token_diffs = [pos for pos, (left, right) in enumerate(zip(corrupted_tokens, target_tokens)) if left != right]
        if len(token_diffs) != 1:
            raise ValueError("Implication repair action requires exactly one token replacement")
        token_idx = token_diffs[0]
        prefix = _line_repair_prefix("implication_chains", target, idx, repair_action_format)
        if token_idx == 3:
            return [f"{prefix} HYP {target_tokens[token_idx]}"]
        if token_idx == 5 and len(target_tokens) == 6 and target_tokens[4] == "FROM":
            return [f"{prefix} FROM {target_tokens[token_idx]}"]
        if token_idx == 1:
            return [f"{prefix} PROP {target_tokens[token_idx]}"]
        raise ValueError("Unsupported implication repair token replacement")

    if family == "relation_composition":
        if len(corrupted) != len(target):
            raise ValueError("Relation repair action requires equal line counts")
        diffs = [idx for idx, (left, right) in enumerate(zip(corrupted, target)) if left != right]
        if len(diffs) != 1:
            raise ValueError("Relation repair action requires exactly one line replacement")
        idx = diffs[0]
        corrupted_tokens = corrupted[idx].split()
        target_tokens = target[idx].split()
        if len(corrupted_tokens) != len(target_tokens):
            raise ValueError("Relation repair action requires equal token counts")
        token_diffs = [pos for pos, (left, right) in enumerate(zip(corrupted_tokens, target_tokens)) if left != right]
        if len(token_diffs) != 1:
            raise ValueError("Relation repair action requires exactly one token replacement")
        token_idx = token_diffs[0]
        token_names = {1: "REL", 2: "LEFT", 3: "RIGHT", 5: "VIA"}
        if token_idx not in token_names:
            raise ValueError("Unsupported relation repair token replacement")
        prefix = _line_repair_prefix("relation_composition", target, idx, repair_action_format)
        return [f"{prefix} {token_names[token_idx]} {target_tokens[token_idx]}"]

    if family == "term_rewriting":
        if len(corrupted) != len(target):
            raise ValueError("Term rewriting repair action requires equal line counts")
        diffs = [idx for idx, (left, right) in enumerate(zip(corrupted, target)) if left != right]
        if len(diffs) != 1:
            raise ValueError("Term rewriting repair action requires exactly one line replacement")
        idx = diffs[0]
        if idx == 0 or not target[idx].startswith("TERM ") or not target[idx - 1].startswith("RW "):
            raise ValueError("Term rewriting repair action requires a corrupted rewrite result")
        return [f"REPAIR {target[idx - 1]}"]

    raise ValueError(f"Unsupported repair action family: {family}")


def _line_repair_prefix(family: str, target: list[str], idx: int, repair_action_format: str) -> str:
    if repair_action_format == "index":
        return f"REPLACE LINE {idx}"
    if repair_action_format != "local":
        raise ValueError(f"Unsupported repair_action_format: {repair_action_format}")
    if idx == 0:
        return "REPLACE FIRST"
    previous_tokens = target[idx - 1].split()
    if family == "implication_chains":
        if len(previous_tokens) < 2 or previous_tokens[0] != "DERIVE":
            raise ValueError("Implication local repair requires previous derivation")
        return f"REPLACE AFTER {previous_tokens[1]}"
    if family == "relation_composition":
        if len(previous_tokens) != 6 or previous_tokens[0] != "DERIVE":
            raise ValueError("Relation local repair requires previous derivation")
        return f"REPLACE AFTER {previous_tokens[3]}"
    raise ValueError(f"Unsupported local line repair family: {family}")


def _graph_state_nodes(state_lines: list[str]) -> list[str]:
    if not state_lines:
        return []
    if len(state_lines) != 1:
        raise ValueError("Graph state must contain one PATH line")
    tokens = state_lines[0].split()
    if len(tokens) < 2 or tokens[0] != "PATH":
        raise ValueError("Graph state must be a PATH line")
    return tokens[1:]


def _lineage_state_nodes(state_lines: list[str]) -> list[str]:
    if not state_lines:
        return []
    if len(state_lines) != 1:
        raise ValueError("Tree state must contain one LINEAGE line")
    tokens = state_lines[0].split()
    if len(tokens) < 2 or tokens[0] != "LINEAGE":
        raise ValueError("Tree state must be a LINEAGE line")
    return tokens[1:]


def _relation_rules(problem_lines: list[str]) -> dict[str, tuple[str, str]]:
    rules: dict[str, tuple[str, str]] = {}
    for line in problem_lines:
        tokens = line.split()
        if len(tokens) == 6 and tokens[0] == "RULE" and tokens[2] == "=" and tokens[4] == ";":
            rules[tokens[1]] = (tokens[3], tokens[5])
    return rules
