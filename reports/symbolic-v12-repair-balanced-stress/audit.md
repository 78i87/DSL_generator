# Dataset Audit

- Data dir: `data/symbolic-v12-repair-balanced-stress`
- Status: `pass`
- Errors: `0`
- Warnings: `0`

## JSONL Summary

### train

- Examples: `10008`
- Problems: `816`
- Families: `{'graph_reachability': 3872, 'implication_chains': 3410, 'relation_composition': 2726}`
- Modes: `{'action': 5064, 'repair_action': 4080, 'verify': 864}`
- Verify targets: `{'INVALID BAD_EDGE': 122, 'INVALID BAD_FACT': 144, 'INVALID BAD_PATH_END': 22, 'INVALID BAD_PREMISE': 120, 'INVALID UNKNOWN_HYP': 24, 'VALID': 432}`

### test

- Examples: `696`
- Problems: `54`
- Families: `{'graph_reachability': 274, 'implication_chains': 222, 'relation_composition': 200}`
- Modes: `{'action': 294, 'repair_action': 294, 'verify': 108}`
- Verify targets: `{'INVALID BAD_EDGE': 14, 'INVALID BAD_FACT': 18, 'INVALID BAD_PATH_END': 4, 'INVALID BAD_PREMISE': 14, 'INVALID UNKNOWN_HYP': 4, 'VALID': 54}`

### ood

- Examples: `1080`
- Problems: `54`
- Families: `{'graph_reachability': 396, 'implication_chains': 360, 'relation_composition': 324}`
- Modes: `{'action': 486, 'repair_action': 486, 'verify': 108}`
- Verify targets: `{'INVALID BAD_EDGE': 18, 'INVALID BAD_FACT': 18, 'INVALID BAD_PREMISE': 16, 'INVALID UNKNOWN_HYP': 2, 'VALID': 54}`

## Difficulty Summary

### graph_reachability

