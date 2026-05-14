from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from reasoning_dsl.core import Example


SCHEMA_VERSION = "relational_object_v1"
TASK_SCHEMA_VERSION = "relational_task_schema_v1"
PATH_FAMILIES = {"graph_reachability", "shortest_path_lite"}


def relational_record(example: Example | Mapping[str, Any]) -> dict[str, Any]:
    row = example.to_json() if isinstance(example, Example) else dict(example)
    family = str(row["family"])
    if family in PATH_FAMILIES:
        return _path_record(row, edge_pred="EDGE", state_pred="PATH", query_pred="REACH", action_op="APPEND")
    if family == "tree_ancestry":
        return _path_record(
            row,
            edge_pred="PARENT",
            state_pred="LINEAGE",
            query_pred="ANCESTOR",
            action_op="DESCEND",
        )
    if family == "implication_chains":
        return _implication_record(row)
    if family == "relation_composition":
        return _relation_record(row)
    if family == "dfa_simulation_lite":
        return _dfa_record(row)
    if family in {"term_rewriting", "equality_rewriting_lite"}:
        return _term_record(row)
    raise ValueError(f"Relational export does not yet support family: {family}")


def model_view(record: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": record["schema_version"],
        "family": record["family"],
        "mode": record["mode"],
        "objects": record["objects"],
        "facts": record["facts"],
        "state": record["state"],
        "target": record["target"],
    }


def task_schema_record(example: Example | Mapping[str, Any]) -> dict[str, Any]:
    """Return a prototype task-declared relational view.

    This is intentionally narrow for now. It covers path-style graph/tree tasks
    and removes family-specific predicate/action names from the model-facing
    record. External names remain side-table metadata only.
    """

    row = example.to_json() if isinstance(example, Example) else dict(example)
    family = str(row["family"])
    if family in PATH_FAMILIES:
        return _path_task_schema_record(
            row,
            edge_pred="EDGE",
            state_pred="PATH",
            query_pred="REACH",
            action_op="APPEND",
        )
    if family == "tree_ancestry":
        return _path_task_schema_record(
            row,
            edge_pred="PARENT",
            state_pred="LINEAGE",
            query_pred="ANCESTOR",
            action_op="DESCEND",
        )
    if family == "implication_chains":
        return _implication_task_schema_record(row)
    if family == "relation_composition":
        return _relation_task_schema_record(row)
    if family in {"term_rewriting", "equality_rewriting_lite"}:
        return _term_task_schema_record(row)
    raise ValueError(f"Task-schema relational view does not yet support family: {family}")


def export_relational_jsonl(
    examples_by_split: Mapping[str, list[Example]],
    output_dir: str | Path,
) -> None:
    out = Path(output_dir) / "relational_jsonl"
    out.mkdir(parents=True, exist_ok=True)
    for split, examples in examples_by_split.items():
        with (out / f"{split}.jsonl").open("w", encoding="utf-8") as f:
            for example in examples:
                f.write(json.dumps(relational_record(example), sort_keys=True) + "\n")


def export_relational_from_jsonl(data_dir: str | Path, output_dir: str | Path) -> None:
    input_root = Path(data_dir) / "jsonl"
    if not input_root.exists():
        raise ValueError(f"Missing JSONL directory: {input_root}")
    out = Path(output_dir) / "relational_jsonl"
    out.mkdir(parents=True, exist_ok=True)
    schema = {
        "schema_version": SCHEMA_VERSION,
        "description": "Anonymous-object relational view. External names are side-table metadata only.",
        "supported_families": sorted(
            [
                *PATH_FAMILIES,
                "dfa_simulation_lite",
                "equality_rewriting_lite",
                "implication_chains",
                "relation_composition",
                "term_rewriting",
                "tree_ancestry",
            ]
        ),
    }
    (Path(output_dir) / "relational_schema.json").write_text(json.dumps(schema, indent=2, sort_keys=True), encoding="utf-8")

    for path in sorted(input_root.glob("*.jsonl")):
        with path.open("r", encoding="utf-8") as src, (out / path.name).open("w", encoding="utf-8") as dst:
            for line in src:
                row = json.loads(line)
                dst.write(json.dumps(relational_record(row), sort_keys=True) + "\n")


class _ObjectTable:
    def __init__(self) -> None:
        self._keys: dict[tuple[str, str], int] = {}
        self.objects: list[dict[str, str]] = []
        self.external_names: list[dict[str, Any]] = []

    def add(self, object_type: str, external_name: str) -> int:
        key = (object_type, external_name)
        existing = self._keys.get(key)
        if existing is not None:
            return existing
        row = len(self.objects)
        self._keys[key] = row
        self.objects.append({"type": object_type})
        self.external_names.append({"object": row, "type": object_type, "name": external_name})
        return row

    def require(self, object_type: str, external_name: str) -> int:
        key = (object_type, external_name)
        if key not in self._keys:
            raise ValueError(f"Unknown {object_type} object {external_name!r}")
        return self._keys[key]


