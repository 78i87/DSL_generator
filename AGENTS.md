# DSL Generator Agent Guide

This repo builds symbolic DSL datasets for TRM-style reasoning experiments.
Agents working here should keep changes narrow, explicit, and compatible with
the existing dataset/export contract.

## Operating Rules

- Work only inside `/Users/morganye/Desktop/reasoning-dsl-generators` unless the user explicitly asks otherwise.
- Do not train models from this repo. Training and evaluation belong in `/Users/morganye/Desktop/TinyRecursiveModels-mlx`.
- Use pre-1.0 semantic versions for new experiments: human label `0.24`, filesystem label `0_24`.
- Treat `0.22` as the stable baseline alias for the final v22 single-error verify run.
- Treat `0.23` as the fresh-holdout robustness check for `0.22`.
- Never rename old `v1` through `v22` configs, data, reports, or logs. They are historical references.
- Keep the no-ID rule: no puzzle/category identifier side channel.
- Prefer one controlled variable per experiment.

## DSL Family Contract

New DSL families should implement a generator under `reasoning_dsl/generators/`.
Each family must define:

- Formal `problem_lines` with anonymous symbols such as `e0`, `p0`, `r0`, `h0`.
- A canonical answer-state representation, also called `y_current`.
- Canonical `state_lines` from empty/partial answer-state to final solved state.
- Compact `action` targets: one primitive delta action per row.
- Compact `repair_action` targets using local anchors when possible.
- `verify` targets as `VALID` or `INVALID CODE`.
- A deterministic transition function from `problem_lines + y_current + action` to `y_next`.
- Where useful, a mechanical patch/diff view from `y_current` to `y_next`.
- Corruption behavior for repair and verify examples.
- Metadata for difficulty and solver-measured properties.
- Canonical fingerprints that detect semantic duplicates across splits.

Design rules:

- Keep targets compact. Do not reintroduce long full-state completion targets unless explicitly requested.
- Use rollout for multi-step completion: generate one action, apply it, check grammar/state/verifier, repeat.
- Invalid verifier examples should contain one clear error where possible.
- Avoid numeric-position repair targets when a visible local anchor form works.
- Action targets should include enough binding information to be self-contained.
- If a new family adds tokens, old checkpoints are not vocab-compatible without retraining.

## State-Refinement Frame

Treat every family as a state-refinement problem:

```text
problem x
current answer-state y_current
        ->
better answer-state y_next
```

Compact actions and global answer refinement are two views of that same update:

```text
compact action = sparse semantic edit to y_current
patch/diff     = explicit local or dense edit to y_current
next_state     = y_next after applying the edit
```

For current symbolic families, compact action prediction remains the primary
target. For future grid, Sudoku, ARC-like, assignment, or dense constraint
families, patch or full-state refinement may become the primary target. Do not
treat these as separate paradigms; both should be generated from the same
canonical transition.

Examples:

```text
Graph:
  y_current = PATH e0 e1 _ _
  action    = APPEND e2
  patch     = SET path[2] e2
  y_next    = PATH e0 e1 e2 _

Term rewriting:
  y_current = TERM g(f(a))
  action    = RW r0
  patch     = REPLACE subtree[...] WITH b
  y_next    = TERM g(b)

Grid:
  y_current = partial output grid
  action    = optional macro, such as FILL r3 c4 7
  patch     = SET grid[3,4] 7, or a multi-cell repaint
  y_next    = updated output grid
```

When adding a new family, first define the answer canvas:

- path slots for reachability-like tasks.
- derived proposition/fact sets for proof-like tasks.
- lineage slots for tree tasks.
- term/tree tokens for rewriting tasks.
- grids for Sudoku, maze, ARC-like, or cellular tasks.
- variable-to-value tables for assignment and constraint tasks.

Then define which supervised views are available:

```python
targets = {
    "action": optional_compact_action,
    "patch": optional_state_diff,
    "next_state": improved_answer_state,
    "final_state": optional_final_answer,
    "validity": verifier_result,
    "error_mask": optional_error_location,
    "halt": solved_bool,
}
```

