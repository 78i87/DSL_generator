from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

import numpy as np

from reasoning_dsl.relational import model_view, task_schema_record
from reasoning_dsl.relational_arrays import _expand_terms


OBJECT_TYPE_IDS = {
    "<PAD>": 0,
    "entity": 1,
    "predicate": 2,
    "operation": 3,
    "hypothesis": 4,
    "proposition": 5,
    "relation_symbol": 6,
    "rule": 7,
    "function_symbol": 8,
    "variable": 9,
    "term_node": 10,
    "field": 11,
    "location_root": 12,
    "location_after": 13,
    "location_index": 14,
    "property": 15,
}
FACT_PRED_IDS = {
    "<PAD>": 0,
    "SCHEMA_BINARY_REL": 1,
    "SCHEMA_SEQUENCE_STATE": 2,
    "SCHEMA_EXTEND_ACTION": 3,
    "RELATION_TUPLE": 4,
    "QUERY_START": 5,
    "QUERY_GOAL": 6,
    "STATE_ITEM": 7,
    "STATE_FIRST": 8,
    "STATE_LAST": 9,
    "STATE_NEXT": 10,
    "SCHEMA_DERIVATION_STATE": 11,
    "SCHEMA_APPLY_ACTION": 12,
    "SOURCE_FACT": 13,
    "SOURCE_RULE": 14,
    "STATE_SUPPORT": 15,
    "STATE_FROM": 16,
    "STATE_USED_SOURCE": 17,
    "SCHEMA_RELATION_STATE": 18,
    "SCHEMA_FOLLOW_ACTION": 19,
    "COMPOSE_RULE": 20,
    "QUERY_TUPLE": 21,
    "STATE_RELATION_TUPLE": 22,
    "STATE_VIA": 23,
    "SCHEMA_REWRITE_STATE": 24,
    "SCHEMA_REWRITE_ACTION": 25,
    "SCHEMA_HALT_ACTION": 26,
    "RULE_REF": 27,
    "RULE_LHS": 28,
    "RULE_RHS": 29,
    "START_TERM": 30,
    "GOAL_TERM": 31,
    "TERM_CONST": 32,
    "TERM_VAR": 33,
    "TERM_UNARY": 34,
    "TERM_BINARY": 35,
    "STATE_TERM": 36,
    "STATE_RW": 37,
    "STATE_HALT": 38,
    "QUERY_NORMAL_FORM": 39,
    "STATE_RW_STEP": 40,
    "STATE_RW_AT": 41,
    "STATE_RW_BAD_PATH": 42,
    "STATE_RW_EXPECTED": 43,
    "STATE_RW_RESULT": 44,
    "NODE_VALUE": 45,
    "NODE_CHILD": 46,
    "NODE_LEFT": 47,
    "NODE_RIGHT": 48,
    "RULE_INPUT": 49,
    "RULE_OUTPUT": 50,
    "QUERY_PROPERTY": 51,
    "TRANSITION_STEP": 52,
    "TRANSITION_AT": 53,
    "TRANSITION_BAD_LOCATION": 54,
    "TRANSITION_EXPECTED": 55,
    "TRANSITION_RESULT": 56,
    "NODE_APPLY": 57,
    "NODE_CONST": 58,
    "NODE_VAR": 59,
    "NODE_UNARY": 60,
    "NODE_BINARY": 61,
    "QUERY_RELATION": 62,
}
FACT_PREDICATE_CLASSES = {
    "<PAD>": "padding",
    "SCHEMA_BINARY_REL": "core_schema",
    "SCHEMA_SEQUENCE_STATE": "core_schema",
    "SCHEMA_EXTEND_ACTION": "core_schema",
    "RELATION_TUPLE": "core_schema",
    "QUERY_START": "core_schema",
    "QUERY_GOAL": "core_schema",
    "STATE_ITEM": "core_schema",
    "STATE_FIRST": "core_schema",
    "STATE_LAST": "core_schema",
    "STATE_NEXT": "core_schema",
    "STATE_SUPPORT": "core_schema",
    "STATE_FROM": "core_schema",
    "STATE_USED_SOURCE": "core_schema",
    "COMPOSE_RULE": "core_schema",
    "QUERY_TUPLE": "core_schema",
    "STATE_RELATION_TUPLE": "core_schema",
    "STATE_VIA": "core_schema",
    "SCHEMA_DERIVATION_STATE": "legacy_task_schema",
    "SCHEMA_APPLY_ACTION": "legacy_task_schema",
    "SOURCE_FACT": "legacy_task_schema",
    "SOURCE_RULE": "legacy_task_schema",
    "SCHEMA_RELATION_STATE": "legacy_task_schema",
    "SCHEMA_FOLLOW_ACTION": "legacy_task_schema",
    "SCHEMA_REWRITE_STATE": "domain_schema",
    "SCHEMA_REWRITE_ACTION": "domain_schema",
    "SCHEMA_HALT_ACTION": "core_schema",
    "RULE_REF": "domain_schema",
    "RULE_LHS": "domain_schema",
    "RULE_RHS": "domain_schema",
    "START_TERM": "domain_schema",
    "GOAL_TERM": "domain_schema",
    "TERM_CONST": "domain_schema",
    "TERM_VAR": "domain_schema",
    "TERM_UNARY": "domain_schema",
    "TERM_BINARY": "domain_schema",
    "STATE_TERM": "domain_schema",
    "STATE_RW": "domain_schema",
    "STATE_HALT": "domain_schema",
    "QUERY_NORMAL_FORM": "domain_schema",
    "STATE_RW_STEP": "domain_schema",
    "STATE_RW_AT": "domain_schema",
    "STATE_RW_BAD_PATH": "domain_schema",
    "STATE_RW_EXPECTED": "domain_schema",
    "STATE_RW_RESULT": "domain_schema",
    "NODE_VALUE": "core_schema",
    "NODE_CHILD": "core_schema",
    "NODE_LEFT": "core_schema",
    "NODE_RIGHT": "core_schema",
    "RULE_INPUT": "core_schema",
    "RULE_OUTPUT": "core_schema",
    "QUERY_PROPERTY": "core_schema",
    "TRANSITION_STEP": "core_schema",
    "TRANSITION_AT": "core_schema",
    "TRANSITION_BAD_LOCATION": "core_schema",
    "TRANSITION_EXPECTED": "core_schema",
    "TRANSITION_RESULT": "core_schema",
    "NODE_APPLY": "core_schema",
    "NODE_CONST": "core_schema",
    "NODE_VAR": "core_schema",
    "NODE_UNARY": "core_schema",
    "NODE_BINARY": "core_schema",
    "QUERY_RELATION": "core_schema",
}
V2_LEGACY_FACT_PREDICATES = {
    name for name, predicate_class in FACT_PREDICATE_CLASSES.items() if predicate_class == "legacy_task_schema"
}
MODE_IDS = {"action": 1, "repair_action": 2, "verify": 3}
OP_IDS = {
    "<PAD>": 0,
    "EXTEND_SEQUENCE": 1,
    "REPLACE_ROOT": 2,
    "REPLACE_AFTER": 3,
    "REPLACE_NODE": 4,
    "VERIFY": 5,
    "APPLY": 6,
    "REPLACE_FIELD_HYP": 7,
    "REPLACE_FIELD_FROM": 8,
    "REPLACE_FIELD_PROP": 9,
    "FOLLOW": 10,
    "REPLACE_FIELD_REL": 11,
    "REPLACE_FIELD_LEFT": 12,
    "REPLACE_FIELD_RIGHT": 13,
    "REPLACE_FIELD_VIA": 14,
    "RW": 15,
    "HALT": 16,
    "REPAIR_FIRST_BAD": 17,
    "REPAIR_REWRITE": 18,
    "REPLACE_FIELD": 19,
    "REPLACE_ITEM": 20,
}
VALIDITY_IDS = {"<PAD>": 0, "VALID": 1, "INVALID": 2}
SUPPORTED_FAMILIES = {
    "graph_reachability",
    "shortest_path_lite",
    "tree_ancestry",
    "implication_chains",
    "relation_composition",
    "term_rewriting",
    "equality_rewriting_lite",
}
SUPPORTED_MODES = set(MODE_IDS)