def _path_task_schema_record(
    row: Mapping[str, Any],
    *,
    edge_pred: str,
    state_pred: str,
    query_pred: str,
    action_op: str,
) -> dict[str, Any]:
    objects = _ObjectTable()
    facts: list[dict[str, Any]] = []
    edge = objects.add("predicate", edge_pred)
    state = objects.add("predicate", state_pred)
    action = objects.add("operation", action_op)
    query_start: str | None = None
    query_goal: str | None = None

    facts.extend(
        [
            {"pred": "SCHEMA_BINARY_REL", "args": [edge]},
            {"pred": "SCHEMA_SEQUENCE_STATE", "args": [state]},
            {"pred": "SCHEMA_EXTEND_ACTION", "args": [action, edge, state]},
        ]
    )

    for line in _string_list(row["problem_lines"]):
        tokens = line.split()
        if len(tokens) == 3 and tokens[0] == edge_pred:
            left = objects.add("entity", tokens[1])
            right = objects.add("entity", tokens[2])
            facts.append({"pred": "RELATION_TUPLE", "args": [edge, left, right]})
        elif len(tokens) == 4 and tokens[:2] == ["QUERY", query_pred]:
            query_start, query_goal = tokens[2], tokens[3]
            start = objects.add("entity", query_start)
            goal = objects.add("entity", query_goal)
            facts.append({"pred": "QUERY_RELATION", "args": [edge]})
            facts.append({"pred": "QUERY_START", "args": [start]})
            facts.append({"pred": "QUERY_GOAL", "args": [goal]})

    if query_start is None or query_goal is None:
        raise ValueError(f"{row['id']}: missing QUERY {query_pred}")

    state_objects = _path_state_objects(_string_list(row["state_lines"]), state_pred, objects)
    return {
        "schema_version": TASK_SCHEMA_VERSION,
        "id": row["id"],
        "split": row["split"],
        "family": row["family"],
        "mode": row["mode"],
        "objects": objects.objects,
        "external_names": objects.external_names,
        "facts": facts,
        "state": {"kind": "sequence", "predicate": state, "objects": state_objects},
        "target": _path_task_schema_target(
            row,
            state_pred=state_pred,
            action_op=action_op,
            action=action,
            objects=objects,
        ),
        "meta": row.get("meta", {}),
    }


def _path_task_schema_target(
    row: Mapping[str, Any],
    *,
    state_pred: str,
    action_op: str,
    action: int,
    objects: _ObjectTable,
) -> dict[str, Any]:
    mode = str(row["mode"])
    target_lines = _string_list(row["target_lines"])
    if mode == "action":
        if len(target_lines) != 1:
            raise ValueError(f"{row['id']}: action target must be one line")
        tokens = target_lines[0].split()
        if len(tokens) != 2 or tokens[0] != action_op:
            raise ValueError(f"{row['id']}: expected {action_op} target")
        return {"kind": "action", "op": "EXTEND_SEQUENCE", "args": [action, objects.require("entity", tokens[1])]}

    if mode == "repair_action":
        if len(target_lines) != 1:
            raise ValueError(f"{row['id']}: repair_action target must be one line")
        return _path_repair_target(row["id"], target_lines[0], objects, generic_location=True)

    if mode == "verify":
        if target_lines == ["VALID"]:
            return {"kind": "verify", "valid": True, "error_code": None}
        tokens = target_lines[0].split() if len(target_lines) == 1 else []
        if len(tokens) == 2 and tokens[0] == "INVALID":
            return {"kind": "verify", "valid": False, "error_code": tokens[1]}
        raise ValueError(f"{row['id']}: malformed verify target")

    if mode in {"improve", "repair", "complete"}:
        return {
            "kind": "state",
            "state": {
                "kind": "sequence",
                "objects": _path_state_objects(target_lines, state_pred, objects),
            },
        }

    raise ValueError(f"{row['id']}: unsupported mode for task-schema relational export: {mode}")


def _implication_task_schema_record(row: Mapping[str, Any]) -> dict[str, Any]:
    objects = _ObjectTable()
    state = objects.add("predicate", "KNOWN")
    action = objects.add("operation", "APPLY")
    premise_rel = objects.add("predicate", "PREMISE")
    conclusion_rel = objects.add("predicate", "CONCLUSION")
    facts: list[dict[str, Any]] = [
        {"pred": "SCHEMA_SEQUENCE_STATE", "args": [state]},
        {"pred": "SCHEMA_EXTEND_ACTION", "args": [action, conclusion_rel, state]},
        {"pred": "SCHEMA_BINARY_REL", "args": [premise_rel]},
        {"pred": "SCHEMA_BINARY_REL", "args": [conclusion_rel]},
        {"pred": "COMPOSE_RULE", "args": [conclusion_rel, premise_rel, state]},
    ]
    for line in _string_list(row["problem_lines"]):
        tokens = line.split()
        if len(tokens) == 4 and tokens[0] == "HYP" and tokens[2] == ":":
            hyp = objects.add("hypothesis", tokens[1])
            prop = objects.add("proposition", tokens[3])
            facts.append({"pred": "RELATION_TUPLE", "args": [conclusion_rel, hyp, prop]})
        elif len(tokens) == 6 and tokens[0] == "HYP" and tokens[2] == ":" and tokens[4] == "->":
            hyp = objects.add("hypothesis", tokens[1])
            premise = objects.add("proposition", tokens[3])
            conclusion = objects.add("proposition", tokens[5])
            facts.append({"pred": "RELATION_TUPLE", "args": [premise_rel, hyp, premise]})
            facts.append({"pred": "RELATION_TUPLE", "args": [conclusion_rel, hyp, conclusion]})
        elif len(tokens) == 2 and tokens[0] == "GOAL":
            facts.append({"pred": "QUERY_GOAL", "args": [objects.add("proposition", tokens[1])]})

    state_items = _implication_state(_string_list(row["state_lines"]), objects)
    return {
        "schema_version": TASK_SCHEMA_VERSION,
        "id": row["id"],
        "split": row["split"],
        "family": row["family"],
        "mode": row["mode"],
        "objects": objects.objects,
        "external_names": objects.external_names,
        "facts": facts,
        "state": {
            "kind": "derivations",
            "predicate": state,
            "items": state_items,
            "objects": [item["args"][0] for item in state_items if item.get("args")],
        },
        "target": _implication_task_schema_target(row, objects, action),
        "meta": row.get("meta", {}),
    }


