# Reasoning DSL Generators

Standalone symbolic data generators for TRM-style recursive reasoning experiments.

The package generates small line-oriented DSL problems and answer states, then exports both:

- inspectable JSONL examples
- TRM-compatible `dataset.json` plus `*.npy` arrays

Current pre-1.0 task families:

- graph reachability
- implication chains
- relation composition
- tree ancestry

## Versioning

Historical experiments used `v1` through `v22`. New experiments should use pre-1.0 semantic labels such as `0.23`, `0.24`, etc. Use filesystem-safe names with underscores, for example:

```text
configs/symbolic_0_23_fresh_holdout.json
data/symbolic-0_23-fresh-holdout
reports/symbolic-0_23-fresh-holdout
```

`0.22` is the stable baseline alias for the final `v22` single-error verify run. Reserve `1.0` for the first major frozen dataset/DSL release.

## Install

```bash
cd /Users/morganye/Desktop/reasoning-dsl-generators
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Generate

```bash
python -m reasoning_dsl.cli generate \
  --config configs/symbolic_v1.json \
  --output-dir data/symbolic-v1 \
  --seed 0
```

Output layout:

```text
data/symbolic-v1/
  vocab.json
  identifiers.json
  generation_report.json
  jsonl/
    train.jsonl
    test.jsonl
    ood.jsonl
  train/
    dataset.json
    all__inputs.npy
    all__labels.npy
    all__puzzle_identifiers.npy
    all__puzzle_indices.npy
    all__group_indices.npy
```

## DSL Shape

Graph reachability:

```text
EDGE e0 e1
EDGE e1 e2
QUERY REACH e0 e2
```

Answer state:

```text
PATH e0 e1 e2
```

Implication chains:

```text
HYP h0 : p0
HYP h1 : p0 -> p1
GOAL p1
```

Answer state:

```text
DERIVE p0 BY h0
DERIVE p1 BY h1 FROM p0
```

Relation composition:

```text
FACT r0 e0 e1
FACT r1 e1 e2
RULE r2 = r0 ; r1
QUERY r2 e0 e2
```

Answer state:

```text
DERIVE r2 e0 e2 VIA e1
```
