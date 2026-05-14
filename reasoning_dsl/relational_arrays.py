from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

import numpy as np

from reasoning_dsl.relational import model_view, relational_record


OBJECT_TYPE_IDS = {
    "<PAD>": 0,
    "entity": 1,
    "hypothesis": 2,
    "proposition": 3,
    "relation_symbol": 4,
    "rule": 5,
    "function_symbol": 6,
    "variable": 7,
    "term_node": 8,
}
FACT_PRED_IDS = {
    "<PAD>": 0,
    "EDGE": 1,
    "PARENT": 2,
    "QUERY_START": 3,
    "QUERY_GOAL": 4,
    "STATE_FIRST": 5,
    "STATE_LAST": 6,
    "STATE_NEXT": 7,
    "HYP_FACT": 8,
    "HYP_RULE": 9,
    "GOAL": 10,
    "FACT": 11,
    "RULE_COMPOSE": 12,
    "QUERY": 13,
    "STATE_DERIVE": 14,
    "STATE_DERIVE_FROM": 15,
    "RULE_REF": 16,
    "RULE_LHS": 17,
    "RULE_RHS": 18,
    "START_TERM": 19,
    "GOAL_TERM": 20,
    "TERM_CONST": 21,
    "TERM_VAR": 22,
    "TERM_UNARY": 23,
    "TERM_BINARY": 24,
    "STATE_TERM": 25,
    "STATE_RW": 26,
    "STATE_HALT": 27,
    "QUERY_NORMAL_FORM": 28,
    "STATE_RW_STEP": 29,
    "STATE_RW_AT": 30,
    "STATE_RW_BAD_PATH": 31,
    "STATE_RW_EXPECTED": 32,
    "STATE_RW_RESULT": 33,
    "STATE_KNOWN": 34,
    "INPUT_REL": 35,
    "INPUT_FIRST": 36,
    "INPUT_NEXT": 37,
    "START": 38,
}
MODE_IDS = {"action": 1, "repair_action": 2, "verify": 3}
OP_IDS = {
    "<PAD>": 0,
    "APPEND": 1,
    "DESCEND": 2,
    "REPLACE_ROOT": 3,
    "REPLACE_AFTER": 4,
    "REPLACE_NODE": 5,
    "VERIFY": 6,
    "APPLY": 7,
    "FOLLOW": 8,
    "REPLACE_FIELD_HYP": 9,
    "REPLACE_FIELD_FROM": 10,
    "REPLACE_FIELD_VIA": 11,
    "RW": 12,
    "HALT": 13,
    "REPAIR_FIRST_BAD": 14,
    "REPAIR_REWRITE": 15,
}
VALIDITY_IDS = {"<PAD>": 0, "VALID": 1, "INVALID": 2}
SUPPORTED_FAMILIES = {
    "graph_reachability",
    "shortest_path_lite",
    "dfa_simulation_lite",
    "equality_rewriting_lite",
    "tree_ancestry",
    "implication_chains",
    "relation_composition",
    "term_rewriting",
}
SUPPORTED_MODES = set(MODE_IDS)


@dataclass(frozen=True)
class RelationalArrayBundle:
    arrays: dict[str, np.ndarray]
    metadata: dict[str, Any]
    records: list[dict[str, Any]]


def records_to_relational_arrays(
    records: list[Mapping[str, Any]],
    *,
    global_shape: Mapping[str, int] | None = None,
    error_vocab: dict[str, int] | None = None,
) -> RelationalArrayBundle:
    if not records:
        raise ValueError("Cannot export empty relational arrays")

    normalized = [_expand_terms(dict(record)) for record in records]
    _validate_supported(normalized)

    max_objects = int(global_shape["max_objects"]) if global_shape else max(len(record["objects"]) for record in normalized)
    encoded_facts = [_facts_with_state(record) for record in normalized]
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
        "schema_version": "relational_path_arrays_v1",
        "examples": n,
        "families": sorted({record["family"] for record in normalized}),
        "modes": sorted({record["mode"] for record in normalized}),
        "object_type_ids": OBJECT_TYPE_IDS,
        "fact_pred_ids": FACT_PRED_IDS,
        "mode_ids": MODE_IDS,
        "op_ids": OP_IDS,
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
    return RelationalArrayBundle(arrays=arrays, metadata=metadata, records=normalized)


