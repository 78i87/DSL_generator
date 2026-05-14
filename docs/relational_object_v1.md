# Relational Object V1

`relational_object_v1` is the v1.x representation line for removing arbitrary DSL symbols from the learned vocabulary.

The model-facing view keeps:

- object types, such as `entity`, `relation_symbol`, `hypothesis`, `proposition`, `rule`, `function_symbol`, and `variable`
- fact predicates, such as `RELATION_TUPLE`, `QUERY_START`, `QUERY_GOAL`, `SOURCE_FACT`, `SOURCE_RULE`, `RULE_LHS`, and `TERM_UNARY`
- operation names, such as `APPEND`, `DESCEND`, `APPLY`, `FOLLOW`, `RW`, and repair operations
- object row references

The model-facing view does not include external object names such as `e0`, `r0`, `h0`, `p0`, `f0`, or arbitrary renamed symbols.

External names live only in `external_names`:

```json
{"object": 0, "type": "entity", "name": "e0"}
```

This side table is for rendering outputs back into the original DSL, not for model input.

## Known Limitation

V1 removes arbitrary object names from the learned vocabulary, but it still treats many fact predicates as closed learned IDs.

Examples:

```text
SOURCE_FACT
SOURCE_RULE
RULE_LHS
STATE_RW_RESULT
INPUT_REL
```

That is useful for a first relational prototype, but it is not the final general-reasoner representation. It means the model can still learn task-shaped predicate rows instead of learning predicate meaning from the task description and relational structure.

The current `relational_task_schema_v1` partially fixes this for path-style tasks:

```text
object 0: predicate object, externally rendered as EDGE or PARENT
object 1: predicate object, externally rendered as PATH or LINEAGE

SCHEMA_BINARY_REL object0
SCHEMA_SEQUENCE_STATE object1
SCHEMA_EXTEND_ACTION action_object object0 object1
RELATION_TUPLE object0 entity0 entity1
STATE_ITEM object1 entity0
```

In that design, `EDGE` and `PARENT` are external names for predicate objects, not permanent fact-predicate vocabulary rows. This is the direction to keep.

The stricter v2 representation should apply the same rule to all families. Keep anonymous object rows, but move family semantics into a task-declared schema. The model should learn generic roles and operators, then read task facts that declare how a local predicate behaves.

V2 sketch:

```text
object 0: predicate object, externally rendered as EDGE
object 1: predicate object, externally rendered as PATH

SCHEMA_BINARY_REL object0
SCHEMA_STATE_SEQUENCE object1
SCHEMA_ACTION_APPEND_FROM object0 TO object1
SCHEMA_QUERY_START_ROLE object0
SCHEMA_QUERY_GOAL_ROLE object0

RELATION_TUPLE object0 entity0 entity1
RELATION_TUPLE object0 entity1 entity2
STATE_ITEM object1 entity0
```

If two unseen tasks can be described with the existing schema roles, the model should have a path to transfer without adding learned predicate IDs.

Current task-schema v1 scope:

- graph/tree-style sequence tasks use generic schema predicates
- implication, relation composition, and term rewriting are supported; term rewriting still uses domain-specific schema predicates for structured terms
- generic fact predicates such as `SCHEMA_BINARY_REL`, `SCHEMA_SEQUENCE_STATE`, `SCHEMA_EXTEND_ACTION`, and `RELATION_TUPLE`
- generic action op `EXTEND_SEQUENCE`
- external names preserved only for rendering/debugging
- relational training/evaluation happens in `/Users/morganye/Desktop/TinyRecursiveModels-mlx`

## V2 Design Rule

For future relational work, do not add a new learned fact predicate just because a source DSL has a new word.

Prefer this:

```text
object 0: predicate, external name EDGE
object 1: predicate, external name BLOCKS

SCHEMA_BINARY_REL object0
SCHEMA_BINARY_REL object1
RELATION_TUPLE object0 entity0 entity1
RELATION_TUPLE object1 entity2 entity3
```

Avoid this:

```text
EDGE entity0 entity1
BLOCKS entity2 entity3
```

The model vocabulary should grow for genuinely new reusable schema concepts, not for every new family name, predicate label, or arbitrary source token.

Acceptable v2 fact predicates should be reusable across families, such as:

```text
RELATION_TUPLE
RULE_TUPLE
QUERY_ROLE
STATE_ITEM
STATE_NEXT
STATE_SUPPORT
ACTION_SCHEMA
VERIFY_SCHEMA
ERROR_SCHEMA
TERM_NODE
TERM_CHILD
```

Family-specific render labels belong in `external_names` or predicate objects. They should not be the only model-visible source of task meaning.

The current v1 cleanup gate is encoded in `FACT_PREDICATE_CLASSES` in
`reasoning_dsl/relational_task_schema_arrays.py`.

Current classes:

- `core_schema`: reusable across path, relation, derivation, and state-tracking tasks.
- `domain_schema`: reusable within a domain such as term rewriting.
- `legacy_task_schema`: task-shaped predicates that should be removed or generalized in v2.

