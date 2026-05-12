from __future__ import annotations

import hashlib


SUPPORTED_TASK_SPEC_FORMATS = {"compact_v1", "line_codes_v1"}


def task_spec_variant(seed: int, family: str, mode: str, suffix: str, variant_count: int) -> int:
    if variant_count < 1:
        raise ValueError("task_spec_variant_count must be >= 1")
    text = f"{seed}:{family}:{mode}:{suffix}"
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return int(digest[:8], 16) % variant_count


def render_task_spec(
    *,
    family: str,
    mode: str,
    seed: int,
    suffix: str,
    variant_count: int,
    task_spec_format: str,
) -> tuple[list[str], int | None]:
    if task_spec_format in {"", "none"}:
        return [], None
    if task_spec_format not in SUPPORTED_TASK_SPEC_FORMATS:
        raise ValueError(f"Unsupported task_spec_format: {task_spec_format}")

    variant = task_spec_variant(seed, family, mode, suffix, variant_count)
    if task_spec_format == "line_codes_v1":
        lines = [*_common_mode_code_lines(mode, variant), *_family_code_lines(family, variant)]
        return lines, variant

    lines = [*_common_mode_lines(mode, variant), *_family_lines(family, variant)]
    return lines, variant


def _common_mode_lines(mode: str, variant: int) -> list[str]:
    mode_lines = {
        "action": [
            "OUTPUT exactly one primitive action line",
            "ACTION changes STATE by one valid step toward DONE",
        ],
        "repair_action": [
            "OUTPUT exactly one local repair action line",
            "REPAIR changes corrupted STATE into the intended STATE",
        ],
        "verify": [
            "OUTPUT VALID when STATE satisfies all rules",
            "OUTPUT INVALID CODE when the first broken rule has CODE",
        ],
        "improve": [
            "OUTPUT a better complete STATE",
            "BETTER STATE adds one valid step toward DONE",
        ],
        "repair": [
            "OUTPUT the corrected STATE",
            "CORRECTED STATE satisfies the same progress step",
        ],
        "complete": [
            "OUTPUT a final valid STATE",
            "FINAL STATE must satisfy DONE",
        ],
    }.get(mode, [f"OUTPUT target for MODE {mode}"])
    verify_line = "VALID means all rules hold; INVALID CODE names the first failed rule"
    if variant % 2:
        return [verify_line, *mode_lines]
    return [*mode_lines, verify_line]


def _common_mode_code_lines(mode: str, variant: int) -> list[str]:
    mode_lines = {
        "action": [
            "SPEC_MODE_ACTION_OUTPUT",
            "SPEC_MODE_ACTION_STEP",
        ],
        "repair_action": [
            "SPEC_MODE_REPAIR_ACTION_OUTPUT",
            "SPEC_MODE_REPAIR_ACTION_REPAIR",
        ],
        "verify": [
            "SPEC_MODE_VERIFY_VALID_OUTPUT",
            "SPEC_MODE_VERIFY_INVALID_OUTPUT",
        ],
        "improve": [
            "SPEC_MODE_IMPROVE_OUTPUT",
            "SPEC_MODE_IMPROVE_BETTER",
        ],
        "repair": [
            "SPEC_MODE_REPAIR_OUTPUT",
            "SPEC_MODE_REPAIR_CORRECTED",
        ],
        "complete": [
            "SPEC_MODE_COMPLETE_OUTPUT",
            "SPEC_MODE_COMPLETE_DONE",
        ],
    }.get(mode, ["SPEC_MODE_UNKNOWN_OUTPUT"])
    verify_line = "SPEC_MODE_VERIFY_RULES"
    if variant % 2:
        return [verify_line, *mode_lines]
    return [*mode_lines, verify_line]


def _family_lines(family: str, variant: int) -> list[str]:
    if family == "graph_reachability":
        return _graph_lines(variant)
    if family == "implication_chains":
        return _implication_lines(variant)
    if family == "relation_composition":
        return _relation_lines(variant)
    if family == "tree_ancestry":
        return _tree_lines(variant)
    if family == "term_rewriting":
        return _term_lines(variant)
    raise ValueError(f"Unsupported task spec family: {family}")


