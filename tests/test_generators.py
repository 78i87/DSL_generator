from __future__ import annotations

from reasoning_dsl.core import build_examples_for_problem
from reasoning_dsl.generators import (
    GraphReachabilityGenerator,
    ImplicationChainGenerator,
    RelationCompositionGenerator,
    TermRewritingGenerator,
    TreeAncestryGenerator,
)


def test_generators_verify_final_and_reject_corruption() -> None:
    cases = [
        (GraphReachabilityGenerator(), {"num_nodes": 7, "path_length": 3, "extra_edges": 2, "require_shortest": True}),
        (ImplicationChainGenerator(), {"num_props": 7, "proof_length": 3, "distractor_hyps": 2}),
        (RelationCompositionGenerator(), {"num_entities": 7, "composition_depth": 3, "distractor_facts": 2}),
        (TreeAncestryGenerator(), {"depth": 3, "branching_factor": 2, "distractor_subtrees": 2}),
        (
            TermRewritingGenerator(),
            {
                "rewrite_steps": 3,
                "term_depth": 4,
                "distractor_rules": 2,
                "variable_rule_rate": 0.5,
                "binary_rule_rate": 0.5,
                "normal_form_rate": 0.5,
            },
        ),
    ]
    for generator, difficulty in cases:
        problem = generator.generate(123, difficulty)
        valid = generator.verify(problem, problem.final_state)
        assert valid.valid, generator.family

        corrupted = generator.corrupt(456, problem, problem.final_state)
        invalid = generator.verify(problem, corrupted)
        assert not invalid.valid, generator.family
        assert invalid.error_code is not None


def test_improve_targets_one_primitive_step() -> None:
    generator = GraphReachabilityGenerator()
    problem = generator.generate(1, {"num_nodes": 6, "path_length": 3, "extra_edges": 1})
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["improve"],
    )
    assert len(examples) == len(problem.canonical_states) - 1
    for idx, example in enumerate(examples):
        assert example.state_lines == problem.canonical_states[idx]
        assert example.target_lines == problem.canonical_states[idx + 1]


def test_action_targets_one_delta_line_with_next_state_metadata() -> None:
    cases = [
        (
            GraphReachabilityGenerator(),
            {"num_nodes": 6, "path_length": 3, "extra_edges": 1, "require_shortest": True},
            "APPEND ",
        ),
        (
            ImplicationChainGenerator(),
            {"num_props": 6, "proof_length": 3, "distractor_hyps": 1},
            "APPLY ",
        ),
        (
            RelationCompositionGenerator(),
            {"num_entities": 6, "composition_depth": 3, "distractor_facts": 1},
            "FOLLOW ",
        ),
        (
            TreeAncestryGenerator(),
            {"depth": 3, "branching_factor": 2, "distractor_subtrees": 1},
            "DESCEND ",
        ),
    ]

    for generator, difficulty, expected_prefix in cases:
        problem = generator.generate(1, difficulty)
        examples = build_examples_for_problem(
            generator=generator,
            problem=problem,
            split="train",
            problem_index=0,
            seed=1,
            modes=["action"],
        )

        assert len(examples) == len(problem.canonical_states) - 1
        for idx, example in enumerate(examples):
            assert example.mode == "action"
            assert len(example.target_lines) == 1
            assert example.target_lines[0].startswith(expected_prefix)
            assert example.state_lines == problem.canonical_states[idx]
            assert example.meta["next_state_lines"] == problem.canonical_states[idx + 1]
            assert example.meta["final_state_lines"] == problem.final_state


def test_relation_action_targets_can_use_disambiguated_compose_form() -> None:
    generator = RelationCompositionGenerator()
    problem = generator.generate(1, {"num_entities": 6, "composition_depth": 3, "distractor_facts": 1})
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
        relation_action_format="compose",
    )

    assert examples
    assert all(example.target_lines[0].startswith("COMPOSE ") for example in examples)
    assert examples[0].target_lines == ["COMPOSE r0 e0 r1 e2 VIA e1"]
    assert examples[0].meta["next_state_lines"] == problem.canonical_states[1]


def test_relation_action_targets_can_use_left_entity_follow_form() -> None:
    generator = RelationCompositionGenerator()
    problem = generator.generate(1, {"num_entities": 6, "composition_depth": 3, "distractor_facts": 1})
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
        relation_action_format="follow_left",
    )

    assert examples
    assert examples[0].target_lines == ["FOLLOW e0 e2 VIA e1"]
    assert examples[0].meta["next_state_lines"] == problem.canonical_states[1]


