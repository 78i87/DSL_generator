from __future__ import annotations

from dataclasses import replace

import numpy as np
import pytest

from reasoning_dsl.core import Example, build_examples_for_problem
from reasoning_dsl.generators import (
    DfaSimulationLiteGenerator,
    EqualityRewritingLiteGenerator,
    GraphReachabilityGenerator,
    ImplicationChainGenerator,
    RelationCompositionGenerator,
    TermRewritingGenerator,
    TreeAncestryGenerator,
)
from reasoning_dsl.relational import model_view, relational_record
from reasoning_dsl.relational_arrays import FACT_PRED_IDS, OP_IDS, records_to_relational_arrays
from reasoning_dsl.relational_task_schema_arrays import (
    FACT_PRED_IDS as SCHEMA_FACT_PRED_IDS,
    FACT_PREDICATE_CLASSES as SCHEMA_FACT_PREDICATE_CLASSES,
    OP_IDS as SCHEMA_OP_IDS,
    V2_LEGACY_FACT_PREDICATES,
    fact_predicate_generality_report,
    records_to_task_schema_arrays,
)
from reasoning_dsl.relational import task_schema_record


def test_task_schema_fact_predicates_are_classified_for_v2_cleanup() -> None:
    assert set(SCHEMA_FACT_PRED_IDS) == set(SCHEMA_FACT_PREDICATE_CLASSES)

    report = fact_predicate_generality_report()

    assert report["legacy_task_schema"] == sorted(V2_LEGACY_FACT_PREDICATES)
    assert {"SOURCE_FACT", "SOURCE_RULE"} <= V2_LEGACY_FACT_PREDICATES
    assert "RELATION_TUPLE" in report["core_schema"]
    assert "QUERY_RELATION" in report["core_schema"]
    assert "RULE_LHS" in report["domain_schema"]
    assert "unclassified" not in report


def test_path_relational_arrays_encode_graph_action_repair_and_verify() -> None:
    generator = GraphReachabilityGenerator()
    problem = generator.generate(1, {"num_nodes": 6, "path_length": 3, "extra_edges": 1})
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action", "repair_action", "verify"],
        repair_action_format="local",
    )
    records = [model_view(relational_record(example)) for example in examples]

    bundle = records_to_relational_arrays(records)

    assert bundle.metadata["families"] == ["graph_reachability"]
    assert bundle.arrays["object_types"].shape[0] == len(records)
    assert bundle.arrays["fact_args"].shape[2] == 2
    assert OP_IDS["APPEND"] in set(bundle.arrays["target_ops"].tolist())
    assert OP_IDS["REPLACE_AFTER"] in set(bundle.arrays["target_ops"].tolist())
    assert OP_IDS["VERIFY"] in set(bundle.arrays["target_ops"].tolist())
    assert np.any(bundle.arrays["target_validity"] != 0)


def test_path_relational_arrays_encode_tree_descend() -> None:
    generator = TreeAncestryGenerator()
    problem = generator.generate(1, {"depth": 3, "branching_factor": 2, "distractor_subtrees": 1})
    example = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
    )[0]

    bundle = records_to_relational_arrays([model_view(relational_record(example))])

    assert bundle.metadata["families"] == ["tree_ancestry"]
    assert bundle.arrays["target_ops"].tolist() == [OP_IDS["DESCEND"]]


