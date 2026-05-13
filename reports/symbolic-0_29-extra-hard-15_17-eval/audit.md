# Dataset Audit

- Data dir: `/Users/morganye/Desktop/reasoning-dsl-generators/data/symbolic-0_29-extra-hard-15_17-eval`
- Status: `fail`
- Errors: `4`
- Warnings: `0`

## Errors

- Missing JSONL file: /Users/morganye/Desktop/reasoning-dsl-generators/data/symbolic-0_29-extra-hard-15_17-eval/jsonl/train.jsonl
- Missing JSONL file: /Users/morganye/Desktop/reasoning-dsl-generators/data/symbolic-0_29-extra-hard-15_17-eval/jsonl/test.jsonl
- Missing metadata file: /Users/morganye/Desktop/reasoning-dsl-generators/data/symbolic-0_29-extra-hard-15_17-eval/train/dataset.json
- Missing metadata file: /Users/morganye/Desktop/reasoning-dsl-generators/data/symbolic-0_29-extra-hard-15_17-eval/test/dataset.json

## JSONL Summary

### ood

- Examples: `954`
- Problems: `27`
- Families: `{'graph_reachability': 324, 'implication_chains': 306, 'tree_ancestry': 324}`
- Modes: `{'action': 450, 'repair_action': 450, 'verify': 54}`
- Verify targets: `{'INVALID BAD_EDGE': 9, 'INVALID BAD_PARENT': 9, 'INVALID BAD_PREMISE': 9, 'VALID': 27}`

## Difficulty Summary

### graph_reachability

- `extra_edges`: `{'min': 5.0, 'max': 8.0, 'mean': 6.327160493827161, 'unique': [5, 6, 7, 8]}`
- `num_nodes`: `{'min': 19.0, 'max': 22.0, 'mean': 20.574074074074073, 'unique': [19, 20, 21, 22]}`
- `path_length`: `{'min': 15.0, 'max': 17.0, 'mean': 16.037037037037038, 'unique': [15, 16, 17]}`
- `require_shortest`: `{True: 324}`
- `symbol_offset`: `{'min': 0.0, 'max': 0.0, 'mean': 0.0, 'unique': [0]}`

### implication_chains

- `distractor_hyps`: `{'min': 3.0, 'max': 5.0, 'mean': 4.006535947712418, 'unique': [3, 4, 5]}`
- `num_props`: `{'min': 17.0, 'max': 18.0, 'mean': 17.464052287581698, 'unique': [17, 18]}`
- `proof_length`: `{'min': 15.0, 'max': 17.0, 'mean': 16.03921568627451, 'unique': [15, 16, 17]}`
- `symbol_offset`: `{'min': 0.0, 'max': 0.0, 'mean': 0.0, 'unique': [0]}`

### tree_ancestry

- `branching_factor`: `{'min': 2.0, 'max': 3.0, 'mean': 2.432098765432099, 'unique': [2, 3]}`
- `depth`: `{'min': 15.0, 'max': 17.0, 'mean': 16.037037037037038, 'unique': [15, 16, 17]}`
- `distractor_subtrees`: `{'min': 5.0, 'max': 9.0, 'mean': 7.5, 'unique': [5, 7, 8, 9]}`
- `symbol_offset`: `{'min': 0.0, 'max': 0.0, 'mean': 0.0, 'unique': [0]}`

## TRM Array Summary

### ood

- Inputs shape: `[954, 285]`
- Labels shape: `[954, 285]`
- Seq len: `285`
- Vocab size: `304`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `954`

## Samples

### ood/graph_reachability/action

- ID: `ood:graph_reachability:0:action:0`

Source:

```text
MODE action
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e10 e11
EDGE e11 e12
EDGE e11 e3
EDGE e12 e13
EDGE e13 e10
EDGE e13 e14
EDGE e14 e15
EDGE e15 e0
EDGE e15 e7
EDGE e18 e13
EDGE e18 e6
EDGE e2 e3
EDGE e3 e4
EDGE e4 e2
EDGE e4 e5
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e8 e9
EDGE e9 e10
QUERY REACH e0 e15
STATE
EMPTY
```

Target:

```text
APPEND e0
```

### ood/graph_reachability/repair_action

- ID: `ood:graph_reachability:0:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e10 e11
EDGE e11 e12
EDGE e11 e3
EDGE e12 e13
EDGE e13 e10
EDGE e13 e14
EDGE e14 e15
EDGE e15 e0
EDGE e15 e7
EDGE e18 e13
EDGE e18 e6
EDGE e2 e3
EDGE e3 e4
EDGE e4 e2
EDGE e4 e5
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e8 e9
EDGE e9 e10
QUERY REACH e0 e15
STATE
PATH e15
```

Target:

```text
REPLACE ROOT WITH e0
```

### ood/graph_reachability/verify

- ID: `ood:graph_reachability:0:verify:valid`

Source:

```text
MODE verify
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e10 e11
EDGE e11 e12
EDGE e11 e3
EDGE e12 e13
EDGE e13 e10
EDGE e13 e14
EDGE e14 e15
EDGE e15 e0
EDGE e15 e7
EDGE e18 e13
EDGE e18 e6
EDGE e2 e3
EDGE e3 e4
EDGE e4 e2
EDGE e4 e5
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e8 e9
EDGE e9 e10
QUERY REACH e0 e15
STATE
PATH e0 e1 e2 e3 e4 e5 e6 e7 e8 e9 e10 e11 e12 e13 e14 e15
```