def export_relational_arrays_from_jsonl(
    data_dir: str | Path,
    output_dir: str | Path,
    *,
    families: set[str] | None = None,
    modes: set[str] | None = None,
) -> None:
    families = set(families or SUPPORTED_FAMILIES)
    modes = set(modes or SUPPORTED_MODES)
    unsupported_families = families - SUPPORTED_FAMILIES
    unsupported_modes = modes - SUPPORTED_MODES
    if unsupported_families:
        raise ValueError(f"Unsupported relational-array families: {sorted(unsupported_families)}")
    if unsupported_modes:
        raise ValueError(f"Unsupported relational-array modes: {sorted(unsupported_modes)}")

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
            records.append(model_view(relational_record(row)))
        if not records:
            continue
        records_by_split[path.stem] = records

    if not records_by_split:
        raise ValueError("No supported examples matched the requested relational-array filters")

    all_records = [record for records in records_by_split.values() for record in records]
    all_expanded = [_expand_terms(dict(record)) for record in all_records]
    global_shape = {
        "max_objects": max(len(record["objects"]) for record in all_expanded),
        "max_facts": max(len(_facts_with_state(record)) for record in all_expanded),
        "max_fact_args": max(_max_fact_args(_facts_with_state(record)) for record in all_expanded),
        "max_state_len": max(len(_state_objects(record)) for record in all_expanded),
        "max_target_args": max(len(_target_args(record["target"])) for record in all_expanded),
    }
    global_error_vocab = _error_vocab(all_expanded)

    for split, records in sorted(records_by_split.items()):
        bundle = records_to_relational_arrays(records, global_shape=global_shape, error_vocab=global_error_vocab)
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
            raise ValueError(f"Unsupported relational-array family: {record['family']}")
        if record["mode"] not in SUPPORTED_MODES:
            raise ValueError(f"Unsupported relational-array mode: {record['mode']}")
        if record["state"]["kind"] not in {"sequence", "derivations", "relation_derivations"}:
            raise ValueError(f"Unsupported state kind: {record['state']['kind']}")
        for obj in record["objects"]:
            if obj["type"] not in OBJECT_TYPE_IDS:
                raise ValueError(f"Unsupported object type: {obj['type']}")
        for fact in record["facts"]:
            if fact["pred"] not in FACT_PRED_IDS:
                raise ValueError(f"Unsupported fact predicate: {fact['pred']}")


