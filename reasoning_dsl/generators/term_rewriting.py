from __future__ import annotations

import random
import re
from dataclasses import dataclass
from typing import Any

from reasoning_dsl.core import ProblemSpec, Span, VerificationResult, int_param


@dataclass(frozen=True)
class Term:
    kind: str
    symbol: str
    left: "Term | None" = None
    right: "Term | None" = None


@dataclass(frozen=True)
class RewriteRule:
    name: str
    lhs: Term
    rhs: Term


Path = tuple[str, ...]


class TermRewritingGenerator:
    family = "term_rewriting"

    def generate(self, seed: int, difficulty: dict[str, Any]) -> ProblemSpec:
        rng = random.Random(seed)
        rewrite_steps = max(1, int_param(rng, difficulty, "rewrite_steps", 3))
        requested_depth = max(1, int_param(rng, difficulty, "term_depth", 3))
        distractor_rules = int_param(rng, difficulty, "distractor_rules", 2)
        symbol_offset = int_param(rng, difficulty, "symbol_offset", 0)
        variable_rule_rate = float(difficulty.get("variable_rule_rate", 0.4))
        binary_rule_rate = float(difficulty.get("binary_rule_rate", 0.35))
        repeated_subterm_rate = float(difficulty.get("repeated_subterm_rate", 0.2))
        normal_form_rate = float(difficulty.get("normal_form_rate", 0.25))

        query_kind = "normal_form" if rng.random() < normal_form_rate else "goal"
        repeated_subterms = query_kind == "goal" and rng.random() < repeated_subterm_rate

        payload_depth = max(0, min(2, requested_depth - 2))
        payload = _payload_term(rng, symbol_offset, payload_depth)
        side = Term("const", f"e{symbol_offset + 1}")
        stage_kinds = [
            "B" if rng.random() < binary_rule_rate else "U"
            for _ in range(rewrite_steps + 1)
        ]
        if rewrite_steps >= 2 and binary_rule_rate > 0 and "B" not in stage_kinds:
            stage_kinds[rng.randrange(len(stage_kinds))] = "B"

        stage_terms = [
            _stage_term(stage_kinds[idx], symbol_offset + idx, payload, side)
            for idx in range(rewrite_steps + 1)
        ]
        context, action_path = _build_context(
            rng,
            stage_terms[0],
            requested_depth,
            symbol_offset,
            repeated_subterms,
            binary_rule_rate,
        )
        trace_terms = [context(term) for term in stage_terms]

        rules: list[RewriteRule] = []
        variable_rules = 0
        for idx in range(rewrite_steps):
            lhs = stage_terms[idx]
            rhs = stage_terms[idx + 1]
            if stage_kinds[idx] == stage_kinds[idx + 1] and rng.random() < variable_rule_rate:
                lhs, rhs = _schematic_rule_terms(stage_kinds[idx], lhs.symbol, rhs.symbol)
                variable_rules += 1
            rules.append(RewriteRule(f"r{symbol_offset + idx}", lhs, rhs))

        for idx in range(distractor_rules):
            rules.append(_distractor_rule(symbol_offset, rewrite_steps, idx, rng))

        problem_lines = [
            *(f"RULE {rule.name} : {_format_term(rule.lhs)} -> {_format_term(rule.rhs)}" for rule in rules),
            f"START {_format_term(trace_terms[0])}",
        ]
        if query_kind == "normal_form":
            problem_lines.append("QUERY NORMAL_FORM")
        else:
            problem_lines.append(f"GOAL {_format_term(trace_terms[-1])}")

        canonical_states: list[list[str]] = []
        state = [f"TERM {_format_term(trace_terms[0])}"]
        canonical_states.append(list(state))
        action_path_text = _format_path(action_path)
        for idx, term in enumerate(trace_terms[1:]):
            state.extend([f"RW {rules[idx].name} AT {action_path_text}", f"TERM {_format_term(term)}"])
            canonical_states.append(list(state))
        if query_kind == "normal_form":
            state.append("HALT")
            canonical_states.append(list(state))

        parsed = _parse_problem(problem_lines)
        final_term = _last_term(canonical_states[-1])
        meta = {
            "requested_difficulty": dict(difficulty),
            "difficulty": {
                "rewrite_steps": rewrite_steps,
                "term_depth": _term_depth(trace_terms[0]),
                "distractor_rules": distractor_rules,
                "symbol_offset": symbol_offset,
                "variable_rules": variable_rules,
                "binary_rules": sum(1 for rule in rules[:rewrite_steps] if rule.lhs.kind == "B" or rule.rhs.kind == "B"),
                "repeated_subterms": repeated_subterms,
                "query_kind": query_kind,
            },
            "solver": {
                "trace_steps": rewrite_steps,
                "action_path": action_path_text,
                "num_rules": len(rules),
                "initial_applicable_actions": len(_applicable_actions(parsed["rules"], trace_terms[0])),
                "final_applicable_actions": len(_applicable_actions(parsed["rules"], final_term)),
                "max_trace_term_depth": max(_term_depth(term) for term in trace_terms),
            },
        }
        return ProblemSpec(
            self.family,
            problem_lines,
            canonical_states,
            meta,
            _fingerprint(problem_lines, symbol_offset),
        )

    def verify(self, problem: ProblemSpec, state_lines: list[str]) -> VerificationResult:
        parsed = _parse_problem(problem.problem_lines)
        if not state_lines:
            return VerificationResult(False, "MISSING_STEP", "No rewrite trace was provided.", Span(0, 0, 1))

        current_result = _parse_term_line(state_lines[0], 0)
        if isinstance(current_result, VerificationResult):
            return current_result
        current = current_result
        if current != parsed["start"]:
            return VerificationResult(False, "BAD_RESULT", "Trace starts from the wrong term.", Span(0, 1, len(state_lines[0].split())))

        line_idx = 1
        while line_idx < len(state_lines):
            line = state_lines[line_idx]
            if line == "HALT":
                if line_idx != len(state_lines) - 1:
                    return VerificationResult(False, "MALFORMED", "HALT must be the final line.", Span(line_idx, 0, 1))
                if _applicable_actions(parsed["rules"], current):
                    return VerificationResult(False, "BAD_PREMATURE_HALT", "A rewrite still applies.", Span(line_idx, 0, 1))
                if parsed["query_kind"] == "goal" and current != parsed["goal"]:
                    return VerificationResult(False, "BAD_PREMATURE_HALT", "HALT before reaching the goal.", Span(line_idx, 0, 1))
                return VerificationResult(True, None, "Valid rewrite trace.", None)

            action = _parse_action_line(line, line_idx)
            if isinstance(action, VerificationResult):
                return action
            rule_name, path = action
            if line_idx + 1 >= len(state_lines):
                return VerificationResult(False, "MALFORMED", "RW must be followed by a TERM line.", Span(line_idx, 0, len(line.split())))
            if rule_name not in parsed["rules_by_name"]:
                return VerificationResult(False, "BAD_NO_MATCH", "Unknown rewrite rule.", Span(line_idx, 1, 2))

            subterm = _subterm_at(current, path)
            if subterm is None:
                return VerificationResult(False, "BAD_PATH", "Rewrite path does not exist.", Span(line_idx, 3, len(line.split())))

            rule = parsed["rules_by_name"][rule_name]
            bindings: dict[str, Term] = {}
            if not _match(rule.lhs, subterm, bindings):
                return VerificationResult(False, "BAD_NO_MATCH", "Rule lhs does not match the selected subterm.", Span(line_idx, 1, len(line.split())))
            expected = _replace_at(current, path, _substitute(rule.rhs, bindings))

            next_result = _parse_term_line(state_lines[line_idx + 1], line_idx + 1)
            if isinstance(next_result, VerificationResult):
                return next_result
            if next_result != expected:
                return VerificationResult(False, "BAD_RESULT", "TERM does not match the rewrite result.", Span(line_idx + 1, 1, len(state_lines[line_idx + 1].split())))
            current = next_result
            line_idx += 2

        if parsed["query_kind"] == "normal_form":
            return VerificationResult(False, "BAD_PREMATURE_HALT", "Normal-form traces must end with HALT.", Span(len(state_lines) - 1, 0, 1))
        if current != parsed["goal"]:
            return VerificationResult(False, "BAD_NOT_GOAL", "Trace does not reach the goal term.", Span(len(state_lines) - 1, 1, len(state_lines[-1].split())))
        return VerificationResult(True, None, "Valid rewrite trace.", None)

    def corrupt(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        rng = random.Random(seed)
        parsed = _parse_problem(problem.problem_lines)
        term_indexes = [
            idx
            for idx, line in enumerate(state_lines)
            if line.startswith("TERM ") and idx > 0 and state_lines[idx - 1].startswith("RW ")
        ]
        if not term_indexes:
            return ["TERM e999"]
        idx = rng.choice(term_indexes)
        term = _parse_term(state_lines[idx].split()[1:])
        corrupted = list(state_lines)
        corrupted[idx] = f"TERM {_format_term(_mutate_term(term, rng, parsed['symbol_offset']))}"
        return corrupted

    def corrupt_for_verify(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        builders = [
            self._bad_path_state,
            self._bad_no_match_state,
            self._bad_result_state,
            self._bad_premature_halt_state,
            self._bad_not_goal_state,
        ]
        start = seed % len(builders)
        for offset in range(len(builders)):
            candidate = builders[(start + offset) % len(builders)](seed, problem, state_lines)
            if candidate is None:
                continue
            result = self.verify(problem, candidate)
            if not result.valid and result.error_code not in {None, "MALFORMED"}:
                return candidate
        return self.corrupt(seed, problem, state_lines)

    def _bad_path_state(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str] | None:
        for idx, line in enumerate(state_lines):
            if line.startswith("RW "):
                corrupted = list(state_lines)
                tokens = line.split()
                corrupted[idx] = " ".join([tokens[0], tokens[1], "AT", "BAD"])
                return corrupted
        return None

    def _bad_no_match_state(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str] | None:
        parsed = _parse_problem(problem.problem_lines)
        for idx, line in enumerate(state_lines):
            if not line.startswith("RW "):
                continue
            action = _parse_action_line(line, idx)
            if isinstance(action, VerificationResult):
                continue
            _current_rule, path = action
            current = _last_term(state_lines[:idx])
            subterm = _subterm_at(current, path)
            if subterm is None:
                continue
            for rule in parsed["rules"]:
                bindings: dict[str, Term] = {}
                if not _match(rule.lhs, subterm, bindings):
                    corrupted = list(state_lines)
                    corrupted[idx] = f"RW {rule.name} AT {_format_path(path)}"
                    return corrupted
        return None

    def _bad_result_state(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str] | None:
        return self.corrupt(seed, problem, state_lines)

    def _bad_premature_halt_state(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str] | None:
        if len(state_lines) < 3:
            return None
        return [state_lines[0], "HALT"]

    def _bad_not_goal_state(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str] | None:
        parsed = _parse_problem(problem.problem_lines)
        if parsed["query_kind"] != "goal":
            return None
        if len(state_lines) < 3 or not state_lines[-1].startswith("TERM ") or not state_lines[-2].startswith("RW "):
            return None
        candidate = list(state_lines[:-2])
        if _last_term(candidate) == parsed["goal"]:
            return None
        return candidate


def _stage_term(kind: str, symbol_idx: int, payload: Term, side: Term) -> Term:
    if kind == "B":
        return Term("B", f"g{symbol_idx}", payload, side)
    return Term("U", f"f{symbol_idx}", payload)


def _schematic_rule_terms(kind: str, lhs_symbol: str, rhs_symbol: str) -> tuple[Term, Term]:
    if kind == "B":
        return (
            Term("B", lhs_symbol, Term("var", "v0"), Term("var", "v1")),
            Term("B", rhs_symbol, Term("var", "v0"), Term("var", "v1")),
        )
    return (
        Term("U", lhs_symbol, Term("var", "v0")),
        Term("U", rhs_symbol, Term("var", "v0")),
    )


def _payload_term(rng: random.Random, symbol_offset: int, depth: int) -> Term:
    term = Term("const", f"e{symbol_offset}")
    for idx in range(depth):
        if rng.random() < 0.35:
            term = Term("B", f"g{symbol_offset + 30 + idx}", term, Term("const", f"e{symbol_offset + 2 + idx}"))
        else:
            term = Term("U", f"f{symbol_offset + 30 + idx}", term)
    return term


def _build_context(
    rng: random.Random,
    initial_stage: Term,
    requested_depth: int,
    symbol_offset: int,
    repeated_subterms: bool,
    binary_rule_rate: float,
):
    max_context_depth = max(0, requested_depth - _term_depth(initial_stage))
    context_depth = rng.randint(0, max_context_depth) if max_context_depth else 0
    if repeated_subterms and max_context_depth:
        context_depth = max(1, context_depth)

    wrappers: list[tuple[str, str, str | None, Term | None]] = []
    for idx in range(context_depth):
        if repeated_subterms and idx == 0:
            side = rng.choice(["L", "R"])
            wrappers.append(("B", f"g{symbol_offset + 60 + idx}", side, initial_stage))
        elif rng.random() < binary_rule_rate:
            side = rng.choice(["L", "R"])
            other = _payload_term(rng, symbol_offset + 70 + idx, 0)
            wrappers.append(("B", f"g{symbol_offset + 60 + idx}", side, other))
        else:
            wrappers.append(("U", f"f{symbol_offset + 60 + idx}", None, None))

    def apply(term: Term) -> Term:
        result = term
        for kind, symbol, side, other in wrappers:
            if kind == "U":
                result = Term("U", symbol, result)
            elif side == "L":
                result = Term("B", symbol, result, other)
            else:
                result = Term("B", symbol, other, result)
        return result

    path: Path = ()
    for kind, _symbol, side, _other in wrappers:
        if kind == "U":
            path = ("IN", *path)
        elif side == "L":
            path = ("L", *path)
        else:
            path = ("R", *path)
    return apply, path


def _distractor_rule(symbol_offset: int, rewrite_steps: int, idx: int, rng: random.Random) -> RewriteRule:
    name = f"r{symbol_offset + rewrite_steps + idx}"
    if rng.random() < 0.5:
        lhs = Term("U", f"f{symbol_offset + 100 + idx}", Term("var", "v0"))
        rhs = Term("U", f"f{symbol_offset + 120 + idx}", Term("var", "v0"))
    else:
        lhs = Term("B", f"g{symbol_offset + 100 + idx}", Term("var", "v0"), Term("var", "v1"))
        rhs = Term("B", f"g{symbol_offset + 120 + idx}", Term("var", "v0"), Term("var", "v1"))
    return RewriteRule(name, lhs, rhs)


def _parse_problem(lines: list[str]) -> dict[str, Any]:
    rules: list[RewriteRule] = []
    start: Term | None = None
    goal: Term | None = None
    query_kind = "goal"
    symbol_offset = 0
    for line in lines:
        tokens = line.split()
        if len(tokens) >= 6 and tokens[0] == "RULE" and tokens[2] == ":" and "->" in tokens:
            arrow = tokens.index("->")
            rules.append(RewriteRule(tokens[1], _parse_term(tokens[3:arrow]), _parse_term(tokens[arrow + 1 :])))
        elif len(tokens) >= 2 and tokens[0] == "START":
            start = _parse_term(tokens[1:])
            first_symbol = _first_numbered_symbol(start)
            if first_symbol is not None:
                symbol_offset = first_symbol
        elif len(tokens) >= 2 and tokens[0] == "GOAL":
            goal = _parse_term(tokens[1:])
            query_kind = "goal"
        elif tokens == ["QUERY", "NORMAL_FORM"]:
            query_kind = "normal_form"
    if start is None:
        raise ValueError("Term rewriting problem is missing START")
    if query_kind == "goal" and goal is None:
        raise ValueError("Term rewriting problem is missing GOAL")
    return {
        "rules": rules,
        "rules_by_name": {rule.name: rule for rule in rules},
        "start": start,
        "goal": goal,
        "query_kind": query_kind,
        "symbol_offset": symbol_offset,
    }


def _parse_term_line(line: str, line_idx: int) -> Term | VerificationResult:
    tokens = line.split()
    if len(tokens) < 2 or tokens[0] != "TERM":
        return VerificationResult(False, "MALFORMED", "Expected TERM line.", Span(line_idx, 0, len(tokens)))
    try:
        return _parse_term(tokens[1:])
    except ValueError as exc:
        return VerificationResult(False, "MALFORMED", str(exc), Span(line_idx, 1, len(tokens)))


def _parse_action_line(line: str, line_idx: int) -> tuple[str, Path] | VerificationResult:
    tokens = line.split()
    if len(tokens) < 4 or tokens[0] != "RW" or tokens[2] != "AT":
        return VerificationResult(False, "MALFORMED", "Expected RW rN AT PATH.", Span(line_idx, 0, len(tokens)))
    path = _parse_path(tokens[3:])
    if path is None:
        return VerificationResult(False, "BAD_PATH", "Invalid rewrite path.", Span(line_idx, 3, len(tokens)))
    return tokens[1], path


def _parse_term(tokens: list[str]) -> Term:
    term, end = _parse_term_at(tokens, 0)
    if end != len(tokens):
        raise ValueError("Unexpected trailing term tokens.")
    return term


def _parse_term_at(tokens: list[str], idx: int) -> tuple[Term, int]:
    if idx >= len(tokens):
        raise ValueError("Unexpected end of term.")
    token = tokens[idx]
    if token == "U":
        if idx + 1 >= len(tokens):
            raise ValueError("Unary term is missing a function symbol.")
        child, end = _parse_term_at(tokens, idx + 2)
        return Term("U", tokens[idx + 1], child), end
    if token == "B":
        if idx + 1 >= len(tokens):
            raise ValueError("Binary term is missing a function symbol.")
        left, next_idx = _parse_term_at(tokens, idx + 2)
        right, end = _parse_term_at(tokens, next_idx)
        return Term("B", tokens[idx + 1], left, right), end
    if token.startswith("v"):
        return Term("var", token), idx + 1
    if token.startswith("e"):
        return Term("const", token), idx + 1
    raise ValueError(f"Unsupported term token {token!r}.")


def _format_term(term: Term) -> str:
    if term.kind in {"const", "var"}:
        return term.symbol
    if term.kind == "U" and term.left is not None:
        return f"U {term.symbol} {_format_term(term.left)}"
    if term.kind == "B" and term.left is not None and term.right is not None:
        return f"B {term.symbol} {_format_term(term.left)} {_format_term(term.right)}"
    raise ValueError(f"Malformed term: {term}")


def _parse_path(tokens: list[str]) -> Path | None:
    if tokens == ["ROOT"]:
        return ()
    if not tokens or "ROOT" in tokens:
        return None
    path: list[str] = []
    for token in tokens:
        if token not in {"IN", "L", "R"}:
            return None
        path.append(token)
    return tuple(path)


def _format_path(path: Path) -> str:
    return "ROOT" if not path else " ".join(path)


def _subterm_at(term: Term, path: Path) -> Term | None:
    current = term
    for step in path:
        if step == "IN" and current.kind == "U":
            current = current.left
        elif step == "L" and current.kind == "B":
            current = current.left
        elif step == "R" and current.kind == "B":
            current = current.right
        else:
            return None
        if current is None:
            return None
    return current


def _replace_at(term: Term, path: Path, replacement: Term) -> Term:
    if not path:
        return replacement
    head, tail = path[0], path[1:]
    if head == "IN" and term.kind == "U" and term.left is not None:
        return Term("U", term.symbol, _replace_at(term.left, tail, replacement))
    if head == "L" and term.kind == "B" and term.left is not None:
        return Term("B", term.symbol, _replace_at(term.left, tail, replacement), term.right)
    if head == "R" and term.kind == "B" and term.right is not None:
        return Term("B", term.symbol, term.left, _replace_at(term.right, tail, replacement))
    raise ValueError("Cannot replace an invalid path.")


def _all_paths(term: Term) -> list[Path]:
    paths: list[Path] = [()]
    if term.kind == "U" and term.left is not None:
        paths.extend(("IN", *path) for path in _all_paths(term.left))
    elif term.kind == "B" and term.left is not None and term.right is not None:
        paths.extend(("L", *path) for path in _all_paths(term.left))
        paths.extend(("R", *path) for path in _all_paths(term.right))
    return paths


def _match(pattern: Term, term: Term, bindings: dict[str, Term]) -> bool:
    if pattern.kind == "var":
        existing = bindings.get(pattern.symbol)
        if existing is None:
            bindings[pattern.symbol] = term
            return True
        return existing == term
    if pattern.kind != term.kind or pattern.symbol != term.symbol:
        return False
    if pattern.kind in {"const"}:
        return True
    if pattern.kind == "U" and pattern.left is not None and term.left is not None:
        return _match(pattern.left, term.left, bindings)
    if pattern.kind == "B" and pattern.left is not None and pattern.right is not None and term.left is not None and term.right is not None:
        return _match(pattern.left, term.left, bindings) and _match(pattern.right, term.right, bindings)
    return False


def _substitute(term: Term, bindings: dict[str, Term]) -> Term:
    if term.kind == "var":
        if term.symbol not in bindings:
            raise ValueError(f"Unbound variable {term.symbol}")
        return bindings[term.symbol]
    if term.kind == "U" and term.left is not None:
        return Term("U", term.symbol, _substitute(term.left, bindings))
    if term.kind == "B" and term.left is not None and term.right is not None:
        return Term("B", term.symbol, _substitute(term.left, bindings), _substitute(term.right, bindings))
    return term


def _applicable_actions(rules: list[RewriteRule], term: Term) -> list[tuple[str, Path]]:
    actions: list[tuple[str, Path]] = []
    for path in _all_paths(term):
        subterm = _subterm_at(term, path)
        if subterm is None:
            continue
        for rule in rules:
            if _match(rule.lhs, subterm, {}):
                actions.append((rule.name, path))
    return actions


def _last_term(state_lines: list[str]) -> Term:
    for line in reversed(state_lines):
        if line.startswith("TERM "):
            return _parse_term(line.split()[1:])
    raise ValueError("State has no TERM line")


def _term_depth(term: Term) -> int:
    if term.kind in {"const", "var"}:
        return 0
    if term.kind == "U" and term.left is not None:
        return 1 + _term_depth(term.left)
    if term.kind == "B" and term.left is not None and term.right is not None:
        return 1 + max(_term_depth(term.left), _term_depth(term.right))
    raise ValueError(f"Malformed term: {term}")


def _mutate_term(term: Term, rng: random.Random, symbol_offset: int) -> Term:
    paths = _all_paths(term)
    rng.shuffle(paths)
    for path in paths:
        subterm = _subterm_at(term, path)
        if subterm is None:
            continue
        replacement: Term | None = None
        if subterm.kind == "const":
            replacement = Term("const", _next_symbol(subterm.symbol, symbol_offset))
        elif subterm.kind == "U" and subterm.left is not None:
            replacement = Term("U", _next_symbol(subterm.symbol, symbol_offset), subterm.left)
        elif subterm.kind == "B" and subterm.left is not None and subterm.right is not None:
            replacement = Term("B", _next_symbol(subterm.symbol, symbol_offset), subterm.left, subterm.right)
        if replacement is not None and replacement != subterm:
            return _replace_at(term, path, replacement)
    return Term("U", f"f{symbol_offset + 999}", term)


def _next_symbol(symbol: str, symbol_offset: int) -> str:
    match = re.fullmatch(r"([efg])(\d+)", symbol)
    if match is None:
        return f"e{symbol_offset + 999}"
    prefix, raw_number = match.groups()
    return f"{prefix}{int(raw_number) + 1}"


def _first_numbered_symbol(term: Term) -> int | None:
    match = re.fullmatch(r"[efgr](\d+)", term.symbol)
    if match is not None:
        return int(match.group(1))
    for child in (term.left, term.right):
        if child is None:
            continue
        found = _first_numbered_symbol(child)
        if found is not None:
            return found
    return None


def _fingerprint(problem_lines: list[str], symbol_offset: int) -> str:
    return "\n".join(_normalize_symbols(line, symbol_offset) for line in problem_lines)


def _normalize_symbols(text: str, symbol_offset: int) -> str:
    def replace(match: re.Match[str]) -> str:
        prefix, raw_number = match.groups()
        if prefix == "v":
            return match.group(0)
        return f"{prefix}{int(raw_number) - symbol_offset}"

    return re.sub(r"\b([efgrv])(\d+)\b", replace, text)