Target:

```text
VALID
```

### ood/implication_chains/action

- ID: `ood:implication_chains:9:action:0`

Source:

```text
MODE action
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p7 -> p8
HYP h9 : p8 -> p9
HYP h10 : p9 -> p10
HYP h11 : p10 -> p11
HYP h12 : p11 -> p12
HYP h13 : p12 -> p13
HYP h14 : p13 -> p14
HYP h15 : p9 -> p14
HYP h16 : p11 -> p1
HYP h17 : p14 -> p4
GOAL p14
STATE
EMPTY
```

Target:

```text
APPLY h0
```

### ood/implication_chains/repair_action

- ID: `ood:implication_chains:9:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p7 -> p8
HYP h9 : p8 -> p9
HYP h10 : p9 -> p10
HYP h11 : p10 -> p11
HYP h12 : p11 -> p12
HYP h13 : p12 -> p13
HYP h14 : p13 -> p14
HYP h15 : p9 -> p14
HYP h16 : p11 -> p1
HYP h17 : p14 -> p4
GOAL p14
STATE
DERIVE p0 BY h999
```

Target:

```text
REPLACE FIRST HYP h0
```

### ood/implication_chains/verify

- ID: `ood:implication_chains:9:verify:valid`

Source:

```text
MODE verify
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p7 -> p8
HYP h9 : p8 -> p9
HYP h10 : p9 -> p10
HYP h11 : p10 -> p11
HYP h12 : p11 -> p12
HYP h13 : p12 -> p13
HYP h14 : p13 -> p14
HYP h15 : p9 -> p14
HYP h16 : p11 -> p1
HYP h17 : p14 -> p4
GOAL p14
STATE
DERIVE p0 BY h0
DERIVE p1 BY h1 FROM p0
DERIVE p2 BY h2 FROM p1
DERIVE p3 BY h3 FROM p2
DERIVE p4 BY h4 FROM p3
DERIVE p5 BY h5 FROM p4
DERIVE p6 BY h6 FROM p5
DERIVE p7 BY h7 FROM p6
DERIVE p8 BY h8 FROM p7
DERIVE p9 BY h9 FROM p8
DERIVE p10 BY h10 FROM p9
DERIVE p11 BY h11 FROM p10
DERIVE p12 BY h12 FROM p11
DERIVE p13 BY h13 FROM p12
DERIVE p14 BY h14 FROM p13
```

Target:

```text
VALID
```

### ood/tree_ancestry/action

- ID: `ood:tree_ancestry:18:action:0`

Source:

```text
MODE action
PROBLEM
PARENT e0 e1
PARENT e1 e2
PARENT e1 e23
PARENT e10 e11
PARENT e11 e12
PARENT e12 e13
PARENT e12 e16
PARENT e13 e14
PARENT e13 e20
PARENT e14 e15
PARENT e15 e22
PARENT e16 e21
PARENT e18 e19
PARENT e2 e3
PARENT e21 e24
PARENT e3 e17
PARENT e3 e18
PARENT e3 e4
PARENT e4 e5
PARENT e5 e6
PARENT e6 e7
PARENT e7 e8
PARENT e8 e9
PARENT e9 e10
QUERY ANCESTOR e0 e15
STATE
EMPTY
```

Target:

```text
DESCEND e0
```

### ood/tree_ancestry/repair_action

- ID: `ood:tree_ancestry:18:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
PARENT e0 e1
PARENT e1 e2
PARENT e1 e23
PARENT e10 e11
PARENT e11 e12
PARENT e12 e13
PARENT e12 e16
PARENT e13 e14
PARENT e13 e20
PARENT e14 e15
PARENT e15 e22
PARENT e16 e21
PARENT e18 e19
PARENT e2 e3
PARENT e21 e24
PARENT e3 e17
PARENT e3 e18
PARENT e3 e4
PARENT e4 e5
PARENT e5 e6
PARENT e6 e7
PARENT e7 e8
PARENT e8 e9
PARENT e9 e10
QUERY ANCESTOR e0 e15
STATE
LINEAGE e15
```

Target:

```text
REPLACE ROOT WITH e0
```

### ood/tree_ancestry/verify

- ID: `ood:tree_ancestry:18:verify:valid`

Source:

```text
MODE verify
PROBLEM
PARENT e0 e1
PARENT e1 e2
PARENT e1 e23
PARENT e10 e11
PARENT e11 e12
PARENT e12 e13
PARENT e12 e16
PARENT e13 e14
PARENT e13 e20
PARENT e14 e15
PARENT e15 e22
PARENT e16 e21
PARENT e18 e19
PARENT e2 e3
PARENT e21 e24
PARENT e3 e17
PARENT e3 e18
PARENT e3 e4
PARENT e4 e5
PARENT e5 e6
PARENT e6 e7
PARENT e7 e8
PARENT e8 e9
PARENT e9 e10
QUERY ANCESTOR e0 e15
STATE
LINEAGE e0 e1 e2 e3 e4 e5 e6 e7 e8 e9 e10 e11 e12 e13 e14 e15
```

Target:

```text
VALID
```