def _implication_task_schema_target(row: Mapping[str, Any], objects: _ObjectTable, action: int) -> dict[str, Any]:
    mode = str(row["mode"])
    target_lines = _string_list(row["target_lines"])
    if mode == "action":
        if len(target_lines) != 1:
            raise ValueError(f"{row['id']}: action target must be one line")
        tokens = target_lines[0].split()
        if len(tokens) == 2 and tokens[0] == "APPLY":
            return {"kind": "action", "op": "EXTEND_SEQUENCE", "args": [action, objects.require("hypothesis", tokens[1])]}
        raise ValueError(f"{row['id']}: malformed implication task-schema action target")

    if mode == "repair_action":
        if len(target_lines) != 1:
            raise ValueError(f"{row['id']}: repair_action target must be one line")
        return _line_repair_target(row["id"], target_lines[0], objects, field_as_arg=True)

    if mode == "verify":
        return _verify_target(row["id"], target_lines)

    if mode in {"improve", "repair", "complete"}:
        return {
            "kind": "state",
            "state": {
                "kind": "derivations",
                "items": _implication_state(target_lines, objects),
            },
        }

    raise ValueError(f"{row['id']}: unsupported mode for implication task-schema export: {mode}")


def _relation_task_schema_record(row: Mapping[str, Any]) -> dict[str, Any]:
    objects = _ObjectTable()
    state = objects.add("predicate", "KNOWN_RELATION")
    action = objects.add("operation", "FOLLOW")
    facts: list[dict[str, Any]] = [
        {"pred": "SCHEMA_SEQUENCE_STATE", "args": [state]},
        {"pred": "SCHEMA_EXTEND_ACTION", "args": [action, state]},
    ]
    for line in _string_list(row["problem_lines"]):
        tokens = line.split()
        if len(tokens) == 4 and tokens[0] == "FACT":
            rel = objects.add("relation_symbol", tokens[1])
            left = objects.add("entity", tokens[2])
            right = objects.add("entity", tokens[3])
            facts.append({"pred": "RELATION_TUPLE", "args": [rel, left, right]})
        elif len(tokens) == 6 and tokens[0] == "RULE" and tokens[2] == "=" and tokens[4] == ";":
            result = objects.add("relation_symbol", tokens[1])
            left_rel = objects.add("relation_symbol", tokens[3])
            right_rel = objects.add("relation_symbol", tokens[5])
            facts.append({"pred": "COMPOSE_RULE", "args": [result, left_rel, right_rel]})
        elif len(tokens) == 4 and tokens[0] == "QUERY":
            rel = objects.add("relation_symbol", tokens[1])
            left = objects.add("entity", tokens[2])
            right = objects.add("entity", tokens[3])
            facts.append({"pred": "QUERY_RELATION", "args": [rel]})
            facts.append({"pred": "QUERY_START", "args": [left]})
            facts.append({"pred": "QUERY_GOAL", "args": [right]})

    state_items = _relation_state(_string_list(row["state_lines"]), objects)
    return {
        "schema_version": TASK_SCHEMA_VERSION,
        "id": row["id"],
        "split": row["split"],
        "family": row["family"],
        "mode": row["mode"],
        "objects": objects.objects,
        "external_names": objects.external_names,
        "facts": facts,
        "state": {
            "kind": "relation_derivations",
            "predicate": state,
            "items": state_items,
            "objects": [arg for item in state_items for arg in item.get("args", [])[:3]],
        },
        "target": _relation_task_schema_target(row, objects, action),
        "meta": row.get("meta", {}),
    }


def _relation_task_schema_target(row: Mapping[str, Any], objects: _ObjectTable, action: int) -> dict[str, Any]:
    mode = str(row["mode"])
    target_lines = _string_list(row["target_lines"])
    if mode == "action":
        if len(target_lines) != 1:
            raise ValueError(f"{row['id']}: action target must be one line")
        target = _relation_action_target(row["id"], target_lines[0], objects)
        if target["op"] == "FOLLOW":
            return {"kind": "action", "op": "EXTEND_SEQUENCE", "args": [action, *target["args"]]}
        return target

    if mode == "repair_action":
        if len(target_lines) != 1:
            raise ValueError(f"{row['id']}: repair_action target must be one line")
        return _line_repair_target(row["id"], target_lines[0], objects, field_as_arg=True)

    if mode == "verify":
        return _verify_target(row["id"], target_lines)

    if mode in {"improve", "repair", "complete"}:
        return {
            "kind": "state",
            "state": {"kind": "relation_derivations", "items": _relation_state(target_lines, objects)},
        }

    raise ValueError(f"{row['id']}: unsupported mode for relation task-schema export: {mode}")


