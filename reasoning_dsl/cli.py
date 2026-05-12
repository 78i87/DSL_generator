from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from reasoning_dsl.alpha_rename import alpha_augment_train_split, alpha_rename_dataset, canonicalize_dataset
from reasoning_dsl.audit import audit_dataset, write_audit_report
from reasoning_dsl.export_jsonl import export_jsonl
from reasoning_dsl.export_trm import export_trm_arrays
from reasoning_dsl.generators import (
    GraphReachabilityGenerator,
    ImplicationChainGenerator,
    RelationCompositionGenerator,
    TermRewritingGenerator,
    TreeAncestryGenerator,
)
from reasoning_dsl.split import generate_examples
from reasoning_dsl.tokenize import Vocab


def _load_config(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_report(examples_by_split: dict[str, list], output_dir: Path, seed: int) -> None:
    report: dict[str, Any] = {"seed": seed, "splits": {}}
    for split, examples in examples_by_split.items():
        families = Counter(example.family for example in examples)
        modes = Counter(example.mode for example in examples)
        fingerprints = {example.meta["fingerprint"] for example in examples}
        report["splits"][split] = {
            "examples": len(examples),
            "problems": len({example.meta["problem_id"] for example in examples}),
            "unique_fingerprints": len(fingerprints),
            "families": dict(sorted(families.items())),
            "modes": dict(sorted(modes.items())),
        }
    with open(output_dir / "generation_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, sort_keys=True)


def generate_command(args: argparse.Namespace) -> None:
    config = _load_config(args.config)
    root_seed = args.seed if args.seed is not None else int(config.get("root_seed", 0))
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    generators = [
        GraphReachabilityGenerator(),
        ImplicationChainGenerator(),
        RelationCompositionGenerator(),
        TreeAncestryGenerator(),
        TermRewritingGenerator(),
    ]
    examples_by_split = generate_examples(generators=generators, config=config, root_seed=root_seed)
    export_jsonl(examples_by_split, output_dir)
    vocab = Vocab.load(args.vocab_from) if args.vocab_from else None
    tokenization = str(config.get("tokenization", "whitespace"))
    export_trm_arrays(examples_by_split, output_dir, vocab=vocab, tokenization=tokenization)
    _write_report(examples_by_split, output_dir, root_seed)

    total_examples = sum(len(examples) for examples in examples_by_split.values())
    total_problems = sum(len({example.meta["problem_id"] for example in examples}) for examples in examples_by_split.values())
    print(f"Wrote {total_examples} examples from {total_problems} problems to {output_dir}")


def audit_command(args: argparse.Namespace) -> None:
    report = audit_dataset(args.data_dir)
    write_audit_report(report, args.output_dir)
    print(f"Audit {report['status']}: {len(report['errors'])} errors, {len(report['warnings'])} warnings")
    print(f"Wrote {Path(args.output_dir) / 'audit.md'}")
    print(f"Wrote {Path(args.output_dir) / 'audit.json'}")
    if report["errors"]:
        raise SystemExit(1)


def alpha_rename_command(args: argparse.Namespace) -> None:
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    examples_by_split = alpha_rename_dataset(args.data_dir, seed=args.seed)
    export_jsonl(examples_by_split, output_dir)
    vocab = Vocab.load(args.vocab_from) if args.vocab_from else None
    export_trm_arrays(examples_by_split, output_dir, vocab=vocab)
    _write_report(examples_by_split, output_dir, args.seed)

    total_examples = sum(len(examples) for examples in examples_by_split.values())
    print(f"Wrote {total_examples} alpha-renamed examples to {output_dir}")


def alpha_augment_command(args: argparse.Namespace) -> None:
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    examples_by_split = alpha_augment_train_split(args.data_dir, seed=args.seed, copies=args.train_copies)
    export_jsonl(examples_by_split, output_dir)
    vocab = Vocab.load(args.vocab_from) if args.vocab_from else None
    export_trm_arrays(examples_by_split, output_dir, vocab=vocab)
    _write_report(examples_by_split, output_dir, args.seed)

    total_examples = sum(len(examples) for examples in examples_by_split.values())
    train_examples = len(examples_by_split.get("train", []))
    print(f"Wrote {total_examples} examples to {output_dir}; train split has {train_examples} examples")


def canonicalize_command(args: argparse.Namespace) -> None:
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    vocab = Vocab.load(args.vocab_from) if args.vocab_from else None
    examples_by_split = canonicalize_dataset(args.data_dir, token_to_id=vocab.token_to_id if vocab else None)
    export_jsonl(examples_by_split, output_dir)
    export_trm_arrays(examples_by_split, output_dir, vocab=vocab)
    _write_report(examples_by_split, output_dir, seed=0)

    total_examples = sum(len(examples) for examples in examples_by_split.values())
    print(f"Wrote {total_examples} canonicalized examples to {output_dir}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate symbolic reasoning DSL datasets.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser("generate", help="Generate JSONL and TRM .npy datasets.")
    generate.add_argument("--config", required=True, help="Path to a JSON config file.")
    generate.add_argument("--output-dir", required=True, help="Output dataset directory.")
    generate.add_argument("--seed", type=int, default=None, help="Root seed override.")
    generate.add_argument("--vocab-from", default=None, help="Reuse an existing vocab.json and fail if generated text is OOV.")
    generate.set_defaults(func=generate_command)

    audit = subparsers.add_parser("audit", help="Audit generated JSONL and TRM .npy datasets.")
    audit.add_argument("--data-dir", required=True, help="Generated dataset directory.")
    audit.add_argument("--output-dir", required=True, help="Directory for audit.md and audit.json.")
    audit.set_defaults(func=audit_command)

    alpha = subparsers.add_parser("alpha-rename", help="Create a consistently symbol-renamed copy of a dataset.")
    alpha.add_argument("--data-dir", required=True, help="Existing generated dataset directory.")
    alpha.add_argument("--output-dir", required=True, help="Output dataset directory.")
    alpha.add_argument("--seed", type=int, default=0, help="Renaming seed.")
    alpha.add_argument("--vocab-from", default=None, help="Reuse an existing vocab.json and fail if renamed text is OOV.")
    alpha.set_defaults(func=alpha_rename_command)

    augment = subparsers.add_parser("alpha-augment", help="Append alpha-renamed copies to the train split.")
    augment.add_argument("--data-dir", required=True, help="Existing generated dataset directory.")
    augment.add_argument("--output-dir", required=True, help="Output dataset directory.")
    augment.add_argument("--seed", type=int, default=0, help="Base renaming seed.")
    augment.add_argument("--train-copies", type=int, default=1, help="Number of renamed train copies to append.")
    augment.add_argument("--vocab-from", default=None, help="Reuse an existing vocab.json and fail if augmented text is OOV.")
    augment.set_defaults(func=alpha_augment_command)

    canonicalize = subparsers.add_parser("canonicalize", help="Map arbitrary symbols to deterministic local names.")
    canonicalize.add_argument("--data-dir", required=True, help="Existing generated dataset directory.")
    canonicalize.add_argument("--output-dir", required=True, help="Output dataset directory.")
    canonicalize.add_argument("--vocab-from", default=None, help="Reuse an existing vocab.json and fail if canonical text is OOV.")
    canonicalize.set_defaults(func=canonicalize_command)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