def test_task_schema_arrays_use_generic_graph_tree_predicates() -> None:
    graph = GraphReachabilityGenerator()
    graph_problem = graph.generate(1, {"num_nodes": 6, "path_length": 3, "extra_edges": 1})
    graph_examples = build_examples_for_problem(
        generator=graph,
        problem=graph_problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action", "repair_action", "verify"],
        repair_action_format="local",
    )
    tree = TreeAncestryGenerator()
    tree_problem = tree.generate(1, {"depth": 3, "branching_factor": 2, "distractor_subtrees": 1})
    tree_examples = build_examples_for_problem(
        generator=tree,
        problem=tree_problem,
        split="train",
        problem_index=1,
        seed=2,
        modes=["action", "repair_action", "verify"],
        repair_action_format="local",
    )

    records = [model_view(task_schema_record(example)) for example in [*graph_examples, *tree_examples]]
    bundle = records_to_task_schema_arrays(records)

    assert bundle.metadata["schema_version"] == "relational_task_schema_arrays_v1"
    assert bundle.metadata["families"] == ["graph_reachability", "tree_ancestry"]
    assert bundle.metadata["object_type_ids"]["entity"] == 1
    assert bundle.metadata["object_type_ids"]["predicate"] == 2
    assert bundle.metadata["object_type_ids"]["operation"] == 3
    assert bundle.metadata["object_type_ids"]["location_root"] == 12
    assert bundle.metadata["object_type_ids"]["location_after"] == 13
    assert "EDGE" not in bundle.metadata["fact_pred_ids"]
    assert "PARENT" not in bundle.metadata["fact_pred_ids"]
    assert "APPEND" not in bundle.metadata["op_ids"]
    assert "DESCEND" not in bundle.metadata["op_ids"]

    fact_values = set(bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert SCHEMA_FACT_PRED_IDS["SCHEMA_BINARY_REL"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["SCHEMA_SEQUENCE_STATE"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["SCHEMA_EXTEND_ACTION"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["RELATION_TUPLE"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["QUERY_RELATION"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["STATE_LAST"] in fact_values

    target_ops = set(bundle.arrays["target_ops"].tolist())
    assert SCHEMA_OP_IDS["EXTEND_SEQUENCE"] in target_ops
    assert SCHEMA_OP_IDS["REPLACE_ITEM"] in target_ops
    assert "REPLACE_ROOT" not in bundle.metadata["active_ops"]
    assert "REPLACE_AFTER" not in bundle.metadata["active_ops"]
    assert SCHEMA_OP_IDS["VERIFY"] in target_ops
    assert np.any(bundle.arrays["target_validity"] != 0)


def test_task_schema_arrays_can_fail_on_legacy_predicates() -> None:
    graph = GraphReachabilityGenerator()
    graph_problem = graph.generate(1, {"num_nodes": 6, "path_length": 3, "extra_edges": 1})
    graph_example = build_examples_for_problem(
        generator=graph,
        problem=graph_problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
    )[0]

    bundle = records_to_task_schema_arrays(
        [model_view(task_schema_record(graph_example))],
        fail_on_legacy_predicates=True,
    )
    assert bundle.metadata["active_legacy_fact_predicates"] == []
    assert "SCHEMA_SEQUENCE_STATE" in bundle.metadata["active_fact_predicate_classes"]["core_schema"]

    legacy_record = model_view(task_schema_record(graph_example))
    legacy_record["facts"] = [*legacy_record["facts"], {"pred": "SOURCE_FACT", "args": []}]

    with pytest.raises(ValueError, match="Legacy task-schema fact predicates"):
        records_to_task_schema_arrays(
            [legacy_record],
            fail_on_legacy_predicates=True,
        )


def test_task_schema_arrays_encode_implication_with_generic_source_facts() -> None:
    generator = ImplicationChainGenerator()
    problem = generator.generate(1, {"chain_length": 3, "distractor_rules": 1})
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action", "repair_action", "verify"],
        repair_action_format="local",
    )
    records = [model_view(task_schema_record(example)) for example in examples]

    bundle = records_to_task_schema_arrays(records)

    assert bundle.metadata["families"] == ["implication_chains"]
    assert bundle.metadata["object_type_ids"]["field"] == 11
    assert "HYP_FACT" not in bundle.metadata["fact_pred_ids"]
    assert "HYP_RULE" not in bundle.metadata["fact_pred_ids"]
    fact_values = set(bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert SCHEMA_FACT_PRED_IDS["SCHEMA_SEQUENCE_STATE"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["SCHEMA_EXTEND_ACTION"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["RELATION_TUPLE"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["SOURCE_FACT"] not in fact_values
    assert SCHEMA_FACT_PRED_IDS["SOURCE_RULE"] not in fact_values
    assert SCHEMA_FACT_PRED_IDS["STATE_ITEM"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["STATE_USED_SOURCE"] in fact_values
    assert SCHEMA_OP_IDS["EXTEND_SEQUENCE"] in set(bundle.arrays["target_ops"].tolist())
    assert SCHEMA_OP_IDS["REPLACE_FIELD"] in set(bundle.arrays["target_ops"].tolist())
    assert "APPLY" not in bundle.metadata["active_ops"]
    assert "REPLACE_FIELD_HYP" not in bundle.metadata["active_ops"]
    assert "REPLACE_FIELD_FROM" not in bundle.metadata["active_ops"]
    assert np.any(bundle.arrays["target_validity"] != 0)


def test_task_schema_arrays_encode_relation_with_generic_source_facts() -> None:
    generator = RelationCompositionGenerator()
    problem = generator.generate(1, {"chain_length": 3, "distractor_facts": 1})
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action", "repair_action", "verify"],
        repair_action_format="local",
        relation_action_format="follow_left",
    )
    records = [model_view(task_schema_record(example)) for example in examples]

    bundle = records_to_task_schema_arrays(records)

    assert bundle.metadata["families"] == ["relation_composition"]
    assert "FACT" not in bundle.metadata["fact_pred_ids"]
    assert "RULE_COMPOSE" not in bundle.metadata["fact_pred_ids"]
    assert bundle.metadata["active_legacy_fact_predicates"] == []
    assert "EXTEND_SEQUENCE" in bundle.metadata["active_ops"]
    assert "FOLLOW" not in bundle.metadata["active_ops"]
    assert "REPLACE_FIELD" in bundle.metadata["active_ops"]
    assert "REPLACE_FIELD_VIA" not in bundle.metadata["active_ops"]
    fact_values = set(bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert SCHEMA_FACT_PRED_IDS["SCHEMA_SEQUENCE_STATE"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["SCHEMA_EXTEND_ACTION"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["SCHEMA_RELATION_STATE"] not in fact_values
    assert SCHEMA_FACT_PRED_IDS["SCHEMA_FOLLOW_ACTION"] not in fact_values
    assert SCHEMA_FACT_PRED_IDS["RELATION_TUPLE"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["COMPOSE_RULE"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["QUERY_RELATION"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["QUERY_TUPLE"] not in fact_values
    assert SCHEMA_FACT_PRED_IDS["QUERY_START"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["QUERY_GOAL"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["STATE_ITEM"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["STATE_SUPPORT"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["STATE_RELATION_TUPLE"] not in fact_values
    assert SCHEMA_FACT_PRED_IDS["STATE_VIA"] not in fact_values
    assert SCHEMA_OP_IDS["EXTEND_SEQUENCE"] in set(bundle.arrays["target_ops"].tolist())
    assert SCHEMA_OP_IDS["REPLACE_FIELD"] in set(bundle.arrays["target_ops"].tolist())
    assert np.any(bundle.arrays["target_validity"] != 0)


def test_path_relational_arrays_are_alpha_invariant() -> None:
    generator = GraphReachabilityGenerator()
    problem = generator.generate(1, {"num_nodes": 6, "path_length": 3, "extra_edges": 1})
    example = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
    )[1]
    renamed = _rename_entities(example, {"e0": "banana", "e1": "moon", "e2": "chair", "e3": "lamp", "e4": "sky", "e5": "river"})

    original = records_to_relational_arrays([model_view(relational_record(example))])
    alpha = records_to_relational_arrays([model_view(relational_record(renamed))])

    assert original.metadata == alpha.metadata
    assert original.arrays.keys() == alpha.arrays.keys()
    for name in original.arrays:
        assert np.array_equal(original.arrays[name], alpha.arrays[name]), name


def test_relational_arrays_encode_implication_actions() -> None:
    generator = ImplicationChainGenerator()
    problem = generator.generate(1, {"chain_length": 3, "distractor_rules": 1})
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action", "repair_action", "verify"],
        repair_action_format="local",
    )
    records = [model_view(relational_record(example)) for example in examples]

    bundle = records_to_relational_arrays(records)

    assert bundle.metadata["families"] == ["implication_chains"]
    assert bundle.metadata["max_fact_args"] == 3
    assert OP_IDS["APPLY"] in set(bundle.arrays["target_ops"].tolist())
    assert OP_IDS["REPLACE_FIELD_HYP"] in set(bundle.arrays["target_ops"].tolist())
    assert FACT_PRED_IDS["STATE_DERIVE"] in set(bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert FACT_PRED_IDS["STATE_KNOWN"] in set(bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert bundle.metadata["max_state_len"] <= 4


def test_relational_arrays_encode_relation_follow_with_three_args() -> None:
    generator = RelationCompositionGenerator()
    problem = generator.generate(1, {"chain_length": 3, "distractor_facts": 1})
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action", "repair_action", "verify"],
        repair_action_format="local",
    )
    records = [model_view(relational_record(example)) for example in examples]

    bundle = records_to_relational_arrays(records)

    assert bundle.metadata["families"] == ["relation_composition"]
    assert bundle.metadata["max_fact_args"] == 4
    assert bundle.metadata["max_target_args"] >= 2
    assert OP_IDS["FOLLOW"] in set(bundle.arrays["target_ops"].tolist())
    assert OP_IDS["REPLACE_FIELD_VIA"] in set(bundle.arrays["target_ops"].tolist())


def test_relational_arrays_encode_term_rewriting_without_symbol_tokens() -> None:
    generator = TermRewritingGenerator()
    problem = generator.generate(1, {"rewrite_steps": 3, "distractor_rules": 1})
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action", "repair_action", "verify"],
        repair_action_format="local",
    )
    records = [model_view(relational_record(example)) for example in examples]

    bundle = records_to_relational_arrays(records)

    assert bundle.metadata["families"] == ["term_rewriting"]
    assert "term_node" in bundle.metadata["object_type_ids"]
    assert FACT_PRED_IDS["TERM_UNARY"] in set(bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert FACT_PRED_IDS["RULE_LHS"] in set(bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert FACT_PRED_IDS["STATE_RW_STEP"] in set(bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert FACT_PRED_IDS["STATE_RW_EXPECTED"] in set(bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert FACT_PRED_IDS["STATE_RW_RESULT"] in set(bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert OP_IDS["RW"] in set(bundle.arrays["target_ops"].tolist())
    target_ops = set(bundle.arrays["target_ops"].tolist())
    assert OP_IDS["REPAIR_FIRST_BAD"] in target_ops or OP_IDS["REPAIR_REWRITE"] in target_ops


def test_task_schema_arrays_encode_term_rewriting_contract() -> None:
    generator = TermRewritingGenerator()
    problem = generator.generate(1, {"rewrite_steps": 3, "distractor_rules": 1})
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action", "repair_action", "verify"],
        repair_action_format="local",
    )
    records = [model_view(task_schema_record(example)) for example in examples]

    bundle = records_to_task_schema_arrays(records)

    assert bundle.metadata["families"] == ["term_rewriting"]
    assert "term_node" in bundle.metadata["object_type_ids"]
    assert "property" in bundle.metadata["object_type_ids"]
    fact_values = set(bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert SCHEMA_FACT_PRED_IDS["SCHEMA_SEQUENCE_STATE"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["SCHEMA_EXTEND_ACTION"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["SCHEMA_HALT_ACTION"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["NODE_CONST"] in fact_values or SCHEMA_FACT_PRED_IDS["NODE_VAR"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["NODE_UNARY"] in fact_values or SCHEMA_FACT_PRED_IDS["NODE_BINARY"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["RULE_INPUT"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["RULE_OUTPUT"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["STATE_ITEM"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["TRANSITION_STEP"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["TRANSITION_EXPECTED"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["TRANSITION_RESULT"] in fact_values
    assert SCHEMA_FACT_PRED_IDS["SCHEMA_REWRITE_STATE"] not in fact_values
    assert SCHEMA_FACT_PRED_IDS["TERM_UNARY"] not in fact_values
    assert SCHEMA_FACT_PRED_IDS["RULE_LHS"] not in fact_values
    assert SCHEMA_FACT_PRED_IDS["STATE_RW_STEP"] not in fact_values
    target_ops = set(bundle.arrays["target_ops"].tolist())
    assert SCHEMA_OP_IDS["EXTEND_SEQUENCE"] in target_ops
    assert "RW" not in bundle.metadata["active_ops"]
    assert "HALT" not in bundle.metadata["active_ops"]
    assert SCHEMA_OP_IDS["REPAIR_FIRST_BAD"] in target_ops or SCHEMA_OP_IDS["REPAIR_REWRITE"] in target_ops


def test_relational_arrays_encode_lite_new_families() -> None:
    dfa = DfaSimulationLiteGenerator()
    dfa_problem = dfa.generate(1, {"input_length": 3, "relation_count": 3, "num_states": 8, "distractor_facts": 2})
    dfa_examples = build_examples_for_problem(
        generator=dfa,
        problem=dfa_problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action", "repair_action", "verify"],
        repair_action_format="local",
    )
    dfa_bundle = records_to_relational_arrays([model_view(relational_record(example)) for example in dfa_examples])

    assert dfa_bundle.metadata["families"] == ["dfa_simulation_lite"]
    assert FACT_PRED_IDS["INPUT_REL"] in set(dfa_bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert FACT_PRED_IDS["INPUT_FIRST"] in set(dfa_bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert FACT_PRED_IDS["INPUT_NEXT"] in set(dfa_bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert OP_IDS["APPEND"] in set(dfa_bundle.arrays["target_ops"].tolist())

    equality = EqualityRewritingLiteGenerator()
    equality_problem = equality.generate(1, {"rewrite_steps": 3, "distractor_rules": 1, "reverse_rule_rate": 0.5})
    equality_examples = build_examples_for_problem(
        generator=equality,
        problem=equality_problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action", "repair_action", "verify"],
        repair_action_format="local",
    )
    equality_bundle = records_to_relational_arrays([model_view(relational_record(example)) for example in equality_examples])

    assert equality_bundle.metadata["families"] == ["equality_rewriting_lite"]
    assert FACT_PRED_IDS["RULE_LHS"] in set(equality_bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert FACT_PRED_IDS["STATE_RW_STEP"] in set(equality_bundle.arrays["fact_preds"].reshape(-1).tolist())
    assert OP_IDS["RW"] in set(equality_bundle.arrays["target_ops"].tolist())


def _rename_entities(example: Example, mapping: dict[str, str]) -> Example:
    def rename_line(line: str) -> str:
        return " ".join(mapping.get(token, token) for token in line.split())

    return replace(
        example,
        problem_lines=[rename_line(line) for line in example.problem_lines],
        state_lines=[rename_line(line) for line in example.state_lines],
        target_lines=[rename_line(line) for line in example.target_lines],
    )
