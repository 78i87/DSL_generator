from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import numpy as np
import pytest

from reasoning_dsl.export_jsonl import export_jsonl
from reasoning_dsl.export_trm import export_trm_arrays
from reasoning_dsl.generators import (
    GraphReachabilityGenerator,
    ImplicationChainGenerator,
    RelationCompositionGenerator,
    TermRewritingGenerator,
)
from reasoning_dsl.split import generate_examples
from reasoning_dsl.tokenize import SPECIAL_TOKENS, Vocab


def _small_config() -> dict:
    return {
        "modes": ["improve", "repair", "complete", "verify"],
        "splits": {
            "train": {"problems_per_family": 3, "difficulty": "train"},
            "test": {"problems_per_family": 2, "difficulty": "test"},
            "ood": {"problems_per_family": 2, "difficulty": "ood"},
        },
        "families": {
            "graph_reachability": {
                "enabled": True,
                "train": {"num_nodes": 7, "path_length": 3, "extra_edges": 2, "require_shortest": True},
                "test": {"num_nodes": 8, "path_length": 4, "extra_edges": 2, "require_shortest": True},
                "ood": {"num_nodes": 9, "path_length": 5, "extra_edges": 3, "require_shortest": True},
            },
            "implication_chains": {
                "enabled": True,
                "train": {"num_props": 7, "proof_length": 3, "distractor_hyps": 2},
                "test": {"num_props": 8, "proof_length": 4, "distractor_hyps": 2},
                "ood": {"num_props": 9, "proof_length": 5, "distractor_hyps": 3},
            },
            "relation_composition": {
                "enabled": True,
                "train": {"num_entities": 7, "composition_depth": 3, "distractor_facts": 2},
                "test": {"num_entities": 8, "composition_depth": 4, "distractor_facts": 2},
                "ood": {"num_entities": 9, "composition_depth": 5, "distractor_facts": 3},
            },
        },
    }


def _mixture_config() -> dict:
    return {
        "modes": ["improve", "repair", "complete", "verify"],
        "splits": {
            "train": {
                "difficulty_mixture": [
                    {"name": "slice_a", "difficulty": "train_a", "problems_per_family": 1},
                    {"name": "slice_b", "difficulty": "train_b", "problems_per_family": 2},
                ]
            },
            "test": {
                "difficulty_mixture": [
                    {"name": "slice_c", "difficulty": "test_c", "problems_per_family": 1},
                ]
            },
            "ood": {
                "difficulty_mixture": [
                    {"name": "slice_d", "difficulty": "ood_d", "problems_per_family": 1},
                ]
            },
        },
        "families": {
            "graph_reachability": {
                "enabled": True,
                "train_a": {"num_nodes": 6, "path_length": 2, "extra_edges": 1, "require_shortest": True},
                "train_b": {"num_nodes": 7, "path_length": 3, "extra_edges": 1, "require_shortest": True},
                "test_c": {"num_nodes": 8, "path_length": 4, "extra_edges": 1, "require_shortest": True},
                "ood_d": {"num_nodes": 9, "path_length": 5, "extra_edges": 2, "require_shortest": True},
            },
            "implication_chains": {
                "enabled": True,
                "train_a": {"num_props": 6, "proof_length": 2, "distractor_hyps": 1},
                "train_b": {"num_props": 7, "proof_length": 3, "distractor_hyps": 1},
                "test_c": {"num_props": 8, "proof_length": 4, "distractor_hyps": 2},
                "ood_d": {"num_props": 9, "proof_length": 5, "distractor_hyps": 2},
            },
            "relation_composition": {
                "enabled": True,
                "train_a": {"num_entities": 6, "composition_depth": 2, "distractor_facts": 1},
                "train_b": {"num_entities": 7, "composition_depth": 3, "distractor_facts": 1},
                "test_c": {"num_entities": 8, "composition_depth": 4, "distractor_facts": 2},
                "ood_d": {"num_entities": 9, "composition_depth": 5, "distractor_facts": 2},
            },
        },
    }


def _term_rewriting_config() -> dict:
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


def test_split_generation_has_no_cross_split_fingerprint_overlap() -> None:
    examples_by_split = generate_examples(
        generators=[GraphReachabilityGenerator(), ImplicationChainGenerator(), RelationCompositionGenerator()],
        config=_small_config(),
        root_seed=0,
    )
    seen: set[str] = set()
    for split, examples in examples_by_split.items():
        fingerprints = {f"{example.family}:{example.meta['fingerprint']}" for example in examples}
        assert fingerprints.isdisjoint(seen), split
        seen.update(fingerprints)