def _term_task_schema_record(row: Mapping[str, Any]) -> dict[str, Any]:
    objects = _ObjectTable()
    state = objects.add("predicate", "CURRENT_TERM")
    rewrite_action = objects.add("operation", "RW")
    halt_action = objects.add("operation", "HALT")
    facts: list[dict[str, Any]] = [
        {"pred": "SCHEMA_SEQUENCE_STATE", "args": [state]},
        {"pred": "SCHEMA_EXTEND_ACTION", "args": [rewrite_action, state]},
        {"pred": "SCHEMA_HALT_ACTION", "args": [halt_action, state]},
    ]
    for line in _string_list(row["problem_lines"]):
        tokens = line.split()
        if len(tokens) >= 6 and tokens[0] == "RULE" and tokens[2] == ":" and "->" in tokens:
            arrow = tokens.index("->")
            rule = objects.add("rule", tokens[1])
            facts.append(
                {
                    "pred": "RULE",
                    "args": [rule],
                    "lhs": _parse_term(tokens[3:arrow], objects),
                    "rhs": _parse_term(tokens[arrow + 1 :], objects),
                }
            )
        elif len(tokens) >= 2 and tokens[0] == "START":
            facts.append({"pred": "QUERY_START", "term": _parse_term(tokens[1:], objects)})
        elif len(tokens) >= 2 and tokens[0] == "GOAL":
            facts.append({"pred": "QUERY_GOAL", "term": _parse_term(tokens[1:], objects)})
        elif tokens == ["QUERY", "NORMAL_FORM"]:
            facts.append({"pred": "QUERY_PROPERTY", "args": [objects.add("property", "NORMAL_FORM")]})

    return {
        "schema_version": TASK_SCHEMA_VERSION,
        "id": row["id"],
        "split": row["split"],
        "family": row["family"],
        "mode": row["mode"],
        "objects": objects.objects,
        "external_names": objects.external_names,
        "facts": facts,
        "state": {
            "kind": "rewrite_trace",
            "predicate": state,
            "items": _term_state(_string_list(row["state_lines"]), objects),
        },
        "target": _term_target(row, objects, rewrite_action=rewrite_action, halt_action=halt_action),
        "meta": row.get("meta", {}),
    }


def _path_record(
    row: Mapping[str, Any],
    *,
    edge_pred: str,
    state_pred: str,
    query_pred: str,
    action_op: str,
) -> dict[str, Any]:
    objects = _ObjectTable()
    facts: list[dict[str, Any]] = []
    query_start: str | None = None
    query_goal: str | None = None

    for line in _string_list(row["problem_lines"]):
        tokens = line.split()
        if len(tokens) == 3 and tokens[0] == edge_pred:
            left = objects.add("entity", tokens[1])
            right = objects.add("entity", tokens[2])
            facts.append({"pred": edge_pred, "args": [left, right]})
        elif len(tokens) == 4 and tokens[:2] == ["QUERY", query_pred]:
            query_start, query_goal = tokens[2], tokens[3]
            start = objects.add("entity", query_start)
            goal = objects.add("entity", query_goal)
            facts.append({"pred": "QUERY_START", "args": [start]})
            facts.append({"pred": "QUERY_GOAL", "args": [goal]})

    if query_start is None or query_goal is None:
        raise ValueError(f"{row['id']}: missing QUERY {query_pred}")

    state_objects = _path_state_objects(_string_list(row["state_lines"]), state_pred, objects)
    return {
        "schema_version": SCHEMA_VERSION,
        "id": row["id"],
        "split": row["split"],
        "family": row["family"],
        "mode": row["mode"],
        "objects": objects.objects,
        "external_names": objects.external_names,
        "facts": facts,
        "state": {"kind": "sequence", "pred": state_pred, "objects": state_objects},
        "target": _path_target(row, state_pred=state_pred, action_op=action_op, objects=objects),
        "meta": row.get("meta", {}),
    }


def _path_state_objects(state_lines: list[str], state_pred: str, objects: _ObjectTable) -> list[int]:
    if not state_lines:
        return []
    if len(state_lines) != 1:
        raise ValueError(f"{state_pred} state must have exactly one line")
    tokens = state_lines[0].split()
    if len(tokens) < 2 or tokens[0] != state_pred:
        raise ValueError(f"Expected {state_pred} state line")
    return [objects.add("entity", token) for token in tokens[1:]]


def _path_target(
    row: Mapping[str, Any],
    *,
    state_pred: str,
    action_op: str,
    objects: _ObjectTable,
) -> dict[str, Any]:
    mode = str(row["mode"])
    target_lines = _string_list(row["target_lines"])
    if mode == "action":
        if len(target_lines) != 1:
            raise ValueError(f"{row['id']}: action target must be one line")
        tokens = target_lines[0].split()
        if len(tokens) != 2 or tokens[0] != action_op:
            raise ValueError(f"{row['id']}: expected {action_op} target")
        return {"kind": "action", "op": action_op, "args": [objects.require("entity", tokens[1])]}

    if mode == "repair_action":
        if len(target_lines) != 1:
            raise ValueError(f"{row['id']}: repair_action target must be one line")
        return _path_repair_target(row["id"], target_lines[0], objects)

    if mode == "verify":
        if target_lines == ["VALID"]:
            return {"kind": "verify", "valid": True, "error_code": None}
        tokens = target_lines[0].split() if len(target_lines) == 1 else []
        if len(tokens) == 2 and tokens[0] == "INVALID":
            return {"kind": "verify", "valid": False, "error_code": tokens[1]}
        raise ValueError(f"{row['id']}: malformed verify target")

    if mode in {"improve", "repair", "complete"}:
        return {"kind": "state", "state": {"kind": "sequence", "pred": state_pred, "objects": _path_state_objects(target_lines, state_pred, objects)}}

    raise ValueError(f"{row['id']}: unsupported mode for relational export: {mode}")