def _family_code_lines(family: str, variant: int) -> list[str]:
    if family == "graph_reachability":
        return _graph_code_lines(variant)
    if family == "implication_chains":
        return _implication_code_lines(variant)
    if family == "relation_composition":
        return _relation_code_lines(variant)
    if family == "tree_ancestry":
        return _tree_code_lines(variant)
    if family == "term_rewriting":
        return _term_code_lines(variant)
    raise ValueError(f"Unsupported task spec family: {family}")


def _demo_symbols(variant: int) -> tuple[str, str, str]:
    choices = [
        ("A0", "A1", "A2"),
        ("N0", "N1", "N2"),
        ("X0", "X1", "X2"),
    ]
    return choices[variant % len(choices)]


def _graph_lines(variant: int) -> list[str]:
    a, b, c = _demo_symbols(variant)
    core = [
        "SYNTAX EDGE A B : directed step from A to B",
        "SYNTAX QUERY REACH A C : DONE needs PATH from A to C",
        "SYNTAX PATH A B C : ordered visited nodes",
        "STATE EMPTY means no PATH has started",
        "VALID PATH requires each adjacent pair has EDGE",
        "ACTION APPEND X starts with query start or extends from last node by EDGE",
        "DONE when PATH starts at query start and ends at query target",
    ]
    demo = f"DEMO EDGE {a} {b} ; EDGE {b} {c} ; QUERY REACH {a} {c} ; EMPTY => APPEND {a} ; PATH {a} => APPEND {b}"
    return [*core, demo] if variant != 2 else [core[1], core[0], *core[2:], demo]


def _graph_code_lines(variant: int) -> list[str]:
    core = [
        "SPEC_GRAPH_EDGE_SYNTAX",
        "SPEC_GRAPH_QUERY_SYNTAX",
        "SPEC_GRAPH_PATH_SYNTAX",
        "SPEC_GRAPH_EMPTY_STATE",
        "SPEC_GRAPH_PATH_VALID",
        "SPEC_GRAPH_APPEND_ACTION",
        "SPEC_GRAPH_DONE",
    ]
    demo = "SPEC_GRAPH_DEMO"
    return [*core, demo] if variant != 2 else [core[1], core[0], *core[2:], demo]


def _implication_lines(variant: int) -> list[str]:
    a, b, c = _demo_symbols(variant)
    h0 = f"K{variant}0"
    h1 = f"K{variant}1"
    core = [
        "SYNTAX HYP K : P : K proves fact P",
        "SYNTAX HYP K : P -> Q : K maps known P to Q",
        "SYNTAX GOAL Q : DONE needs Q derived",
        "SYNTAX DERIVE Q BY K FROM P : Q follows by implication K and prior P",
        "ACTION APPLY K adds the derivation licensed by K",
        "VALID proof uses only known facts and prior derived premises",
        "DONE when GOAL proposition is derived",
    ]
    demo = f"DEMO HYP {h0} : {a} ; HYP {h1} : {a} -> {b} ; GOAL {b} ; EMPTY => APPLY {h0} ; DERIVE {a} BY {h0} => APPLY {h1}"
    return [*core, demo] if variant != 1 else [core[0], core[2], core[1], *core[3:], demo]


def _implication_code_lines(variant: int) -> list[str]:
    core = [
        "SPEC_IMPL_FACT_HYP_SYNTAX",
        "SPEC_IMPL_RULE_HYP_SYNTAX",
        "SPEC_IMPL_GOAL_SYNTAX",
        "SPEC_IMPL_DERIVE_SYNTAX",
        "SPEC_IMPL_APPLY_ACTION",
        "SPEC_IMPL_PROOF_VALID",
        "SPEC_IMPL_DONE",
    ]
    demo = "SPEC_IMPL_DEMO"
    return [*core, demo] if variant != 1 else [core[0], core[2], core[1], *core[3:], demo]


def _relation_lines(variant: int) -> list[str]:
    a, b, c = _demo_symbols(variant)
    rel0 = f"REL{variant}0"
    rel1 = f"REL{variant}1"
    rel2 = f"REL{variant}2"
    core = [
        "SYNTAX FACT R A B : relation R holds from A to B",
        "SYNTAX RULE RC = RA ; RB : compose RA then RB through a shared middle",
        "SYNTAX QUERY R A C : DONE needs relation R from A to C",
        "SYNTAX DERIVE R A C VIA B : composed fact uses middle B",
        "ACTION FOLLOW C VIA B adds the next composed fact ending at C",
        "VALID derivation requires matching left fact, right fact, and rule",
        "DONE when queried relation fact is available",
    ]
    demo = f"DEMO FACT {rel0} {a} {b} ; FACT {rel1} {b} {c} ; RULE {rel2} = {rel0} ; {rel1} ; QUERY {rel2} {a} {c} ; EMPTY => FOLLOW {c} VIA {b}"
    return [*core, demo] if variant != 2 else [core[1], core[0], *core[2:], demo]