def test_difficulty_mixture_has_exact_slice_counts_and_no_leakage() -> None:
    examples_by_split = generate_examples(
        generators=[GraphReachabilityGenerator(), ImplicationChainGenerator(), RelationCompositionGenerator()],
        config=_mixture_config(),
        root_seed=0,
    )
    counts: Counter[tuple[str, str, str]] = Counter()
    seen_fingerprints: set[str] = set()
    seen_problem_ids: set[str] = set()

    for split, examples in examples_by_split.items():
        for example in examples:
            problem_key = f"{example.family}:{example.meta['problem_id']}"
            if problem_key not in seen_problem_ids:
                seen_problem_ids.add(problem_key)
                counts[(split, example.family, example.meta["difficulty_slice"])] += 1
            fingerprint = f"{example.family}:{example.meta['fingerprint']}"
            if fingerprint in seen_fingerprints:
                continue
            seen_fingerprints.add(fingerprint)

    for family in ("graph_reachability", "implication_chains", "relation_composition"):
        assert counts[("train", family, "slice_a")] == 1
        assert counts[("train", family, "slice_b")] == 2
        assert counts[("test", family, "slice_c")] == 1
        assert counts[("ood", family, "slice_d")] == 1
    assert sum(counts.values()) == len(seen_fingerprints)


def test_difficulty_mixture_can_override_modes_per_slice() -> None:
    config = _mixture_config()
    config["splits"]["train"]["difficulty_mixture"][1]["modes"] = ["complete"]

    examples_by_split = generate_examples(
        generators=[GraphReachabilityGenerator(), ImplicationChainGenerator(), RelationCompositionGenerator()],
        config=config,
        root_seed=0,
    )

    for example in examples_by_split["train"]:
        if example.meta["difficulty_slice"] == "slice_a":
            assert example.mode in {"improve", "repair", "complete", "verify"}
        if example.meta["difficulty_slice"] == "slice_b":
            assert example.mode == "complete"


def test_difficulty_mixture_can_filter_families_per_slice() -> None:
    config = _mixture_config()
    config["splits"]["train"]["difficulty_mixture"].append(
        {
            "name": "relation_only",
            "difficulty": "train_b",
            "problems_per_family": 2,
            "families": ["relation_composition"],
        }
    )

    examples_by_split = generate_examples(
        generators=[GraphReachabilityGenerator(), ImplicationChainGenerator(), RelationCompositionGenerator()],
        config=config,
        root_seed=0,
    )

    relation_only = [
        example for example in examples_by_split["train"] if example.meta.get("difficulty_slice") == "relation_only"
    ]
    assert relation_only
    assert {example.family for example in relation_only} == {"relation_composition"}
    assert len({example.meta["problem_id"] for example in relation_only}) == 2


def test_v4_config_replaces_complete_with_action() -> None:
    config_path = Path("configs/symbolic_v4_action_completion.json")
    config = json.loads(config_path.read_text(encoding="utf-8"))

    assert "action" in config["modes"]
    assert "complete" not in config["modes"]
    for split_info in config["splits"].values():
        for item in split_info.get("difficulty_mixture", []):
            assert item.get("modes") != ["complete"]


def test_v5_action_symbol_exposure_config_is_action_only_extra_data() -> None:
    config_path = Path("configs/symbolic_v5_action_symbol_exposure.json")
    config = json.loads(config_path.read_text(encoding="utf-8"))

    assert config["modes"] == ["improve", "repair", "action", "verify"]
    assert "complete" not in config["modes"]
    exposure_slices = [
        item for item in config["splits"]["train"]["difficulty_mixture"] if item["name"].startswith("action_symbol_")
    ]
    assert {item["difficulty_overrides"]["symbol_offset"] for item in exposure_slices} == {3, 6}
    assert all(item["modes"] == ["action"] for item in exposure_slices)


def test_v6_compact_targets_config_has_no_full_state_modes() -> None:
    config_path = Path("configs/symbolic_v6_compact_targets.json")
    config = json.loads(config_path.read_text(encoding="utf-8"))

    assert config["modes"] == ["action", "repair_action", "verify"]
    assert "improve" not in config["modes"]
    assert "repair" not in config["modes"]
    assert "complete" not in config["modes"]
    symbol_slices = [
        item for item in config["splits"]["train"]["difficulty_mixture"] if item["name"].startswith("compact_symbol_")
    ]
    assert {item["difficulty_overrides"]["symbol_offset"] for item in symbol_slices} == {3, 6}
    assert all(item["modes"] == ["action", "repair_action"] for item in symbol_slices)