def _path_repair_target(
    example_id: str,
    line: str,
    objects: _ObjectTable,
    *,
    generic_location: bool = False,
) -> dict[str, Any]:
    tokens = line.split()
    if len(tokens) == 4 and tokens[:3] == ["REPLACE", "ROOT", "WITH"]:
        if generic_location:
            return {
                "kind": "repair_action",
                "op": "REPLACE_ITEM",
                "args": [objects.add("location_root", "ROOT"), objects.require("entity", tokens[3])],
            }
        return {"kind": "repair_action", "op": "REPLACE_ROOT", "args": [objects.require("entity", tokens[3])]}
    if len(tokens) == 5 and tokens[0] == "REPLACE" and tokens[1] == "AFTER" and tokens[3] == "WITH":
        if generic_location:
            return {
                "kind": "repair_action",
                "op": "REPLACE_ITEM",
                "args": [
                    objects.add("location_after", "AFTER"),
                    objects.require("entity", tokens[2]),
                    objects.require("entity", tokens[4]),
                ],
            }
        return {
            "kind": "repair_action",
            "op": "REPLACE_AFTER",
            "args": [objects.require("entity", tokens[2]), objects.require("entity", tokens[4])],
        }
    if len(tokens) == 5 and tokens[0] == "REPLACE" and tokens[1] == "NODE" and tokens[3] == "WITH":
        if generic_location:
            return {
                "kind": "repair_action",
                "op": "REPLACE_ITEM",
                "index": int(tokens[2]),
                "args": [objects.add("location_index", "NODE"), objects.require("entity", tokens[4])],
            }
        return {
            "kind": "repair_action",
            "op": "REPLACE_NODE",
            "index": int(tokens[2]),
            "args": [objects.require("entity", tokens[4])],
        }
    raise ValueError(f"{example_id}: malformed path repair target")


def _implication_record(row: Mapping[str, Any]) -> dict[str, Any]:
    objects = _ObjectTable()
    facts: list[dict[str, Any]] = []
    for line in _string_list(row["problem_lines"]):
        tokens = line.split()
        if len(tokens) == 4 and tokens[0] == "HYP" and tokens[2] == ":":
            hyp = objects.add("hypothesis", tokens[1])
            prop = objects.add("proposition", tokens[3])
            facts.append({"pred": "HYP_FACT", "args": [hyp, prop]})
        elif len(tokens) == 6 and tokens[0] == "HYP" and tokens[2] == ":" and tokens[4] == "->":
            hyp = objects.add("hypothesis", tokens[1])
            premise = objects.add("proposition", tokens[3])
            conclusion = objects.add("proposition", tokens[5])
            facts.append({"pred": "HYP_RULE", "args": [hyp, premise, conclusion]})
        elif len(tokens) == 2 and tokens[0] == "GOAL":
            facts.append({"pred": "GOAL", "args": [objects.add("proposition", tokens[1])]})

    return {
        "schema_version": SCHEMA_VERSION,
        "id": row["id"],
        "split": row["split"],
        "family": row["family"],
        "mode": row["mode"],
        "objects": objects.objects,
        "external_names": objects.external_names,
        "facts": facts,
        "state": {"kind": "derivations", "items": _implication_state(_string_list(row["state_lines"]), objects)},
        "target": _implication_target(row, objects),
        "meta": row.get("meta", {}),
    }


def _implication_state(state_lines: list[str], objects: _ObjectTable) -> list[dict[str, Any]]:
    items = []
    for line in state_lines:
        tokens = line.split()
        if len(tokens) == 4 and tokens[0] == "DERIVE" and tokens[2] == "BY":
            items.append(
                {
                    "pred": "DERIVE",
                    "args": [objects.add("proposition", tokens[1]), objects.add("hypothesis", tokens[3])],
                }
            )
        elif len(tokens) == 6 and tokens[0] == "DERIVE" and tokens[2] == "BY" and tokens[4] == "FROM":
            items.append(
                {
                    "pred": "DERIVE_FROM",
                    "args": [
                        objects.add("proposition", tokens[1]),
                        objects.add("hypothesis", tokens[3]),
                        objects.add("proposition", tokens[5]),
                    ],
                }
            )
        else:
            raise ValueError(f"Malformed implication state line: {line}")
    return items


def _implication_target(row: Mapping[str, Any], objects: _ObjectTable) -> dict[str, Any]:
    mode = str(row["mode"])
    target_lines = _string_list(row["target_lines"])
    if mode == "action":
        if len(target_lines) != 1:
            raise ValueError(f"{row['id']}: action target must be one line")
        tokens = target_lines[0].split()
        if len(tokens) == 2 and tokens[0] == "APPLY":
            return {"kind": "action", "op": "APPLY", "args": [objects.require("hypothesis", tokens[1])]}
        if len(tokens) >= 2 and tokens[:2] == ["ADD", "DERIVE"]:
            return {"kind": "action", "op": "ADD_DERIVE", "derivation": _implication_state([" ".join(tokens[1:])], objects)[0]}
        raise ValueError(f"{row['id']}: malformed implication action target")

    if mode == "repair_action":
        if len(target_lines) != 1:
            raise ValueError(f"{row['id']}: repair_action target must be one line")
        return _line_repair_target(row["id"], target_lines[0], objects)

    if mode == "verify":
        return _verify_target(row["id"], target_lines)

    if mode in {"improve", "repair", "complete"}:
        return {"kind": "state", "state": {"kind": "derivations", "items": _implication_state(target_lines, objects)}}

    raise ValueError(f"{row['id']}: unsupported mode for relational export: {mode}")


