from __future__ import annotations

import random
from collections import deque
from typing import Any

from reasoning_dsl.core import ProblemSpec, Span, VerificationResult, int_param


class GraphReachabilityGenerator:
    family = "graph_reachability"

    def generate(self, seed: int, difficulty: dict[str, Any]) -> ProblemSpec:
        rng = random.Random(seed)
        path_length = int_param(rng, difficulty, "path_length", 3)
        num_nodes = max(int_param(rng, difficulty, "num_nodes", path_length + 2), path_length + 1)
        extra_edges = int_param(rng, difficulty, "extra_edges", 2)
        symbol_offset = int_param(rng, difficulty, "symbol_offset", 0)
        require_shortest = bool(difficulty.get("require_shortest", True))

        nodes = [f"e{symbol_offset + i}" for i in range(num_nodes)]
        start = nodes[0]
        goal = nodes[path_length]
        path_nodes = nodes[: path_length + 1]
        edges = {(path_nodes[i], path_nodes[i + 1]) for i in range(path_length)}

        candidates = [(a, b) for a in nodes for b in nodes if a != b and (a, b) not in edges]
        rng.shuffle(candidates)
        for edge in candidates:
            if len(edges) >= path_length + extra_edges:
                break
            trial = set(edges)
            trial.add(edge)
            shortest = _shortest_path_length(trial, start, goal)
            if not require_shortest or shortest == path_length:
                edges = trial

        edge_lines = [f"EDGE {a} {b}" for a, b in sorted(edges)]
        problem_lines = [*edge_lines, f"QUERY REACH {start} {goal}"]
        canonical_states = [[]]
        for idx in range(1, len(path_nodes) + 1):
            canonical_states.append(["PATH " + " ".join(path_nodes[:idx])])

        shortest = _shortest_path_length(edges, start, goal)
        meta = {
            "requested_difficulty": dict(difficulty),
            "difficulty": {
                "num_nodes": num_nodes,
                "path_length": path_length,
                "extra_edges": len(edges) - path_length,
                "symbol_offset": symbol_offset,
                "require_shortest": require_shortest,
            },
            "solver": {
                "shortest_path_length": shortest,
                "reachable_node_count": len(_reachable_nodes(edges, start)),
                "dead_end_count": _dead_end_count(edges, goal),
                "num_shortest_paths": _num_shortest_paths(edges, start, goal, shortest),
            },
        }
        fingerprint = _graph_fingerprint(edges, start, goal, path_nodes, require_shortest)
        return ProblemSpec(self.family, problem_lines, canonical_states, meta, fingerprint)

    def verify(self, problem: ProblemSpec, state_lines: list[str]) -> VerificationResult:
        parsed = _parse_problem(problem.problem_lines)
        if len(state_lines) != 1:
            return VerificationResult(False, "MALFORMED", "Expected one PATH line.", Span(0, 0, 1))
        tokens = state_lines[0].split()
        if len(tokens) < 2 or tokens[0] != "PATH":
            return VerificationResult(False, "MALFORMED", "Expected PATH followed by nodes.", Span(0, 0, 1))
        path = tokens[1:]
        if path[0] != parsed["start"]:
            return VerificationResult(False, "BAD_PATH_START", "Path starts at the wrong node.", Span(0, 1, 2))
        if path[-1] != parsed["goal"]:
            return VerificationResult(False, "BAD_PATH_END", "Path ends at the wrong node.", Span(0, len(tokens) - 1, len(tokens)))
        edges = parsed["edges"]
        for idx, pair in enumerate(zip(path, path[1:]), start=1):
            if pair not in edges:
                return VerificationResult(False, "BAD_EDGE", f"Missing edge {pair[0]} -> {pair[1]}.", Span(0, idx, idx + 2))
        shortest = _shortest_path_length(edges, parsed["start"], parsed["goal"])
        if shortest is not None and len(path) - 1 != shortest:
            return VerificationResult(False, "NOT_SHORTEST", "Path is valid but not shortest.", Span(0, 1, len(tokens)))
        return VerificationResult(True, None, "Valid shortest path.", None)

    def corrupt(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        rng = random.Random(seed)
        parsed = _parse_problem(problem.problem_lines)
        nodes = sorted(parsed["nodes"])
        if not state_lines:
            return [f"PATH {parsed['goal']}"]
        tokens = state_lines[0].split()
        if len(tokens) < 2:
            return [f"PATH {parsed['goal']}"]
        path = tokens[1:]
        if len(path) == 1:
            return [f"PATH {parsed['goal']}"]
        idx = rng.randrange(1, len(path))
        prev = path[idx - 1]
        replacement = next((node for node in nodes if (prev, node) not in parsed["edges"] and node != path[idx]), parsed["start"])
        path[idx] = replacement
        return ["PATH " + " ".join(path)]

    def corrupt_for_verify(self, seed: int, problem: ProblemSpec, state_lines: list[str]) -> list[str]:
        rng = random.Random(seed)
        parsed = _parse_problem(problem.problem_lines)
        nodes = sorted(parsed["nodes"])
        if not state_lines:
            return self.corrupt(seed, problem, state_lines)
        tokens = state_lines[0].split()
        if len(tokens) < 4 or tokens[0] != "PATH":
            return self.corrupt(seed, problem, state_lines)

        path = tokens[1:]
        candidates = list(range(1, len(path) - 1))
        rng.shuffle(candidates)
        for idx in candidates:
            prev = path[idx - 1]
            replacement = next(
                (
                    node
                    for node in nodes
                    if node not in path and (prev, node) not in parsed["edges"]
                ),
                None,
            )
            if replacement is not None:
                corrupted = list(path)
                corrupted[idx] = replacement
                return ["PATH " + " ".join(corrupted)]

        return self.corrupt(seed, problem, state_lines)


def _parse_problem(lines: list[str]) -> dict[str, Any]:
    edges: set[tuple[str, str]] = set()
    nodes: set[str] = set()
    start = goal = None
    for line in lines:
        tokens = line.split()
        if tokens[:1] == ["EDGE"] and len(tokens) == 3:
            edges.add((tokens[1], tokens[2]))
            nodes.update(tokens[1:3])
        elif tokens[:2] == ["QUERY", "REACH"] and len(tokens) == 4:
            start, goal = tokens[2], tokens[3]
            nodes.update([start, goal])
    if start is None or goal is None:
        raise ValueError("Graph problem is missing QUERY REACH")
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


def _reachable_nodes(edges: set[tuple[str, str]], start: str) -> set[str]:
    queue = deque([start])
    seen = {start}
    while queue:
        node = queue.popleft()
        for a, b in edges:
            if a == node and b not in seen:
                seen.add(b)
                queue.append(b)
    return seen


def _dead_end_count(edges: set[tuple[str, str]], goal: str) -> int:
    sources = {a for a, _ in edges}
    targets = {b for _, b in edges}
    return len([node for node in targets | sources if node != goal and node not in sources])


def _num_shortest_paths(edges: set[tuple[str, str]], start: str, goal: str, shortest: int | None) -> int:
    if shortest is None:
        return 0
    count = 0
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        if dist > shortest:
            continue
        if node == goal and dist == shortest:
            count += 1
            continue
        for a, b in edges:
            if a == node:
                queue.append((b, dist + 1))
    return count


def _graph_fingerprint(
    edges: set[tuple[str, str]],
    start: str,
    goal: str,
    path_nodes: list[str],
    require_shortest: bool,
) -> str:
    order = {node: idx for idx, node in enumerate(path_nodes)}
    next_idx = len(order)
    for node in sorted({n for edge in edges for n in edge} | {start, goal}):
        if node not in order:
            order[node] = next_idx
            next_idx += 1
    canonical_edges = sorted((order[a], order[b]) for a, b in edges)
    return f"start={order[start]};goal={order[goal]};shortest={require_shortest};edges={canonical_edges}"