def test_v7_primitive_repair_config_has_no_full_state_modes() -> None:
    config_path = Path("configs/symbolic_v7_primitive_repair.json")
    config = json.loads(config_path.read_text(encoding="utf-8"))

    assert config["modes"] == ["action", "repair_action", "verify"]
    assert "improve" not in config["modes"]
    assert "repair" not in config["modes"]
    assert "complete" not in config["modes"]


def test_v8_primitive_action_config_has_no_full_state_modes() -> None:
    config_path = Path("configs/symbolic_v8_primitive_action.json")
    config = json.loads(config_path.read_text(encoding="utf-8"))

    assert config["modes"] == ["action", "repair_action", "verify"]
    assert "improve" not in config["modes"]
    assert "repair" not in config["modes"]
    assert "complete" not in config["modes"]


def test_v9_follow_action_config_has_no_full_state_modes() -> None:
    config_path = Path("configs/symbolic_v9_follow_action.json")
    config = json.loads(config_path.read_text(encoding="utf-8"))

    assert config["modes"] == ["action", "repair_action", "verify"]
    assert "improve" not in config["modes"]
    assert "repair" not in config["modes"]
    assert "complete" not in config["modes"]


def test_v10_short_follow_action_config_has_no_full_state_modes() -> None:
    config_path = Path("configs/symbolic_v10_short_follow_action.json")
    config = json.loads(config_path.read_text(encoding="utf-8"))

    assert config["modes"] == ["action", "repair_action", "verify"]
    assert "improve" not in config["modes"]
    assert "repair" not in config["modes"]
    assert "complete" not in config["modes"]


def test_v10_same_vocab_stress_config_uses_compact_modes_and_offsets() -> None:
    config_path = Path("configs/symbolic_v10_same_vocab_stress.json")
    config = json.loads(config_path.read_text(encoding="utf-8"))

    assert config["modes"] == ["action", "repair_action", "verify"]
    ood_slices = config["splits"]["ood"]["difficulty_mixture"]
    assert [item["difficulty_overrides"]["symbol_offset"] for item in ood_slices] == [4, 2, 0]
    assert [item["difficulty"] for item in ood_slices] == ["stress_8", "stress_9", "stress_10"]
    assert ood_slices[2]["modes"] == ["action", "verify"]


def test_v11_stress_curriculum_keeps_v10_dsl_and_adds_stress_train_slices() -> None:
    config_path = Path("configs/symbolic_v11_stress_curriculum.json")
    config = json.loads(config_path.read_text(encoding="utf-8"))

    assert config["modes"] == ["action", "repair_action", "verify"]
    train_slices = config["splits"]["train"]["difficulty_mixture"]
    stress_slices = [item for item in train_slices if item["name"].startswith("stress_")]
    assert [item["difficulty_overrides"]["symbol_offset"] for item in stress_slices] == [4, 2, 0]
    assert stress_slices[0]["modes"] == ["action", "repair_action", "verify"]
    assert stress_slices[1]["modes"] == ["action", "repair_action", "verify"]
    assert stress_slices[2]["modes"] == ["action", "verify"]


def test_v12_repair_balanced_config_keeps_v11_stress_and_adds_repair_slices() -> None:
    config_path = Path("configs/symbolic_v12_repair_balanced_stress.json")
    config = json.loads(config_path.read_text(encoding="utf-8"))

    assert config["modes"] == ["action", "repair_action", "verify"]
    train_slices = config["splits"]["train"]["difficulty_mixture"]
    repair_slices = [item for item in train_slices if item["name"].startswith("repair_balance_")]
    assert [item["name"] for item in repair_slices] == [
        "repair_balance_graph_6",
        "repair_balance_graph_7",
        "repair_balance_implication_6",
        "repair_balance_implication_7",
    ]
    assert all(item["modes"] == ["repair_action"] for item in repair_slices)
    assert [item["families"] for item in repair_slices] == [
        ["graph_reachability"],
        ["graph_reachability"],
        ["implication_chains"],
        ["implication_chains"],
    ]

    stress_slices = [item for item in train_slices if item["name"].startswith("stress_")]
    assert [item["difficulty_overrides"]["symbol_offset"] for item in stress_slices] == [4, 2, 0]
    assert stress_slices[2]["modes"] == ["action", "verify"]