def _relation_record(row: Mapping[str, Any]) -> dict[str, Any]:
    objects = _ObjectTable()
    facts: list[dict[str, Any]] = []
    for line in _string_list(row["problem_lines"]):
        tokens = line.split()
        if len(tokens) == 4 and tokens[0] == "FACT":
            rel = objects.add("relation_symbol", tokens[1])
            left = objects.add("entity", tokens[2])
            right = objects.add("entity", tokens[3])
            facts.append({"pred": "FACT", "args": [rel, left, right]})
        elif len(tokens) == 6 and tokens[0] == "RULE" and tokens[2] == "=" and tokens[4] == ";":
            result = objects.add("relation_symbol", tokens[1])
            left_rel = objects.add("relation_symbol", tokens[3])
            right_rel = objects.add("relation_symbol", tokens[5])
            facts.append({"pred": "RULE_COMPOSE", "args": [result, left_rel, right_rel]})
        elif len(tokens) == 4 and tokens[0] == "QUERY":
            rel = objects.add("relation_symbol", tokens[1])
            left = objects.add("entity", tokens[2])
            right = objects.add("entity", tokens[3])
            facts.append({"pred": "QUERY", "args": [rel, left, right]})

    return {
        "schema_version": SCHEMA_VERSION,
        "id": row["id"],
        "split": row["split"],
        "family": row["family"],
        "mode": row["mode"],
        "objects": objects.objects,
        "external_names": objects.external_names,
        "facts": facts,
        "state": {"kind": "relation_derivations", "items": _relation_state(_string_list(row["state_lines"]), objects)},
        "target": _relation_target(row, objects),
        "meta": row.get("meta", {}),
    }


def _relation_state(state_lines: list[str], objects: _ObjectTable) -> list[dict[str, Any]]:
    items = []
    for line in state_lines:
        tokens = line.split()
        if len(tokens) != 6 or tokens[0] != "DERIVE" or tokens[4] != "VIA":
            raise ValueError(f"Malformed relation state line: {line}")
        items.append(
            {
                "pred": "DERIVE",
                "args": [
                    objects.add("relation_symbol", tokens[1]),
                    objects.add("entity", tokens[2]),
                    objects.add("entity", tokens[3]),
                    objects.add("entity", tokens[5]),
                ],
            }
        )
    return items


def _relation_target(row: Mapping[str, Any], objects: _ObjectTable) -> dict[str, Any]:
    mode = str(row["mode"])
    target_lines = _string_list(row["target_lines"])
    if mode == "action":
        if len(target_lines) != 1:
            raise ValueError(f"{row['id']}: action target must be one line")
        return _relation_action_target(row["id"], target_lines[0], objects)

    if mode == "repair_action":
        if len(target_lines) != 1:
            raise ValueError(f"{row['id']}: repair_action target must be one line")
        return _line_repair_target(row["id"], target_lines[0], objects)

    if mode == "verify":
        return _verify_target(row["id"], target_lines)

    if mode in {"improve", "repair", "complete"}:
        return {"kind": "state", "state": {"kind": "relation_derivations", "items": _relation_state(target_lines, objects)}}

    raise ValueError(f"{row['id']}: unsupported mode for relational export: {mode}")


def _relation_action_target(example_id: str, line: str, objects: _ObjectTable) -> dict[str, Any]:
    tokens = line.split()
    if len(tokens) == 4 and tokens[0] == "FOLLOW" and tokens[2] == "VIA":
        return {
            "kind": "action",
            "op": "FOLLOW",
            "args": [objects.require("entity", tokens[1]), objects.require("entity", tokens[3])],
        }
    if len(tokens) == 5 and tokens[0] == "FOLLOW" and tokens[3] == "VIA":
        object_type = "relation_symbol" if tokens[1].startswith("r") else "entity"
        return {
            "kind": "action",
            "op": "FOLLOW",
            "args": [
                objects.require(object_type, tokens[1]),
                objects.require("entity", tokens[2]),
                objects.require("entity", tokens[4]),
            ],
        }
    if len(tokens) == 7 and tokens[0] == "COMPOSE" and tokens[5] == "VIA":
        return {
            "kind": "action",
            "op": "COMPOSE",
            "args": [
                objects.require("relation_symbol", tokens[1]),
                objects.require("entity", tokens[2]),
                objects.require("relation_symbol", tokens[3]),
                objects.require("entity", tokens[4]),
                objects.require("entity", tokens[6]),
            ],
        }
    if len(tokens) >= 2 and tokens[:2] == ["ADD", "DERIVE"]:
        return {"kind": "action", "op": "ADD_DERIVE", "derivation": _relation_state([" ".join(tokens[1:])], objects)[0]}
    raise ValueError(f"{example_id}: malformed relation action target")