def test_term_rewriting_action_targets_include_rewrite_and_halt() -> None:
    generator = TermRewritingGenerator()
    problem = generator.generate(
        1,
        {
            "rewrite_steps": 3,
            "term_depth": 4,
            "distractor_rules": 2,
            "variable_rule_rate": 1.0,
            "binary_rule_rate": 0.5,
            "normal_form_rate": 1.0,
        },
    )
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["action"],
    )

    assert examples
    assert all(example.target_lines[0].startswith("RW ") for example in examples[:-1])
    assert examples[-1].target_lines == ["HALT"]
    assert examples[-1].meta["next_state_lines"] == problem.final_state


def test_repair_action_targets_one_compact_edit() -> None:
    cases = [
        (
            GraphReachabilityGenerator(),
            {"num_nodes": 6, "path_length": 3, "extra_edges": 1, "require_shortest": True},
            "REPLACE NODE ",
        ),
        (
            ImplicationChainGenerator(),
            {"num_props": 6, "proof_length": 3, "distractor_hyps": 1},
            "REPLACE LINE ",
        ),
        (
            RelationCompositionGenerator(),
            {"num_entities": 6, "composition_depth": 3, "distractor_facts": 1},
            "REPLACE LINE ",
        ),
        (
            TreeAncestryGenerator(),
            {"depth": 3, "branching_factor": 2, "distractor_subtrees": 1},
            "REPLACE NODE ",
        ),
    ]

    for generator, difficulty, expected_prefix in cases:
        problem = generator.generate(1, difficulty)
        examples = build_examples_for_problem(
            generator=generator,
            problem=problem,
            split="train",
            problem_index=0,
            seed=1,
            modes=["repair_action"],
        )

        assert len(examples) == len(problem.canonical_states) - 1
        for idx, example in enumerate(examples, start=1):
            assert example.mode == "repair_action"
            assert len(example.target_lines) == 1
            assert example.target_lines[0].startswith(expected_prefix)
            if generator.family in {"implication_chains", "relation_composition"}:
                assert " WITH DERIVE " not in example.target_lines[0]
            assert example.state_lines != problem.canonical_states[idx]
            assert example.meta["repaired_state_lines"] == problem.canonical_states[idx]


def test_tree_repair_action_targets_can_use_local_after_form() -> None:
    generator = TreeAncestryGenerator()
    problem = generator.generate(1, {"depth": 3, "branching_factor": 2, "distractor_subtrees": 1})
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["repair_action"],
        tree_repair_action_format="after",
    )

    assert examples
    assert examples[0].target_lines == ["REPLACE ROOT WITH e0"]
    assert all(
        line.startswith("REPLACE ROOT WITH ") or line.startswith("REPLACE AFTER ")
        for example in examples
        for line in example.target_lines
    )


def test_repair_action_targets_can_use_local_context_form() -> None:
    cases = [
        (
            GraphReachabilityGenerator(),
            {"num_nodes": 6, "path_length": 3, "extra_edges": 1, "require_shortest": True},
            ("REPLACE ROOT WITH ", "REPLACE AFTER "),
        ),
        (
            ImplicationChainGenerator(),
            {"num_props": 6, "proof_length": 3, "distractor_hyps": 1},
            ("REPLACE FIRST ", "REPLACE AFTER "),
        ),
        (
            RelationCompositionGenerator(),
            {"num_entities": 6, "composition_depth": 3, "distractor_facts": 1},
            ("REPLACE FIRST ", "REPLACE AFTER "),
        ),
        (
            TreeAncestryGenerator(),
            {"depth": 3, "branching_factor": 2, "distractor_subtrees": 1},
            ("REPLACE ROOT WITH ", "REPLACE AFTER "),
        ),
    ]

    for generator, difficulty, expected_prefixes in cases:
        problem = generator.generate(1, difficulty)
        examples = build_examples_for_problem(
            generator=generator,
            problem=problem,
            split="train",
            problem_index=0,
            seed=1,
            modes=["repair_action"],
            repair_action_format="local",
        )

        assert examples
        assert all(example.target_lines[0].startswith(expected_prefixes) for example in examples)


def test_term_rewriting_repair_action_targets_visible_rewrite() -> None:
    generator = TermRewritingGenerator()
    problem = generator.generate(
        2,
        {
            "rewrite_steps": 4,
            "term_depth": 5,
            "distractor_rules": 3,
            "variable_rule_rate": 0.8,
            "binary_rule_rate": 0.8,
            "normal_form_rate": 1.0,
        },
    )
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=2,
        modes=["repair_action"],
    )

    assert examples
    assert all(example.target_lines[0].startswith("REPAIR RW ") for example in examples)
    for example in examples:
        assert not generator.verify(problem, example.state_lines).valid
        assert example.meta["repaired_state_lines"] == problem.canonical_states[example.meta["target_step"]]
    assert generator.verify(problem, problem.final_state).valid