Do not add puzzle/category identifier side channels to select the view. The
structure of `problem_lines`, `state_lines`, and target syntax should carry the
task meaning.

## Compact Target Design

Compact actions are the default for new families. The model should predict the
smallest meaningful reasoning move, not every low-level execution coordinate.

Examples:

```text
Good:  RW r0
Avoid when deterministic semantics exist: RW r0 AT L IN R
```

Rules:

- Compact away execution details only when the DSL defines deterministic semantics for the missing detail.
- If a compact action can apply in more than one place, either define a deterministic policy such as leftmost match, or include the minimum extra binding needed to disambiguate.
- The generator's canonical traces must follow that deterministic policy exactly.
- Do not hide the reasoning task behind opaque lookup IDs. The action should still name the meaningful primitive choice.
- Prefer changing target representation before adding large curriculum patches when failures are mostly syntax/path/binding precision.

## Semantic Self-Consistency

Every generated target must be correct under the same semantics used by the evaluator.
Before training on a new or changed family, tests should prove:

- every `action` target applies to `state_lines` and produces `next_state_lines`.
- every `repair_action` target applies to the corrupted `state_lines` and produces `repaired_state_lines`.
- every canonical final state verifies as `VALID`.
- every invalid verifier example returns the intended single `INVALID CODE`.
- exact targets are also semantically valid under the family verifier/action applier.

This matters especially for compact actions. For example, if `RW r0` means
"apply rule `r0` at the leftmost matching subterm", repeated-subterm problems
must generate canonical traces that actually rewrite the leftmost match.

## Evaluator Contract

Any target syntax or semantic change in this repo must be mirrored in
`/Users/morganye/Desktop/TinyRecursiveModels-mlx` before training:

- parser support for the new target form.
- action application and repair application semantics.
- verifier/semantic scoring.
- rollout grammar for syntactic generation.
- unit tests for valid, invalid, malformed, and unapplicable cases.

Primary rollout metrics may use grammar constraints, syntax checks, state
application, and verifier checks after generation. Do not use legal-action
enumeration as the main metric unless the user explicitly asks for a ceiling or
control experiment.

## Dataset And Export Rules

- JSONL is the inspectable source of truth.
- TRM arrays must preserve the no-ID export contract:
  - `identifiers.json` is `["<blank>"]`.
  - every `puzzle_identifiers` value is `0`.
  - `num_puzzle_identifiers` is `1`.
  - each generated example is its own training group.
- Use `--vocab-from` only for compatibility checks against existing checkpoints.
- Fixed-vocab export must fail clearly on OOV tokens.
- Generate and audit datasets only after tests pass.

## Adding A New Family

1. Add the generator implementation under `reasoning_dsl/generators/`.
2. Register it in generator imports and CLI paths if needed.
3. Add or extend a config named like `configs/symbolic_0_24_<short_name>.json`.
4. Add focused generator tests covering:
   - valid final states
   - corruption behavior
   - action target application
   - repair target application
   - verifier error codes
   - fingerprint uniqueness
   - symbol offsets
5. Add export or audit tests if the family changes dataset shape, vocab behavior, or metadata assumptions.
6. Run tests before generation:

```bash
cd /Users/morganye/Desktop/reasoning-dsl-generators
python3 -m pytest
```

7. Generate and audit the dataset:

```bash
python3 -m reasoning_dsl.cli generate \
  --config configs/symbolic_0_24_<short_name>.json \
  --output-dir data/symbolic-0_24-<short-name>

python3 -m reasoning_dsl.cli audit \
  --data-dir data/symbolic-0_24-<short-name> \
  --output-dir reports/symbolic-0_24-<short-name>
```

## Current Baseline

- Stable baseline: `configs/symbolic_0_22_single_error_verify.json`
- Fresh holdout: `configs/symbolic_0_23_fresh_holdout.json`
- Stable families: graph reachability, implication chains, relation composition, tree ancestry.
- Active experimental family: term rewriting (`0.24+`), not stable until its chosen compact-action version passes.
- Current modes: `action`, `repair_action`, `verify`.
