from __future__ import annotations

import json

import numpy as np

from reasoning_dsl.audit import audit_dataset, write_audit_report
from reasoning_dsl.export_jsonl import export_jsonl
from reasoning_dsl.export_trm import export_trm_arrays
from reasoning_dsl.generators import (
    GraphReachabilityGenerator,
    ImplicationChainGenerator,
    RelationCompositionGenerator,
    TermRewritingGenerator,
)
from reasoning_dsl.split import generate_examples


def _small_config() -> dict:
    return {
        "modes": ["improve", "repair", "complete", "verify"],
        "splits": {
            "train": {"problems_per_family": 2, "difficulty": "train"},
            "test": {"problems_per_family": 1, "difficulty": "test"},
            "ood": {"problems_per_family": 1, "difficulty": "ood"},
        },
        "families": {
            "graph_reachability": {
                "enabled": True,
                "train": {"num_nodes": 6, "path_length": 3, "extra_edges": 1, "require_shortest": True},
                "test": {"num_nodes": 7, "path_length": 4, "extra_edges": 1, "require_shortest": True},
                "ood": {"num_nodes": 8, "path_length": 5, "extra_edges": 2, "require_shortest": True},
            },
            "implication_chains": {
                "enabled": True,
                "train": {"num_props": 6, "proof_length": 3, "distractor_hyps": 1},
                "test": {"num_props": 7, "proof_length": 4, "distractor_hyps": 1},
                "ood": {"num_props": 8, "proof_length": 5, "distractor_hyps": 2},
            },
            "relation_composition": {
                "enabled": True,
                "train": {"num_entities": 6, "composition_depth": 3, "distractor_facts": 1},
                "test": {"num_entities": 7, "composition_depth": 4, "distractor_facts": 1},
                "ood": {"num_entities": 8, "composition_depth": 5, "distractor_facts": 2},
            },
        },
    }


def _small_rewrite_config() -> dict:
    return {
        "modes": ["action", "repair_action", "verify"],
        "verify_corruption_strategy": "single_error",
        "splits": {
            "train": {"problems_per_family": 2, "difficulty": "train"},
            "test": {"problems_per_family": 1, "difficulty": "test"},
            "ood": {"problems_per_family": 1, "difficulty": "ood"},
        },
        "families": {
            "term_rewriting": {
                "enabled": True,
                "train": {
                    "rewrite_steps": 3,
                    "term_depth": 4,
                    "distractor_rules": 2,
                    "variable_rule_rate": 0.5,
                    "binary_rule_rate": 0.5,
                    "normal_form_rate": 0.5,
                },
                "test": {
                    "rewrite_steps": 4,
                    "term_depth": 5,
                    "distractor_rules": 3,
                    "variable_rule_rate": 0.6,
                    "binary_rule_rate": 0.6,
                    "normal_form_rate": 0.5,
                },
                "ood": {
                    "rewrite_steps": 5,
                    "term_depth": 6,
                    "distractor_rules": 4,
                    "variable_rule_rate": 0.7,
                    "binary_rule_rate": 0.7,
                    "normal_form_rate": 0.5,
                },
            },
        },
    }


def _write_dataset(path) -> None:
    examples_by_split = generate_examples(
        generators=[GraphReachabilityGenerator(), ImplicationChainGenerator(), RelationCompositionGenerator()],
        config=_small_config(),
        root_seed=0,
    )
    export_jsonl(examples_by_split, path)
    export_trm_arrays(examples_by_split, path)


def _write_rewrite_dataset(path) -> None:
    examples_by_split = generate_examples(
        generators=[TermRewritingGenerator()],
        config=_small_rewrite_config(),
        root_seed=0,
    )
    export_jsonl(examples_by_split, path)
    export_trm_arrays(examples_by_split, path)


def _jsonl_rows(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def _write_jsonl_rows(path, rows) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True) + "\n")


def test_audit_passes_valid_dataset(tmp_path) -> None:
    data_dir = tmp_path / "dataset"
    report_dir = tmp_path / "report"
    _write_dataset(data_dir)

    report = audit_dataset(data_dir)
    write_audit_report(report, report_dir)

    assert report["status"] == "pass"
    assert report["errors"] == []
    assert (report_dir / "audit.md").exists()
    assert (report_dir / "audit.json").exists()


def test_audit_passes_valid_term_rewriting_dataset(tmp_path) -> None:
    data_dir = tmp_path / "rewrite_dataset"
    _write_rewrite_dataset(data_dir)

    report = audit_dataset(data_dir)

    assert report["status"] == "pass"
    assert report["errors"] == []
    assert set(report["jsonl"]["splits"]["train"]["families"]) == {"term_rewriting"}


def test_audit_fails_on_cross_split_fingerprint(tmp_path) -> None:
    data_dir = tmp_path / "dataset"
    _write_dataset(data_dir)

    train = _jsonl_rows(data_dir / "jsonl" / "train.jsonl")
    test = _jsonl_rows(data_dir / "jsonl" / "test.jsonl")
    test[0]["family"] = train[0]["family"]
    test[0]["meta"]["fingerprint"] = train[0]["meta"]["fingerprint"]
    _write_jsonl_rows(data_dir / "jsonl" / "test.jsonl", test)

    report = audit_dataset(data_dir)
    assert report["status"] == "fail"
    assert any("Cross-split fingerprint leakage" in error for error in report["errors"])


def test_audit_fails_on_nonzero_puzzle_identifier(tmp_path) -> None:
    data_dir = tmp_path / "dataset"
    _write_dataset(data_dir)

    ids_path = data_dir / "train" / "all__puzzle_identifiers.npy"
    ids = np.load(ids_path)
    ids[0] = 1
    np.save(ids_path, ids)

    report = audit_dataset(data_dir)
    assert report["status"] == "fail"
    assert any("puzzle_identifiers must all be zero" in error for error in report["errors"])


def test_audit_fails_on_mismatched_array_shape(tmp_path) -> None:
    data_dir = tmp_path / "dataset"
    _write_dataset(data_dir)

    labels_path = data_dir / "train" / "all__labels.npy"
    labels = np.load(labels_path)
    np.save(labels_path, labels[:-1])

    report = audit_dataset(data_dir)
    assert report["status"] == "fail"
    assert any("input/label shape mismatch" in error for error in report["errors"])


def test_audit_fails_on_missing_jsonl_field(tmp_path) -> None:
    data_dir = tmp_path / "dataset"
    _write_dataset(data_dir)

    rows = _jsonl_rows(data_dir / "jsonl" / "train.jsonl")
    rows[0].pop("source_text")
    _write_jsonl_rows(data_dir / "jsonl" / "train.jsonl", rows)

    report = audit_dataset(data_dir)
    assert report["status"] == "fail"
    assert any("missing example fields" in error for error in report["errors"])


def test_audit_fails_on_empty_target_row(tmp_path) -> None:
    data_dir = tmp_path / "dataset"
    _write_dataset(data_dir)

    labels_path = data_dir / "train" / "all__labels.npy"
    labels = np.load(labels_path)
    labels[0] = 0
    np.save(labels_path, labels)

    report = audit_dataset(data_dir)
    assert report["status"] == "fail"
    assert any("all-empty target rows" in error for error in report["errors"])