def fact_predicate_generality_report() -> dict[str, list[str]]:
    """Return current task-schema predicate classes for v2 cleanup planning."""
    missing = sorted(set(FACT_PRED_IDS) - set(FACT_PREDICATE_CLASSES))
    extra = sorted(set(FACT_PREDICATE_CLASSES) - set(FACT_PRED_IDS))
    by_class: dict[str, list[str]] = {}
    for name in FACT_PRED_IDS:
        by_class.setdefault(FACT_PREDICATE_CLASSES.get(name, "unclassified"), []).append(name)
    if missing:
        by_class["unclassified"] = missing
    if extra:
        by_class["unused_classifications"] = extra
    return {key: sorted(value) for key, value in sorted(by_class.items())}


@dataclass(frozen=True)
class TaskSchemaArrayBundle:
    arrays: dict[str, np.ndarray]
    metadata: dict[str, Any]
    records: list[dict[str, Any]]


def records_to_task_schema_arrays(
    records: list[Mapping[str, Any]],
    *,
    global_shape: Mapping[str, int] | None = None,
    error_vocab: dict[str, int] | None = None,
    fail_on_legacy_predicates: bool = False,
) -> TaskSchemaArrayBundle:
    if not records:
        raise ValueError("Cannot export empty task-schema arrays")
    normalized = [_normalize_record(dict(record)) for record in records]
    _validate_supported(normalized)

    encoded_facts = [_facts_with_state(record) for record in normalized]
    active_fact_predicates = sorted({fact["pred"] for facts in encoded_facts for fact in facts})
    active_fact_predicate_classes: dict[str, list[str]] = {}
    for name in active_fact_predicates:
        predicate_class = FACT_PREDICATE_CLASSES.get(name, "unclassified")
        active_fact_predicate_classes.setdefault(predicate_class, []).append(name)
    active_legacy_fact_predicates = sorted(set(active_fact_predicates) & V2_LEGACY_FACT_PREDICATES)
    active_ops = sorted({_target_op(record["target"]) for record in normalized if _target_op(record["target"]) != "<PAD>"})
    if fail_on_legacy_predicates:
        if active_legacy_fact_predicates:
            raise ValueError(f"Legacy task-schema fact predicates present: {active_legacy_fact_predicates}")
    max_objects = int(global_shape["max_objects"]) if global_shape else max(len(record["objects"]) for record in normalized)
    max_facts = int(global_shape["max_facts"]) if global_shape else max(len(facts) for facts in encoded_facts)
    max_fact_args = int(global_shape["max_fact_args"]) if global_shape else max(_max_fact_args(facts) for facts in encoded_facts)
    max_state_len = int(global_shape["max_state_len"]) if global_shape else max(len(_state_objects(record)) for record in normalized)
    max_target_args = int(global_shape["max_target_args"]) if global_shape else max(len(_target_args(record["target"])) for record in normalized)
    error_vocab = dict(error_vocab or _error_vocab(normalized))

    n = len(normalized)
    object_types = np.zeros((n, max_objects), dtype=np.int32)
    fact_preds = np.zeros((n, max_facts), dtype=np.int32)
    fact_args = np.zeros((n, max_facts, max_fact_args), dtype=np.int32)
    state_objects = np.zeros((n, max_state_len), dtype=np.int32)
    mode_ids = np.zeros((n,), dtype=np.int32)
    target_ops = np.zeros((n,), dtype=np.int32)
    target_args = np.zeros((n, max_target_args), dtype=np.int32)
    target_indices = np.full((n,), -1, dtype=np.int32)
    target_validity = np.zeros((n,), dtype=np.int32)
    target_errors = np.zeros((n,), dtype=np.int32)

    for row_idx, record in enumerate(normalized):
        mode_ids[row_idx] = MODE_IDS[record["mode"]]
        for obj_idx, obj in enumerate(record["objects"]):
            object_types[row_idx, obj_idx] = OBJECT_TYPE_IDS[obj["type"]]
        for fact_idx, fact in enumerate(encoded_facts[row_idx]):
            fact_preds[row_idx, fact_idx] = FACT_PRED_IDS[fact["pred"]]
            for arg_idx, arg in enumerate(fact.get("args", [])[:max_fact_args]):
                fact_args[row_idx, fact_idx, arg_idx] = int(arg) + 1
        for pos, obj_idx in enumerate(_state_objects(record)):
            state_objects[row_idx, pos] = int(obj_idx) + 1
        _encode_target(
            record["target"],
            row_idx=row_idx,
            target_ops=target_ops,
            target_args=target_args,
            target_indices=target_indices,
            target_validity=target_validity,
            target_errors=target_errors,
            error_vocab=error_vocab,
        )

    metadata = {
        "schema_version": "relational_task_schema_arrays_v1",
        "examples": n,
        "families": sorted({record["family"] for record in normalized}),
        "modes": sorted({record["mode"] for record in normalized}),
        "object_type_ids": OBJECT_TYPE_IDS,
        "fact_pred_ids": FACT_PRED_IDS,
        "fact_predicate_classes": FACT_PREDICATE_CLASSES,
        "active_fact_predicates": active_fact_predicates,
        "active_fact_predicate_classes": {
            key: sorted(value) for key, value in sorted(active_fact_predicate_classes.items())
        },
        "active_legacy_fact_predicates": active_legacy_fact_predicates,
        "mode_ids": MODE_IDS,
        "op_ids": OP_IDS,
        "active_ops": active_ops,
        "validity_ids": VALIDITY_IDS,
        "error_ids": error_vocab,
        "max_objects": int(max_objects),
        "max_facts": int(max_facts),
        "max_fact_args": int(max_fact_args),
        "max_state_len": int(max_state_len),
        "max_target_args": int(max_target_args),
        "arg_pad_id": 0,
        "object_ref_offset": 1,
    }
    arrays = {
        "object_types": object_types,
        "fact_preds": fact_preds,
        "fact_args": fact_args,
        "state_objects": state_objects,
        "mode_ids": mode_ids,
        "target_ops": target_ops,
        "target_args": target_args,
        "target_indices": target_indices,
        "target_validity": target_validity,
        "target_errors": target_errors,
    }
    return TaskSchemaArrayBundle(arrays=arrays, metadata=metadata, records=normalized)


