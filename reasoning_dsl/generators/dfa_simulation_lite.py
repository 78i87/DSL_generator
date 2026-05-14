from __future__ import annotations

import random
from typing import Any

from reasoning_dsl.core import ProblemSpec, Span, VerificationResult, int_param


class DfaSimulationLiteGenerator:
    family = "dfa_simulation_lite"

    def generate(self, seed: int, difficulty: dict[str, Any]) -> ProblemSpec:
        rng = random.Random(seed)
        input_length = max(1, int_param(rng, difficulty, "input_length", 3))
        relation_count = max(2, int_param(rng, difficulty, "relation_count", 3))
        distractor_facts = max(0, int_param(rng, difficulty, "distractor_facts", 3))
        symbol_offset = int_param(rng, difficulty, "symbol_offset", 0)
        num_states = max(int_param(rng, difficulty, "num_states", input_length + distractor_facts + 2), input_length + 1)

        states = [f"e{symbol_offset + idx}" for idx in range(num_states)]
        relations = [f"r{idx}" for idx in range(relation_count)]
        path = states[: input_length + 1]
        input_rels = [relations[(seed + idx) % relation_count] for idx in range(input_length)]
        facts = {(input_rels[idx], path[idx], path[idx + 1]) for idx in range(input_length)}

        candidates = [(rel, a, b) for rel in relations for a in states for b in states if a != b and (rel, a, b) not in facts]
        rng.shuffle(candidates)
        for fact in candidates[:distractor_facts]:
            facts.add(fact)

        problem_lines = [
            *(f"FACT {rel} {a} {b}" for rel, a, b in sorted(facts)),
            *(f"HYP h{idx} : {rel}" for idx, rel in enumerate(input_rels)),
            f"START {path[0]}",
            f"GOAL {path[-1]}",
        ]
        canonical_states: list[list[str]] = [[]]
        for idx in range(1, len(path) + 1):
            canonical_states.append(["PATH " + " ".join(path[:idx])])

        meta = {
            "requested_difficulty": dict(difficulty),
            "difficulty": {
                "input_length": input_length,
                "relation_count": relation_count,
                "distractor_facts": len(facts) - input_length,
                "num_states": num_states,
                "symbol_offset": symbol_offset,
            },
            "solver": {"trace_steps": input_length, "num_facts": len(facts)},
        }
        return ProblemSpec(self.family, problem_lines, canonical_states, meta, _fingerprint(facts, input_rels, path))

    def verify(self, problem: ProblemSpec, state_lines: list[str]) -> VerificationResult:
        parsed = _parse_problem(problem.problem_lines)
        if len(state_lines) != 1:
            return VerificationResult(False, "BAD_PATH", "Expected one PATH line.", Span(0, 0, 1))
        tokens = state_lines[0].split()
        if len(tokens) < 2 or tokens[0] != "PATH":
            return VerificationResult(False, "BAD_PATH", "Expected PATH followed by states.", Span(0, 0, 1))
        path = tokens[1:]
        if path[0] != parsed["start"]:
            return VerificationResult(False, "BAD_PATH", "Path starts at the wrong state.", Span(0, 1, 2))
        if len(path) != len(parsed["input_rels"]) + 1:
            return VerificationResult(False, "BAD_PATH", "Path length does not match HYP input.", Span(0, 1, len(tokens)))
        if path[-1] != parsed["goal"]:
            return VerificationResult(False, "BAD_PATH", "Path ends at the wrong state.", Span(0, len(tokens) - 1, len(tokens)))
        for idx, rel in enumerate(parsed["input_rels"]):
            if (rel, path[idx], path[idx + 1]) not in parsed["facts"]:
                return VerificationResult(False, "BAD_FACT", "Transition fact is missing.", Span(0, idx + 1, idx + 3))
        return VerificationResult(True, None, "Valid transition trace.", None)

    def corrupt(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        rng = random.Random(seed)
        parsed = _parse_problem(problem.problem_lines)
        states = sorted(parsed["states"])
        if not state_lines:
            return [f"PATH {parsed['goal']}"]
        tokens = state_lines[0].split()
        if len(tokens) < 3 or tokens[0] != "PATH":
            return [f"PATH {parsed['goal']}"]
        path = tokens[1:]
        idx = rng.randrange(1, len(path))
        rel = parsed["input_rels"][idx - 1] if idx - 1 < len(parsed["input_rels"]) else parsed["input_rels"][-1]
        prev = path[idx - 1]
        replacement = next((node for node in states if node != path[idx] and (rel, prev, node) not in parsed["facts"]), parsed["start"])
        path[idx] = replacement
        return ["PATH " + " ".join(path)]

    def corrupt_for_verify(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        return self.corrupt(seed, problem, state_lines)


def _parse_problem(lines: list[str]) -> dict[str, Any]:
    facts: set[tuple[str, str, str]] = set()
    states: set[str] = set()
    input_rels_by_index: dict[int, str] = {}
    start = goal = None
    for line in lines:
        tokens = line.split()
        if len(tokens) == 4 and tokens[0] == "FACT":
            facts.add((tokens[1], tokens[2], tokens[3]))
            states.update(tokens[2:4])
        elif len(tokens) == 4 and tokens[0] == "HYP" and tokens[2] == ":":
            index = int(tokens[1][1:]) if tokens[1].startswith("h") and tokens[1][1:].isdigit() else len(input_rels_by_index)
            input_rels_by_index[index] = tokens[3]
        elif len(tokens) == 2 and tokens[0] == "START":
            start = tokens[1]
            states.add(start)
        elif len(tokens) == 2 and tokens[0] == "GOAL":
            goal = tokens[1]
            states.add(goal)
    if start is None or goal is None or not input_rels_by_index:
        raise ValueError("DFA-lite problem is missing START, GOAL, or HYP input")
    input_rels = [input_rels_by_index[idx] for idx in sorted(input_rels_by_index)]
    return {"facts": facts, "states": states, "input_rels": input_rels, "start": start, "goal": goal}


def _fingerprint(facts: set[tuple[str, str, str]], input_rels: list[str], path: list[str]) -> str:
    state_order = {node: idx for idx, node in enumerate(path)}
    for _, a, b in sorted(facts):
        state_order.setdefault(a, len(state_order))
        state_order.setdefault(b, len(state_order))
    rel_order: dict[str, int] = {}
    for rel in input_rels:
        rel_order.setdefault(rel, len(rel_order))
    for rel, _, _ in sorted(facts):
        rel_order.setdefault(rel, len(rel_order))
    canonical_facts = sorted((rel_order[rel], state_order[a], state_order[b]) for rel, a, b in facts)
    canonical_input = [rel_order[rel] for rel in input_rels]
    canonical_path = [state_order[node] for node in path]
    return f"input={canonical_input};path={canonical_path};facts={canonical_facts}"
