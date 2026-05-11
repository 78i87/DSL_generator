from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import numpy as np


SPLITS = ("train", "test", "ood")
REQUIRED_EXAMPLE_FIELDS = {
    "id",
    "split",
    "family",
    "mode",
    "problem_lines",
    "state_lines",
    "target_lines",
    "source_text",
    "target_text",
    "meta",
}
REQUIRED_META_FIELDS = {"fingerprint", "problem_id", "difficulty", "solver", "seed"}


def audit_dataset(data_dir: str | Path) -> dict[str, Any]:
    data_path = Path(data_dir)
    report: dict[str, Any] = {
        "data_dir": str(data_path),
        "status": "pass",
        "errors": [],
        "warnings": [],
        "jsonl": {},
        "trm": {},
    }

    examples_by_split = _audit_jsonl(data_path, report)
    _audit_trm_arrays(data_path, examples_by_split, report)
    if report["errors"]:
        report["status"] = "fail"
    elif report["warnings"]:
        report["status"] = "warn"
    return report


def write_audit_report(report: dict[str, Any], output_dir: str | Path) -> None:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    with open(output / "audit.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, sort_keys=True)
    with open(output / "audit.md", "w", encoding="utf-8") as f:
        f.write(render_markdown_report(report))


def render_markdown_report(report: dict[str, Any]) -> str:
    lines = [
        "# Dataset Audit",
        "",
        f"- Data dir: `{report['data_dir']}`",
        f"- Status: `{report['status']}`",
        f"- Errors: `{len(report['errors'])}`",
        f"- Warnings: `{len(report['warnings'])}`",
        "",
    ]
    if report["errors"]:
        lines.extend(["## Errors", ""])
        lines.extend(f"- {item}" for item in report["errors"])
        lines.append("")
    if report["warnings"]:
        lines.extend(["## Warnings", ""])
        lines.extend(f"- {item}" for item in report["warnings"])
        lines.append("")

    lines.extend(["## JSONL Summary", ""])
    for split, summary in report["jsonl"].get("splits", {}).items():
        lines.extend(
            [
                f"### {split}",
                "",
                f"- Examples: `{summary['examples']}`",
                f"- Problems: `{summary['problems']}`",
                f"- Families: `{summary['families']}`",
                f"- Modes: `{summary['modes']}`",
                f"- Verify targets: `{summary['verify_targets']}`",
                "",
            ]
        )

    lines.extend(["## Difficulty Summary", ""])
    for family, stats in report["jsonl"].get("difficulty", {}).items():
        lines.extend([f"### {family}", ""])
        for key, value in stats.items():
            lines.append(f"- `{key}`: `{value}`")
        lines.append("")

    lines.extend(["## TRM Array Summary", ""])
    for split, summary in report["trm"].get("splits", {}).items():
        lines.extend(
            [
                f"### {split}",
                "",
                f"- Inputs shape: `{summary['inputs_shape']}`",
                f"- Labels shape: `{summary['labels_shape']}`",
                f"- Seq len: `{summary['seq_len']}`",
                f"- Vocab size: `{summary['vocab_size']}`",
                f"- Puzzle identifiers unique: `{summary['puzzle_identifier_values']}`",
                f"- Non-empty target rows: `{summary['non_empty_target_rows']}`",
                "",
            ]
        )

    lines.extend(["## Samples", ""])
    for key, sample in report["jsonl"].get("samples", {}).items():
        lines.extend(
            [
                f"### {key}",
                "",
                f"- ID: `{sample['id']}`",
                "",
                "Source:",
                "",
                "```text",
                sample["source_text"],
                "```",
                "",
                "Target:",
                "",
                "```text",
                sample["target_text"],
                "```",
                "",
            ]
        )

    return "\n".join(lines)


def _audit_jsonl(data_path: Path, report: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    examples_by_split: dict[str, list[dict[str, Any]]] = {}
    all_ids: Counter[str] = Counter()
    problem_fingerprints: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    difficulty_values: dict[str, dict[str, list[Any]]] = defaultdict(lambda: defaultdict(list))
    samples: dict[str, dict[str, str]] = {}

    split_summaries: dict[str, Any] = {}
    for split in SPLITS:
        path = data_path / "jsonl" / f"{split}.jsonl"
        if not path.exists():
            report["errors"].append(f"Missing JSONL file: {path}")
            examples_by_split[split] = []
            continue

        examples: list[dict[str, Any]] = []
        with open(path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                try:
                    example = json.loads(line)
                except json.JSONDecodeError as exc:
                    report["errors"].append(f"{path}:{line_no}: invalid JSON: {exc}")
                    continue
                examples.append(example)
                _check_example_schema(example, path, line_no, report)

        examples_by_split[split] = examples
        families = Counter(str(ex.get("family")) for ex in examples)
        modes = Counter(str(ex.get("mode")) for ex in examples)
        verify_targets = Counter(
            str(ex.get("target_lines", [""])[0])
            for ex in examples
            if ex.get("mode") == "verify" and ex.get("target_lines")
        )
        problem_ids = {str(ex.get("meta", {}).get("problem_id")) for ex in examples}
        split_summaries[split] = {
            "examples": len(examples),
            "problems": len(problem_ids - {"None"}),
            "families": dict(sorted(families.items())),
            "modes": dict(sorted(modes.items())),
            "verify_targets": dict(sorted(verify_targets.items())),
        }

        for example in examples:
            example_id = str(example.get("id"))
            all_ids[example_id] += 1
            family = str(example.get("family"))
            meta = example.get("meta") if isinstance(example.get("meta"), dict) else {}
            fingerprint = meta.get("fingerprint")
            problem_id = meta.get("problem_id")
            if fingerprint and problem_id:
                key = f"{family}:{fingerprint}"
                problem_fingerprints[key][split].add(str(problem_id))
            difficulty = meta.get("difficulty")
            if isinstance(difficulty, dict):
                for key, value in difficulty.items():
                    difficulty_values[family][key].append(value)

            sample_key = f"{split}/{family}/{example.get('mode')}"
            if sample_key not in samples and "source_text" in example and "target_text" in example:
                samples[sample_key] = {
                    "id": str(example.get("id")),
                    "source_text": str(example["source_text"]),
                    "target_text": str(example["target_text"]),
                }

    duplicate_ids = sorted(example_id for example_id, count in all_ids.items() if count > 1)
    if duplicate_ids:
        report["errors"].append(f"Duplicate example IDs: {duplicate_ids[:20]}")

    for fingerprint, split_map in sorted(problem_fingerprints.items()):
        used_splits = [split for split, ids in split_map.items() if ids]
        if len(used_splits) > 1:
            report["errors"].append(f"Cross-split fingerprint leakage for {fingerprint}: {used_splits}")
        for split, ids in split_map.items():
            if len(ids) > 1:
                report["warnings"].append(f"Duplicate fingerprint within {split}: {fingerprint} maps to {sorted(ids)}")

    report["jsonl"]["splits"] = split_summaries
    report["jsonl"]["difficulty"] = _summarize_difficulty(difficulty_values)
    report["jsonl"]["samples"] = dict(sorted(samples.items()))
    return examples_by_split


def _check_example_schema(example: dict[str, Any], path: Path, line_no: int, report: dict[str, Any]) -> None:
    missing = sorted(REQUIRED_EXAMPLE_FIELDS - set(example))
    if missing:
        report["errors"].append(f"{path}:{line_no}: missing example fields {missing}")
    meta = example.get("meta")
    if not isinstance(meta, dict):
        report["errors"].append(f"{path}:{line_no}: meta must be an object")
        return
    missing_meta = sorted(REQUIRED_META_FIELDS - set(meta))
    if missing_meta:
        report["errors"].append(f"{path}:{line_no}: missing meta fields {missing_meta}")


def _summarize_difficulty(values: dict[str, dict[str, list[Any]]]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for family, fields in sorted(values.items()):
        result[family] = {}
        for key, raw_values in sorted(fields.items()):
            if not raw_values:
                continue
            if all(isinstance(v, bool) for v in raw_values):
                result[family][key] = dict(sorted(Counter(raw_values).items()))
            elif all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in raw_values):
                nums = [float(v) for v in raw_values]
                result[family][key] = {
                    "min": min(nums),
                    "max": max(nums),
                    "mean": sum(nums) / len(nums),
                    "unique": sorted(set(raw_values)),
                }
            else:
                result[family][key] = dict(sorted(Counter(str(v) for v in raw_values).items()))
    return result


def _audit_trm_arrays(data_path: Path, examples_by_split: dict[str, list[dict[str, Any]]], report: dict[str, Any]) -> None:
    identifiers_path = data_path / "identifiers.json"
    vocab_path = data_path / "vocab.json"
    identifiers: list[str] | None = None
    vocab: dict[str, int] | None = None
    if not identifiers_path.exists():
        report["errors"].append(f"Missing identifiers file: {identifiers_path}")
    else:
        identifiers = json.loads(identifiers_path.read_text(encoding="utf-8"))
        if identifiers != ["<blank>"]:
            report["errors"].append(f"Expected identifiers.json to be ['<blank>'], got {identifiers}")

    if not vocab_path.exists():
        report["errors"].append(f"Missing vocab file: {vocab_path}")
    else:
        vocab = json.loads(vocab_path.read_text(encoding="utf-8"))

    split_summaries: dict[str, Any] = {}
    for split in SPLITS:
        split_dir = data_path / split
        metadata_path = split_dir / "dataset.json"
        if not metadata_path.exists():
            report["errors"].append(f"Missing metadata file: {metadata_path}")
            continue

        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        arrays = _load_arrays(split_dir, report)
        if arrays is None:
            continue

        inputs, labels, puzzle_identifiers, puzzle_indices, group_indices = arrays
        expected_examples = len(examples_by_split.get(split, []))
        _check_array_metadata(split, metadata, inputs, labels, puzzle_identifiers, puzzle_indices, group_indices, expected_examples, report)
        if vocab is not None and inputs.ndim == 2 and labels.ndim == 2 and inputs.shape == labels.shape:
            _check_token_contract(split, metadata, inputs, labels, vocab, report)

        split_summaries[split] = {
            "inputs_shape": list(inputs.shape),
            "labels_shape": list(labels.shape),
            "seq_len": metadata.get("seq_len"),
            "vocab_size": metadata.get("vocab_size"),
            "puzzle_identifier_values": sorted(set(puzzle_identifiers.tolist())),
            "non_empty_target_rows": int(np.sum(np.any(labels != 0, axis=1))),
        }

    report["trm"]["identifiers"] = identifiers
    report["trm"]["splits"] = split_summaries


def _load_arrays(split_dir: Path, report: dict[str, Any]) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray] | None:
    arrays = []
    for name in ["inputs", "labels", "puzzle_identifiers", "puzzle_indices", "group_indices"]:
        path = split_dir / f"all__{name}.npy"
        if not path.exists():
            report["errors"].append(f"Missing array file: {path}")
            return None
        arrays.append(np.load(path))
    return tuple(arrays)  # type: ignore[return-value]


def _check_array_metadata(
    split: str,
    metadata: dict[str, Any],
    inputs: np.ndarray,
    labels: np.ndarray,
    puzzle_identifiers: np.ndarray,
    puzzle_indices: np.ndarray,
    group_indices: np.ndarray,
    expected_examples: int,
    report: dict[str, Any],
) -> None:
    prefix = f"{split}:"
    if inputs.shape != labels.shape:
        report["errors"].append(f"{prefix} input/label shape mismatch: {inputs.shape} vs {labels.shape}")
    if inputs.ndim != 2:
        report["errors"].append(f"{prefix} inputs must be 2D, got shape {inputs.shape}")
        return
    if inputs.shape[0] != expected_examples:
        report["errors"].append(f"{prefix} array rows {inputs.shape[0]} != JSONL examples {expected_examples}")
    if inputs.shape[1] != metadata.get("seq_len"):
        report["errors"].append(f"{prefix} seq_len metadata mismatch: {metadata.get('seq_len')} vs {inputs.shape[1]}")
    if metadata.get("vocab_size") is None:
        report["errors"].append(f"{prefix} missing vocab_size")
    else:
        vocab_size = int(metadata["vocab_size"])
        if inputs.size and (inputs.min() < 0 or inputs.max() >= vocab_size):
            report["errors"].append(f"{prefix} inputs contain IDs outside [0, {vocab_size})")
        if labels.size and (labels.min() < 0 or labels.max() >= vocab_size):
            report["errors"].append(f"{prefix} labels contain IDs outside [0, {vocab_size})")
    if metadata.get("num_puzzle_identifiers") != 1:
        report["errors"].append(f"{prefix} num_puzzle_identifiers must be 1, got {metadata.get('num_puzzle_identifiers')}")
    if puzzle_identifiers.shape != (inputs.shape[0],):
        report["errors"].append(f"{prefix} puzzle_identifiers shape mismatch: {puzzle_identifiers.shape}")
    elif np.any(puzzle_identifiers != 0):
        report["errors"].append(f"{prefix} puzzle_identifiers must all be zero")
    expected_indices = np.arange(inputs.shape[0] + 1, dtype=puzzle_indices.dtype)
    if puzzle_indices.shape != (inputs.shape[0] + 1,) or not np.array_equal(puzzle_indices, expected_indices):
        report["errors"].append(f"{prefix} every example must be its own puzzle index")
    expected_groups = np.arange(inputs.shape[0] + 1, dtype=group_indices.dtype)
    if group_indices.shape != (inputs.shape[0] + 1,) or not np.array_equal(group_indices, expected_groups):
        report["errors"].append(f"{prefix} every example must be its own group")
    if metadata.get("total_groups") != inputs.shape[0]:
        report["errors"].append(f"{prefix} total_groups must equal number of examples")
    if metadata.get("total_puzzles") != inputs.shape[0]:
        report["errors"].append(f"{prefix} total_puzzles must equal number of examples")


def _check_token_contract(
    split: str,
    metadata: dict[str, Any],
    inputs: np.ndarray,
    labels: np.ndarray,
    vocab: dict[str, int],
    report: dict[str, Any],
) -> None:
    sep_id = vocab.get("<SEP>")
    blank_id = vocab.get("<BLANK>")
    if sep_id is None or blank_id is None:
        report["errors"].append("Vocab must contain <SEP> and <BLANK>")
        return

    empty_rows = np.where(~np.any(labels != 0, axis=1))[0]
    if empty_rows.size:
        report["errors"].append(f"{split}: labels contain all-empty target rows, first rows {empty_rows[:20].tolist()}")

    for row_idx in range(inputs.shape[0]):
        sep_positions = np.where(inputs[row_idx] == sep_id)[0]
        if sep_positions.size == 0:
            report["errors"].append(f"{split}: row {row_idx} has no <SEP> token")
            continue
        sep_pos = int(sep_positions[0])
        if np.any(labels[row_idx, : sep_pos + 1] != 0):
            report["errors"].append(f"{split}: row {row_idx} has non-ignored labels before target region")
            continue
        supervised = np.where(labels[row_idx] != 0)[0]
        if supervised.size and np.any(inputs[row_idx, supervised] != blank_id):
            report["errors"].append(f"{split}: row {row_idx} supervised positions must use <BLANK> inputs")
            continue