def _expand_terms(record: dict[str, Any], *, generic_predicates: bool = False) -> dict[str, Any]:
    if record.get("family") not in {"term_rewriting", "equality_rewriting_lite"}:
        return record

    objects = [dict(obj) for obj in record["objects"]]
    facts: list[dict[str, Any]] = []
    term_cache: dict[tuple[Any, ...], int] = {}
    node_terms: dict[int, tuple[Any, ...]] = {}
    rule_terms: dict[int, tuple[tuple[Any, ...], tuple[Any, ...]]] = {}

    def add_term_key(key: tuple[Any, ...]) -> int:
        if key in term_cache:
            return term_cache[key]
        node_idx = len(objects)
        objects.append({"type": "term_node"})
        term_cache[key] = node_idx
        node_terms[node_idx] = key
        kind = key[0]
        if kind == "constant":
            pred = "NODE_CONST" if generic_predicates else "TERM_CONST"
            facts.append({"pred": pred, "args": [node_idx, int(key[1])]})
            return node_idx
        if kind == "variable":
            pred = "NODE_VAR" if generic_predicates else "TERM_VAR"
            facts.append({"pred": pred, "args": [node_idx, int(key[1])]})
            return node_idx
        if kind == "unary":
            child = add_term_key(key[2])
            if generic_predicates:
                facts.append({"pred": "NODE_UNARY", "args": [node_idx, int(key[1]), child]})
            else:
                facts.append({"pred": "TERM_UNARY", "args": [node_idx, int(key[1]), child]})
            return node_idx
        if kind == "binary":
            left = add_term_key(key[2])
            right = add_term_key(key[3])
            if generic_predicates:
                facts.append({"pred": "NODE_BINARY", "args": [node_idx, int(key[1]), left, right]})
            else:
                facts.append({"pred": "TERM_BINARY", "args": [node_idx, int(key[1]), left, right]})
            return node_idx
        raise ValueError(f"Unsupported term kind: {kind}")

    def add_term(term: Mapping[str, Any]) -> int:
        return add_term_key(_term_key(term))

    for fact in record["facts"]:
        pred = fact["pred"]
        if pred == "RULE":
            rule = int(fact["args"][0])
            lhs_key = _term_key(fact["lhs"])
            rhs_key = _term_key(fact["rhs"])
            lhs = add_term_key(lhs_key)
            rhs = add_term_key(rhs_key)
            rule_terms[rule] = (lhs_key, rhs_key)
            if generic_predicates:
                facts.append({"pred": "RULE_INPUT", "args": [rule, lhs]})
                facts.append({"pred": "RULE_OUTPUT", "args": [rule, rhs]})
            else:
                facts.append({"pred": "RULE_REF", "args": [rule]})
                facts.append({"pred": "RULE_LHS", "args": [rule, lhs]})
                facts.append({"pred": "RULE_RHS", "args": [rule, rhs]})
        elif pred in {"START_TERM", "GOAL_TERM"}:
            root = add_term(fact["term"])
            if generic_predicates:
                facts.append({"pred": "QUERY_START" if pred == "START_TERM" else "QUERY_GOAL", "args": [root]})
            else:
                facts.append({"pred": pred, "args": [root]})
        elif generic_predicates and pred in {"QUERY_START", "QUERY_GOAL"} and "term" in fact:
            facts.append({"pred": pred, "args": [add_term(fact["term"])]})
        elif generic_predicates and pred == "QUERY_NORMAL_FORM":
            property_idx = len(objects)
            objects.append({"type": "property"})
            facts.append({"pred": "QUERY_PROPERTY", "args": [property_idx]})
        else:
            facts.append(dict(fact))

    state_objects: list[int] = []
    state_items: list[dict[str, Any]] = []
    for item in record["state"].get("items", []):
        pred = item["pred"]
        if pred == "TERM":
            root = add_term(item["term"])
            state_objects.append(root)
            if not generic_predicates:
                facts.append({"pred": "STATE_TERM", "args": [root]})
            state_items.append({"pred": "TERM", "root": root})
        elif pred == "RW":
            rule = int(item["args"][0])
            state_objects.append(rule)
            if not generic_predicates:
                facts.append({"pred": "STATE_RW", "args": [rule]})
            state_items.append({"pred": "RW", "rule": rule, "path": item.get("path")})
        elif pred == "HALT":
            if not generic_predicates:
                facts.append({"pred": "STATE_HALT", "args": []})
            state_items.append({"pred": "HALT"})
        else:
            facts.append(dict(item))

    previous_term: int | None = None
    pending_rewrite: dict[str, Any] | None = None
    for item in state_items:
        if item["pred"] == "TERM":
            root = int(item["root"])
            if previous_term is not None and pending_rewrite is not None:
                rule = int(pending_rewrite["rule"])
                if generic_predicates:
                    facts.append({"pred": "TRANSITION_STEP", "args": [previous_term, rule, root]})
                else:
                    facts.append({"pred": "STATE_RW_STEP", "args": [previous_term, rule, root]})
                path = pending_rewrite.get("path")
                if isinstance(path, list):
                    subterm_key = _term_key_at_path(node_terms[previous_term], path)
                    if subterm_key is None:
                        if generic_predicates:
                            facts.append({"pred": "TRANSITION_BAD_LOCATION", "args": [previous_term, rule, root]})
                        else:
                            facts.append({"pred": "STATE_RW_BAD_PATH", "args": [previous_term, rule, root]})
                    else:
                        if generic_predicates:
                            facts.append({"pred": "TRANSITION_AT", "args": [previous_term, rule, term_cache[subterm_key]]})
                        else:
                            facts.append({"pred": "STATE_RW_AT", "args": [previous_term, rule, term_cache[subterm_key]]})
                        expected_key = _rewrite_key_at_path(node_terms[previous_term], path, rule_terms.get(rule))
                        if expected_key is not None:
                            expected = add_term_key(expected_key)
                            if generic_predicates:
                                facts.append({"pred": "TRANSITION_EXPECTED", "args": [previous_term, rule, expected]})
                                facts.append({"pred": "TRANSITION_RESULT", "args": [previous_term, rule, root, expected]})
                            else:
                                facts.append({"pred": "STATE_RW_EXPECTED", "args": [previous_term, rule, expected]})
                                facts.append({"pred": "STATE_RW_RESULT", "args": [previous_term, rule, root, expected]})
                elif isinstance(path, dict):
                    if generic_predicates:
                        facts.append({"pred": "TRANSITION_BAD_LOCATION", "args": [previous_term, rule, root]})
                    else:
                        facts.append({"pred": "STATE_RW_BAD_PATH", "args": [previous_term, rule, root]})
                elif path is None:
                    expected_key = _rewrite_first_key_match(node_terms[previous_term], rule_terms.get(rule))
                    if expected_key is not None:
                        expected = add_term_key(expected_key)
                        if generic_predicates:
                            facts.append({"pred": "TRANSITION_EXPECTED", "args": [previous_term, rule, expected]})
                            facts.append({"pred": "TRANSITION_RESULT", "args": [previous_term, rule, root, expected]})
                        else:
                            facts.append({"pred": "STATE_RW_EXPECTED", "args": [previous_term, rule, expected]})
                            facts.append({"pred": "STATE_RW_RESULT", "args": [previous_term, rule, root, expected]})
            previous_term = root
            pending_rewrite = None
        elif item["pred"] == "RW":
            pending_rewrite = item

    expanded = dict(record)
    expanded["objects"] = objects
    expanded["facts"] = facts
    expanded["state"] = {"kind": "sequence", "objects": state_objects}
    return expanded


