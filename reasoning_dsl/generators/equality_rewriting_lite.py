from __future__ import annotations

import random
from typing import Any

from reasoning_dsl.core import ProblemSpec, Span, VerificationResult, int_param


class EqualityRewritingLiteGenerator:
    family = "equality_rewriting_lite"

    def generate(self, seed: int, difficulty: dict[str, Any]) -> ProblemSpec:
        rng = random.Random(seed)
        rewrite_steps = max(1, int_param(rng, difficulty, "rewrite_steps", 3))
        distractor_rules = max(0, int_param(rng, difficulty, "distractor_rules", 2))
        symbol_offset = int_param(rng, difficulty, "symbol_offset", 0)
        reverse_rule_rate = float(difficulty.get("reverse_rule_rate", 0.5))

        terms = [_term(symbol_offset + idx) for idx in range(rewrite_steps + 1)]
        rules: list[tuple[str, str, str]] = []
        reversed_rules = 0
        for idx in range(rewrite_steps):
            lhs, rhs = terms[idx], terms[idx + 1]
            if rng.random() < reverse_rule_rate:
                lhs, rhs = rhs, lhs
                reversed_rules += 1
            rules.append((f"r{idx}", lhs, rhs))

        for idx in range(distractor_rules):
            base = symbol_offset + rewrite_steps + 1 + idx
            rules.append((f"r{rewrite_steps + idx}", _term(base), _term(base + 1)))

        problem_lines = [
            *(f"RULE {name} : {lhs} -> {rhs}" for name, lhs, rhs in rules),
            f"START {terms[0]}",
            f"GOAL {terms[-1]}",
        ]
        state = [f"TERM {terms[0]}"]
        canonical_states: list[list[str]] = [list(state)]
        for idx, term in enumerate(terms[1:]):
            state.extend([f"RW r{idx} AT ROOT", f"TERM {term}"])
            canonical_states.append(list(state))

        meta = {
            "requested_difficulty": dict(difficulty),
            "difficulty": {
                "rewrite_steps": rewrite_steps,
                "distractor_rules": distractor_rules,
                "symbol_offset": symbol_offset,
                "reversed_rules": reversed_rules,
            },
            "solver": {"trace_steps": rewrite_steps, "num_rules": len(rules)},
        }
        return ProblemSpec(self.family, problem_lines, canonical_states, meta, _fingerprint(rules, terms))

    def verify(self, problem: ProblemSpec, state_lines: list[str]) -> VerificationResult:
        parsed = _parse_problem(problem.problem_lines)
        if not state_lines:
            return VerificationResult(False, "BAD_RESULT", "No equality trace was provided.", Span(0, 0, 1))
        first = _parse_term_line(state_lines[0])
        if first is None:
            return VerificationResult(False, "BAD_RESULT", "Expected TERM line.", Span(0, 0, 1))
        if first != parsed["start"]:
            return VerificationResult(False, "BAD_RESULT", "Trace starts from the wrong term.", Span(0, 1, len(state_lines[0].split())))

        current = first
        idx = 1
        while idx < len(state_lines):
            if state_lines[idx] == "HALT":
                if idx != len(state_lines) - 1:
                    return VerificationResult(False, "BAD_RESULT", "HALT must be final.", Span(idx, 0, 1))
                return VerificationResult(True) if current == parsed["goal"] else VerificationResult(False, "BAD_NOT_GOAL")
            action = state_lines[idx].split()
            if len(action) != 4 or action[0] != "RW" or action[2] != "AT" or action[3] != "ROOT":
                return VerificationResult(False, "BAD_PATH", "Expected root rewrite.", Span(idx, 0, len(action)))
            if idx + 1 >= len(state_lines):
                return VerificationResult(False, "BAD_RESULT", "RW must be followed by TERM.", Span(idx, 0, len(action)))
            rule = parsed["rules"].get(action[1])
            if rule is None:
                return VerificationResult(False, "BAD_NO_MATCH", "Unknown rule.", Span(idx, 1, 2))
            expected = _apply_rule_text(current, rule)
            if expected is None:
                return VerificationResult(False, "BAD_NO_MATCH", "Rule does not match current term.", Span(idx, 1, len(action)))
            next_term = _parse_term_line(state_lines[idx + 1])
            if next_term != expected:
                return VerificationResult(False, "BAD_RESULT", "TERM does not match rewrite result.", Span(idx + 1, 1, len(state_lines[idx + 1].split())))
            current = next_term
            idx += 2

        if current != parsed["goal"]:
            return VerificationResult(False, "BAD_NOT_GOAL", "Trace does not reach the goal.", Span(len(state_lines) - 1, 1, len(state_lines[-1].split())))
        return VerificationResult(True)

    def corrupt(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        rng = random.Random(seed)
        term_indexes = [idx for idx, line in enumerate(state_lines) if idx > 0 and line.startswith("TERM ")]
        if not term_indexes:
            return ["TERM U f13 e0"]
        corrupted = list(state_lines)
        idx = rng.choice(term_indexes)
        replacement = "TERM U f13 e0"
        if corrupted[idx] == replacement:
            replacement = "TERM U f12 e0"
        corrupted[idx] = replacement
        return corrupted

    def corrupt_for_verify(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        return self.corrupt(seed, problem, state_lines)


def _term(index: int) -> str:
    return f"U f{index} e0"


def _parse_problem(lines: list[str]) -> dict[str, Any]:
    rules: dict[str, tuple[str, str]] = {}
    start = goal = None
    for line in lines:
        tokens = line.split()
        if len(tokens) >= 6 and tokens[0] == "RULE" and tokens[2] == ":" and "->" in tokens:
            arrow = tokens.index("->")
            rules[tokens[1]] = (" ".join(tokens[3:arrow]), " ".join(tokens[arrow + 1 :]))
        elif len(tokens) >= 2 and tokens[0] == "START":
            start = " ".join(tokens[1:])
        elif len(tokens) >= 2 and tokens[0] == "GOAL":
            goal = " ".join(tokens[1:])
    if start is None or goal is None:
        raise ValueError("Equality rewrite problem is missing START or GOAL")
    return {"rules": rules, "start": start, "goal": goal}


def _parse_term_line(line: str) -> str | None:
    tokens = line.split()
    if len(tokens) < 2 or tokens[0] != "TERM":
        return None
    return " ".join(tokens[1:])


def _apply_rule_text(current: str, rule: tuple[str, str]) -> str | None:
    lhs, rhs = rule
    if current == lhs:
        return rhs
    if current == rhs:
        return lhs
    return None


def _fingerprint(rules: list[tuple[str, str, str]], terms: list[str]) -> str:
    term_order = {term: idx for idx, term in enumerate(terms)}
    for _, lhs, rhs in rules:
        term_order.setdefault(lhs, len(term_order))
        term_order.setdefault(rhs, len(term_order))
    canonical_rules = [(idx, term_order[lhs], term_order[rhs]) for idx, (_name, lhs, rhs) in enumerate(rules)]
    return f"terms={[term_order[term] for term in terms]};rules={canonical_rules}"