def test_v13_tree_ancestry_config_adds_fourth_family_without_changing_modes() -> None:
    config_path = Path("configs/symbolic_v13_tree_ancestry.json")
    config = json.loads(config_path.read_text(encoding="utf-8"))

    assert config["modes"] == ["action", "repair_action", "verify"]
    assert config["families"]["tree_ancestry"]["enabled"] is True
    assert config["families"]["tree_ancestry"]["train_bridge_6"]["depth"] == 6
    assert config["families"]["tree_ancestry"]["train_bridge_7"]["depth"] == 7
    assert config["families"]["tree_ancestry"]["ood_10"]["depth"] == 10

    repair_slices = [
        item for item in config["splits"]["train"]["difficulty_mixture"] if item["name"].startswith("repair_balance_")
    ]
    assert all(item["families"] != ["tree_ancestry"] for item in repair_slices)


def test_v14_repair_hardened_tree_keeps_v13_surface_and_adds_repair_only_slices() -> None:
    v13_path = Path("configs/symbolic_v13_tree_ancestry.json")
    v14_path = Path("configs/symbolic_v14_repair_hardened_tree.json")
    v13 = json.loads(v13_path.read_text(encoding="utf-8"))
    v14 = json.loads(v14_path.read_text(encoding="utf-8"))

    assert v14["modes"] == ["action", "repair_action", "verify"]
    assert set(v14["families"]) == set(v13["families"]) == {
        "graph_reachability",
        "implication_chains",
        "relation_composition",
        "tree_ancestry",
    }
    assert v14["splits"]["test"] == v13["splits"]["test"]
    assert v14["splits"]["ood"] == v13["splits"]["ood"]

    v13_train_names = {item["name"] for item in v13["splits"]["train"]["difficulty_mixture"]}
    v14_train_slices = v14["splits"]["train"]["difficulty_mixture"]
    added_slices = [item for item in v14_train_slices if item["name"] not in v13_train_names]
    assert [item["name"] for item in added_slices] == [
        "repair_balance_relation_6",
        "repair_balance_relation_7",
        "repair_balance_tree_6",
        "repair_balance_tree_7",
        "repair_balance_stress_10",
    ]
    assert all(item["modes"] == ["repair_action"] for item in added_slices)
    assert [item["families"] for item in added_slices[:4]] == [
        ["relation_composition"],
        ["relation_composition"],
        ["tree_ancestry"],
        ["tree_ancestry"],
    ]
    assert "families" not in added_slices[4]
    assert added_slices[4]["difficulty"] == "train_stress_10"
    assert added_slices[4]["difficulty_overrides"] == {"symbol_offset": 0}


def test_v15_relation_stress_reinforced_changes_only_relation_stress_balance() -> None:
    v14_path = Path("configs/symbolic_v14_repair_hardened_tree.json")
    v15_path = Path("configs/symbolic_v15_relation_stress_reinforced.json")
    v14 = json.loads(v14_path.read_text(encoding="utf-8"))
    v15 = json.loads(v15_path.read_text(encoding="utf-8"))

    assert v15["modes"] == v14["modes"] == ["action", "repair_action", "verify"]
    assert set(v15["families"]) == set(v14["families"])
    assert v15["splits"]["test"] == v14["splits"]["test"]
    assert v15["splits"]["ood"] == v14["splits"]["ood"]

    v14_train_names = {item["name"] for item in v14["splits"]["train"]["difficulty_mixture"]}
    added_slices = [
        item for item in v15["splits"]["train"]["difficulty_mixture"] if item["name"] not in v14_train_names
    ]
    assert [item["name"] for item in added_slices] == [
        "relation_stress_8_action_repair",
        "relation_stress_9_action_repair",
        "relation_stress_10_action_repair",
    ]
    assert [item["difficulty"] for item in added_slices] == [
        "train_stress_8",
        "train_stress_9",
        "train_stress_10",
    ]
    assert [item["difficulty_overrides"]["symbol_offset"] for item in added_slices] == [4, 2, 0]
    assert all(item["problems_per_family"] == 48 for item in added_slices)
    assert all(item["modes"] == ["action", "repair_action"] for item in added_slices)
    assert all(item["families"] == ["relation_composition"] for item in added_slices)