def test_verify_examples_are_balanced_valid_invalid() -> None:
    generator = ImplicationChainGenerator()
    problem = generator.generate(1, {"num_props": 6, "proof_length": 3, "distractor_hyps": 2})
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["verify"],
    )
    targets = [example.target_lines[0] for example in examples]
    assert targets[0] == "VALID"
    assert targets[1].startswith("INVALID ")


def test_single_error_verify_corruption_avoids_endpoint_ambiguity() -> None:
    graph = GraphReachabilityGenerator()
    graph_problem = graph.generate(
        1,
        {"num_nodes": 8, "path_length": 4, "extra_edges": 2, "require_shortest": True},
    )
    graph_examples = build_examples_for_problem(
        generator=graph,
        problem=graph_problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["verify"],
        verify_corruption_strategy="single_error",
    )
    assert graph_examples[1].target_lines == ["INVALID BAD_EDGE"]

    tree = TreeAncestryGenerator()
    tree_problem = tree.generate(1, {"depth": 4, "branching_factor": 2, "distractor_subtrees": 3})
    tree_examples = build_examples_for_problem(
        generator=tree,
        problem=tree_problem,
        split="train",
        problem_index=0,
        seed=1,
        modes=["verify"],
        verify_corruption_strategy="single_error",
    )
    assert tree_examples[1].target_lines == ["INVALID BAD_PARENT"]


def test_term_rewriting_verify_uses_single_error_labels() -> None:
    generator = TermRewritingGenerator()
    problem = generator.generate(
        3,
        {
            "rewrite_steps": 4,
            "term_depth": 5,
            "distractor_rules": 4,
            "variable_rule_rate": 0.8,
            "binary_rule_rate": 0.8,
            "normal_form_rate": 0.5,
        },
    )
    examples = build_examples_for_problem(
        generator=generator,
        problem=problem,
        split="train",
        problem_index=0,
        seed=3,
        modes=["verify"],
        verify_corruption_strategy="single_error",
    )

    assert examples[0].target_lines == ["VALID"]
    assert examples[1].target_lines[0] in {
        "INVALID BAD_PATH",
        "INVALID BAD_NO_MATCH",
        "INVALID BAD_RESULT",
        "INVALID BAD_NOT_GOAL",
        "INVALID BAD_PREMATURE_HALT",
    }


def test_symbol_offset_changes_surface_symbols_without_changing_fingerprint() -> None:
    cases = [
        (
            GraphReachabilityGenerator(),
            {"num_nodes": 8, "path_length": 4, "extra_edges": 2, "require_shortest": True},
            "e5",
        ),
        (
            ImplicationChainGenerator(),
            {"num_props": 8, "proof_length": 4, "distractor_hyps": 2},
            "p5",
        ),
        (
            RelationCompositionGenerator(),
            {"num_entities": 8, "composition_depth": 4, "distractor_facts": 2},
            "r9",
        ),
        (
            TreeAncestryGenerator(),
            {"depth": 4, "branching_factor": 2, "distractor_subtrees": 2},
            "e5",
        ),
        (
            TermRewritingGenerator(),
            {
                "rewrite_steps": 4,
                "term_depth": 5,
                "distractor_rules": 2,
                "variable_rule_rate": 0.5,
                "binary_rule_rate": 0.5,
            },
            "e5",
        ),
    ]

    for generator, base_difficulty, expected_symbol in cases:
        base = generator.generate(123, base_difficulty)
        shifted = generator.generate(123, {**base_difficulty, "symbol_offset": 5})

        assert shifted.fingerprint == base.fingerprint
        assert expected_symbol in "\n".join([*shifted.problem_lines, *shifted.final_state])
        assert generator.verify(shifted, shifted.final_state).valid
        assert shifted.meta["difficulty"]["symbol_offset"] == 5


def test_tree_verifier_rejects_expected_error_types() -> None:
    generator = TreeAncestryGenerator()
    problem = generator.generate(1, {"depth": 3, "branching_factor": 2, "distractor_subtrees": 2})

    assert generator.verify(problem, ["BROKEN e0 e1 e2 e3"]).error_code == "MALFORMED"
    assert generator.verify(problem, ["LINEAGE e1 e2 e3"]).error_code == "BAD_LINEAGE_START"
    assert generator.verify(problem, ["LINEAGE e0 e1 e2"]).error_code == "BAD_LINEAGE_END"
    assert generator.verify(problem, ["LINEAGE e0 e2 e3"]).error_code == "BAD_PARENT"
    assert generator.verify(problem, ["LINEAGE e0 e1 e1 e3"]).error_code == "REPEATED_NODE"