def _term_key(term: Mapping[str, Any]) -> tuple[Any, ...]:
    kind = term["kind"]
    if kind in {"constant", "variable"}:
        return (kind, int(term["object"]))
    if kind == "unary":
        return (kind, int(term["function"]), _term_key(term["child"]))
    if kind == "binary":
        return (kind, int(term["function"]), _term_key(term["left"]), _term_key(term["right"]))
    raise ValueError(f"Unsupported term kind: {kind}")


def _term_key_at_path(term: tuple[Any, ...], path: list[str]) -> tuple[Any, ...] | None:
    current = term
    for step in path:
        if step == "IN" and current[0] == "unary":
            current = current[2]
        elif step == "L" and current[0] == "binary":
            current = current[2]
        elif step == "R" and current[0] == "binary":
            current = current[3]
        else:
            return None
    return current


def _rewrite_key_at_path(
    term: tuple[Any, ...],
    path: list[str],
    rule: tuple[tuple[Any, ...], tuple[Any, ...]] | None,
) -> tuple[Any, ...] | None:
    if rule is None:
        return None
    lhs, rhs = rule
    subterm = _term_key_at_path(term, path)
    if subterm is None:
        return None
    bindings: dict[int, tuple[Any, ...]] = {}
    if not _term_key_matches(lhs, subterm, bindings):
        return None
    return _replace_key_at_path(term, path, _instantiate_key(rhs, bindings))


def _rewrite_first_key_match(
    term: tuple[Any, ...],
    rule: tuple[tuple[Any, ...], tuple[Any, ...]] | None,
) -> tuple[Any, ...] | None:
    if rule is None:
        return None
    lhs, rhs = rule
    bindings: dict[int, tuple[Any, ...]] = {}
    if _term_key_matches(lhs, term, bindings):
        return _instantiate_key(rhs, bindings)
    if term[0] == "unary":
        child = _rewrite_first_key_match(term[2], rule)
        if child is not None:
            return ("unary", term[1], child)
    if term[0] == "binary":
        left = _rewrite_first_key_match(term[2], rule)
        if left is not None:
            return ("binary", term[1], left, term[3])
        right = _rewrite_first_key_match(term[3], rule)
        if right is not None:
            return ("binary", term[1], term[2], right)
    return None


def _replace_key_at_path(term: tuple[Any, ...], path: list[str], replacement: tuple[Any, ...]) -> tuple[Any, ...]:
    if not path:
        return replacement
    head, *tail = path
    if head == "IN" and term[0] == "unary":
        return ("unary", term[1], _replace_key_at_path(term[2], tail, replacement))
    if head == "L" and term[0] == "binary":
        return ("binary", term[1], _replace_key_at_path(term[2], tail, replacement), term[3])
    if head == "R" and term[0] == "binary":
        return ("binary", term[1], term[2], _replace_key_at_path(term[3], tail, replacement))
    return term