def _dfa_record(row: Mapping[str, Any]) -> dict[str, Any]:
    objects = _ObjectTable()
    facts: list[dict[str, Any]] = []
    input_steps: list[int] = []
    for line in _string_list(row["problem_lines"]):
        tokens = line.split()
        if len(tokens) == 4 and tokens[0] == "FACT":
            rel = objects.add("relation_symbol", tokens[1])
            left = objects.add("entity", tokens[2])
            right = objects.add("entity", tokens[3])
            facts.append({"pred": "FACT", "args": [rel, left, right]})
        elif len(tokens) == 4 and tokens[0] == "HYP" and tokens[2] == ":":
            step = objects.add("hypothesis", tokens[1])
            input_steps.append(step)
            facts.append({"pred": "INPUT_REL", "args": [step, objects.add("relation_symbol", tokens[3])]})
        elif len(tokens) == 2 and tokens[0] == "START":
            facts.append({"pred": "START", "args": [objects.add("entity", tokens[1])]})
        elif len(tokens) == 2 and tokens[0] == "GOAL":
            facts.append({"pred": "GOAL", "args": [objects.add("entity", tokens[1])]})
    if input_steps:
        facts.append({"pred": "INPUT_FIRST", "args": [input_steps[0]]})
        for left, right in zip(input_steps, input_steps[1:]):
            facts.append({"pred": "INPUT_NEXT", "args": [left, right]})

    return {
        "schema_version": SCHEMA_VERSION,
        "id": row["id"],
        "split": row["split"],
        "family": row["family"],
        "mode": row["mode"],
        "objects": objects.objects,
        "external_names": objects.external_names,
        "facts": facts,
        "state": {"kind": "sequence", "pred": "PATH", "objects": _path_state_objects(_string_list(row["state_lines"]), "PATH", objects)},
        "target": _path_target(row, state_pred="PATH", action_op="APPEND", objects=objects),
        "meta": row.get("meta", {}),
    }


def _line_repair_target(
    example_id: str,
    line: str,
    objects: _ObjectTable,
    *,
    field_as_arg: bool = False,
) -> dict[str, Any]:
    tokens = line.split()
    if len(tokens) < 4 or tokens[0] != "REPLACE":
        raise ValueError(f"{example_id}: malformed line repair target")
    if tokens[1] == "LINE":
        location = {"kind": "line_index", "index": int(tokens[2])}
        field_idx = 3
    elif tokens[1] == "FIRST":
        location = {"kind": "first"}
        field_idx = 2
    elif tokens[1] == "AFTER":
        anchor = tokens[2]
        anchor_type = _object_type_for_symbol(anchor)
        location = {"kind": "after", "anchor": objects.require(anchor_type, anchor)}
        field_idx = 3
    else:
        raise ValueError(f"{example_id}: malformed line repair target")

    field = tokens[field_idx]
    value = " ".join(tokens[field_idx + 1 :])
    if field == "WITH":
        return {
            "kind": "repair_action",
            "op": "REPLACE_LINE",
            "location": location,
            "line": _line_repair_replacement(value, objects),
        }
    args = [objects.require(_field_object_type(field, value), value)]
    if field_as_arg:
        args = [objects.add("field", field), *args]
    return {
        "kind": "repair_action",
        "op": "REPLACE_FIELD",
        "location": location,
        "field": field,
        "field_as_arg": field_as_arg,
        "args": args,
    }


def _line_repair_replacement(line: str, objects: _ObjectTable) -> dict[str, Any]:
    tokens = line.split()
    if len(tokens) in {4, 6} and tokens[0] == "DERIVE" and tokens[2] == "BY":
        return _implication_state([line], objects)[0]
    if len(tokens) == 6 and tokens[0] == "DERIVE" and tokens[4] == "VIA":
        return _relation_state([line], objects)[0]
    raise ValueError(f"Unsupported replacement line: {line}")


def _field_object_type(field: str, value: str) -> str:
    if field in {"HYP"}:
        return "hypothesis"
    if field in {"PROP", "FROM"}:
        return "proposition"
    if field in {"REL"}:
        return "relation_symbol"
    if field in {"LEFT", "RIGHT", "VIA"}:
        return "entity"
    return _object_type_for_symbol(value)


def _object_type_for_symbol(symbol: str) -> str:
    if symbol.startswith("h"):
        return "hypothesis"
    if symbol.startswith("p"):
        return "proposition"
    if symbol.startswith("r"):
        return "relation_symbol"
    return "entity"


def _verify_target(example_id: str, target_lines: list[str]) -> dict[str, Any]:
    if target_lines == ["VALID"]:
        return {"kind": "verify", "valid": True, "error_code": None}
    tokens = target_lines[0].split() if len(target_lines) == 1 else []
    if len(tokens) == 2 and tokens[0] == "INVALID":
        return {"kind": "verify", "valid": False, "error_code": tokens[1]}
    raise ValueError(f"{example_id}: malformed verify target")


def _term_record(row: Mapping[str, Any]) -> dict[str, Any]:
    objects = _ObjectTable()
    facts: list[dict[str, Any]] = []
    for line in _string_list(row["problem_lines"]):
        tokens = line.split()
        if len(tokens) >= 6 and tokens[0] == "RULE" and tokens[2] == ":" and "->" in tokens:
            arrow = tokens.index("->")
            rule = objects.add("rule", tokens[1])
            facts.append(
                {
                    "pred": "RULE",
                    "args": [rule],
                    "lhs": _parse_term(tokens[3:arrow], objects),
                    "rhs": _parse_term(tokens[arrow + 1 :], objects),
                }
            )
        elif len(tokens) >= 2 and tokens[0] == "START":
            facts.append({"pred": "START_TERM", "term": _parse_term(tokens[1:], objects)})
        elif len(tokens) >= 2 and tokens[0] == "GOAL":
            facts.append({"pred": "GOAL_TERM", "term": _parse_term(tokens[1:], objects)})
        elif tokens == ["QUERY", "NORMAL_FORM"]:
            facts.append({"pred": "QUERY_NORMAL_FORM", "args": []})

    return {
        "schema_version": SCHEMA_VERSION,
        "id": row["id"],
        "split": row["split"],
        "family": row["family"],
        "mode": row["mode"],
        "objects": objects.objects,
        "external_names": objects.external_names,
        "facts": facts,
        "state": {"kind": "rewrite_trace", "items": _term_state(_string_list(row["state_lines"]), objects)},
        "target": _term_target(row, objects),
        "meta": row.get("meta", {}),
    }


