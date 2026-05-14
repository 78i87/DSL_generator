from __future__ import annotations

import random
from collections import deque
from typing import Any

from reasoning_dsl.core import ProblemSpec, Span, VerificationResult, int_param


class ShortestPathLiteGenerator:
    family = "shortest_path_lite"

    def generate(self, seed: int, difficulty: dict[str, Any]) -> ProblemSpec:
        rng = random.Random(seed)
        path_length = max(1, int_param(rng, difficulty, "path_length", 3))
        extra_edges = max(0, int_param(rng, difficulty, "extra_edges", 3))
        symbol_offset = int_param(rng, difficulty, "symbol_offset", 0)
        num_nodes = max(int_param(rng, difficulty, "num_nodes", path_length + extra_edges + 3), path_length + 2)

        nodes = [f"e{symbol_offset + idx}" for idx in range(num_nodes)]
        start = nodes[0]
        goal = nodes[path_length]
        path_nodes = nodes[: path_length + 1]
        edges = {(path_nodes[idx], path_nodes[idx + 1]) for idx in range(path_length)}

        candidates = [(a, b) for a in nodes for b in nodes if a != b and (a, b) not in edges]
        rng.shuffle(candidates)
        for edge in candidates:
            if len(edges) >= path_length + extra_edges:
                break
            trial = set(edges)
            trial.add(edge)
            if _shortest_path_length(trial, start, goal) == path_length:
                edges = trial

        problem_lines = [*(f"EDGE {a} {b}" for a, b in sorted(edges)), f"QUERY REACH {start} {goal}"]
        canonical_states: list[list[str]] = [[]]
        for idx in range(1, len(path_nodes) + 1):
            canonical_states.append(["PATH " + " ".join(path_nodes[:idx])])

        meta = {
            "requested_difficulty": dict(difficulty),
            "difficulty": {
                "path_length": path_length,
                "num_nodes": num_nodes,
                "extra_edges": len(edges) - path_length,
                "symbol_offset": symbol_offset,
            },
            "solver": {
                "shortest_path_length": _shortest_path_length(edges, start, goal),
                "num_shortest_paths": _num_shortest_paths(edges, start, goal, path_length),
            },
        }
        return ProblemSpec(self.family, problem_lines, canonical_states, meta, _fingerprint(edges, start, goal, path_nodes))

    def verify(self, problem: ProblemSpec, state_lines: list[str]) -> VerificationResult:
        parsed = _parse_problem(problem.problem_lines)
        if len(state_lines) != 1:
            return VerificationResult(False, "BAD_PATH", "Expected one PATH line.", Span(0, 0, 1))
        tokens = state_lines[0].split()
        if len(tokens) < 2 or tokens[0] != "PATH":
            return VerificationResult(False, "BAD_PATH", "Expected PATH followed by nodes.", Span(0, 0, 1))
        path = tokens[1:]
        if path[0] != parsed["start"] or path[-1] != parsed["goal"]:
            return VerificationResult(False, "BAD_PATH", "Path has the wrong endpoints.", Span(0, 1, len(tokens)))
        for idx, pair in enumerate(zip(path, path[1:]), start=1):
            if pair not in parsed["edges"]:
                return VerificationResult(False, "BAD_EDGE", "Missing edge.", Span(0, idx, idx + 2))
        shortest = _shortest_path_length(parsed["edges"], parsed["start"], parsed["goal"])
        if shortest is not None and len(path) - 1 != shortest:
            return VerificationResult(False, "BAD_PATH", "Path is not canonical shortest.", Span(0, 1, len(tokens)))
        return VerificationResult(True, None, "Valid shortest path.", None)

    def corrupt(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        rng = random.Random(seed)
        parsed = _parse_problem(problem.problem_lines)
        nodes = sorted(parsed["nodes"])
        if not state_lines:
            return [f"PATH {parsed['goal']}"]
        tokens = state_lines[0].split()
        if len(tokens) < 3 or tokens[0] != "PATH":
            return [f"PATH {parsed['goal']}"]
        path = tokens[1:]
        idx = rng.randrange(1, len(path))
        prev = path[idx - 1]
        replacement = next((node for node in nodes if node != path[idx] and (prev, node) not in parsed["edges"]), parsed["start"])
        path[idx] = replacement
        return ["PATH " + " ".join(path)]

    def corrupt_for_verify(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        return self.corrupt(seed, problem, state_lines)


def _parse_problem(lines: list[str]) -> dict[str, Any]:
    edges: set[tuple[str, str]] = set()
    nodes: set[str] = set()
    start = goal = None
    for line in lines:
        tokens = line.split()
        if len(tokens) == 3 and tokens[0] == "EDGE":
            edges.add((tokens[1], tokens[2]))
            nodes.update(tokens[1:3])
        elif len(tokens) == 4 and tokens[:2] == ["QUERY", "REACH"]:
            start, goal = tokens[2], tokens[3]
            nodes.update([start, goal])
    if start is None or goal is None:
        raise ValueError("Shortest path problem is missing QUERY REACH")
    return {"edges": edges, "nodes": nodes, "start": start, "goal": goal}


def _shortest_path_length(edges: set[tuple[str, str]], start: str, goal: str) -> int | None:
    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        node, dist = queue.popleft()
        if node == goal:
            return dist
        for a, b in edges:
            if a == node and b not in seen:
                seen.add(b)
                queue.append((b, dist + 1))
    return None


def _num_shortest_paths(edges: set[tuple[str, str]], start: str, goal: str, length: int) -> int:
    count = 0
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        if dist > length:
            continue
        if node == goal and dist == length:
            count += 1
            continue
        for a, b in edges:
            if a == node:
                queue.append((b, dist + 1))
    return count


def _fingerprint(edges: set[tuple[str, str]], start: str, goal: str, path_nodes: list[str]) -> str:
    order = {node: idx for idx, node in enumerate(path_nodes)}
    for node in sorted({part for edge in edges for part in edge} | {start, goal}):
        order.setdefault(node, len(order))
    canonical_edges = sorted((order[a], order[b]) for a, b in edges)
    return f"start={order[start]};goal={order[goal]};edges={canonical_edges}"
