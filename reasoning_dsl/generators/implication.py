from __future__ import annotations

import random
from typing import Any

from reasoning_dsl.core import ProblemSpec, Span, VerificationResult, int_param


class ImplicationChainGenerator:
    family = "implication_chains"

    def generate(self, seed: int, difficulty: dict[str, Any]) -> ProblemSpec:
        rng = random.Random(seed)
        proof_length = int_param(rng, difficulty, "proof_length", 3)
        num_props = max(int_param(rng, difficulty, "num_props", proof_length + 2), proof_length + 1)
        distractor_hyps = int_param(rng, difficulty, "distractor_hyps", 2)
        symbol_offset = int_param(rng, difficulty, "symbol_offset", 0)

        props = [f"p{symbol_offset + i}" for i in range(num_props)]
        lines = [f"HYP h{symbol_offset} : {props[0]}"]
        chain_hyps = [(f"h{symbol_offset}", None, props[0])]
        hyp_idx = 1
        for i in range(proof_length):
            hyp = f"h{symbol_offset + hyp_idx}"
            lines.append(f"HYP {hyp} : {props[i]} -> {props[i + 1]}")
            chain_hyps.append((hyp, props[i], props[i + 1]))
            hyp_idx += 1

        distractors = set()
        while len(distractors) < distractor_hyps:
            src = rng.randrange(num_props)
            dst = rng.randrange(num_props)
            if src == dst or (src < proof_length and dst == src + 1):
                continue
            distractors.add((src, dst))
        for src, dst in sorted(distractors):
            lines.append(f"HYP h{symbol_offset + hyp_idx} : {props[src]} -> {props[dst]}")
            hyp_idx += 1

        goal = props[proof_length]
        lines.append(f"GOAL {goal}")

        canonical_states = [[]]
        proof_lines: list[str] = []
        proof_lines.append(f"DERIVE {props[0]} BY h{symbol_offset}")
        canonical_states.append(list(proof_lines))
        for i in range(1, proof_length + 1):
            proof_lines.append(f"DERIVE {props[i]} BY h{symbol_offset + i} FROM {props[i - 1]}")
            canonical_states.append(list(proof_lines))

        parsed = _parse_problem(lines)
        meta = {
            "requested_difficulty": dict(difficulty),
            "difficulty": {
                "proof_length": proof_length + 1,
                "num_props": num_props,
                "distractor_hyps": distractor_hyps,
                "symbol_offset": symbol_offset,
            },
            "solver": {
                "proof_length": proof_length + 1,
                "num_possible_proofs": _count_possible_proofs(parsed),
                "distractor_count": distractor_hyps,
                "max_fan_out": _max_fan_out(parsed),
            },
        }
        return ProblemSpec(self.family, lines, canonical_states, meta, _fingerprint(parsed, chain_hyps))

    def verify(self, problem: ProblemSpec, state_lines: list[str]) -> VerificationResult:
        parsed = _parse_problem(problem.problem_lines)
        derived: set[str] = set()
        if not state_lines:
            return VerificationResult(False, "MISSING_STEP", "No proof lines were provided.", Span(0, 0, 1))
        for line_idx, line in enumerate(state_lines):
            tokens = line.split()
            if len(tokens) == 4 and tokens[0] == "DERIVE" and tokens[2] == "BY":
                prop, hyp = tokens[1], tokens[3]
                if hyp not in parsed["facts"]:
                    return VerificationResult(False, "UNKNOWN_HYP", f"{hyp} is not a fact hypothesis.", Span(line_idx, 3, 4))
                if parsed["facts"][hyp] != prop:
                    return VerificationResult(False, "BAD_PREMISE", f"{hyp} derives {parsed['facts'][hyp]}, not {prop}.", Span(line_idx, 1, 2))
                derived.add(prop)
            elif len(tokens) == 6 and tokens[0] == "DERIVE" and tokens[2] == "BY" and tokens[4] == "FROM":
                prop, hyp, premise = tokens[1], tokens[3], tokens[5]
                if hyp not in parsed["rules"]:
                    return VerificationResult(False, "UNKNOWN_HYP", f"{hyp} is not an implication hypothesis.", Span(line_idx, 3, 4))
                expected_premise, expected_prop = parsed["rules"][hyp]
                if premise not in derived or premise != expected_premise:
                    return VerificationResult(False, "BAD_PREMISE", "The premise has not been derived for this implication.", Span(line_idx, 5, 6))
                if prop != expected_prop:
                    return VerificationResult(False, "BAD_GOAL", "The implication derives a different proposition.", Span(line_idx, 1, 2))
                derived.add(prop)
            else:
                return VerificationResult(False, "MALFORMED", "Expected DERIVE syntax.", Span(line_idx, 0, len(tokens)))
        if parsed["goal"] not in derived:
            return VerificationResult(False, "MISSING_STEP", "The goal proposition was not derived.", Span(len(state_lines) - 1, 0, 1))
        return VerificationResult(True, None, "Valid proof.", None)

    def corrupt(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        rng = random.Random(seed)
        parsed = _parse_problem(problem.problem_lines)
        props = sorted(parsed["props"])
        if not state_lines:
            return ["DERIVE p999 BY h999"]
        corrupted = list(state_lines)
        line_idx = rng.randrange(len(corrupted))
        tokens = corrupted[line_idx].split()
        if len(tokens) == 4:
            tokens[3] = "h999"
        elif len(tokens) == 6:
            current = tokens[5]
            tokens[5] = next((prop for prop in props if prop != current), "p999")
        else:
            return ["BROKEN"]
        corrupted[line_idx] = " ".join(tokens)
        return corrupted


def _parse_problem(lines: list[str]) -> dict[str, Any]:
    facts: dict[str, str] = {}
    rules: dict[str, tuple[str, str]] = {}
    props: set[str] = set()
    goal = None
    for line in lines:
        tokens = line.split()
        if len(tokens) == 4 and tokens[0] == "HYP" and tokens[2] == ":":
            facts[tokens[1]] = tokens[3]
            props.add(tokens[3])
        elif len(tokens) == 6 and tokens[0] == "HYP" and tokens[2] == ":" and tokens[4] == "->":
            rules[tokens[1]] = (tokens[3], tokens[5])
            props.update([tokens[3], tokens[5]])
        elif len(tokens) == 2 and tokens[0] == "GOAL":
            goal = tokens[1]
            props.add(goal)
    if goal is None:
        raise ValueError("Implication problem is missing GOAL")
    return {"facts": facts, "rules": rules, "props": props, "goal": goal}


def _count_possible_proofs(parsed: dict[str, Any]) -> int:
    derived = set(parsed["facts"].values())
    changed = True
    while changed:
        changed = False
        for premise, conclusion in parsed["rules"].values():
            if premise in derived and conclusion not in derived:
                derived.add(conclusion)
                changed = True
    return int(parsed["goal"] in derived)


def _max_fan_out(parsed: dict[str, Any]) -> int:
    counts: dict[str, int] = {}
    for premise, _ in parsed["rules"].values():
        counts[premise] = counts.get(premise, 0) + 1
    return max(counts.values(), default=0)


def _fingerprint(parsed: dict[str, Any], chain_hyps: list[tuple[str, str | None, str]]) -> str:
    prop_order: dict[str, int] = {}
    for _, premise, conclusion in chain_hyps:
        if premise is not None and premise not in prop_order:
            prop_order[premise] = len(prop_order)
        if conclusion not in prop_order:
            prop_order[conclusion] = len(prop_order)
    for prop in sorted(parsed["props"]):
        prop_order.setdefault(prop, len(prop_order))
    facts = sorted(prop_order[prop] for prop in parsed["facts"].values())
    rules = sorted((prop_order[a], prop_order[b]) for a, b in parsed["rules"].values())
    return f"facts={facts};rules={rules};goal={prop_order[parsed['goal']]}"