def test_v15b_relation_stress_reinforced_keeps_v14_seed_for_one_variable_comparison() -> None:
    v14_path = Path("configs/symbolic_v14_repair_hardened_tree.json")
    v15b_path = Path("configs/symbolic_v15b_relation_stress_reinforced_same_seed.json")
    v14 = json.loads(v14_path.read_text(encoding="utf-8"))
    v15b = json.loads(v15b_path.read_text(encoding="utf-8"))

    assert v15b["root_seed"] == v14["root_seed"]
    assert v15b["modes"] == v14["modes"]
    assert set(v15b["families"]) == set(v14["families"])
    assert v15b["splits"]["test"] == v14["splits"]["test"]
    assert v15b["splits"]["ood"] == v14["splits"]["ood"]

    v14_train_names = {item["name"] for item in v14["splits"]["train"]["difficulty_mixture"]}
    added_slices = [
        item for item in v15b["splits"]["train"]["difficulty_mixture"] if item["name"] not in v14_train_names
    ]
    assert [item["name"] for item in added_slices] == [
        "relation_stress_8_action_repair",
        "relation_stress_9_action_repair",
        "relation_stress_10_action_repair",
    ]
    assert all(item["families"] == ["relation_composition"] for item in added_slices)
    assert all(item["modes"] == ["action", "repair_action"] for item in added_slices)


def test_v16_relation_compose_action_changes_only_relation_action_format() -> None:
    v14_path = Path("configs/symbolic_v14_repair_hardened_tree.json")
    v16_path = Path("configs/symbolic_v16_relation_compose_action.json")
    v14 = json.loads(v14_path.read_text(encoding="utf-8"))
    v16 = json.loads(v16_path.read_text(encoding="utf-8"))

    assert v14.get("relation_action_format", "follow") == "follow"
    assert v16["relation_action_format"] == "compose"
    assert v16["root_seed"] == v14["root_seed"]
    assert v16["modes"] == v14["modes"]
    assert v16["splits"] == v14["splits"]
    assert v16["families"] == v14["families"]


def test_v17_relation_follow_left_action_changes_only_relation_action_format() -> None:
    v14_path = Path("configs/symbolic_v14_repair_hardened_tree.json")
    v17_path = Path("configs/symbolic_v17_relation_follow_left_action.json")
    v14 = json.loads(v14_path.read_text(encoding="utf-8"))
    v17 = json.loads(v17_path.read_text(encoding="utf-8"))

    assert v14.get("relation_action_format", "follow") == "follow"
    assert v17["relation_action_format"] == "follow_left"
    assert v17["root_seed"] == v14["root_seed"]
    assert v17["modes"] == v14["modes"]
    assert v17["splits"] == v14["splits"]
    assert v17["families"] == v14["families"]


def test_v18_tree_after_repair_action_changes_only_tree_repair_format() -> None:
    v17_path = Path("configs/symbolic_v17_relation_follow_left_action.json")
    v18_path = Path("configs/symbolic_v18_tree_after_repair_action.json")
    v17 = json.loads(v17_path.read_text(encoding="utf-8"))
    v18 = json.loads(v18_path.read_text(encoding="utf-8"))

    assert v17.get("tree_repair_action_format", "index") == "index"
    assert v18["tree_repair_action_format"] == "after"
    assert v18["relation_action_format"] == v17["relation_action_format"]
    assert v18["root_seed"] == v17["root_seed"]
    assert v18["modes"] == v17["modes"]
    assert v18["splits"] == v17["splits"]
    assert v18["families"] == v17["families"]


def test_v19_local_repair_action_changes_only_repair_format() -> None:
    v18_path = Path("configs/symbolic_v18_tree_after_repair_action.json")
    v19_path = Path("configs/symbolic_v19_local_repair_action.json")
    v18 = json.loads(v18_path.read_text(encoding="utf-8"))
    v19 = json.loads(v19_path.read_text(encoding="utf-8"))

    assert v18.get("repair_action_format", "index") == "index"
    assert v19["repair_action_format"] == "local"
    assert v19["relation_action_format"] == v18["relation_action_format"]
    assert v19["tree_repair_action_format"] == v18["tree_repair_action_format"]
    assert v19["root_seed"] == v18["root_seed"]
    assert v19["modes"] == v18["modes"]
    assert v19["splits"] == v18["splits"]
    assert v19["families"] == v18["families"]


def test_v20_graph_verify_hardened_adds_only_graph_verify_slices() -> None:
    v19_path = Path("configs/symbolic_v19_local_repair_action.json")
    v20_path = Path("configs/symbolic_v20_graph_verify_hardened.json")
    v19 = json.loads(v19_path.read_text(encoding="utf-8"))
    v20 = json.loads(v20_path.read_text(encoding="utf-8"))

    assert v20["relation_action_format"] == v19["relation_action_format"]
    assert v20["repair_action_format"] == v19["repair_action_format"]
    assert v20["tree_repair_action_format"] == v19["tree_repair_action_format"]
    assert v20["root_seed"] == v19["root_seed"]
    assert v20["modes"] == v19["modes"]
    assert v20["families"] == v19["families"]
    assert v20["splits"]["test"] == v19["splits"]["test"]
    assert v20["splits"]["ood"] == v19["splits"]["ood"]

    v19_train_names = {item["name"] for item in v19["splits"]["train"]["difficulty_mixture"]}
    added = [
        item
        for item in v20["splits"]["train"]["difficulty_mixture"]
        if item["name"] not in v19_train_names
    ]

    assert [item["name"] for item in added] == [
        "verify_balance_graph_8",
        "verify_balance_graph_9",
        "verify_balance_graph_10",
    ]
    assert all(item["modes"] == ["verify"] for item in added)
    assert all(item["families"] == ["graph_reachability"] for item in added)
    assert all(item["problems_per_family"] == 24 for item in added)