def export_task_schema_arrays_from_jsonl(
    data_dir: str | Path,
    output_dir: str | Path,
    *,
    families: set[str] | None = None,
    modes: set[str] | None = None,
    fail_on_legacy_predicates: bool = False,
) -> None:
    families = set(families or SUPPORTED_FAMILIES)
    modes = set(modes or SUPPORTED_MODES)
    unsupported_families = families - SUPPORTED_FAMILIES
    unsupported_modes = modes - SUPPORTED_MODES
    if unsupported_families:
        raise ValueError(f"Unsupported task-schema families: {sorted(unsupported_families)}")
    if unsupported_modes:
        raise ValueError(f"Unsupported task-schema modes: {sorted(unsupported_modes)}")

    input_root = Path(data_dir) / "jsonl"
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    if not input_root.exists():
        raise ValueError(f"Missing JSONL directory: {input_root}")

    records_by_split: dict[str, list[dict[str, Any]]] = {}
    for path in sorted(input_root.glob("*.jsonl")):
        records = []
        for row in _read_jsonl(path):
            if row["family"] not in families or row["mode"] not in modes:
                continue
            records.append(model_view(task_schema_record(row)))
        if records:
            records_by_split[path.stem] = records
    if not records_by_split:
        raise ValueError("No supported examples matched the requested task-schema array filters")

    all_records = [_normalize_record(dict(record)) for records in records_by_split.values() for record in records]
    all_facts = [_facts_with_state(record) for record in all_records]
    global_shape = {
        "max_objects": max(len(record["objects"]) for record in all_records),
        "max_facts": max(len(facts) for facts in all_facts),
        "max_fact_args": max(_max_fact_args(facts) for facts in all_facts),
        "max_state_len": max(len(_state_objects(record)) for record in all_records),
        "max_target_args": max(len(_target_args(record["target"])) for record in all_records),
    }
    global_error_vocab = _error_vocab(all_records)

    for split, records in sorted(records_by_split.items()):
        bundle = records_to_task_schema_arrays(
            records,
            global_shape=global_shape,
            error_vocab=global_error_vocab,
            fail_on_legacy_predicates=fail_on_legacy_predicates,
        )
        split_dir = output / split
        split_dir.mkdir(parents=True, exist_ok=True)
        (split_dir / "dataset.json").write_text(json.dumps(bundle.metadata, indent=2, sort_keys=True), encoding="utf-8")
        with (split_dir / "records.jsonl").open("w", encoding="utf-8") as f:
            for record in bundle.records:
                f.write(json.dumps(record, sort_keys=True) + "\n")
        for name, array in bundle.arrays.items():
            np.save(split_dir / f"all__{name}.npy", array)


