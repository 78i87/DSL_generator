from __future__ import annotations

import json
import random
import re
from pathlib import Path
from typing import Any

from reasoning_dsl.core import Example


SYMBOL_RE = re.compile(r"\b([ephrfgv]\d+)\b")
PREFIX_RE = re.compile(r"^([ephrfgv])\d+$")


def alpha_rename_dataset(data_dir: str | Path, *, seed: int) -> dict[str, list[Example]]:
    """Return a symbol-renamed copy of an existing generated JSONL dataset."""
    examples_by_split = _load_examples(data_dir)
    rows_by_problem: dict[str, list[Example]] = {}
    for examples in examples_by_split.values():
        for example in examples:
            problem_id = str(example.meta.get("problem_id", example.id))
            rows_by_problem.setdefault(problem_id, []).append(example)

    maps_by_problem = {
        problem_id: _symbol_map(rows, seed=seed, problem_id=problem_id)
        for problem_id, rows in rows_by_problem.items()
    }

    renamed: dict[str, list[Example]] = {}
    for split, examples in examples_by_split.items():
        renamed[split] = []
        for example in examples:
            problem_id = str(example.meta.get("problem_id", example.id))
            symbol_map = maps_by_problem[problem_id]
            renamed[split].append(_rename_example(example, symbol_map, seed))
    return renamed


def alpha_augment_train_split(data_dir: str | Path, *, seed: int, copies: int) -> dict[str, list[Example]]:
    if copies < 1:
        raise ValueError("copies must be >= 1")
    examples_by_split = _load_examples(data_dir)
    augmented = {split: list(examples) for split, examples in examples_by_split.items()}
    for copy_idx in range(copies):
        renamed = alpha_rename_dataset(data_dir, seed=seed + copy_idx)
        augmented["train"].extend(_copy_with_augmented_ids(example, copy_idx) for example in renamed.get("train", []))
    return augmented


def canonicalize_dataset(data_dir: str | Path, *, token_to_id: dict[str, int] | None = None) -> dict[str, list[Example]]:
    examples_by_split = _load_examples(data_dir)
    rows_by_problem: dict[str, list[Example]] = {}
    for examples in examples_by_split.values():
        for example in examples:
            problem_id = str(example.meta.get("problem_id", example.id))
            rows_by_problem.setdefault(problem_id, []).append(example)

    maps_by_problem = {
        problem_id: _canonical_symbol_map(rows, token_to_id=token_to_id)
        for problem_id, rows in rows_by_problem.items()
    }

    canonicalized: dict[str, list[Example]] = {}
    for split, examples in examples_by_split.items():
        canonicalized[split] = []
        for example in examples:
            problem_id = str(example.meta.get("problem_id", example.id))
            symbol_map = maps_by_problem[problem_id]
            renamed = _rename_example(example, symbol_map, seed=0)
            meta = dict(renamed.meta)
            meta.pop("alpha_renamed", None)
            meta.pop("alpha_rename_seed", None)
            meta.pop("alpha_symbol_map", None)
            meta["canonicalized_symbols"] = True
            meta["canonical_symbol_map"] = symbol_map
            canonicalized[split].append(
                    Example(
                        id=renamed.id,
                        split=renamed.split,
                        family=renamed.family,
                        mode=renamed.mode,
                        problem_lines=renamed.problem_lines,
                        state_lines=renamed.state_lines,
                        target_lines=renamed.target_lines,
                        meta=meta,
                        task_lines=renamed.task_lines,
                    )
                )
    return canonicalized


def _load_examples(data_dir: str | Path) -> dict[str, list[Example]]:
    jsonl_dir = Path(data_dir) / "jsonl"
    if not jsonl_dir.exists():
        raise ValueError(f"Missing JSONL directory: {jsonl_dir}")
    examples_by_split: dict[str, list[Example]] = {}
    for path in sorted(jsonl_dir.glob("*.jsonl")):
        split = path.stem
        examples: list[Example] = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                row = json.loads(line)
                examples.append(
                    Example(
                        id=str(row["id"]),
                        split=str(row["split"]),
                        family=str(row["family"]),
                        mode=str(row["mode"]),
                        problem_lines=[str(item) for item in row["problem_lines"]],
                        state_lines=[str(item) for item in row["state_lines"]],
                        target_lines=[str(item) for item in row["target_lines"]],
                        meta=dict(row["meta"]),
                        task_lines=[str(item) for item in row.get("task_lines", [])],
                    )
                )
        examples_by_split[split] = examples
    if not examples_by_split:
        raise ValueError(f"No JSONL files found under {jsonl_dir}")
    return examples_by_split