def test_v21_graph_tree_verify_hardened_adds_only_tree_verify_slices() -> None:
    v20_path = Path("configs/symbolic_v20_graph_verify_hardened.json")
    v21_path = Path("configs/symbolic_v21_graph_tree_verify_hardened.json")
    v20 = json.loads(v20_path.read_text(encoding="utf-8"))
    v21 = json.loads(v21_path.read_text(encoding="utf-8"))

    assert v21["relation_action_format"] == v20["relation_action_format"]
    assert v21["repair_action_format"] == v20["repair_action_format"]
    assert v21["tree_repair_action_format"] == v20["tree_repair_action_format"]
    assert v21["root_seed"] == v20["root_seed"]
    assert v21["modes"] == v20["modes"]
    assert v21["families"] == v20["families"]
    assert v21["splits"]["test"] == v20["splits"]["test"]
    assert v21["splits"]["ood"] == v20["splits"]["ood"]

    v20_train_names = {item["name"] for item in v20["splits"]["train"]["difficulty_mixture"]}
    added = [
        item
        for item in v21["splits"]["train"]["difficulty_mixture"]
        if item["name"] not in v20_train_names
    ]

    assert [item["name"] for item in added] == [
        "verify_balance_tree_8",
        "verify_balance_tree_9",
        "verify_balance_tree_10",
    ]
    assert all(item["modes"] == ["verify"] for item in added)
    assert all(item["families"] == ["tree_ancestry"] for item in added)
    assert all(item["problems_per_family"] == 24 for item in added)


def test_v22_single_error_verify_changes_only_verify_corruption_strategy() -> None:
    v19_path = Path("configs/symbolic_v19_local_repair_action.json")
    v22_path = Path("configs/symbolic_v22_single_error_verify.json")
    v19 = json.loads(v19_path.read_text(encoding="utf-8"))
    v22 = json.loads(v22_path.read_text(encoding="utf-8"))

    v22_without_note = {key: value for key, value in v22.items() if key != "experiment_note"}
    assert v22_without_note.pop("verify_corruption_strategy") == "single_error"
    v19_without_note = {key: value for key, value in v19.items() if key != "experiment_note"}
    assert v22_without_note == v19_without_note


def test_0_22_alias_matches_v22_single_error_verify_baseline() -> None:
    v22_path = Path("configs/symbolic_v22_single_error_verify.json")
    alias_path = Path("configs/symbolic_0_22_single_error_verify.json")
    v22 = json.loads(v22_path.read_text(encoding="utf-8"))
    alias = json.loads(alias_path.read_text(encoding="utf-8"))

    assert alias["experiment_note"].startswith("0.22 is the stable pre-1.0 baseline.")
    alias_without_note = {key: value for key, value in alias.items() if key != "experiment_note"}
    v22_without_note = {key: value for key, value in v22.items() if key != "experiment_note"}
    assert alias_without_note == v22_without_note


def test_0_23_fresh_holdout_changes_only_root_seed() -> None:
    baseline_path = Path("configs/symbolic_0_22_single_error_verify.json")
    holdout_path = Path("configs/symbolic_0_23_fresh_holdout.json")
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    holdout = json.loads(holdout_path.read_text(encoding="utf-8"))

    assert holdout["root_seed"] != baseline["root_seed"]
    assert holdout["experiment_note"].startswith("0.23 is a fresh holdout")
    holdout_without_note = {key: value for key, value in holdout.items() if key != "experiment_note"}
    baseline_without_note = {key: value for key, value in baseline.items() if key != "experiment_note"}
    holdout_without_note.pop("root_seed")
    baseline_without_note.pop("root_seed")
    assert holdout_without_note == baseline_without_note