def _validate_supported(records: list[Mapping[str, Any]]) -> None:
    for record in records:
        if record["family"] not in SUPPORTED_FAMILIES:
            raise ValueError(f"Unsupported task-schema family: {record['family']}")
        if record["mode"] not in SUPPORTED_MODES:
            raise ValueError(f"Unsupported task-schema mode: {record['mode']}")
        for obj in record["objects"]:
            if obj["type"] not in OBJECT_TYPE_IDS:
                raise ValueError(f"Unsupported task-schema object type: {obj['type']}")
        for fact in _facts_with_state(record):
            if fact["pred"] not in FACT_PRED_IDS:
                raise ValueError(f"Unsupported task-schema fact predicate: {fact['pred']}")


def _normalize_record(record: dict[str, Any]) -> dict[str, Any]:
    state = dict(record.get("state", {}))
    if record.get("family") in {"term_rewriting", "equality_rewriting_lite"} and state.get("kind") != "rewrite_trace":
        return record
    expanded = _expand_terms(record, generic_predicates=True)
    if state.get("kind") == "rewrite_trace" and "predicate" in state:
        expanded["state"] = dict(expanded["state"])
        expanded["state"]["predicate"] = int(state["predicate"])
    return expanded


def _facts_with_state(record: Mapping[str, Any]) -> list[dict[str, Any]]:
    facts = [dict(fact) for fact in record["facts"]]
    state = record["state"]
    state_pred = int(state["predicate"])
    if state["kind"] == "derivations":
        for item in state.get("items", []):
            args = [int(arg) for arg in item.get("args", [])]
            if not args:
                continue
            facts.append({"pred": "STATE_ITEM", "args": [state_pred, args[0]]})
            if item.get("pred") in {"DERIVE", "DERIVE_FROM"} and len(args) >= 2:
                facts.append({"pred": "STATE_SUPPORT", "args": [state_pred, args[0], args[1]]})
                facts.append({"pred": "STATE_USED_SOURCE", "args": [state_pred, args[1]]})
            if item.get("pred") == "DERIVE_FROM" and len(args) >= 3:
                facts.append({"pred": "STATE_FROM", "args": [state_pred, args[0], args[2]]})
        return facts
    if state["kind"] == "relation_derivations":
        for item in state.get("items", []):
            args = [int(arg) for arg in item.get("args", [])]
            if len(args) >= 3:
                facts.append({"pred": "STATE_ITEM", "args": [state_pred, args[0], args[1], args[2]]})
            if len(args) >= 4:
                facts.append({"pred": "STATE_SUPPORT", "args": [state_pred, args[0], args[1], args[2], args[3]]})
        return facts
    if state["kind"] != "sequence":
        raise ValueError(f"Unsupported task-schema state kind: {state['kind']}")
    objects = [int(obj) for obj in state.get("objects", [])]
    for obj in objects:
        facts.append({"pred": "STATE_ITEM", "args": [state_pred, obj]})
    if objects:
        facts.append({"pred": "STATE_FIRST", "args": [state_pred, objects[0]]})
        facts.append({"pred": "STATE_LAST", "args": [state_pred, objects[-1]]})
    for left, right in zip(objects, objects[1:]):
        facts.append({"pred": "STATE_NEXT", "args": [state_pred, left, right]})
    return facts


