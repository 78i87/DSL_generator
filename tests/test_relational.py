from __future__ import annotations

import re
from dataclasses import replace

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
from reasoning_dsl.relational import model_view, relational_record, task_schema_record


def test_graph_relational_record_has_anonymous_objects() -> None:
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

    record = relational_record(example)

    assert record["objects"] == [{"type": "entity"} for _ in record["objects"]]
    assert {"object": 0, "type": "entity", "name": "e0"} in record["external_names"]
    assert record["state"] == {"kind": "sequence", "pred": "PATH", "objects": [0]}
    assert record["target"] == {"kind": "action", "op": "APPEND", "args": [1]}
    assert "e0" not in str(model_view(record))


def test_tree_relational_record_uses_same_path_contract() -> None:
    generator = TreeAncestryGenerator()
    problem = generator.generate(1, {"depth": 3, "branching_factor": 2, "distractor_subtrees": 1})
    example = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
    )[1]

    record = relational_record(example)

    assert record["facts"][0]["pred"] == "PARENT"
    assert record["state"]["pred"] == "LINEAGE"
    assert record["target"]["op"] == "DESCEND"
    assert "e0" not in str(model_view(record))


def test_path_task_schema_record_removes_family_specific_predicates() -> None:
    graph = GraphReachabilityGenerator()
    graph_problem = graph.generate(1, {"num_nodes": 6, "path_length": 3, "extra_edges": 1})
    graph_example = build_examples_for_problem(
        generator=graph,
        problem=graph_problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
    )[1]

    tree = TreeAncestryGenerator()
    tree_problem = tree.generate(1, {"depth": 3, "branching_factor": 2, "distractor_subtrees": 1})
    tree_example = build_examples_for_problem(
        generator=tree,
        problem=tree_problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
    )[0]

    graph_record = task_schema_record(graph_example)
    tree_record = task_schema_record(tree_example)
    graph_view = model_view(graph_record)
    tree_view = model_view(tree_record)

    assert graph_record["schema_version"] == "relational_task_schema_v1"
    assert tree_record["schema_version"] == "relational_task_schema_v1"
    assert {"SCHEMA_BINARY_REL", "SCHEMA_SEQUENCE_STATE", "SCHEMA_EXTEND_ACTION", "RELATION_TUPLE"} <= {
        fact["pred"] for fact in graph_record["facts"]
    }
    assert {"SCHEMA_BINARY_REL", "SCHEMA_SEQUENCE_STATE", "SCHEMA_EXTEND_ACTION", "RELATION_TUPLE"} <= {
        fact["pred"] for fact in tree_record["facts"]
    }
    assert graph_record["target"]["op"] == "EXTEND_SEQUENCE"
    assert tree_record["target"]["op"] == "EXTEND_SEQUENCE"
    assert {"type": "predicate", "name": "EDGE"} in [
        {"type": item["type"], "name": item["name"]} for item in graph_record["external_names"]
    ]
    assert {"type": "predicate", "name": "PARENT"} in [
        {"type": item["type"], "name": item["name"]} for item in tree_record["external_names"]
    ]
    for forbidden in ["EDGE", "PARENT", "PATH", "LINEAGE", "REACH", "ANCESTOR", "APPEND", "DESCEND"]:
        assert forbidden not in str(graph_view)
        assert forbidden not in str(tree_view)


def test_alpha_renaming_changes_only_external_name_table() -> None:
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

    original_record = relational_record(example)
    renamed_record = relational_record(renamed)

    assert model_view(original_record) == model_view(renamed_record)
    assert original_record["external_names"] != renamed_record["external_names"]
    assert {"object": 0, "type": "entity", "name": "banana"} in renamed_record["external_names"]


