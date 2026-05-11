# Dataset Audit

- Data dir: `data/symbolic-v10-same-vocab-stress`
- Status: `pass`
- Errors: `0`
- Warnings: `0`

## JSONL Summary

### train

- Examples: `20`
- Problems: `3`
- Families: `{'graph_reachability': 8, 'implication_chains': 8, 'relation_composition': 4}`
- Modes: `{'action': 7, 'repair_action': 7, 'verify': 6}`
- Verify targets: `{'INVALID BAD_EDGE': 1, 'INVALID BAD_FACT': 1, 'INVALID BAD_PREMISE': 1, 'VALID': 3}`

### test

- Examples: `26`
- Problems: `3`
- Families: `{'graph_reachability': 10, 'implication_chains': 10, 'relation_composition': 6}`
- Modes: `{'action': 10, 'repair_action': 10, 'verify': 6}`
- Verify targets: `{'INVALID BAD_FACT': 1, 'INVALID BAD_PATH_END': 1, 'INVALID BAD_PREMISE': 1, 'VALID': 3}`

### ood

- Examples: `1800`
- Problems: `108`
- Families: `{'graph_reachability': 660, 'implication_chains': 600, 'relation_composition': 540}`
- Modes: `{'action': 972, 'repair_action': 612, 'verify': 216}`
- Verify targets: `{'INVALID BAD_EDGE': 34, 'INVALID BAD_FACT': 36, 'INVALID BAD_PATH_END': 2, 'INVALID BAD_PREMISE': 31, 'INVALID UNKNOWN_HYP': 5, 'VALID': 108}`

## Difficulty Summary

### graph_reachability

- `extra_edges`: `{'min': 1.0, 'max': 15.0, 'mean': 12.889380530973451, 'unique': [1, 11, 12, 13, 14, 15]}`
- `num_nodes`: `{'min': 5.0, 'max': 19.0, 'mean': 15.079646017699115, 'unique': [5, 6, 13, 14, 15, 16, 17, 18, 19]}`
- `path_length`: `{'min': 2.0, 'max': 10.0, 'mean': 8.705014749262537, 'unique': [2, 3, 8, 9, 10]}`
- `require_shortest`: `{True: 678}`
- `symbol_offset`: `{'min': 0.0, 'max': 4.0, 'mean': 2.1946902654867255, 'unique': [0, 2, 4]}`

### implication_chains

- `distractor_hyps`: `{'min': 1.0, 'max': 12.0, 'mean': 9.462783171521036, 'unique': [1, 8, 9, 10, 11, 12]}`
- `num_props`: `{'min': 5.0, 'max': 19.0, 'mean': 15.346278317152104, 'unique': [5, 6, 13, 14, 15, 16, 17, 18, 19]}`
- `proof_length`: `{'min': 3.0, 'max': 10.0, 'mean': 8.724919093851133, 'unique': [3, 4, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 4.0, 'mean': 2.174757281553398, 'unique': [0, 2, 4]}`

### relation_composition

- `composition_depth`: `{'min': 2.0, 'max': 10.0, 'mean': 8.774545454545455, 'unique': [2, 3, 8, 9, 10]}`
- `distractor_facts`: `{'min': 1.0, 'max': 16.0, 'mean': 12.605454545454545, 'unique': [1, 10, 11, 12, 13, 14, 15, 16]}`
- `num_entities`: `{'min': 5.0, 'max': 19.0, 'mean': 15.212727272727273, 'unique': [5, 6, 13, 14, 15, 16, 17, 18, 19]}`
- `symbol_offset`: `{'min': 0.0, 'max': 4.0, 'mean': 2.1818181818181817, 'unique': [0, 2, 4]}`

## TRM Array Summary

### train

- Inputs shape: `[20, 272]`
- Labels shape: `[20, 272]`
- Seq len: `272`
- Vocab size: `133`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `20`

### test

- Inputs shape: `[26, 272]`
- Labels shape: `[26, 272]`
- Seq len: `272`
- Vocab size: `133`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `26`

### ood