- `extra_edges`: `{'min': 1.0, 'max': 16.0, 'mean': 8.057683839718186, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `num_nodes`: `{'min': 5.0, 'max': 19.0, 'mean': 12.256494936151475, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `path_length`: `{'min': 2.0, 'max': 10.0, 'mean': 7.3029502421840595, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `require_shortest`: `{True: 4542}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.416116248348745, 'unique': [0, 2, 3, 4, 6]}`

### implication_chains

- `distractor_hyps`: `{'min': 1.0, 'max': 12.0, 'mean': 7.628507014028056, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}`
- `num_props`: `{'min': 5.0, 'max': 19.0, 'mean': 12.148547094188377, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `proof_length`: `{'min': 2.0, 'max': 10.0, 'mean': 7.351703406813627, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.4308617234468939, 'unique': [0, 2, 3, 4, 6]}`

### relation_composition

- `composition_depth`: `{'min': 2.0, 'max': 10.0, 'mean': 7.478769230769231, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_facts`: `{'min': 1.0, 'max': 16.0, 'mean': 8.574461538461538, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `num_entities`: `{'min': 5.0, 'max': 19.0, 'mean': 12.492, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.536, 'unique': [0, 2, 3, 4, 6]}`

## TRM Array Summary

### train

- Inputs shape: `[10008, 272]`
- Labels shape: `[10008, 272]`
- Seq len: `272`
- Vocab size: `133`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `10008`

### test

- Inputs shape: `[696, 272]`
- Labels shape: `[696, 272]`
- Seq len: `272`
- Vocab size: `133`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `696`

### ood

- Inputs shape: `[1080, 272]`
- Labels shape: `[1080, 272]`
- Seq len: `272`
- Vocab size: `133`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1080`

## Samples

### ood/graph_reachability/action

- ID: `ood:graph_reachability:0:action:0`

Source:

```text
MODE action
PROBLEM
EDGE e0 e1
EDGE e1 e0
EDGE e1 e2
EDGE e11 e8
EDGE e12 e0
EDGE e12 e1
EDGE e2 e10
EDGE e2 e3
EDGE e3 e4
EDGE e4 e12
EDGE e4 e5
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e9 e0
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
EDGE e1 e0
EDGE e1 e2
EDGE e11 e8
EDGE e12 e0
EDGE e12 e1
EDGE e2 e10
EDGE e2 e3
EDGE e3 e4
EDGE e4 e12
EDGE e4 e5
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e9 e0
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
EDGE e1 e0
EDGE e1 e2
EDGE e11 e8
EDGE e12 e0
EDGE e12 e1
EDGE e2 e10
EDGE e2 e3
EDGE e3 e4
EDGE e4 e12
EDGE e4 e5
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e9 e0
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
HYP h8 : p5 -> p4
HYP h9 : p6 -> p1
HYP h10 : p6 -> p3
HYP h11 : p7 -> p6
HYP h12 : p8 -> p4
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
HYP h8 : p5 -> p4
HYP h9 : p6 -> p1
HYP h10 : p6 -> p3
HYP h11 : p7 -> p6
HYP h12 : p8 -> p4
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
HYP h8 : p5 -> p4
HYP h9 : p6 -> p1
HYP h10 : p6 -> p3
HYP h11 : p7 -> p6
HYP h12 : p8 -> p4
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
FACT r1 e5 e7
FACT r1 e11 e1
FACT r2 e3 e10
FACT r3 e3 e11
FACT r4 e5 e6
FACT r4 e5 e8
FACT r5 e8 e2
FACT r6 e8 e9
FACT r7 e8 e0
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
FACT r1 e5 e7
FACT r1 e11 e1
FACT r2 e3 e10
FACT r3 e3 e11
FACT r4 e5 e6
FACT r4 e5 e8
FACT r5 e8 e2
FACT r6 e8 e9
FACT r7 e8 e0
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
FACT r1 e5 e7
FACT r1 e11 e1
FACT r2 e3 e10
FACT r3 e3 e11
FACT r4 e5 e6
FACT r4 e5 e8
FACT r5 e8 e2
FACT r6 e8 e9
FACT r7 e8 e0
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

### test/graph_reachability/action

- ID: `test:graph_reachability:0:action:0`

Source:

```text
MODE action
PROBLEM
EDGE e0 e1
EDGE e0 e6
EDGE e1 e2
EDGE e2 e3
EDGE e3 e4
EDGE e3 e5
EDGE e5 e0
EDGE e6 e0
EDGE e7 e4
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
EDGE e0 e6
EDGE e1 e2
EDGE e2 e3
EDGE e3 e4
EDGE e3 e5
EDGE e5 e0
EDGE e6 e0
EDGE e7 e4
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
EDGE e0 e6
EDGE e1 e2
EDGE e2 e3
EDGE e3 e4
EDGE e3 e5
EDGE e5 e0
EDGE e6 e0
EDGE e7 e4
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
HYP h2 : p0 -> p4
HYP h3 : p1 -> p0
HYP h4 : p2 -> p0
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
HYP h2 : p0 -> p4
HYP h3 : p1 -> p0
HYP h4 : p2 -> p0
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
HYP h2 : p0 -> p4
HYP h3 : p1 -> p0
HYP h4 : p2 -> p0
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
FACT r4 e4 e5
RULE r5 = r0 ; r1
RULE r6 = r5 ; r2
RULE r7 = r6 ; r3
RULE r8 = r7 ; r4
FACT r0 e1 e4
FACT r1 e4 e1
FACT r2 e5 e4
FACT r3 e5 e1
QUERY r8 e0 e5
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
FACT r4 e4 e5
RULE r5 = r0 ; r1
RULE r6 = r5 ; r2
RULE r7 = r6 ; r3
RULE r8 = r7 ; r4
FACT r0 e1 e4
FACT r1 e4 e1
FACT r2 e5 e4
FACT r3 e5 e1
QUERY r8 e0 e5
STATE
DERIVE r5 e0 e2 VIA e0
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
FACT r4 e4 e5
RULE r5 = r0 ; r1
RULE r6 = r5 ; r2
RULE r7 = r6 ; r3
RULE r8 = r7 ; r4
FACT r0 e1 e4
FACT r1 e4 e1
FACT r2 e5 e4
FACT r3 e5 e1
QUERY r8 e0 e5
STATE
DERIVE r5 e0 e2 VIA e1
DERIVE r6 e0 e3 VIA e2
DERIVE r7 e0 e4 VIA e3
DERIVE r8 e0 e5 VIA e4
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
EDGE e2 e5
EDGE e3 e0
EDGE e3 e4
EDGE e5 e3
QUERY REACH e0 e4
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
EDGE e2 e5
EDGE e3 e0
EDGE e3 e4
EDGE e5 e3
QUERY REACH e0 e4
STATE
PATH e4
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
EDGE e2 e5
EDGE e3 e0
EDGE e3 e4
EDGE e5 e3
QUERY REACH e0 e4
STATE
PATH e0 e1 e2 e3 e4
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
HYP h5 : p0 -> p4
HYP h6 : p1 -> p0
HYP h7 : p1 -> p4
HYP h8 : p3 -> p5
HYP h9 : p4 -> p2
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
HYP h5 : p0 -> p4
HYP h6 : p1 -> p0
HYP h7 : p1 -> p4
HYP h8 : p3 -> p5
HYP h9 : p4 -> p2
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
HYP h5 : p0 -> p4
HYP h6 : p1 -> p0
HYP h7 : p1 -> p4
HYP h8 : p3 -> p5
HYP h9 : p4 -> p2
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
FACT r0 e3 e7
FACT r3 e3 e1
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
FACT r0 e3 e7
FACT r3 e3 e1
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
FACT r0 e3 e7
FACT r3 e3 e1
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
