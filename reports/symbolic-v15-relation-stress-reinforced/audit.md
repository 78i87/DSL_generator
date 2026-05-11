# Dataset Audit

- Data dir: `data/symbolic-v15-relation-stress-reinforced`
- Status: `pass`
- Errors: `0`
- Warnings: `0`

## JSONL Summary

### train

- Examples: `17430`
- Problems: `1392`
- Families: `{'graph_reachability': 4134, 'implication_chains': 3650, 'relation_composition': 5494, 'tree_ancestry': 4152}`
- Modes: `{'action': 8139, 'repair_action': 8139, 'verify': 1152}`
- Verify targets: `{'INVALID BAD_EDGE': 117, 'INVALID BAD_FACT': 144, 'INVALID BAD_LINEAGE_END': 23, 'INVALID BAD_PATH_END': 27, 'INVALID BAD_PREMISE': 111, 'INVALID REPEATED_NODE': 121, 'INVALID UNKNOWN_HYP': 33, 'VALID': 576}`

### test

- Examples: `978`
- Problems: `72`
- Families: `{'graph_reachability': 268, 'implication_chains': 230, 'relation_composition': 202, 'tree_ancestry': 278}`
- Modes: `{'action': 417, 'repair_action': 417, 'verify': 144}`
- Verify targets: `{'INVALID BAD_EDGE': 14, 'INVALID BAD_FACT': 18, 'INVALID BAD_LINEAGE_END': 5, 'INVALID BAD_PATH_END': 4, 'INVALID BAD_PREMISE': 16, 'INVALID REPEATED_NODE': 13, 'INVALID UNKNOWN_HYP': 2, 'VALID': 72}`

### ood

- Examples: `1476`
- Problems: `72`
- Families: `{'graph_reachability': 396, 'implication_chains': 360, 'relation_composition': 324, 'tree_ancestry': 396}`
- Modes: `{'action': 666, 'repair_action': 666, 'verify': 144}`
- Verify targets: `{'INVALID BAD_EDGE': 15, 'INVALID BAD_FACT': 18, 'INVALID BAD_LINEAGE_END': 1, 'INVALID BAD_PATH_END': 3, 'INVALID BAD_PREMISE': 16, 'INVALID REPEATED_NODE': 17, 'INVALID UNKNOWN_HYP': 2, 'VALID': 72}`

## Difficulty Summary

### graph_reachability