def test_0_24_term_rewriting_adds_only_new_family() -> None:
    baseline_path = Path("configs/symbolic_0_22_single_error_verify.json")
    rewrite_path = Path("configs/symbolic_0_24_term_rewriting.json")
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    rewrite = json.loads(rewrite_path.read_text(encoding="utf-8"))

    assert rewrite["root_seed"] == baseline["root_seed"]
    assert rewrite["experiment_note"].startswith("0.24 adds term_rewriting")
    assert "term_rewriting" not in baseline["families"]
    assert rewrite["families"]["term_rewriting"]["enabled"] is True

    rewrite_existing_families = {
        name: info for name, info in rewrite["families"].items() if name != "term_rewriting"
    }
    assert rewrite_existing_families == baseline["families"]

    rewrite_without_note_and_families = {
        key: value for key, value in rewrite.items() if key not in {"experiment_note", "families"}
    }
    baseline_without_note_and_families = {
        key: value for key, value in baseline.items() if key not in {"experiment_note", "families"}
    }
    assert rewrite_without_note_and_families == baseline_without_note_and_families


def test_term_rewriting_export_preserves_no_id_contract(tmp_path) -> None:
    examples_by_split = generate_examples(
        generators=[TermRewritingGenerator()],
        config=_term_rewriting_config(),
        root_seed=0,
    )
    out_dir = tmp_path / "term_rewriting"
    export_jsonl(examples_by_split, out_dir)
    export_trm_arrays(examples_by_split, out_dir)

    identifiers = json.loads((out_dir / "identifiers.json").read_text(encoding="utf-8"))
    assert identifiers == ["<blank>"]
    for split in ("train", "test", "ood"):
        metadata = json.loads((out_dir / split / "dataset.json").read_text(encoding="utf-8"))
        ids = np.load(out_dir / split / "all__puzzle_identifiers.npy")
        labels = np.load(out_dir / split / "all__labels.npy")
        assert metadata["num_puzzle_identifiers"] == 1
        assert set(ids.tolist()) == {0}
        assert np.any(labels != 0, axis=1).all()