Compatibility IDs still classified as legacy:

```text
SCHEMA_APPLY_ACTION
SCHEMA_DERIVATION_STATE
SCHEMA_FOLLOW_ACTION
SCHEMA_RELATION_STATE
SOURCE_FACT
SOURCE_RULE
```

After the implication cleanup, newly exported implication task-schema arrays no
longer use `SOURCE_FACT`, `SOURCE_RULE`, `SCHEMA_APPLY_ACTION`, or
`SCHEMA_DERIVATION_STATE`. They encode hypotheses and implication rules through
`RELATION_TUPLE`, `COMPOSE_RULE`, `SCHEMA_SEQUENCE_STATE`, and
`SCHEMA_EXTEND_ACTION`.

After the relation cleanup, newly exported relation-composition task-schema
arrays also avoid `SCHEMA_FOLLOW_ACTION` and `SCHEMA_RELATION_STATE`. Current
five-family task-schema exports should pass the no-legacy predicate gate.
Those legacy IDs remain only so older arrays/checkpoints can still be inspected.
Relation-composition action targets in task-schema arrays also use
`EXTEND_SEQUENCE` with the local action object as an argument instead of using
`FOLLOW` as the learned top-level op.
Implication action targets follow the same rule: `APPLY` remains a local action
object, while the learned top-level op is `EXTEND_SEQUENCE`.
Task-schema line repair targets use the generic `REPLACE_FIELD` op with the
field name represented as an anonymous `field` object argument, rather than
separate learned ops such as `REPLACE_FIELD_HYP` or `REPLACE_FIELD_VIA`.
Path-style repair targets use the generic `REPLACE_ITEM` op with reusable
location object types such as `location_root`, `location_after`, and
`location_index`, rather than separate learned ops such as `REPLACE_ROOT` or
`REPLACE_AFTER`.
Term action targets also use `EXTEND_SEQUENCE`; `RW` and `HALT` remain local
operation objects declared by `SCHEMA_REWRITE_ACTION` / `SCHEMA_HALT_ACTION`,
not active learned top-level ops in task-schema arrays.

Task-schema array metadata records the active predicate surface separately from
the compatibility vocab:

```text
active_fact_predicates
active_fact_predicate_classes
active_legacy_fact_predicates
active_ops
```

Use `active_legacy_fact_predicates`, not the full `fact_pred_ids` map, to decide
whether newly exported data still exposes legacy task-shaped predicates to the
model.

## CLI

Export relational JSONL from any generated dataset:

```bash
python -m reasoning_dsl.cli relational-export \
  --data-dir data/symbolic-0_83-term-ordinal-rule-labels \
  --output-dir /tmp/relational-0_83
```

Export task-schema relational arrays:

```bash
python -m reasoning_dsl.cli relational-task-schema-arrays \
  --data-dir data/symbolic-0_83-term-ordinal-rule-labels \
  --output-dir /tmp/relational-task-schema \
  --family graph_reachability \
  --family tree_ancestry \
  --mode action \
  --mode repair_action \
  --mode verify
```

For v2 cleanup work, require that the selected examples avoid legacy
task-shaped predicates:

```bash
python -m reasoning_dsl.cli relational-task-schema-arrays \
  --data-dir data/symbolic-0_83-term-ordinal-rule-labels \
  --output-dir /tmp/relational-task-schema-core-only \
  --family graph_reachability \
  --family tree_ancestry \
  --mode action \
  --fail-on-legacy-predicates
```

The output is:

```text
relational_schema.json
relational_jsonl/train.jsonl
relational_jsonl/test.jsonl
relational_jsonl/ood.jsonl
```

Inspect the current fact-predicate classes:

```bash
python -m reasoning_dsl.cli relational-schema-report
```

## Invariance Rule

Alpha-renaming may change `external_names`, but it must not change the model-facing view:

```python
model_view(original_record) == model_view(alpha_renamed_record)
```

Tests enforce this for graph-style examples, and generated 1.52 task-schema arrays have been checked against alpha-renamed copies across train/test/OOD. Future tensor exports and models should preserve the same invariant.

The stronger v2 invariant is:

```python
schema_view(task_a) == schema_view(task_b)
```

when two tasks have the same declared relational semantics and differ only by family-specific predicate names.

## Current Support

Supported families in relational exports:

- `graph_reachability`
- `shortest_path_lite`
- `dfa_simulation_lite`
- `implication_chains`
- `relation_composition`
- `tree_ancestry`
- `term_rewriting`
- `equality_rewriting_lite`

This is an export/schema contract only. Training a relational model is the next step.
Current relational model training is implemented in the TRM repo. As of the 1.52-1.66 experiments, the best checkpoint reaches perfect verifier-guided candidate/rollout accuracy, but greedy direct top-1 still trails the 0.85 text-model baseline. That is a model/evaluation gap, not an object-anonymity failure.