def _symbol_map(examples: list[Example], *, seed: int, problem_id: str) -> dict[str, str]:
    by_prefix: dict[str, set[str]] = {}
    for example in examples:
        for text in _example_strings(example):
            for symbol in SYMBOL_RE.findall(text):
                prefix_match = PREFIX_RE.fullmatch(symbol)
                if prefix_match:
                    by_prefix.setdefault(prefix_match.group(1), set()).add(symbol)

    rng = random.Random(f"{seed}:{problem_id}")
    symbol_map: dict[str, str] = {}
    for _prefix, values in sorted(by_prefix.items()):
        source = sorted(values, key=_symbol_sort_key)
        target = list(source)
        if len(target) > 1:
            for _attempt in range(8):
                rng.shuffle(target)
                if target != source:
                    break
            if target == source:
                target = [*target[1:], target[0]]
        symbol_map.update(dict(zip(source, target)))
    return symbol_map


def _canonical_symbol_map(examples: list[Example], *, token_to_id: dict[str, int] | None) -> dict[str, str]:
    by_prefix: dict[str, list[str]] = {}
    seen: set[str] = set()

    # Problem text defines the public variable namespace. State/target-only
    # symbols are appended afterward so corrupted examples remain encodable.
    ordered_strings: list[str] = []
    if examples:
        ordered_strings.extend(examples[0].problem_lines)
        ordered_strings.extend(examples[0].task_lines)
    for example in examples:
        ordered_strings.extend(example.task_lines)
        ordered_strings.extend(example.state_lines)
        ordered_strings.extend(example.target_lines)
        ordered_strings.extend(_strings_from_value(example.meta))

    for text in ordered_strings:
        for symbol in SYMBOL_RE.findall(text):
            if symbol in seen:
                continue
            prefix_match = PREFIX_RE.fullmatch(symbol)
            if not prefix_match:
                continue
            seen.add(symbol)
            by_prefix.setdefault(prefix_match.group(1), []).append(symbol)

    symbol_map: dict[str, str] = {}
    for prefix, symbols in by_prefix.items():
        canonical_symbols = _available_canonical_symbols(prefix, len(symbols), token_to_id)
        for idx, symbol in enumerate(symbols):
            symbol_map[symbol] = canonical_symbols[idx]
    return symbol_map


def _available_canonical_symbols(prefix: str, count: int, token_to_id: dict[str, int] | None) -> list[str]:
    if token_to_id is None:
        return [f"{prefix}{idx}" for idx in range(count)]
    values = sorted(
        (token for token in token_to_id if PREFIX_RE.fullmatch(token) and token.startswith(prefix)),
        key=_symbol_sort_key,
    )
    if len(values) < count:
        raise ValueError(f"Fixed vocabulary has only {len(values)} {prefix!r} symbols, need {count}")
    return values[:count]


def _rename_example(example: Example, symbol_map: dict[str, str], seed: int) -> Example:
    meta = _rename_value(example.meta, symbol_map)
    meta["alpha_renamed"] = True
    meta["alpha_rename_seed"] = seed
    meta["alpha_symbol_map"] = symbol_map
    return Example(
        id=example.id,
        split=example.split,
        family=example.family,
        mode=example.mode,
        problem_lines=[_rename_text(line, symbol_map) for line in example.problem_lines],
        state_lines=[_rename_text(line, symbol_map) for line in example.state_lines],
        target_lines=[_rename_text(line, symbol_map) for line in example.target_lines],
        meta=meta,
        task_lines=[_rename_text(line, symbol_map) for line in example.task_lines],
    )


def _copy_with_augmented_ids(example: Example, copy_idx: int) -> Example:
    suffix = f"alpha{copy_idx + 1}"
    meta = dict(example.meta)
    if "problem_id" in meta:
        meta["problem_id"] = f"{meta['problem_id']}:{suffix}"
    meta["alpha_augmentation_copy"] = copy_idx + 1
    return Example(
        id=f"{example.id}:{suffix}",
        split=example.split,
        family=example.family,
        mode=example.mode,
        problem_lines=example.problem_lines,
        state_lines=example.state_lines,
        target_lines=example.target_lines,
        meta=meta,
        task_lines=example.task_lines,
    )


def _example_strings(example: Example) -> list[str]:
    values: list[str] = []
    values.extend(example.problem_lines)
    values.extend(example.task_lines)
    values.extend(example.state_lines)
    values.extend(example.target_lines)
    values.extend(_strings_from_value(example.meta))
    return values


def _strings_from_value(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        output: list[str] = []
        for item in value:
            output.extend(_strings_from_value(item))
        return output
    if isinstance(value, dict):
        output = []
        for item in value.values():
            output.extend(_strings_from_value(item))
        return output
    return []


def _rename_value(value: Any, symbol_map: dict[str, str]) -> Any:
    if isinstance(value, str):
        return _rename_text(value, symbol_map)
    if isinstance(value, list):
        return [_rename_value(item, symbol_map) for item in value]
    if isinstance(value, dict):
        return {key: _rename_value(item, symbol_map) for key, item in value.items()}
    return value


def _rename_text(text: str, symbol_map: dict[str, str]) -> str:
    return SYMBOL_RE.sub(lambda match: symbol_map.get(match.group(1), match.group(1)), text)


def _symbol_sort_key(symbol: str) -> tuple[str, int]:
    prefix = symbol[0]
    try:
        index = int(symbol[1:])
    except ValueError:
        index = -1
    return prefix, index
