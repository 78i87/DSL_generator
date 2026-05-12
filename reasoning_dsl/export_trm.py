from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from reasoning_dsl.core import Example
from reasoning_dsl.tokenize import BLANK, BOS, EOS, SEP, Vocab


IDENTIFIERS = ["<blank>"]


def _sequence_lengths(examples: list[Example], vocab: Vocab) -> list[int]:
    lengths = []
    for example in examples:
        prefix_len = 1 + len(vocab.encode(example.source_text())) + 1
        target_len = len(vocab.encode(example.target_text())) + 1
        lengths.append(prefix_len + target_len)
    return lengths


def export_trm_arrays(
    examples_by_split: dict[str, list[Example]],
    output_dir: str | Path,
    *,
    vocab: Vocab | None = None,
    tokenization: str = "whitespace",
) -> None:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    all_examples = [example for examples in examples_by_split.values() for example in examples]
    if not all_examples:
        raise ValueError("Cannot export an empty dataset")

    vocab = vocab or Vocab.build(all_examples, tokenization=tokenization)
    seq_len = max(_sequence_lengths(all_examples, vocab))

    vocab.save(output / "vocab.json")
    with open(output / "identifiers.json", "w", encoding="utf-8") as f:
        json.dump(IDENTIFIERS, f, indent=2)

    for split, examples in examples_by_split.items():
        split_dir = output / split
        split_dir.mkdir(parents=True, exist_ok=True)
        inputs = np.full((len(examples), seq_len), vocab.pad_id, dtype=np.int32)
        labels = np.zeros((len(examples), seq_len), dtype=np.int32)

        puzzle_identifiers: list[int] = []
        puzzle_indices = [0]

        for idx, example in enumerate(examples):
            source = [vocab.token_to_id[BOS], *vocab.encode(example.source_text()), vocab.token_to_id[SEP]]
            target = [*vocab.encode(example.target_text()), vocab.token_to_id[EOS]]
            end = len(source) + len(target)
            if end > seq_len:
                raise ValueError(f"Example {example.id} exceeds seq_len={seq_len}")

            inputs[idx, : len(source)] = source
            inputs[idx, len(source) : end] = vocab.token_to_id[BLANK]
            labels[idx, len(source) : end] = target

            puzzle_identifiers.append(0)
            puzzle_indices.append(idx + 1)

        group_indices = list(range(len(examples) + 1))

        metadata = {
            "seq_len": int(seq_len),
            "vocab_size": vocab.vocab_size,
            "pad_id": vocab.pad_id,
            "ignore_label_id": 0,
            "blank_identifier_id": 0,
            "num_puzzle_identifiers": len(IDENTIFIERS),
            "total_groups": len(group_indices) - 1,
            "mean_puzzle_examples": 1.0,
            "total_puzzles": len(examples),
            "sets": ["all"],
        }
        with open(split_dir / "dataset.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, sort_keys=True)

        np.save(split_dir / "all__inputs.npy", inputs)
        np.save(split_dir / "all__labels.npy", labels)
        np.save(split_dir / "all__puzzle_identifiers.npy", np.array(puzzle_identifiers, dtype=np.int32))
        np.save(split_dir / "all__puzzle_indices.npy", np.array(puzzle_indices, dtype=np.int32))
        np.save(split_dir / "all__group_indices.npy", np.array(group_indices, dtype=np.int32))