def test_task_schema_alpha_renaming_is_invariant_across_current_families() -> None:
    cases = [
        (
            GraphReachabilityGenerator(),
            {"num_nodes": 6, "path_length": 3, "extra_edges": 1},
        ),
        (
            ImplicationChainGenerator(),
            {"chain_length": 3, "distractor_rules": 1},
        ),
        (
            RelationCompositionGenerator(),
            {"chain_length": 3, "distractor_facts": 1},
        ),
        (
            TreeAncestryGenerator(),
            {"depth": 3, "branching_factor": 2, "distractor_subtrees": 1},
        ),
        (
            TermRewritingGenerator(),
            {
                "rewrite_steps": 3,
                "term_depth": 3,
                "distractor_rules": 1,
                "variable_rule_rate": 0.5,
                "binary_rule_rate": 0.3,
                "normal_form_rate": 0.0,
            },
        ),
    ]

    for generator, difficulty in cases:
        problem = generator.generate(1, difficulty)
        example = build_examples_for_problem(
            generator=generator,
            problem=problem,
            split="train",
            problem_index=0,
            seed=1,
            modes=["action"],
            relation_action_format="follow_left",
        )[0]
        renamed = _rename_symbols(example)

        original_record = task_schema_record(example)
        renamed_record = task_schema_record(renamed)

        assert model_view(original_record) == model_view(renamed_record), example.family
        assert original_record["external_names"] != renamed_record["external_names"], example.family


def test_implication_relational_record_anonymizes_hypotheses_and_props() -> None:
    generator = ImplicationChainGenerator()
    problem = generator.generate(1, {"num_props": 6, "proof_length": 3, "distractor_hyps": 1})
    example = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
    )[0]

    record = relational_record(example)

    assert any(fact["pred"] == "HYP_FACT" for fact in record["facts"])
    assert record["target"]["op"] == "APPLY"
    assert "h0" not in str(model_view(record))
    assert "p0" not in str(model_view(record))


def test_implication_task_schema_record_uses_generic_source_facts() -> None:
    generator = ImplicationChainGenerator()
    problem = generator.generate(1, {"num_props": 6, "proof_length": 3, "distractor_hyps": 1})
    example = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
    )[0]

    record = task_schema_record(example)
    view = model_view(record)

    assert record["schema_version"] == "relational_task_schema_v1"
    assert {"SCHEMA_SEQUENCE_STATE", "SCHEMA_EXTEND_ACTION", "SCHEMA_BINARY_REL", "RELATION_TUPLE"} <= {
        fact["pred"] for fact in record["facts"]
    }
    assert "SOURCE_FACT" not in {fact["pred"] for fact in record["facts"]}
    assert "SOURCE_RULE" not in {fact["pred"] for fact in record["facts"]}
    assert record["target"]["op"] == "EXTEND_SEQUENCE"
    assert record["objects"][record["target"]["args"][0]]["type"] == "operation"
    assert record["state"]["predicate"] >= 0
    assert "HYP_FACT" not in str(view)
    assert "HYP_RULE" not in str(view)
    assert "h0" not in str(view)
    assert "p0" not in str(view)


def test_relation_relational_record_anonymizes_relation_symbols_and_entities() -> None:
    generator = RelationCompositionGenerator()
    problem = generator.generate(1, {"num_entities": 6, "composition_depth": 3, "distractor_facts": 1})
    example = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
    )[0]

    record = relational_record(example)

    assert any(fact["pred"] == "RULE_COMPOSE" for fact in record["facts"])
    assert record["target"]["op"] in {"FOLLOW", "COMPOSE", "ADD_DERIVE"}
    assert "r0" not in str(model_view(record))
    assert "e0" not in str(model_view(record))


def test_relation_task_schema_record_uses_generic_relation_facts() -> None:
    generator = RelationCompositionGenerator()
    problem = generator.generate(1, {"num_entities": 6, "composition_depth": 3, "distractor_facts": 1})
    example = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
        relation_action_format="follow_left",
    )[0]

    record = task_schema_record(example)
    view = model_view(record)

    assert record["schema_version"] == "relational_task_schema_v1"
    fact_preds = {fact["pred"] for fact in record["facts"]}
    assert {"SCHEMA_SEQUENCE_STATE", "SCHEMA_EXTEND_ACTION", "RELATION_TUPLE", "COMPOSE_RULE"} <= {
        fact["pred"] for fact in record["facts"]
    }
    assert {"QUERY_RELATION", "QUERY_START", "QUERY_GOAL"} <= fact_preds
    assert "QUERY_TUPLE" not in fact_preds
    assert "SCHEMA_RELATION_STATE" not in fact_preds
    assert "SCHEMA_FOLLOW_ACTION" not in fact_preds
    assert record["target"]["op"] == "EXTEND_SEQUENCE"
    assert record["objects"][record["target"]["args"][0]]["type"] == "operation"
    assert "RULE_COMPOSE" not in str(view)
    assert "FACT" not in str(view)
    assert "r0" not in str(view)
    assert "e0" not in str(view)