def _term_key_matches(
    pattern: tuple[Any, ...],
    term: tuple[Any, ...],
    bindings: dict[int, tuple[Any, ...]],
) -> bool:
    if pattern[0] == "variable":
        var = int(pattern[1])
        if var in bindings:
            return bindings[var] == term
        bindings[var] = term
        return True
    if pattern[0] != term[0]:
        return False
    if pattern[0] == "constant":
        return pattern[1] == term[1]
    if pattern[0] == "unary":
        return pattern[1] == term[1] and _term_key_matches(pattern[2], term[2], bindings)
    if pattern[0] == "binary":
        return (
            pattern[1] == term[1]
            and _term_key_matches(pattern[2], term[2], bindings)
            and _term_key_matches(pattern[3], term[3], bindings)
        )
    return False


def _instantiate_key(term: tuple[Any, ...], bindings: dict[int, tuple[Any, ...]]) -> tuple[Any, ...]:
    if term[0] == "variable":
        return bindings.get(int(term[1]), term)
    if term[0] == "constant":
        return term
    if term[0] == "unary":
        return ("unary", term[1], _instantiate_key(term[2], bindings))
    if term[0] == "binary":
        return ("binary", term[1], _instantiate_key(term[2], bindings), _instantiate_key(term[3], bindings))
    return term


def _facts_with_state(record: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    facts: list[Mapping[str, Any]] = list(record["facts"])
    state = record["state"]
    if state["kind"] in {"derivations", "relation_derivations"}:
        for item in state["items"]:
            facts.append({"pred": f"STATE_{item['pred']}", "args": list(item.get("args", []))})
            if state["kind"] == "derivations" and item.get("args"):
                facts.append({"pred": "STATE_KNOWN", "args": [int(item["args"][0])]})
        return facts
    state_objects = list(state["objects"])
    if not state_objects:
        return facts
    facts.append({"pred": "STATE_FIRST", "args": [state_objects[0]]})
    facts.append({"pred": "STATE_LAST", "args": [state_objects[-1]]})
    for left, right in zip(state_objects, state_objects[1:]):
        facts.append({"pred": "STATE_NEXT", "args": [left, right]})
    return facts


def _state_objects(record: Mapping[str, Any]) -> list[int]:
    state = record["state"]
    if state["kind"] == "sequence":
        return list(state["objects"])
    if state["kind"] == "derivations":
        return [int(item["args"][0]) for item in state.get("items", []) if item.get("args")]
    objects: list[int] = []
    for item in state.get("items", []):
        objects.extend(int(arg) for arg in item.get("args", []))
    return objects


def _max_fact_args(facts: list[Mapping[str, Any]]) -> int:
    return max((len(fact.get("args", [])) for fact in facts), default=1)


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
    if kind == "action":
        target_ops[row_idx] = OP_IDS[_target_op(target)]
        for idx, arg in enumerate(target.get("args", [])[: target_args.shape[1]]):
            target_args[row_idx, idx] = int(arg) + 1
        return
    if kind == "repair_action":
        target_ops[row_idx] = OP_IDS[_target_op(target)]
        for idx, arg in enumerate(_target_args(target)[: target_args.shape[1]]):
            target_args[row_idx, idx] = int(arg) + 1
        if "index" in target:
            target_indices[row_idx] = int(target["index"])
        return
    if kind == "verify":
        target_ops[row_idx] = OP_IDS["VERIFY"]
        if target["valid"]:
            target_validity[row_idx] = VALIDITY_IDS["VALID"]
        else:
            target_validity[row_idx] = VALIDITY_IDS["INVALID"]
            target_errors[row_idx] = error_vocab[str(target["error_code"])]
        return
    raise ValueError(f"Unsupported path-array target kind: {kind}")


def _target_op(target: Mapping[str, Any]) -> str:
    if target["kind"] == "repair_action" and target["op"] == "REPLACE_FIELD":
        return f"REPLACE_FIELD_{target['field']}"
    return str(target["op"])


def _target_args(target: Mapping[str, Any]) -> list[Any]:
    args = list(target.get("args", []))
    if not args and isinstance(target.get("action"), Mapping):
        args = list(target["action"].get("args", []))
    return args


def _error_vocab(records: Iterable[Mapping[str, Any]]) -> dict[str, int]:
    errors = sorted(
        {
            str(record["target"]["error_code"])
            for record in records
            if record["target"]["kind"] == "verify" and not record["target"]["valid"]
        }
    )
    return {"<PAD>": 0, **{error: idx + 1 for idx, error in enumerate(errors)}}


def _read_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)
