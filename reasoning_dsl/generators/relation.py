from __future__ import annotations

import random
from typing import Any

from reasoning_dsl.core import ProblemSpec, Span, VerificationResult, int_param


class RelationCompositionGenerator:
    family = "relation_composition"

    def generate(self, seed: int, difficulty: dict[str, Any]) -> ProblemSpec:
        rng = random.Random(seed)
        composition_depth = max(int_param(rng, difficulty, "composition_depth", 2), 2)
        num_entities = max(int_param(rng, difficulty, "num_entities", composition_depth + 2), composition_depth + 1)
        distractor_facts = int_param(rng, difficulty, "distractor_facts", 2)
        symbol_offset = int_param(rng, difficulty, "symbol_offset", 0)

        entities = [f"e{symbol_offset + i}" for i in range(num_entities)]

        def rel(idx: int) -> str:
            return f"r{symbol_offset + idx}"

        lines: list[str] = []
        for idx in range(composition_depth):
            lines.append(f"FACT {rel(idx)} {entities[idx]} {entities[idx + 1]}")

        rule_lines = []
        derived_rel = composition_depth
        rule_lines.append(f"RULE {rel(derived_rel)} = {rel(0)} ; {rel(1)}")
        for idx in range(2, composition_depth):
            rule_lines.append(f"RULE {rel(derived_rel + 1)} = {rel(derived_rel)} ; {rel(idx)}")
            derived_rel += 1
        lines.extend(rule_lines)

        fact_candidates = set()
        max_base_rel = composition_depth - 1
        while len(fact_candidates) < distractor_facts:
            rel_idx = rng.randrange(max_base_rel + 1)
            a = rng.randrange(num_entities)
            b = rng.randrange(num_entities)
            if a == b or (a == rel_idx and b == rel_idx + 1):
                continue
            fact_candidates.add((rel_idx, a, b))
        for rel_idx, a, b in sorted(fact_candidates):
            lines.append(f"FACT {rel(rel_idx)} e{symbol_offset + a} e{symbol_offset + b}")

        query_rel = derived_rel
        lines.append(f"QUERY {rel(query_rel)} {entities[0]} {entities[composition_depth]}")

        proof_lines: list[str] = []
        canonical_states = [[]]
        if composition_depth == 2:
            proof_lines.append(f"DERIVE {rel(query_rel)} {entities[0]} {entities[2]} VIA {entities[1]}")
            canonical_states.append(list(proof_lines))
        else:
            current_rel = composition_depth
            proof_lines.append(f"DERIVE {rel(current_rel)} {entities[0]} {entities[2]} VIA {entities[1]}")
            canonical_states.append(list(proof_lines))
            for idx in range(2, composition_depth):
                current_rel += 1
                proof_lines.append(f"DERIVE {rel(current_rel)} {entities[0]} {entities[idx + 1]} VIA {entities[idx]}")
                canonical_states.append(list(proof_lines))

        parsed = _parse_problem(lines)
        meta = {
            "requested_difficulty": dict(difficulty),
            "difficulty": {
                "composition_depth": composition_depth,
                "num_entities": num_entities,
                "distractor_facts": distractor_facts,
                "symbol_offset": symbol_offset,
            },
            "solver": {
                "derivation_depth": len(canonical_states) - 1,
                "num_candidate_bindings": _candidate_bindings(parsed),
                "num_valid_derivations": 1,
            },
        }
        return ProblemSpec(self.family, lines, canonical_states, meta, _fingerprint(parsed, composition_depth, symbol_offset))

    def verify(self, problem: ProblemSpec, state_lines: list[str]) -> VerificationResult:
        parsed = _parse_problem(problem.problem_lines)
        available = set(parsed["facts"])
        if not state_lines:
            return VerificationResult(False, "MISSING_STEP", "No derivation lines were provided.", Span(0, 0, 1))
        for line_idx, line in enumerate(state_lines):
            tokens = line.split()
            if len(tokens) != 6 or tokens[0] != "DERIVE" or tokens[4] != "VIA":
                return VerificationResult(False, "MALFORMED", "Expected DERIVE rX eA eB VIA eM.", Span(line_idx, 0, len(tokens)))
            rel, a, b, mid = tokens[1], tokens[2], tokens[3], tokens[5]
            if rel not in parsed["rules"]:
                return VerificationResult(False, "BAD_RULE", "No composition rule defines this relation.", Span(line_idx, 1, 2))
            left, right = parsed["rules"][rel]
            if (left, a, mid) not in available:
                return VerificationResult(False, "BAD_FACT", "Left side of composition is unavailable.", Span(line_idx, 2, 6))
            if (right, mid, b) not in available:
                return VerificationResult(False, "BAD_BINDING", "Right side of composition does not match VIA binding.", Span(line_idx, 3, 6))
            available.add((rel, a, b))
        if parsed["query"] not in available:
            return VerificationResult(False, "BAD_QUERY", "The requested relation was not derived.", Span(len(state_lines) - 1, 0, 1))
        return VerificationResult(True, None, "Valid relation derivation.", None)

    def corrupt(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        rng = random.Random(seed)
        parsed = _parse_problem(problem.problem_lines)
        entities = sorted(parsed["entities"])
        if not state_lines:
            rel, a, b = parsed["query"]
            return [f"DERIVE {rel} {a} {b} VIA e999"]
        corrupted = list(state_lines)
        line_idx = rng.randrange(len(corrupted))
        tokens = corrupted[line_idx].split()
        if len(tokens) != 6:
            return ["BROKEN"]
        current = tokens[5]
        tokens[5] = next((entity for entity in entities if entity != current), "e999")
        corrupted[line_idx] = " ".join(tokens)
        return corrupted


def _parse_problem(lines: list[str]) -> dict[str, Any]:
    facts: set[tuple[str, str, str]] = set()
    rules: dict[str, tuple[str, str]] = {}
    entities: set[str] = set()
    relations: set[str] = set()
    query = None
    for line in lines:
        tokens = line.split()
        if len(tokens) == 4 and tokens[0] == "FACT":
            facts.add((tokens[1], tokens[2], tokens[3]))
            relations.add(tokens[1])
            entities.update(tokens[2:4])
        elif len(tokens) == 6 and tokens[0] == "RULE" and tokens[2] == "=" and tokens[4] == ";":
            rules[tokens[1]] = (tokens[3], tokens[5])
            relations.update([tokens[1], tokens[3], tokens[5]])
        elif len(tokens) == 4 and tokens[0] == "QUERY":
            query = (tokens[1], tokens[2], tokens[3])
            relations.add(tokens[1])
            entities.update(tokens[2:4])
    if query is None:
        raise ValueError("Relation problem is missing QUERY")
    return {"facts": facts, "rules": rules, "entities": entities, "relations": relations, "query": query}


def _candidate_bindings(parsed: dict[str, Any]) -> int:
    count = 0
    for left, right in parsed["rules"].values():
        left_facts = [fact for fact in parsed["facts"] if fact[0] == left]
        right_facts = [fact for fact in parsed["facts"] if fact[0] == right]
        for _, _, mid_a in left_facts:
            for _, mid_b, _ in right_facts:
                if mid_a == mid_b:
                    count += 1
    return count


def _fingerprint(parsed: dict[str, Any], composition_depth: int, symbol_offset: int) -> str:
    entity_order = {f"e{symbol_offset + i}": i for i in range(composition_depth + 1)}
    for entity in sorted(parsed["entities"]):
        entity_order.setdefault(entity, len(entity_order))
    relation_order = {f"r{symbol_offset + i}": i for i in range(composition_depth)}
    for idx in range(composition_depth, composition_depth * 2 - 1):
        relation_order[f"r{symbol_offset + idx}"] = idx
    for relation in sorted(parsed["relations"]):
        relation_order.setdefault(relation, len(relation_order))
    facts = sorted((relation_order[r], entity_order[a], entity_order[b]) for r, a, b in parsed["facts"])
    rules = sorted((relation_order[r], relation_order[a], relation_order[b]) for r, (a, b) in parsed["rules"].items())
    q = parsed["query"]
    query = (relation_order[q[0]], entity_order[q[1]], entity_order[q[2]])
    return f"facts={facts};rules={rules};query={query}"