def test_term_relational_record_anonymizes_rules_functions_and_entities() -> None:
    generator = TermRewritingGenerator()
    problem = generator.generate(
        1,
        {
            "rewrite_steps": 3,
            "term_depth": 3,
            "distractor_rules": 1,
            "variable_rule_rate": 0.5,
            "binary_rule_rate": 0.3,
            "normal_form_rate": 0.0,
        },
    )
    example = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
    )[0]

    record = relational_record(example)
    view = str(model_view(record))

    assert any(fact["pred"] == "RULE" for fact in record["facts"])
    assert record["target"]["op"] in {"RW", "HALT"}
    assert "r0" not in view
    assert "f0" not in view
    assert "e0" not in view


def test_term_task_schema_record_declares_rewrite_contract() -> None:
    generator = TermRewritingGenerator()
    problem = generator.generate(
        1,
        {
            "rewrite_steps": 3,
            "term_depth": 3,
            "distractor_rules": 1,
            "variable_rule_rate": 0.5,
            "binary_rule_rate": 0.3,
            "normal_form_rate": 0.0,
        },
    )
    example = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
    )[0]

    record = task_schema_record(example)
    view = str(model_view(record))

    assert record["schema_version"] == "relational_task_schema_v1"
    assert {"SCHEMA_SEQUENCE_STATE", "SCHEMA_EXTEND_ACTION", "SCHEMA_HALT_ACTION"} <= {
        fact["pred"] for fact in record["facts"]
    }
    assert record["state"]["kind"] == "rewrite_trace"
    assert "predicate" in record["state"]
    assert record["target"]["op"] == "EXTEND_SEQUENCE"
    assert record["objects"][record["target"]["args"][0]]["type"] == "operation"
    assert "r0" not in view
    assert "f0" not in view
    assert "e0" not in view


def test_lite_new_families_have_relational_views() -> None:
    dfa = DfaSimulationLiteGenerator()
    dfa_problem = dfa.generate(1, {"input_length": 3, "relation_count": 3, "num_states": 8, "distractor_facts": 2})
    dfa_example = build_examples_for_problem(
        generator=dfa,
        problem=dfa_problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
    )[0]
    dfa_record = relational_record(dfa_example)

    assert any(fact["pred"] == "INPUT_REL" for fact in dfa_record["facts"])
    assert any(fact["pred"] == "INPUT_FIRST" for fact in dfa_record["facts"])
    assert any(fact["pred"] == "INPUT_NEXT" for fact in dfa_record["facts"])
    assert dfa_record["target"]["op"] == "APPEND"
    assert "h0" not in str(model_view(dfa_record))
    assert "r0" not in str(model_view(dfa_record))

    equality = EqualityRewritingLiteGenerator()
    equality_problem = equality.generate(1, {"rewrite_steps": 3, "distractor_rules": 1, "reverse_rule_rate": 0.5})
    equality_example = build_examples_for_problem(
        generator=equality,
        problem=equality_problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
    )[0]
    equality_record = relational_record(equality_example)

    assert any(fact["pred"] == "RULE" for fact in equality_record["facts"])
    assert equality_record["target"]["op"] == "RW"
    assert "r0" not in str(model_view(equality_record))
    assert "f0" not in str(model_view(equality_record))


def _rename_entities(example: Example, mapping: dict[str, str]) -> Example:
    def rename_line(line: str) -> str:
        return " ".join(mapping.get(token, token) for token in line.split())

    return replace(
        example,
        problem_lines=[rename_line(line) for line in example.problem_lines],
        state_lines=[rename_line(line) for line in example.state_lines],
        target_lines=[rename_line(line) for line in example.target_lines],
    )


def _rename_symbols(example: Example) -> Example:
    mapping: dict[str, str] = {}

    def rename_token(token: str) -> str:
        if not re.fullmatch(r"[efhpr]\d+", token):
            return token
        if token not in mapping:
            mapping[token] = f"{token[0]}x{len(mapping)}"
        return mapping[token]

    def rename_line(line: str) -> str:
        return " ".join(rename_token(token) for token in line.split())

    return replace(
        example,
        problem_lines=[rename_line(line) for line in example.problem_lines],
        state_lines=[rename_line(line) for line in example.state_lines],
        target_lines=[rename_line(line) for line in example.target_lines],
    )