- `extra_edges`: `{'min': 1.0, 'max': 16.0, 'mean': 8.561692371821593, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `num_nodes`: `{'min': 5.0, 'max': 19.0, 'mean': 12.510421008753648, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `path_length`: `{'min': 2.0, 'max': 10.0, 'mean': 7.448520216756982, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `require_shortest`: `{True: 4798}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.3405585660691954, 'unique': [0, 2, 3, 4, 6]}`

### implication_chains

- `distractor_hyps`: `{'min': 1.0, 'max': 12.0, 'mean': 7.694103773584906, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}`
- `num_props`: `{'min': 5.0, 'max': 19.0, 'mean': 12.446462264150943, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `proof_length`: `{'min': 2.0, 'max': 10.0, 'mean': 7.5, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.3471698113207546, 'unique': [0, 2, 3, 4, 6]}`

### relation_composition

- `composition_depth`: `{'min': 2.0, 'max': 10.0, 'mean': 8.146179401993356, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_facts`: `{'min': 1.0, 'max': 16.0, 'mean': 10.353156146179401, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `num_entities`: `{'min': 5.0, 'max': 19.0, 'mean': 13.811627906976744, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.5308970099667774, 'unique': [0, 2, 3, 4, 6]}`

### tree_ancestry

- `branching_factor`: `{'min': 2.0, 'max': 4.0, 'mean': 2.7331123083298796, 'unique': [2, 3, 4]}`
- `depth`: `{'min': 2.0, 'max': 10.0, 'mean': 7.454206382096975, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_subtrees`: `{'min': 1.0, 'max': 16.0, 'mean': 8.502900953170327, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.3327807708246995, 'unique': [0, 2, 3, 4, 6]}`

## TRM Array Summary

### train

- Inputs shape: `[17430, 275]`
- Labels shape: `[17430, 275]`
- Seq len: `275`
- Vocab size: `148`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `17430`

### test

- Inputs shape: `[978, 275]`
- Labels shape: `[978, 275]`
- Seq len: `275`
- Vocab size: `148`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `978`

### ood

- Inputs shape: `[1476, 275]`
- Labels shape: `[1476, 275]`
- Seq len: `275`
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
EDGE e0 e10
EDGE e1 e2
EDGE e2 e3
EDGE e3 e10
EDGE e3 e4
EDGE e4 e5
EDGE e5 e1
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e9 e3
EDGE e9 e8
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
EDGE e0 e10
EDGE e1 e2
EDGE e2 e3
EDGE e3 e10
EDGE e3 e4
EDGE e4 e5
EDGE e5 e1
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e9 e3
EDGE e9 e8
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
EDGE e0 e10
EDGE e1 e2
EDGE e2 e3
EDGE e3 e10
EDGE e3 e4
EDGE e4 e5
EDGE e5 e1
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e9 e3
EDGE e9 e8
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
HYP h8 : p0 -> p5
HYP h9 : p0 -> p8
HYP h10 : p2 -> p11
HYP h11 : p4 -> p0
HYP h12 : p5 -> p12
HYP h13 : p6 -> p10
HYP h14 : p8 -> p10
HYP h15 : p9 -> p3
HYP h16 : p11 -> p2
HYP h17 : p12 -> p9
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
HYP h8 : p0 -> p5
HYP h9 : p0 -> p8
HYP h10 : p2 -> p11
HYP h11 : p4 -> p0
HYP h12 : p5 -> p12
HYP h13 : p6 -> p10
HYP h14 : p8 -> p10
HYP h15 : p9 -> p3
HYP h16 : p11 -> p2
HYP h17 : p12 -> p9
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
HYP h8 : p0 -> p5
HYP h9 : p0 -> p8
HYP h10 : p2 -> p11
HYP h11 : p4 -> p0
HYP h12 : p5 -> p12
HYP h13 : p6 -> p10
HYP h14 : p8 -> p10
HYP h15 : p9 -> p3
HYP h16 : p11 -> p2
HYP h17 : p12 -> p9
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
FACT r0 e4 e5
FACT r1 e6 e5
FACT r1 e7 e1
FACT r2 e5 e7
FACT r4 e8 e2
FACT r6 e13 e3
FACT r7 e3 e1
FACT r7 e6 e10
FACT r7 e8 e13
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
FACT r0 e4 e5
FACT r1 e6 e5
FACT r1 e7 e1
FACT r2 e5 e7
FACT r4 e8 e2
FACT r6 e13 e3
FACT r7 e3 e1
FACT r7 e6 e10
FACT r7 e8 e13
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
FACT r0 e4 e5
FACT r1 e6 e5
FACT r1 e7 e1
FACT r2 e5 e7
FACT r4 e8 e2
FACT r6 e13 e3
FACT r7 e3 e1
FACT r7 e6 e10
FACT r7 e8 e13
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
PARENT e11 e14
PARENT e2 e3
PARENT e3 e4
PARENT e3 e9
PARENT e4 e5
PARENT e5 e10
PARENT e5 e11
PARENT e5 e6
PARENT e6 e7
PARENT e7 e13
PARENT e7 e8
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
PARENT e11 e14
PARENT e2 e3
PARENT e3 e4
PARENT e3 e9
PARENT e4 e5
PARENT e5 e10
PARENT e5 e11
PARENT e5 e6
PARENT e6 e7
PARENT e7 e13
PARENT e7 e8
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
PARENT e11 e14
PARENT e2 e3
PARENT e3 e4
PARENT e3 e9
PARENT e4 e5
PARENT e5 e10
PARENT e5 e11
PARENT e5 e6
PARENT e6 e7
PARENT e7 e13
PARENT e7 e8
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
EDGE e2 e3
EDGE e3 e2
EDGE e3 e4
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
EDGE e2 e3
EDGE e3 e2
EDGE e3 e4
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
EDGE e2 e3
EDGE e3 e2
EDGE e3 e4
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
HYP h2 : p1 -> p2
HYP h3 : p1 -> p6
GOAL p2
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
HYP h2 : p1 -> p2
HYP h3 : p1 -> p6
GOAL p2
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
HYP h2 : p1 -> p2
HYP h3 : p1 -> p6
GOAL p2
STATE
DERIVE p0 BY h0
DERIVE p1 BY h1 FROM p0
DERIVE p2 BY h2 FROM p1
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
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e2 e1
FACT r1 e0 e5
FACT r1 e3 e1
FACT r1 e4 e7
FACT r1 e6 e1
QUERY r4 e0 e3
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
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e2 e1
FACT r1 e0 e5
FACT r1 e3 e1
FACT r1 e4 e7
FACT r1 e6 e1
QUERY r4 e0 e3
STATE
DERIVE r3 e0 e2 VIA e0
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
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e2 e1
FACT r1 e0 e5
FACT r1 e3 e1
FACT r1 e4 e7
FACT r1 e6 e1
QUERY r4 e0 e3
STATE
DERIVE r3 e0 e2 VIA e1
DERIVE r4 e0 e3 VIA e2
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
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e4 e5
PARENT e4 e6
QUERY ANCESTOR e0 e4
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
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e4 e5
PARENT e4 e6
QUERY ANCESTOR e0 e4
STATE
LINEAGE e4
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
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e4 e5
PARENT e4 e6
QUERY ANCESTOR e0 e4
STATE
LINEAGE e0 e1 e2 e3 e4
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
EDGE e4 e3
EDGE e5 e2
EDGE e6 e0
QUERY REACH e0 e2
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
EDGE e4 e3
EDGE e5 e2
EDGE e6 e0
QUERY REACH e0 e2
STATE
PATH e2
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
EDGE e4 e3
EDGE e5 e2
EDGE e6 e0
QUERY REACH e0 e2
STATE
PATH e0 e1 e2
```

Target:

```text
VALID
```

### train/implication_chains/action

- ID: `train:implication_chains:312:action:0`

Source:

```text
MODE action
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p1
HYP h5 : p4 -> p2
GOAL p3
STATE
EMPTY
```

Target:

```text
APPLY h0
```

### train/implication_chains/repair_action

- ID: `train:implication_chains:312:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p1
HYP h5 : p4 -> p2
GOAL p3
STATE
DERIVE p0 BY h999
```

Target:

```text
REPLACE LINE 0 HYP h0
```

### train/implication_chains/verify

- ID: `train:implication_chains:312:verify:valid`

Source:

```text
MODE verify
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p1
HYP h5 : p4 -> p2
GOAL p3
STATE
DERIVE p0 BY h0
DERIVE p1 BY h1 FROM p0
DERIVE p2 BY h2 FROM p1
DERIVE p3 BY h3 FROM p2
```

Target:

```text
VALID
```

### train/relation_composition/action

- ID: `train:relation_composition:624:action:0`

Source:

```text
MODE action
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e3 e6
FACT r1 e5 e8
FACT r2 e1 e0
QUERY r4 e0 e3
STATE
EMPTY
```

Target:

```text
FOLLOW e2 VIA e1
```

### train/relation_composition/repair_action

- ID: `train:relation_composition:624:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e3 e6
FACT r1 e5 e8
FACT r2 e1 e0
QUERY r4 e0 e3
STATE
DERIVE r3 e0 e2 VIA e0
```

Target:

```text
REPLACE LINE 0 VIA e1
```

### train/relation_composition/verify

- ID: `train:relation_composition:624:verify:valid`

Source:

```text
MODE verify
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e3 e6
FACT r1 e5 e8
FACT r2 e1 e0
QUERY r4 e0 e3
STATE
DERIVE r3 e0 e2 VIA e1
DERIVE r4 e0 e3 VIA e2
```

Target:

```text
VALID
```

### train/tree_ancestry/action

- ID: `train:tree_ancestry:1080:action:0`

Source:

```text
MODE action
PROBLEM
PARENT e0 e1
PARENT e0 e5
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e4 e6
PARENT e4 e7
QUERY ANCESTOR e0 e4
STATE
EMPTY
```

Target:

```text
DESCEND e0
```

### train/tree_ancestry/repair_action

- ID: `train:tree_ancestry:1080:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
PARENT e0 e1
PARENT e0 e5
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e4 e6
PARENT e4 e7
QUERY ANCESTOR e0 e4
STATE
LINEAGE e4
```

Target:

```text
REPLACE NODE 0 WITH e0
```

### train/tree_ancestry/verify

- ID: `train:tree_ancestry:1080:verify:valid`

Source:

```text
MODE verify
PROBLEM
PARENT e0 e1
PARENT e0 e5
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e4 e6
PARENT e4 e7
QUERY ANCESTOR e0 e4
STATE
LINEAGE e0 e1 e2 e3 e4
```

Target:

```text
VALID
```