- Inputs shape: `[1800, 272]`
- Labels shape: `[1800, 272]`
- Seq len: `272`
- Vocab size: `133`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1800`

## Samples

### ood/graph_reachability/action

- ID: `ood:graph_reachability:0:action:0`

Source:

```text
MODE action
PROBLEM
EDGE e10 e11
EDGE e10 e17
EDGE e11 e12
EDGE e11 e14
EDGE e11 e5
EDGE e11 e9
EDGE e12 e15
EDGE e12 e9
EDGE e13 e10
EDGE e13 e8
EDGE e16 e5
EDGE e4 e5
EDGE e5 e14
EDGE e5 e6
EDGE e6 e7
EDGE e7 e14
EDGE e7 e8
EDGE e8 e9
EDGE e9 e10
EDGE e9 e5
EDGE e9 e7
QUERY REACH e4 e12
STATE
EMPTY
```

Target:

```text
APPEND e4
```

### ood/graph_reachability/repair_action

- ID: `ood:graph_reachability:0:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
EDGE e10 e11
EDGE e10 e17
EDGE e11 e12
EDGE e11 e14
EDGE e11 e5
EDGE e11 e9
EDGE e12 e15
EDGE e12 e9
EDGE e13 e10
EDGE e13 e8
EDGE e16 e5
EDGE e4 e5
EDGE e5 e14
EDGE e5 e6
EDGE e6 e7
EDGE e7 e14
EDGE e7 e8
EDGE e8 e9
EDGE e9 e10
EDGE e9 e5
EDGE e9 e7
QUERY REACH e4 e12
STATE
PATH e12
```

Target:

```text
REPLACE NODE 0 WITH e4
```

### ood/graph_reachability/verify

- ID: `ood:graph_reachability:0:verify:valid`

Source:

```text
MODE verify
PROBLEM
EDGE e10 e11
EDGE e10 e17
EDGE e11 e12
EDGE e11 e14
EDGE e11 e5
EDGE e11 e9
EDGE e12 e15
EDGE e12 e9
EDGE e13 e10
EDGE e13 e8
EDGE e16 e5
EDGE e4 e5
EDGE e5 e14
EDGE e5 e6
EDGE e6 e7
EDGE e7 e14
EDGE e7 e8
EDGE e8 e9
EDGE e9 e10
EDGE e9 e5
EDGE e9 e7
QUERY REACH e4 e12
STATE
PATH e4 e5 e6 e7 e8 e9 e10 e11 e12
```

Target:

```text
VALID
```

### ood/implication_chains/action

- ID: `ood:implication_chains:36:action:0`

Source:

```text
MODE action
PROBLEM
HYP h4 : p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p7 -> p8
HYP h9 : p8 -> p9
HYP h10 : p9 -> p10
HYP h11 : p10 -> p11
HYP h12 : p4 -> p11
HYP h13 : p4 -> p15
HYP h14 : p7 -> p12
HYP h15 : p9 -> p14
HYP h16 : p10 -> p6
HYP h17 : p15 -> p14
HYP h18 : p16 -> p8
HYP h19 : p17 -> p15
GOAL p11
STATE
EMPTY
```

Target:

```text
APPLY h4
```

### ood/implication_chains/repair_action

- ID: `ood:implication_chains:36:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
HYP h4 : p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p7 -> p8
HYP h9 : p8 -> p9
HYP h10 : p9 -> p10
HYP h11 : p10 -> p11
HYP h12 : p4 -> p11
HYP h13 : p4 -> p15
HYP h14 : p7 -> p12
HYP h15 : p9 -> p14
HYP h16 : p10 -> p6
HYP h17 : p15 -> p14
HYP h18 : p16 -> p8
HYP h19 : p17 -> p15
GOAL p11
STATE
DERIVE p4 BY h999
```

Target:

```text
REPLACE LINE 0 HYP h4
```

### ood/implication_chains/verify

- ID: `ood:implication_chains:36:verify:valid`

Source:

```text
MODE verify
PROBLEM
HYP h4 : p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p7 -> p8
HYP h9 : p8 -> p9
HYP h10 : p9 -> p10
HYP h11 : p10 -> p11
HYP h12 : p4 -> p11
HYP h13 : p4 -> p15
HYP h14 : p7 -> p12
HYP h15 : p9 -> p14
HYP h16 : p10 -> p6
HYP h17 : p15 -> p14
HYP h18 : p16 -> p8
HYP h19 : p17 -> p15
GOAL p11
STATE
DERIVE p4 BY h4
DERIVE p5 BY h5 FROM p4
DERIVE p6 BY h6 FROM p5
DERIVE p7 BY h7 FROM p6
DERIVE p8 BY h8 FROM p7
DERIVE p9 BY h9 FROM p8
DERIVE p10 BY h10 FROM p9
DERIVE p11 BY h11 FROM p10
```

Target:

```text
VALID
```

### ood/relation_composition/action

- ID: `ood:relation_composition:72:action:0`

Source:

```text
MODE action
PROBLEM
FACT r4 e4 e5
FACT r5 e5 e6
FACT r6 e6 e7
FACT r7 e7 e8
FACT r8 e8 e9
FACT r9 e9 e10
FACT r10 e10 e11
FACT r11 e11 e12
RULE r12 = r4 ; r5
RULE r13 = r12 ; r6
RULE r14 = r13 ; r7
RULE r15 = r14 ; r8
RULE r16 = r15 ; r9
RULE r17 = r16 ; r10
RULE r18 = r17 ; r11
FACT r4 e5 e12
FACT r4 e7 e13
FACT r5 e13 e15
FACT r7 e4 e9
FACT r7 e6 e11
FACT r7 e8 e9
FACT r8 e5 e18
FACT r8 e16 e10
FACT r8 e18 e12
FACT r9 e5 e12
FACT r9 e8 e4
FACT r10 e5 e16
FACT r10 e7 e4
FACT r10 e9 e6
QUERY r18 e4 e12
STATE
EMPTY
```

Target:

```text
FOLLOW e6 VIA e5
```

### ood/relation_composition/repair_action

- ID: `ood:relation_composition:72:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
FACT r4 e4 e5
FACT r5 e5 e6
FACT r6 e6 e7
FACT r7 e7 e8
FACT r8 e8 e9
FACT r9 e9 e10
FACT r10 e10 e11
FACT r11 e11 e12
RULE r12 = r4 ; r5
RULE r13 = r12 ; r6
RULE r14 = r13 ; r7
RULE r15 = r14 ; r8
RULE r16 = r15 ; r9
RULE r17 = r16 ; r10
RULE r18 = r17 ; r11
FACT r4 e5 e12
FACT r4 e7 e13
FACT r5 e13 e15
FACT r7 e4 e9
FACT r7 e6 e11
FACT r7 e8 e9
FACT r8 e5 e18
FACT r8 e16 e10
FACT r8 e18 e12
FACT r9 e5 e12
FACT r9 e8 e4
FACT r10 e5 e16
FACT r10 e7 e4
FACT r10 e9 e6
QUERY r18 e4 e12
STATE
DERIVE r12 e4 e6 VIA e10
```

Target:

```text
REPLACE LINE 0 VIA e5
```

### ood/relation_composition/verify

- ID: `ood:relation_composition:72:verify:valid`

Source:

```text
MODE verify
PROBLEM
FACT r4 e4 e5
FACT r5 e5 e6
FACT r6 e6 e7
FACT r7 e7 e8
FACT r8 e8 e9
FACT r9 e9 e10
FACT r10 e10 e11
FACT r11 e11 e12
RULE r12 = r4 ; r5
RULE r13 = r12 ; r6
RULE r14 = r13 ; r7
RULE r15 = r14 ; r8
RULE r16 = r15 ; r9
RULE r17 = r16 ; r10
RULE r18 = r17 ; r11
FACT r4 e5 e12
FACT r4 e7 e13
FACT r5 e13 e15
FACT r7 e4 e9
FACT r7 e6 e11
FACT r7 e8 e9
FACT r8 e5 e18
FACT r8 e16 e10
FACT r8 e18 e12
FACT r9 e5 e12
FACT r9 e8 e4
FACT r10 e5 e16
FACT r10 e7 e4
FACT r10 e9 e6
QUERY r18 e4 e12
STATE
DERIVE r12 e4 e6 VIA e5
DERIVE r13 e4 e7 VIA e6
DERIVE r14 e4 e8 VIA e7
DERIVE r15 e4 e9 VIA e8
DERIVE r16 e4 e10 VIA e9
DERIVE r17 e4 e11 VIA e10
DERIVE r18 e4 e12 VIA e11
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
EDGE e2 e0
EDGE e2 e3
QUERY REACH e0 e3
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
EDGE e2 e0
EDGE e2 e3
QUERY REACH e0 e3
STATE
PATH e3
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
EDGE e2 e0
EDGE e2 e3
QUERY REACH e0 e3
STATE
PATH e0 e1 e2 e3
```

Target:

```text
VALID
```

### test/implication_chains/action

- ID: `test:implication_chains:1:action:0`

Source:

```text
MODE action
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p4 -> p5
GOAL p3
STATE
EMPTY
```

Target:

```text
APPLY h0
```

### test/implication_chains/repair_action

- ID: `test:implication_chains:1:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p4 -> p5
GOAL p3
STATE
DERIVE p0 BY h999
```

Target:

```text
REPLACE LINE 0 HYP h0
```

### test/implication_chains/verify

- ID: `test:implication_chains:1:verify:valid`

Source:

```text
MODE verify
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p4 -> p5
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

