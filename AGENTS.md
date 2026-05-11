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
- Canonical `state_lines` from empty/partial state to final solved state.
- Compact `action` targets: one primitive delta action per row.
- Compact `repair_action` targets using local anchors when possible.
- `verify` targets as `VALID` or `INVALID CODE`.
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
- Current families: graph reachability, implication chains, relation composition, tree ancestry.
- Current modes: `action`, `repair_action`, `verify`.