def _state_objects(record: Mapping[str, Any]) -> list[int]:
    state = record["state"]
    if "objects" in state:
        return [int(obj) for obj in state.get("objects", [])]
    if state.get("kind") == "derivations":
        return [int(item["args"][0]) for item in state.get("items", []) if item.get("args")]
    return []


def _target_args(target: Mapping[str, Any]) -> list[int]:
    args = list(target.get("args", []))
    if not args and isinstance(target.get("action"), Mapping):
        args = list(target["action"].get("args", []))
    return [int(arg) for arg in args]


def _max_fact_args(facts: list[Mapping[str, Any]]) -> int:
    return max((len(fact.get("args", [])) for fact in facts), default=0)


def _error_vocab(records: list[Mapping[str, Any]]) -> dict[str, int]:
    codes = sorted(
        {
            str(record["target"]["error_code"])
            for record in records
            if record["target"].get("kind") == "verify" and record["target"].get("error_code") is not None
        }
    )
    return {"<PAD>": 0, **{code: idx + 1 for idx, code in enumerate(codes)}}


def _encode_target(
    target: Mapping[str, Any],
    *,
    row_idx: int,
    target_ops: np.ndarray,
    target_args: np.ndarray,
    target_indices: np.ndarray,
    target_validity: np.ndarray,
    target_errors: np.ndarray,
    error_vocab: dict[str, int],
) -> None:
    kind = target["kind"]
    if kind in {"action", "repair_action"}:
        target_ops[row_idx] = OP_IDS[_target_op(target)]
        for arg_idx, arg in enumerate(_target_args(target)):
            target_args[row_idx, arg_idx] = int(arg) + 1
        target_indices[row_idx] = int(target.get("index", -1))
        return
    if kind == "verify":
        target_ops[row_idx] = OP_IDS["VERIFY"]
        if target["valid"]:
            target_validity[row_idx] = VALIDITY_IDS["VALID"]
        else:
            target_validity[row_idx] = VALIDITY_IDS["INVALID"]
            target_errors[row_idx] = error_vocab[str(target["error_code"])]
        return
    raise ValueError(f"Unsupported task-schema target kind: {kind}")


def _target_op(target: Mapping[str, Any]) -> str:
    if target["kind"] == "verify":
        return "VERIFY"
    if target["kind"] == "repair_action" and target["op"] == "REPLACE_FIELD":
        if target.get("field_as_arg"):
            return "REPLACE_FIELD"
        return f"REPLACE_FIELD_{target['field']}"
    return str(target["op"])


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]
