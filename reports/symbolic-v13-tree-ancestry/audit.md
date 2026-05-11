# Dataset Audit

- Data dir: `data/symbolic-v13-tree-ancestry`
- Status: `pass`
- Errors: `0`
- Warnings: `0`

## JSONL Summary

### train

- Examples: `13578`
- Problems: `1056`
- Families: `{'graph_reachability': 3884, 'implication_chains': 3442, 'relation_composition': 2730, 'tree_ancestry': 3522}`
- Modes: `{'action': 7017, 'repair_action': 5409, 'verify': 1152}`
- Verify targets: `{'INVALID BAD_EDGE': 122, 'INVALID BAD_FACT': 144, 'INVALID BAD_LINEAGE_END': 27, 'INVALID BAD_PATH_END': 22, 'INVALID BAD_PREMISE': 122, 'INVALID REPEATED_NODE': 117, 'INVALID UNKNOWN_HYP': 22, 'VALID': 576}`

### test

- Examples: `980`
- Problems: `72`
- Families: `{'graph_reachability': 276, 'implication_chains': 224, 'relation_composition': 200, 'tree_ancestry': 280}`
- Modes: `{'action': 418, 'repair_action': 418, 'verify': 144}`
- Verify targets: `{'INVALID BAD_EDGE': 17, 'INVALID BAD_FACT': 18, 'INVALID BAD_LINEAGE_END': 3, 'INVALID BAD_PATH_END': 1, 'INVALID BAD_PREMISE': 16, 'INVALID REPEATED_NODE': 15, 'INVALID UNKNOWN_HYP': 2, 'VALID': 72}`

### ood

- Examples: `1476`
- Problems: `72`
- Families: `{'graph_reachability': 396, 'implication_chains': 360, 'relation_composition': 324, 'tree_ancestry': 396}`
- Modes: `{'action': 666, 'repair_action': 666, 'verify': 144}`
- Verify targets: `{'INVALID BAD_EDGE': 15, 'INVALID BAD_FACT': 18, 'INVALID BAD_LINEAGE_END': 1, 'INVALID BAD_PATH_END': 3, 'INVALID BAD_PREMISE': 16, 'INVALID REPEATED_NODE': 17, 'INVALID UNKNOWN_HYP': 2, 'VALID': 72}`

## Difficulty Summary

### graph_reachability