def _term_target(
    row: Mapping[str, Any],
    objects: _ObjectTable,
    *,
    rewrite_action: int | None = None,
    halt_action: int | None = None,
) -> dict[str, Any]:
    mode = str(row["mode"])
    target_lines = _string_list(row["target_lines"])
    if mode == "action":
        if len(target_lines) != 1:
            raise ValueError(f"{row['id']}: action target must be one line")
        target = _term_action_target(row["id"], target_lines[0], objects)
        if target["op"] == "RW" and rewrite_action is not None:
            return {"kind": "action", "op": "EXTEND_SEQUENCE", "args": [rewrite_action, *target["args"]], "path": target.get("path")}
        if target["op"] == "HALT" and halt_action is not None:
            return {"kind": "action", "op": "EXTEND_SEQUENCE", "args": [halt_action]}
        return target

    if mode == "repair_action":
        if len(target_lines) != 1:
            raise ValueError(f"{row['id']}: repair_action target must be one line")
        tokens = target_lines[0].split()
        if tokens == ["REPAIR", "FIRST_BAD"]:
            return {"kind": "repair_action", "op": "REPAIR_FIRST_BAD", "args": []}
        if tokens[:1] == ["REPAIR"]:
            action = _term_action_target(row["id"], " ".join(tokens[1:]), objects)
            return {"kind": "repair_action", "op": "REPAIR_REWRITE", "action": action}
        raise ValueError(f"{row['id']}: malformed term repair target")

    if mode == "verify":
        return _verify_target(row["id"], target_lines)

    if mode in {"improve", "repair", "complete"}:
        return {"kind": "state", "state": {"kind": "rewrite_trace", "items": _term_state(target_lines, objects)}}

    raise ValueError(f"{row['id']}: unsupported mode for relational export: {mode}")


def _term_state(state_lines: list[str], objects: _ObjectTable) -> list[dict[str, Any]]:
    items = []
    for line in state_lines:
        tokens = line.split()
        if len(tokens) >= 2 and tokens[0] == "TERM":
            items.append({"pred": "TERM", "term": _parse_term(tokens[1:], objects)})
        elif tokens[:1] == ["RW"]:
            items.append(_term_action_item(line, objects))
        elif tokens == ["HALT"]:
            items.append({"pred": "HALT", "args": []})
        else:
            raise ValueError(f"Malformed term state line: {line}")
    return items


def _term_action_target(example_id: str, line: str, objects: _ObjectTable) -> dict[str, Any]:
    tokens = line.split()
    if tokens == ["HALT"]:
        return {"kind": "action", "op": "HALT", "args": []}
    if tokens[:1] != ["RW"]:
        raise ValueError(f"{example_id}: malformed term action target")
    item = _term_action_item(line, objects)
    return {"kind": "action", "op": "RW", "args": item["args"], "path": item["path"]}


def _term_action_item(line: str, objects: _ObjectTable) -> dict[str, Any]:
    tokens = line.split()
    if len(tokens) == 2 and tokens[0] == "RW":
        return {"pred": "RW", "args": [objects.add("rule", tokens[1])], "path": None}
    if len(tokens) >= 4 and tokens[0] == "RW" and tokens[2] == "AT":
        return {"pred": "RW", "args": [objects.add("rule", tokens[1])], "path": _parse_path(tokens[3:])}
    raise ValueError(f"Malformed term action line: {line}")


def _parse_path(tokens: list[str]) -> list[str] | dict[str, list[str]]:
    if tokens == ["ROOT"]:
        return []
    if not tokens or any(token not in {"IN", "L", "R"} for token in tokens):
        return {"malformed": list(tokens)}
    return list(tokens)


def _parse_term(tokens: list[str], objects: _ObjectTable) -> dict[str, Any]:
    term, idx = _parse_term_at(tokens, 0, objects)
    if idx != len(tokens):
        raise ValueError(f"Unexpected trailing term tokens: {' '.join(tokens[idx:])}")
    return term


def _parse_term_at(tokens: list[str], idx: int, objects: _ObjectTable) -> tuple[dict[str, Any], int]:
    if idx >= len(tokens):
        raise ValueError("Unexpected end of term")
    token = tokens[idx]
    if token == "U":
        if idx + 1 >= len(tokens):
            raise ValueError("Unary term missing function symbol")
        function = objects.add("function_symbol", tokens[idx + 1])
        child, end = _parse_term_at(tokens, idx + 2, objects)
        return {"kind": "unary", "function": function, "child": child}, end
    if token == "B":
        if idx + 1 >= len(tokens):
            raise ValueError("Binary term missing function symbol")
        function = objects.add("function_symbol", tokens[idx + 1])
        left, next_idx = _parse_term_at(tokens, idx + 2, objects)
        right, end = _parse_term_at(tokens, next_idx, objects)
        return {"kind": "binary", "function": function, "left": left, "right": right}, end
    if token.startswith("v"):
        return {"kind": "variable", "object": objects.add("variable", token)}, idx + 1
    return {"kind": "constant", "object": objects.add("entity", token)}, idx + 1


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        raise ValueError("Expected a list of strings")
    return [str(item) for item in value]