### test/relation_composition/action

- ID: `test:relation_composition:2:action:0`

Source:

```text
MODE action
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e3 e1
QUERY r4 e0 e3
STATE
EMPTY
```

Target:

```text
FOLLOW e2 VIA e1
```

### test/relation_composition/repair_action

- ID: `test:relation_composition:2:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e3 e1
QUERY r4 e0 e3
STATE
DERIVE r3 e0 e2 VIA e0
```

Target:

```text
REPLACE LINE 0 VIA e1
```

### test/relation_composition/verify

- ID: `test:relation_composition:2:verify:valid`

Source:

```text
MODE verify
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e3 e1
QUERY r4 e0 e3
STATE
DERIVE r3 e0 e2 VIA e1
DERIVE r4 e0 e3 VIA e2
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
EDGE e4 e1
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
EDGE e4 e1
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
EDGE e4 e1
QUERY REACH e0 e2
STATE
PATH e0 e1 e2
```

Target:

```text
VALID
```

### train/implication_chains/action

- ID: `train:implication_chains:1:action:0`

Source:

```text
MODE action
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p4
GOAL p2
STATE
EMPTY
```

Target:

```text
APPLY h0
```

### train/implication_chains/repair_action

- ID: `train:implication_chains:1:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p4
GOAL p2
STATE
DERIVE p0 BY h999
```

Target:

```text
REPLACE LINE 0 HYP h0
```

### train/implication_chains/verify

- ID: `train:implication_chains:1:verify:valid`

Source:

```text
MODE verify
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p4
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

### train/relation_composition/action

- ID: `train:relation_composition:2:action:0`

Source:

```text
MODE action
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
RULE r2 = r0 ; r1
FACT r1 e2 e1
QUERY r2 e0 e2
STATE
EMPTY
```

Target:

```text
FOLLOW e2 VIA e1
```

### train/relation_composition/repair_action

- ID: `train:relation_composition:2:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
RULE r2 = r0 ; r1
FACT r1 e2 e1
QUERY r2 e0 e2
STATE
DERIVE r2 e0 e2 VIA e0
```

Target:

```text
REPLACE LINE 0 VIA e1
```

### train/relation_composition/verify

- ID: `train:relation_composition:2:verify:valid`

Source:

```text
MODE verify
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
RULE r2 = r0 ; r1
FACT r1 e2 e1
QUERY r2 e0 e2
STATE
DERIVE r2 e0 e2 VIA e1
```

Target:

```text
VALID
```