- `extra_edges`: `{'min': 1.0, 'max': 16.0, 'mean': 8.278533801580334, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `num_nodes`: `{'min': 5.0, 'max': 19.0, 'mean': 12.237489025460931, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `path_length`: `{'min': 2.0, 'max': 10.0, 'mean': 7.306409130816506, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `require_shortest`: `{True: 4556}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.411764705882353, 'unique': [0, 2, 3, 4, 6]}`

### implication_chains

- `distractor_hyps`: `{'min': 1.0, 'max': 12.0, 'mean': 7.352459016393443, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}`
- `num_props`: `{'min': 5.0, 'max': 19.0, 'mean': 12.062096373571784, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `proof_length`: `{'min': 2.0, 'max': 10.0, 'mean': 7.354197714853453, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.4187779433681074, 'unique': [0, 2, 3, 4, 6]}`

### relation_composition

- `composition_depth`: `{'min': 2.0, 'max': 10.0, 'mean': 7.481868469575907, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_facts`: `{'min': 1.0, 'max': 16.0, 'mean': 8.536877688998157, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `num_entities`: `{'min': 5.0, 'max': 19.0, 'mean': 12.519975414874, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.5341118623232943, 'unique': [0, 2, 3, 4, 6]}`

### tree_ancestry

- `branching_factor`: `{'min': 2.0, 'max': 4.0, 'mean': 2.6805621724630777, 'unique': [2, 3, 4]}`
- `depth`: `{'min': 2.0, 'max': 10.0, 'mean': 7.376369699857075, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_subtrees`: `{'min': 1.0, 'max': 16.0, 'mean': 8.410671748451644, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.5321581705574083, 'unique': [0, 2, 3, 4, 6]}`

## TRM Array Summary

### train

- Inputs shape: `[13578, 272]`
- Labels shape: `[13578, 272]`
- Seq len: `272`
- Vocab size: `148`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `13578`

### test

- Inputs shape: `[980, 272]`
- Labels shape: `[980, 272]`
- Seq len: `272`
- Vocab size: `148`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `980`

### ood

- Inputs shape: `[1476, 272]`
- Labels shape: `[1476, 272]`
- Seq len: `272`
- Vocab size: `148`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1476`

## Samples

### ood/graph_reachability/action

- ID: `ood:graph_reachability:0:action:0`

Source:

```text
MODE action
PROBLEM
EDGE e0 e1
EDGE e1 e11
EDGE e1 e12
EDGE e1 e2
EDGE e1 e9
EDGE e10 e1
EDGE e10 e9
EDGE e2 e3
EDGE e3 e4
EDGE e4 e10
EDGE e4 e5
EDGE e5 e2
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e8 e4
EDGE e9 e10
QUERY REACH e0 e8
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
EDGE e1 e11
EDGE e1 e12
EDGE e1 e2
EDGE e1 e9
EDGE e10 e1
EDGE e10 e9
EDGE e2 e3
EDGE e3 e4
EDGE e4 e10
EDGE e4 e5
EDGE e5 e2
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e8 e4
EDGE e9 e10
QUERY REACH e0 e8
STATE
PATH e8
```

Target:

```text
REPLACE NODE 0 WITH e0
```

### ood/graph_reachability/verify

- ID: `ood:graph_reachability:0:verify:valid`

Source:

```text
MODE verify
PROBLEM
EDGE e0 e1
EDGE e1 e11
EDGE e1 e12
EDGE e1 e2
EDGE e1 e9
EDGE e10 e1
EDGE e10 e9
EDGE e2 e3
EDGE e3 e4
EDGE e4 e10
EDGE e4 e5
EDGE e5 e2
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e8 e4
EDGE e9 e10
QUERY REACH e0 e8
STATE
PATH e0 e1 e2 e3 e4 e5 e6 e7 e8
```

Target:

```text
VALID
```

### ood/implication_chains/action

- ID: `ood:implication_chains:18:action:0`

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
HYP h8 : p1 -> p11
HYP h9 : p2 -> p13
HYP h10 : p5 -> p9
HYP h11 : p7 -> p6
HYP h12 : p10 -> p6
HYP h13 : p10 -> p8
HYP h14 : p11 -> p5
HYP h15 : p12 -> p10
GOAL p7
STATE
EMPTY
```

Target:

```text
APPLY h0
```

### ood/implication_chains/repair_action

- ID: `ood:implication_chains:18:repair_action:1`

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
HYP h8 : p1 -> p11
HYP h9 : p2 -> p13
HYP h10 : p5 -> p9
HYP h11 : p7 -> p6
HYP h12 : p10 -> p6
HYP h13 : p10 -> p8
HYP h14 : p11 -> p5
HYP h15 : p12 -> p10
GOAL p7
STATE
DERIVE p0 BY h999
```

Target:

```text
REPLACE LINE 0 HYP h0
```

### ood/implication_chains/verify

- ID: `ood:implication_chains:18:verify:valid`

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
HYP h8 : p1 -> p11
HYP h9 : p2 -> p13
HYP h10 : p5 -> p9
HYP h11 : p7 -> p6
HYP h12 : p10 -> p6
HYP h13 : p10 -> p8
HYP h14 : p11 -> p5
HYP h15 : p12 -> p10
GOAL p7
STATE
DERIVE p0 BY h0
DERIVE p1 BY h1 FROM p0
DERIVE p2 BY h2 FROM p1
DERIVE p3 BY h3 FROM p2
DERIVE p4 BY h4 FROM p3
DERIVE p5 BY h5 FROM p4
DERIVE p6 BY h6 FROM p5
DERIVE p7 BY h7 FROM p6
```

Target:

```text
VALID
```

### ood/relation_composition/action

- ID: `ood:relation_composition:36:action:0`

Source:

```text
MODE action
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
FACT r3 e3 e4
FACT r4 e4 e5
FACT r5 e5 e6
FACT r6 e6 e7
FACT r7 e7 e8
RULE r8 = r0 ; r1
RULE r9 = r8 ; r2
RULE r10 = r9 ; r3
RULE r11 = r10 ; r4
RULE r12 = r11 ; r5
RULE r13 = r12 ; r6
RULE r14 = r13 ; r7
FACT r0 e8 e0
FACT r2 e3 e4
FACT r2 e10 e9
FACT r5 e10 e11
FACT r5 e12 e1
FACT r6 e11 e8
FACT r7 e6 e0
QUERY r14 e0 e8
STATE
EMPTY
```

Target:

```text
FOLLOW e2 VIA e1
```

### ood/relation_composition/repair_action

- ID: `ood:relation_composition:36:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
FACT r3 e3 e4
FACT r4 e4 e5
FACT r5 e5 e6
FACT r6 e6 e7
FACT r7 e7 e8
RULE r8 = r0 ; r1
RULE r9 = r8 ; r2
RULE r10 = r9 ; r3
RULE r11 = r10 ; r4
RULE r12 = r11 ; r5
RULE r13 = r12 ; r6
RULE r14 = r13 ; r7
FACT r0 e8 e0
FACT r2 e3 e4
FACT r2 e10 e9
FACT r5 e10 e11
FACT r5 e12 e1
FACT r6 e11 e8
FACT r7 e6 e0
QUERY r14 e0 e8
STATE
DERIVE r8 e0 e2 VIA e0
```

Target:

```text
REPLACE LINE 0 VIA e1
```

### ood/relation_composition/verify

- ID: `ood:relation_composition:36:verify:valid`

Source:

```text
MODE verify
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
FACT r3 e3 e4
FACT r4 e4 e5
FACT r5 e5 e6
FACT r6 e6 e7
FACT r7 e7 e8
RULE r8 = r0 ; r1
RULE r9 = r8 ; r2
RULE r10 = r9 ; r3
RULE r11 = r10 ; r4
RULE r12 = r11 ; r5
RULE r13 = r12 ; r6
RULE r14 = r13 ; r7
FACT r0 e8 e0
FACT r2 e3 e4
FACT r2 e10 e9
FACT r5 e10 e11
FACT r5 e12 e1
FACT r6 e11 e8
FACT r7 e6 e0
QUERY r14 e0 e8
STATE
DERIVE r8 e0 e2 VIA e1
DERIVE r9 e0 e3 VIA e2
DERIVE r10 e0 e4 VIA e3
DERIVE r11 e0 e5 VIA e4
DERIVE r12 e0 e6 VIA e5
DERIVE r13 e0 e7 VIA e6
DERIVE r14 e0 e8 VIA e7
```

Target:

```text
VALID
```

### ood/tree_ancestry/action

- ID: `ood:tree_ancestry:54:action:0`

Source:

```text
MODE action
PROBLEM
PARENT e0 e1
PARENT e1 e2
PARENT e10 e12
PARENT e2 e3
PARENT e3 e4
PARENT e4 e5
PARENT e4 e9
PARENT e5 e6
PARENT e6 e7
PARENT e7 e8
PARENT e8 e10
PARENT e8 e11
PARENT e9 e13
QUERY ANCESTOR e0 e8
STATE
EMPTY
```

Target:

```text
DESCEND e0
```

### ood/tree_ancestry/repair_action

- ID: `ood:tree_ancestry:54:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
PARENT e0 e1
PARENT e1 e2
PARENT e10 e12
PARENT e2 e3
PARENT e3 e4
PARENT e4 e5
PARENT e4 e9
PARENT e5 e6
PARENT e6 e7
PARENT e7 e8
PARENT e8 e10
PARENT e8 e11
PARENT e9 e13
QUERY ANCESTOR e0 e8
STATE
LINEAGE e8
```

Target:

```text
REPLACE NODE 0 WITH e0
```

### ood/tree_ancestry/verify

- ID: `ood:tree_ancestry:54:verify:valid`

Source:

```text
MODE verify
PROBLEM
PARENT e0 e1
PARENT e1 e2
PARENT e10 e12
PARENT e2 e3
PARENT e3 e4
PARENT e4 e5
PARENT e4 e9
PARENT e5 e6
PARENT e6 e7
PARENT e7 e8
PARENT e8 e10
PARENT e8 e11
PARENT e9 e13
QUERY ANCESTOR e0 e8
STATE
LINEAGE e0 e1 e2 e3 e4 e5 e6 e7 e8
```

Target:

```text
VALID
```

### test/graph_reachability/action

- ID: `test:graph_reachability:0:action:0`

Source:

```text
MODE action
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e1 e6
EDGE e2 e0
EDGE e2 e3
EDGE e3 e4
EDGE e4 e3
EDGE e6 e5
QUERY REACH e0 e4
STATE
EMPTY
```

Target:

```text
APPEND e0
```

### test/graph_reachability/repair_action

- ID: `test:graph_reachability:0:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e1 e6
EDGE e2 e0
EDGE e2 e3
EDGE e3 e4
EDGE e4 e3
EDGE e6 e5
QUERY REACH e0 e4
STATE
PATH e4
```

Target:

```text
REPLACE NODE 0 WITH e0
```

### test/graph_reachability/verify

- ID: `test:graph_reachability:0:verify:valid`

Source:

```text
MODE verify
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e1 e6
EDGE e2 e0
EDGE e2 e3
EDGE e3 e4
EDGE e4 e3
EDGE e6 e5
QUERY REACH e0 e4
STATE
PATH e0 e1 e2 e3 e4
```

Target:

```text
VALID
```

### test/implication_chains/action

- ID: `test:implication_chains:18:action:0`

Source:

```text
MODE action
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p4
HYP h3 : p2 -> p6
GOAL p1
STATE
EMPTY
```

Target:

```text
APPLY h0
```

### test/implication_chains/repair_action

- ID: `test:implication_chains:18:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p4
HYP h3 : p2 -> p6
GOAL p1
STATE
DERIVE p0 BY h999
```

Target:

```text
REPLACE LINE 0 HYP h0
```

### test/implication_chains/verify

- ID: `test:implication_chains:18:verify:valid`

Source:

```text
MODE verify
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p4
HYP h3 : p2 -> p6
GOAL p1
STATE
DERIVE p0 BY h0
DERIVE p1 BY h1 FROM p0
```

Target:

```text
VALID
```

### test/relation_composition/action

- ID: `test:relation_composition:36:action:0`

Source:

```text
MODE action
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
FACT r3 e3 e4
RULE r4 = r0 ; r1
RULE r5 = r4 ; r2
RULE r6 = r5 ; r3
FACT r0 e4 e3
FACT r0 e6 e5
FACT r2 e0 e2
FACT r3 e0 e1
FACT r3 e5 e1
QUERY r6 e0 e4
STATE
EMPTY
```

Target:

```text
FOLLOW e2 VIA e1
```

### test/relation_composition/repair_action

- ID: `test:relation_composition:36:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
FACT r3 e3 e4
RULE r4 = r0 ; r1
RULE r5 = r4 ; r2
RULE r6 = r5 ; r3
FACT r0 e4 e3
FACT r0 e6 e5
FACT r2 e0 e2
FACT r3 e0 e1
FACT r3 e5 e1
QUERY r6 e0 e4
STATE
DERIVE r4 e0 e2 VIA e0
```

Target:

```text
REPLACE LINE 0 VIA e1
```

### test/relation_composition/verify

- ID: `test:relation_composition:36:verify:valid`

Source:

```text
MODE verify
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
FACT r3 e3 e4
RULE r4 = r0 ; r1
RULE r5 = r4 ; r2
RULE r6 = r5 ; r3
FACT r0 e4 e3
FACT r0 e6 e5
FACT r2 e0 e2
FACT r3 e0 e1
FACT r3 e5 e1
QUERY r6 e0 e4
STATE
DERIVE r4 e0 e2 VIA e1
DERIVE r5 e0 e3 VIA e2
DERIVE r6 e0 e4 VIA e3
```

Target:

```text
VALID
```

### test/tree_ancestry/action

- ID: `test:tree_ancestry:54:action:0`

Source:

```text
MODE action
PROBLEM
PARENT e0 e1
PARENT e0 e6
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e4 e5
PARENT e4 e7
QUERY ANCESTOR e0 e5
STATE
EMPTY
```

Target:

```text
DESCEND e0
```

### test/tree_ancestry/repair_action

- ID: `test:tree_ancestry:54:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
PARENT e0 e1
PARENT e0 e6
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e4 e5
PARENT e4 e7
QUERY ANCESTOR e0 e5
STATE
LINEAGE e5
```

Target:

```text
REPLACE NODE 0 WITH e0
```

### test/tree_ancestry/verify

- ID: `test:tree_ancestry:54:verify:valid`

Source:

```text
MODE verify
PROBLEM
PARENT e0 e1
PARENT e0 e6
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e4 e5
PARENT e4 e7
QUERY ANCESTOR e0 e5
STATE
LINEAGE e0 e1 e2 e3 e4 e5
```

Target:

```text
VALID
```

### train/graph_reachability/action

- ID: `train:graph_reachability:0:action:0`

Source:

```text
MODE action
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e2 e0
EDGE e2 e3
EDGE e2 e4
EDGE e3 e1
EDGE e3 e4
EDGE e4 e0
QUERY REACH e0 e3
STATE
EMPTY
```

Target:

```text
APPEND e0
```

### train/graph_reachability/repair_action

- ID: `train:graph_reachability:0:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e2 e0
EDGE e2 e3
EDGE e2 e4
EDGE e3 e1
EDGE e3 e4
EDGE e4 e0
QUERY REACH e0 e3
STATE
PATH e3
```

Target:

```text
REPLACE NODE 0 WITH e0
```

### train/graph_reachability/verify

- ID: `train:graph_reachability:0:verify:valid`

Source:

```text
MODE verify
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e2 e0
EDGE e2 e3
EDGE e2 e4
EDGE e3 e1
EDGE e3 e4
EDGE e4 e0
QUERY REACH e0 e3
STATE
PATH e0 e1 e2 e3
```

Target:

```text
VALID
```

### train/implication_chains/action

- ID: `train:implication_chains:288:action:0`

Source:

```text
MODE action
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p0 -> p2
HYP h6 : p3 -> p1
HYP h7 : p5 -> p0
HYP h8 : p6 -> p0
GOAL p4
STATE
EMPTY
```

Target:

```text
APPLY h0
```

### train/implication_chains/repair_action

- ID: `train:implication_chains:288:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p0 -> p2
HYP h6 : p3 -> p1
HYP h7 : p5 -> p0
HYP h8 : p6 -> p0
GOAL p4
STATE
DERIVE p0 BY h999
```

Target:

```text
REPLACE LINE 0 HYP h0
```

### train/implication_chains/verify

- ID: `train:implication_chains:288:verify:valid`

Source:

```text
MODE verify
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p0 -> p2
HYP h6 : p3 -> p1
HYP h7 : p5 -> p0
HYP h8 : p6 -> p0
GOAL p4
STATE
DERIVE p0 BY h0
DERIVE p1 BY h1 FROM p0
DERIVE p2 BY h2 FROM p1
DERIVE p3 BY h3 FROM p2
DERIVE p4 BY h4 FROM p3
```

Target:

```text
VALID
```

### train/relation_composition/action

- ID: `train:relation_composition:576:action:0`

Source:

```text
MODE action
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
FACT r3 e3 e4
RULE r4 = r0 ; r1
RULE r5 = r4 ; r2
RULE r6 = r5 ; r3
FACT r1 e2 e1
FACT r1 e6 e2
FACT r3 e1 e3
FACT r3 e1 e5
QUERY r6 e0 e4
STATE
EMPTY
```

Target:

```text
FOLLOW e2 VIA e1
```

### train/relation_composition/repair_action

- ID: `train:relation_composition:576:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
FACT r3 e3 e4
RULE r4 = r0 ; r1
RULE r5 = r4 ; r2
RULE r6 = r5 ; r3
FACT r1 e2 e1
FACT r1 e6 e2
FACT r3 e1 e3
FACT r3 e1 e5
QUERY r6 e0 e4
STATE
DERIVE r4 e0 e2 VIA e0
```

Target:

```text
REPLACE LINE 0 VIA e1
```

### train/relation_composition/verify

- ID: `train:relation_composition:576:verify:valid`

Source:

```text
MODE verify
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
FACT r3 e3 e4
RULE r4 = r0 ; r1
RULE r5 = r4 ; r2
RULE r6 = r5 ; r3
FACT r1 e2 e1
FACT r1 e6 e2
FACT r3 e1 e3
FACT r3 e1 e5
QUERY r6 e0 e4
STATE
DERIVE r4 e0 e2 VIA e1
DERIVE r5 e0 e3 VIA e2
DERIVE r6 e0 e4 VIA e3
```

Target:

```text
VALID
```

### train/tree_ancestry/action

- ID: `train:tree_ancestry:816:action:0`

Source:

```text
MODE action
PROBLEM
PARENT e0 e1
PARENT e0 e7
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e3 e6
PARENT e4 e5
QUERY ANCESTOR e0 e5
STATE
EMPTY
```

Target:

```text
DESCEND e0
```

### train/tree_ancestry/repair_action

- ID: `train:tree_ancestry:816:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
PARENT e0 e1
PARENT e0 e7
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e3 e6
PARENT e4 e5
QUERY ANCESTOR e0 e5
STATE
LINEAGE e5
```

Target:

```text
REPLACE NODE 0 WITH e0
```

### train/tree_ancestry/verify

- ID: `train:tree_ancestry:816:verify:valid`

Source:

```text
MODE verify
PROBLEM
PARENT e0 e1
PARENT e0 e7
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e3 e6
PARENT e4 e5
QUERY ANCESTOR e0 e5
STATE
LINEAGE e0 e1 e2 e3 e4 e5
```

Target:

```text
VALID
```
