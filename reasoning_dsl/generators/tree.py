from __future__ import annotations

import random
from collections import Counter, deque
from typing import Any

from reasoning_dsl.core import ProblemSpec, Span, VerificationResult, int_param


class TreeAncestryGenerator:
    family = "tree_ancestry"

    def generate(self, seed: int, difficulty: dict[str, Any]) -> ProblemSpec:
        rng = random.Random(seed)
        depth = int_param(rng, difficulty, "depth", 3)
        branching_factor = max(1, int_param(rng, difficulty, "branching_factor", 2))
        distractor_subtrees = int_param(rng, difficulty, "distractor_subtrees", 2)
        symbol_offset = int_param(rng, difficulty, "symbol_offset", 0)

        nodes = [f"e{symbol_offset + idx}" for idx in range(depth + 1 + distractor_subtrees)]
        lineage = nodes[: depth + 1]
        edges = {(lineage[idx], lineage[idx + 1]) for idx in range(depth)}
        child_counts = Counter(parent for parent, _child in edges)

        next_node_idx = depth + 1
        while next_node_idx < len(nodes):
            candidates = [node for node in nodes[:next_node_idx] if child_counts[node] < branching_factor]
            parent = rng.choice(candidates or nodes[:next_node_idx])
            child = nodes[next_node_idx]
            edges.add((parent, child))
            child_counts[parent] += 1
            next_node_idx += 1

        root = lineage[0]
        target = lineage[-1]
        problem_lines = [*(f"PARENT {parent} {child}" for parent, child in sorted(edges)), f"QUERY ANCESTOR {root} {target}"]
        canonical_states = [[]]
        for idx in range(1, len(lineage) + 1):
            canonical_states.append(["LINEAGE " + " ".join(lineage[:idx])])

        meta = {
            "requested_difficulty": dict(difficulty),
            "difficulty": {
                "depth": depth,
                "branching_factor": branching_factor,
                "distractor_subtrees": distractor_subtrees,
                "symbol_offset": symbol_offset,
            },
            "solver": {
                "target_depth": depth,
                "total_nodes": len({node for edge in edges for node in edge}),
                "distractor_count": distractor_subtrees,
                "branching_factor": branching_factor,
                "unique_path_length": len(_path_to_target(edges, root, target) or []) - 1,
            },
        }
        fingerprint = _tree_fingerprint(edges, root, target, lineage)
        return ProblemSpec(self.family, problem_lines, canonical_states, meta, fingerprint)

    def verify(self, problem: ProblemSpec, state_lines: list[str]) -> VerificationResult:
        parsed = _parse_problem(problem.problem_lines)
        if len(state_lines) != 1:
            return VerificationResult(False, "MALFORMED", "Expected one LINEAGE line.", Span(0, 0, 1))
        tokens = state_lines[0].split()
        if len(tokens) < 2 or tokens[0] != "LINEAGE":
            return VerificationResult(False, "MALFORMED", "Expected LINEAGE followed by nodes.", Span(0, 0, 1))
        lineage = tokens[1:]
        if lineage[0] != parsed["root"]:
            return VerificationResult(False, "BAD_LINEAGE_START", "Lineage starts at the wrong root.", Span(0, 1, 2))
        if lineage[-1] != parsed["target"]:
            return VerificationResult(False, "BAD_LINEAGE_END", "Lineage ends at the wrong target.", Span(0, len(tokens) - 1, len(tokens)))
        seen: set[str] = set()
        for idx, node in enumerate(lineage, start=1):
            if node in seen:
                return VerificationResult(False, "REPEATED_NODE", "Lineage repeats a node.", Span(0, idx, idx + 1))
            seen.add(node)
        for idx, pair in enumerate(zip(lineage, lineage[1:]), start=1):
            if pair not in parsed["edges"]:
                return VerificationResult(False, "BAD_PARENT", f"Missing parent edge {pair[0]} -> {pair[1]}.", Span(0, idx, idx + 2))
        return VerificationResult(True, None, "Valid ancestry lineage.", None)

    def corrupt(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        rng = random.Random(seed)
        parsed = _parse_problem(problem.problem_lines)
        nodes = sorted(parsed["nodes"])
        if not state_lines:
            return [f"LINEAGE {parsed['target']}"]
        tokens = state_lines[0].split()
        if len(tokens) < 2 or tokens[0] != "LINEAGE":
            return [f"LINEAGE {parsed['target']}"]
        lineage = tokens[1:]
        if len(lineage) == 1:
            return [f"LINEAGE {parsed['target']}"]
        idx = rng.randrange(1, len(lineage))
        prev = lineage[idx - 1]
        replacement = next((node for node in nodes if (prev, node) not in parsed["edges"] and node != lineage[idx]), parsed["root"])
        lineage[idx] = replacement
        return ["LINEAGE " + " ".join(lineage)]

    def corrupt_for_verify(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        rng = random.Random(seed)
        parsed = _parse_problem(problem.problem_lines)
        nodes = sorted(parsed["nodes"])
        if not state_lines:
            return self.corrupt(seed, problem, state_lines)
        tokens = state_lines[0].split()
        if len(tokens) < 4 or tokens[0] != "LINEAGE":
            return self.corrupt(seed, problem, state_lines)

        lineage = tokens[1:]
        candidates = list(range(1, len(lineage) - 1))
        rng.shuffle(candidates)
        for idx in candidates:
            prev = lineage[idx - 1]
            replacement = next(
                (
                    node
                    for node in nodes
                    if node not in lineage and (prev, node) not in parsed["edges"]
                ),
                None,
            )
            if replacement is not None:
                corrupted = list(lineage)
                corrupted[idx] = replacement
                return ["LINEAGE " + " ".join(corrupted)]

        return self.corrupt(seed, problem, state_lines)


def _parse_problem(lines: list[str]) -> dict[str, Any]:
    edges: set[tuple[str, str]] = set()
    nodes: set[str] = set()
    root = target = None
    for line in lines:
        tokens = line.split()
        if tokens[:1] == ["PARENT"] and len(tokens) == 3:
            edges.add((tokens[1], tokens[2]))
            nodes.update(tokens[1:3])
        elif tokens[:2] == ["QUERY", "ANCESTOR"] and len(tokens) == 4:
            root, target = tokens[2], tokens[3]
            nodes.update([root, target])
    if root is None or target is None:
        raise ValueError("Tree problem is missing QUERY ANCESTOR")
    return {"edges": edges, "nodes": nodes, "root": root, "target": target}


def _path_to_target(edges: set[tuple[str, str]], root: str, target: str) -> list[str] | None:
    queue = deque([(root, [root])])
    seen = {root}
    while queue:
        node, path = queue.popleft()
        if node == target:
            return path
        for parent, child in edges:
            if parent == node and child not in seen:
                seen.add(child)
                queue.append((child, [*path, child]))
    return None


def _tree_fingerprint(edges: set[tuple[str, str]], root: str, target: str, lineage: list[str]) -> str:
    order = {node: idx for idx, node in enumerate(lineage)}
    next_idx = len(order)
    for node in sorted({node for edge in edges for node in edge} | {root, target}):
        if node not in order:
            order[node] = next_idx
            next_idx += 1
    canonical_edges = sorted((order[parent], order[child]) for parent, child in edges)
    return f"root={order[root]};target={order[target]};edges={canonical_edges}"