def test_fixed_vocab_export_preserves_token_ids(tmp_path) -> None:
    examples_by_split = generate_examples(
        generators=[GraphReachabilityGenerator(), ImplicationChainGenerator(), RelationCompositionGenerator()],
        config=_small_config(),
        root_seed=0,
    )
    base_dir = tmp_path / "base"
    fixed_dir = tmp_path / "fixed"

    export_trm_arrays(examples_by_split, base_dir)
    vocab = Vocab.load(base_dir / "vocab.json")
    export_trm_arrays(examples_by_split, fixed_dir, vocab=vocab)

    base_vocab = json.loads((base_dir / "vocab.json").read_text(encoding="utf-8"))
    fixed_vocab = json.loads((fixed_dir / "vocab.json").read_text(encoding="utf-8"))
    assert fixed_vocab == base_vocab

    with open(fixed_dir / "train" / "dataset.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)
    assert metadata["vocab_size"] == len(base_vocab)
    assert np.load(fixed_dir / "train" / "all__inputs.npy").max() < metadata["vocab_size"]
    assert np.load(fixed_dir / "train" / "all__labels.npy").max() < metadata["vocab_size"]


def test_fixed_vocab_export_fails_on_oov_token(tmp_path) -> None:
    examples_by_split = generate_examples(
        generators=[GraphReachabilityGenerator(), ImplicationChainGenerator(), RelationCompositionGenerator()],
        config=_small_config(),
        root_seed=0,
    )
    tiny_vocab_path = tmp_path / "tiny_vocab.json"
    tiny_vocab_path.write_text(
        json.dumps({token: idx for idx, token in enumerate(SPECIAL_TOKENS)}),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="fixed vocabulary"):
        export_trm_arrays(examples_by_split, tmp_path / "out", vocab=Vocab.load(tiny_vocab_path))


def test_action_rows_export_with_supervised_targets(tmp_path) -> None:
    config = _small_config()
    config["modes"] = ["action"]

    examples_by_split = generate_examples(
        generators=[GraphReachabilityGenerator(), ImplicationChainGenerator(), RelationCompositionGenerator()],
        config=config,
        root_seed=0,
    )
    export_jsonl(examples_by_split, tmp_path)
    export_trm_arrays(examples_by_split, tmp_path)

    rows = [json.loads(line) for line in (tmp_path / "jsonl" / "train.jsonl").read_text(encoding="utf-8").splitlines()]
    assert rows
    assert {row["mode"] for row in rows} == {"action"}
    assert all(len(row["target_lines"]) == 1 for row in rows)
    assert all("next_state_lines" in row["meta"] and "final_state_lines" in row["meta"] for row in rows)

    with open(tmp_path / "train" / "dataset.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)
    labels = np.load(tmp_path / "train" / "all__labels.npy")
    puzzle_identifiers = np.load(tmp_path / "train" / "all__puzzle_identifiers.npy")

    assert np.all(puzzle_identifiers == 0)
    assert np.all(np.any(labels != 0, axis=1))
    assert labels.max() < metadata["vocab_size"]


def test_repair_action_rows_export_with_supervised_targets(tmp_path) -> None:
    config = _small_config()
    config["modes"] = ["repair_action"]

    examples_by_split = generate_examples(
        generators=[GraphReachabilityGenerator(), ImplicationChainGenerator(), RelationCompositionGenerator()],
        config=config,
        root_seed=0,
    )
    export_jsonl(examples_by_split, tmp_path)
    export_trm_arrays(examples_by_split, tmp_path)

    rows = [json.loads(line) for line in (tmp_path / "jsonl" / "train.jsonl").read_text(encoding="utf-8").splitlines()]
    assert rows
    assert {row["mode"] for row in rows} == {"repair_action"}
    assert all(len(row["target_lines"]) == 1 for row in rows)
    assert all("repaired_state_lines" in row["meta"] for row in rows)
    assert all(row["target_lines"][0].startswith("REPLACE ") for row in rows)

    with open(tmp_path / "train" / "dataset.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)
    labels = np.load(tmp_path / "train" / "all__labels.npy")
    puzzle_identifiers = np.load(tmp_path / "train" / "all__puzzle_identifiers.npy")

    assert np.all(puzzle_identifiers == 0)
    assert np.all(np.any(labels != 0, axis=1))
    assert labels.max() < metadata["vocab_size"]


def test_difficulty_mixture_can_override_difficulty_params_per_slice() -> None:
    config = _mixture_config()
    config["splits"]["train"]["difficulty_mixture"][1]["difficulty_overrides"] = {"symbol_offset": 5}

    examples_by_split = generate_examples(
        generators=[GraphReachabilityGenerator(), ImplicationChainGenerator(), RelationCompositionGenerator()],
        config=config,
        root_seed=0,
    )

    shifted_examples = [example for example in examples_by_split["train"] if example.meta["difficulty_slice"] == "slice_b"]
    assert shifted_examples
    assert all(example.meta["difficulty"]["symbol_offset"] == 5 for example in shifted_examples)
    assert any("e5" in "\n".join([*example.problem_lines, *example.target_lines]) for example in shifted_examples)


def test_jsonl_and_trm_export(tmp_path) -> None:
    examples_by_split = generate_examples(
        generators=[GraphReachabilityGenerator(), ImplicationChainGenerator(), RelationCompositionGenerator()],
        config=_small_config(),
        root_seed=0,
    )
    export_jsonl(examples_by_split, tmp_path)
    export_trm_arrays(examples_by_split, tmp_path)

    jsonl_path = tmp_path / "jsonl" / "train.jsonl"
    first = json.loads(jsonl_path.read_text(encoding="utf-8").splitlines()[0])
    assert "source_text" in first
    assert "target_text" in first

    with open(tmp_path / "train" / "dataset.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)
    with open(tmp_path / "identifiers.json", "r", encoding="utf-8") as f:
        identifiers = json.load(f)
    inputs = np.load(tmp_path / "train" / "all__inputs.npy")
    labels = np.load(tmp_path / "train" / "all__labels.npy")
    puzzle_identifiers = np.load(tmp_path / "train" / "all__puzzle_identifiers.npy")
    puzzle_indices = np.load(tmp_path / "train" / "all__puzzle_indices.npy")
    group_indices = np.load(tmp_path / "train" / "all__group_indices.npy")

    assert inputs.shape == labels.shape
    assert inputs.shape[1] == metadata["seq_len"]
    assert identifiers == ["<blank>"]
    assert metadata["num_puzzle_identifiers"] == 1
    assert puzzle_identifiers.shape[0] == inputs.shape[0]
    assert np.all(puzzle_identifiers == 0)
    assert puzzle_indices.shape[0] == inputs.shape[0] + 1
    assert np.array_equal(puzzle_indices, np.arange(inputs.shape[0] + 1))
    assert group_indices[0] == 0
    assert group_indices[-1] == inputs.shape[0]
    assert np.array_equal(group_indices, np.arange(inputs.shape[0] + 1))
    assert metadata["total_groups"] == inputs.shape[0]
    assert labels.max() < metadata["vocab_size"]
    assert inputs.max() < metadata["vocab_size"]