def _relation_code_lines(variant: int) -> list[str]:
    core = [
        "SPEC_REL_FACT_SYNTAX",
        "SPEC_REL_RULE_SYNTAX",
        "SPEC_REL_QUERY_SYNTAX",
        "SPEC_REL_DERIVE_SYNTAX",
        "SPEC_REL_FOLLOW_ACTION",
        "SPEC_REL_DERIVATION_VALID",
        "SPEC_REL_DONE",
    ]
    demo = "SPEC_REL_DEMO"
    return [*core, demo] if variant != 2 else [core[1], core[0], *core[2:], demo]


def _tree_lines(variant: int) -> list[str]:
    a, b, c = _demo_symbols(variant)
    core = [
        "SYNTAX PARENT A B : A is direct parent of B",
        "SYNTAX QUERY ANCESTOR A C : DONE needs lineage from A to C",
        "SYNTAX LINEAGE A B C : ordered ancestor chain",
        "STATE EMPTY means no lineage has started",
        "VALID LINEAGE starts at query ancestor and follows PARENT steps",
        "ACTION DESCEND X starts with query ancestor or appends a child of last node",
        "DONE when LINEAGE ends at query target",
    ]
    demo = f"DEMO PARENT {a} {b} ; PARENT {b} {c} ; QUERY ANCESTOR {a} {c} ; EMPTY => DESCEND {a} ; LINEAGE {a} => DESCEND {b}"
    return [*core, demo] if variant != 1 else [core[1], core[0], *core[2:], demo]


def _tree_code_lines(variant: int) -> list[str]:
    core = [
        "SPEC_TREE_PARENT_SYNTAX",
        "SPEC_TREE_QUERY_SYNTAX",
        "SPEC_TREE_LINEAGE_SYNTAX",
        "SPEC_TREE_EMPTY_STATE",
        "SPEC_TREE_LINEAGE_VALID",
        "SPEC_TREE_DESCEND_ACTION",
        "SPEC_TREE_DONE",
    ]
    demo = "SPEC_TREE_DEMO"
    return [*core, demo] if variant != 1 else [core[1], core[0], *core[2:], demo]


def _term_lines(variant: int) -> list[str]:
    a, b, _c = _demo_symbols(variant)
    rule = f"K{variant}0"
    op0 = f"OP{variant}0"
    op1 = f"OP{variant}1"
    core = [
        "SYNTAX RULE K : L -> R : K replaces a matching L subterm with R",
        "SYNTAX START T : initial TERM is T",
        "SYNTAX GOAL T : DONE needs current TERM equal T",
        "SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable",
        "SYNTAX TERM T : current expression",
        "ACTION RW K AT PATH applies rule K to the subterm at PATH",
        "ACTION HALT stops only when DONE already holds",
        "VALID trace alternates TERM then RW then TERM, with optional final HALT",
    ]
    demo = f"DEMO RULE {rule} : {op0} {a} -> {op1} {a} ; START {op0} {a} ; GOAL {op1} {a} ; TERM {op0} {a} => RW {rule} AT ROOT"
    return [*core, demo] if variant != 2 else [core[0], core[4], core[1], *core[2:4], *core[5:], demo]


def _term_code_lines(variant: int) -> list[str]:
    core = [
        "SPEC_TERM_RULE_SYNTAX",
        "SPEC_TERM_START_SYNTAX",
        "SPEC_TERM_GOAL_SYNTAX",
        "SPEC_TERM_NORMAL_FORM_SYNTAX",
        "SPEC_TERM_TERM_SYNTAX",
        "SPEC_TERM_RW_ACTION",
        "SPEC_TERM_HALT_ACTION",
        "SPEC_TERM_TRACE_VALID",
    ]
    demo = "SPEC_TERM_DEMO"
    return [*core, demo] if variant != 2 else [core[0], core[4], core[1], *core[2:4], *core[5:], demo]
