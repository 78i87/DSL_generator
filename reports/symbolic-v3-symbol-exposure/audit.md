# Dataset Audit

- Data dir: `data/symbolic-v3-symbol-exposure`
- Status: `pass`
- Errors: `0`
- Warnings: `0`

## JSONL Summary

### train

- Examples: `8220`
- Problems: `504`
- Families: `{'graph_reachability': 3144, 'implication_chains': 2745, 'relation_composition': 2331}`
- Modes: `{'complete': 3124, 'improve': 2188, 'repair': 2188, 'verify': 720}`
- Verify targets: `{'INVALID BAD_EDGE': 99, 'INVALID BAD_FACT': 120, 'INVALID BAD_PATH_END': 21, 'INVALID BAD_PREMISE': 99, 'INVALID UNKNOWN_HYP': 21, 'VALID': 360}`

### test

- Examples: `1008`
- Problems: `54`
- Families: `{'graph_reachability': 390, 'implication_chains': 336, 'relation_composition': 282}`
- Modes: `{'complete': 300, 'improve': 300, 'repair': 300, 'verify': 108}`
- Verify targets: `{'INVALID BAD_EDGE': 13, 'INVALID BAD_FACT': 18, 'INVALID BAD_PATH_END': 5, 'INVALID BAD_PREMISE': 15, 'INVALID UNKNOWN_HYP': 3, 'VALID': 54}`

### ood

- Examples: `1566`
- Problems: `54`
- Families: `{'graph_reachability': 576, 'implication_chains': 522, 'relation_composition': 468}`
- Modes: `{'complete': 486, 'improve': 486, 'repair': 486, 'verify': 108}`
- Verify targets: `{'INVALID BAD_EDGE': 15, 'INVALID BAD_FACT': 18, 'INVALID BAD_PATH_END': 3, 'INVALID BAD_PREMISE': 18, 'VALID': 54}`

## Difficulty Summary

### graph_reachability

- `extra_edges`: `{'min': 1.0, 'max': 10.0, 'mean': 6.315328467153285, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `num_nodes`: `{'min': 5.0, 'max': 16.0, 'mean': 11.083698296836983, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `path_length`: `{'min': 2.0, 'max': 10.0, 'mean': 6.7153284671532845, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `require_shortest`: `{True: 4110}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.3664233576642335, 'unique': [0, 3, 6]}`

### implication_chains

- `distractor_hyps`: `{'min': 1.0, 'max': 11.0, 'mean': 6.37496530668887, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}`
- `num_props`: `{'min': 5.0, 'max': 17.0, 'mean': 11.044407438245907, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]}`
- `proof_length`: `{'min': 2.0, 'max': 10.0, 'mean': 6.748542880932556, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.3788509575353871, 'unique': [0, 3, 6]}`

### relation_composition

- `composition_depth`: `{'min': 2.0, 'max': 10.0, 'mean': 6.826355079519637, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_facts`: `{'min': 1.0, 'max': 10.0, 'mean': 6.372930866601752, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `num_entities`: `{'min': 5.0, 'max': 16.0, 'mean': 11.200908795845505, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.4021421616358325, 'unique': [0, 3, 6]}`

## TRM Array Summary

### train

- Inputs shape: `[8220, 302]`
- Labels shape: `[8220, 302]`
- Seq len: `302`
- Vocab size: `117`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `8220`

### test

- Inputs shape: `[1008, 302]`
- Labels shape: `[1008, 302]`
- Seq len: `302`
- Vocab size: `117`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1008`

### ood

- Inputs shape: `[1566, 302]`
- Labels shape: `[1566, 302]`
- Seq len: `302`
- Vocab size: `117`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1566`

## Samples

### ood/graph_reachability/complete

- ID: `ood:graph_reachability:0:complete:0`

Source:

```text
MODE complete
PROBLEM
EDGE e0 e1
EDGE e1 e11
EDGE e1 e2
EDGE e10 e7
EDGE e2 e3
EDGE e3 e4
EDGE e4 e5
EDGE e5 e11
EDGE e5 e6
EDGE e6 e2
EDGE e6 e7
EDGE e7 e10
EDGE e7 e5
EDGE e7 e8
EDGE e8 e2
QUERY REACH e0 e8
STATE
EMPTY
```

Target:

```text
PATH e0 e1 e2 e3 e4 e5 e6 e7 e8
```

### ood/graph_reachability/improve

- ID: `ood:graph_reachability:0:improve:0`

Source:

```text
MODE improve
PROBLEM
EDGE e0 e1
EDGE e1 e11
EDGE e1 e2
EDGE e10 e7
EDGE e2 e3
EDGE e3 e4
EDGE e4 e5
EDGE e5 e11
EDGE e5 e6
EDGE e6 e2
EDGE e6 e7
EDGE e7 e10
EDGE e7 e5
EDGE e7 e8
EDGE e8 e2
QUERY REACH e0 e8
STATE
EMPTY
```

Target:

```text
PATH e0
```

### ood/graph_reachability/repair

- ID: `ood:graph_reachability:0:repair:1`

Source:

```text
MODE repair
PROBLEM
EDGE e0 e1
EDGE e1 e11
EDGE e1 e2
EDGE e10 e7
EDGE e2 e3
EDGE e3 e4
EDGE e4 e5
EDGE e5 e11
EDGE e5 e6
EDGE e6 e2
EDGE e6 e7
EDGE e7 e10
EDGE e7 e5
EDGE e7 e8
EDGE e8 e2
QUERY REACH e0 e8
STATE
PATH e8
```

Target:

```text
PATH e0
```

### ood/graph_reachability/verify

- ID: `ood:graph_reachability:0:verify:valid`

Source:

```text
MODE verify
PROBLEM
EDGE e0 e1
EDGE e1 e11
EDGE e1 e2
EDGE e10 e7
EDGE e2 e3
EDGE e3 e4
EDGE e4 e5
EDGE e5 e11
EDGE e5 e6
EDGE e6 e2
EDGE e6 e7
EDGE e7 e10
EDGE e7 e5
EDGE e7 e8
EDGE e8 e2
QUERY REACH e0 e8
STATE
PATH e0 e1 e2 e3 e4 e5 e6 e7 e8
```

Target:

```text
VALID
```

### ood/implication_chains/complete

- ID: `ood:implication_chains:18:complete:0`

Source:

```text
MODE complete
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p0 -> p7
HYP h9 : p1 -> p10
HYP h10 : p2 -> p1
HYP h11 : p3 -> p5
HYP h12 : p3 -> p11
HYP h13 : p5 -> p8
HYP h14 : p6 -> p4
HYP h15 : p7 -> p8
HYP h16 : p8 -> p1
HYP h17 : p9 -> p7
HYP h18 : p10 -> p9
GOAL p7
STATE
EMPTY
```

Target:

```text
DERIVE p0 BY h0
DERIVE p1 BY h1 FROM p0
DERIVE p2 BY h2 FROM p1
DERIVE p3 BY h3 FROM p2
DERIVE p4 BY h4 FROM p3
DERIVE p5 BY h5 FROM p4
DERIVE p6 BY h6 FROM p5
DERIVE p7 BY h7 FROM p6
```

### ood/implication_chains/improve

- ID: `ood:implication_chains:18:improve:0`

Source:

```text
MODE improve
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p0 -> p7
HYP h9 : p1 -> p10
HYP h10 : p2 -> p1
HYP h11 : p3 -> p5
HYP h12 : p3 -> p11
HYP h13 : p5 -> p8
HYP h14 : p6 -> p4
HYP h15 : p7 -> p8
HYP h16 : p8 -> p1
HYP h17 : p9 -> p7
HYP h18 : p10 -> p9
GOAL p7
STATE
EMPTY
```

Target:

```text
DERIVE p0 BY h0
```

### ood/implication_chains/repair

- ID: `ood:implication_chains:18:repair:1`

Source:

```text
MODE repair
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p0 -> p7
HYP h9 : p1 -> p10
HYP h10 : p2 -> p1
HYP h11 : p3 -> p5
HYP h12 : p3 -> p11
HYP h13 : p5 -> p8
HYP h14 : p6 -> p4
HYP h15 : p7 -> p8
HYP h16 : p8 -> p1
HYP h17 : p9 -> p7
HYP h18 : p10 -> p9
GOAL p7
STATE
DERIVE p0 BY h999
```

Target:

```text
DERIVE p0 BY h0
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
HYP h8 : p0 -> p7
HYP h9 : p1 -> p10
HYP h10 : p2 -> p1
HYP h11 : p3 -> p5
HYP h12 : p3 -> p11
HYP h13 : p5 -> p8
HYP h14 : p6 -> p4
HYP h15 : p7 -> p8
HYP h16 : p8 -> p1
HYP h17 : p9 -> p7
HYP h18 : p10 -> p9
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

### ood/relation_composition/complete

- ID: `ood:relation_composition:36:complete:0`

Source:

```text
MODE complete
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
FACT r0 e3 e9
FACT r3 e2 e7
FACT r3 e4 e1
FACT r4 e2 e11
FACT r7 e2 e3
FACT r7 e5 e7
FACT r7 e6 e9
FACT r7 e8 e10
QUERY r14 e0 e8
STATE
EMPTY
```

Target:

```text
DERIVE r8 e0 e2 VIA e1
DERIVE r9 e0 e3 VIA e2
DERIVE r10 e0 e4 VIA e3
DERIVE r11 e0 e5 VIA e4
DERIVE r12 e0 e6 VIA e5
DERIVE r13 e0 e7 VIA e6
DERIVE r14 e0 e8 VIA e7
```

### ood/relation_composition/improve

- ID: `ood:relation_composition:36:improve:0`

Source:

```text
MODE improve
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
FACT r0 e3 e9
FACT r3 e2 e7
FACT r3 e4 e1
FACT r4 e2 e11
FACT r7 e2 e3
FACT r7 e5 e7
FACT r7 e6 e9
FACT r7 e8 e10
QUERY r14 e0 e8
STATE
EMPTY
```

Target:

```text
DERIVE r8 e0 e2 VIA e1
```

### ood/relation_composition/repair

- ID: `ood:relation_composition:36:repair:1`

Source:

```text
MODE repair
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
FACT r0 e3 e9
FACT r3 e2 e7
FACT r3 e4 e1
FACT r4 e2 e11
FACT r7 e2 e3
FACT r7 e5 e7
FACT r7 e6 e9
FACT r7 e8 e10
QUERY r14 e0 e8
STATE
DERIVE r8 e0 e2 VIA e0
```

Target:

```text
DERIVE r8 e0 e2 VIA e1
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
FACT r0 e3 e9
FACT r3 e2 e7
FACT r3 e4 e1
FACT r4 e2 e11
FACT r7 e2 e3
FACT r7 e5 e7
FACT r7 e6 e9
FACT r7 e8 e10
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

### test/graph_reachability/complete

- ID: `test:graph_reachability:0:complete:0`

Source:

```text
MODE complete
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e2 e3
EDGE e3 e6
EDGE e5 e8
QUERY REACH e0 e3
STATE
EMPTY
```

Target:

```text
PATH e0 e1 e2 e3
```

### test/graph_reachability/improve

- ID: `test:graph_reachability:0:improve:0`

Source:

```text
MODE improve
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e2 e3
EDGE e3 e6
EDGE e5 e8
QUERY REACH e0 e3
STATE
EMPTY
```

Target:

```text
PATH e0
```

### test/graph_reachability/repair

- ID: `test:graph_reachability:0:repair:1`

Source:

```text
MODE repair
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e2 e3
EDGE e3 e6
EDGE e5 e8
QUERY REACH e0 e3
STATE
PATH e3
```

Target:

```text
PATH e0
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
EDGE e3 e6
EDGE e5 e8
QUERY REACH e0 e3
STATE
PATH e0 e1 e2 e3
```

Target:

```text
VALID
```

### test/implication_chains/complete

- ID: `test:implication_chains:18:complete:0`

Source:

```text
MODE complete
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p0 -> p7
HYP h4 : p2 -> p5
HYP h5 : p4 -> p8
HYP h6 : p5 -> p2
HYP h7 : p7 -> p5
GOAL p2
STATE
EMPTY
```

Target:

```text
DERIVE p0 BY h0
DERIVE p1 BY h1 FROM p0
DERIVE p2 BY h2 FROM p1
```

### test/implication_chains/improve

- ID: `test:implication_chains:18:improve:0`

Source:

```text
MODE improve
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p0 -> p7
HYP h4 : p2 -> p5
HYP h5 : p4 -> p8
HYP h6 : p5 -> p2
HYP h7 : p7 -> p5
GOAL p2
STATE
EMPTY
```

Target:

```text
DERIVE p0 BY h0
```

### test/implication_chains/repair

- ID: `test:implication_chains:18:repair:1`

Source:

```text
MODE repair
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p0 -> p7
HYP h4 : p2 -> p5
HYP h5 : p4 -> p8
HYP h6 : p5 -> p2
HYP h7 : p7 -> p5
GOAL p2
STATE
DERIVE p0 BY h999
```

Target:

```text
DERIVE p0 BY h0
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
HYP h3 : p0 -> p7
HYP h4 : p2 -> p5
HYP h5 : p4 -> p8
HYP h6 : p5 -> p2
HYP h7 : p7 -> p5
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

### test/relation_composition/complete

- ID: `test:relation_composition:36:complete:0`

Source:

```text
MODE complete
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r1 e0 e1
FACT r2 e0 e5
QUERY r4 e0 e3
STATE
EMPTY
```

Target:

```text
DERIVE r3 e0 e2 VIA e1
DERIVE r4 e0 e3 VIA e2
```

### test/relation_composition/improve

- ID: `test:relation_composition:36:improve:0`

Source:

```text
MODE improve
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r1 e0 e1
FACT r2 e0 e5
QUERY r4 e0 e3
STATE
EMPTY
```

Target:

```text
DERIVE r3 e0 e2 VIA e1
```

### test/relation_composition/repair

- ID: `test:relation_composition:36:repair:1`

Source:

```text
MODE repair
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r1 e0 e1
FACT r2 e0 e5
QUERY r4 e0 e3
STATE
DERIVE r3 e0 e2 VIA e0
```

Target:

```text
DERIVE r3 e0 e2 VIA e1
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
FACT r1 e0 e1
FACT r2 e0 e5
QUERY r4 e0 e3
STATE
DERIVE r3 e0 e2 VIA e1
DERIVE r4 e0 e3 VIA e2
```

Target:

```text
VALID
```

### train/graph_reachability/complete

- ID: `train:graph_reachability:0:complete:0`

Source:

```text
MODE complete
PROBLEM
EDGE e0 e1
EDGE e1 e0
EDGE e1 e2
EDGE e2 e0
EDGE e2 e1
EDGE e2 e3
EDGE e3 e0
EDGE e3 e2
EDGE e3 e4
EDGE e4 e5
QUERY REACH e0 e5
STATE
EMPTY
```

Target:

```text
PATH e0 e1 e2 e3 e4 e5
```

### train/graph_reachability/improve

- ID: `train:graph_reachability:0:improve:0`

Source:

```text
MODE improve
PROBLEM
EDGE e0 e1
EDGE e1 e0
EDGE e1 e2
EDGE e2 e0
EDGE e2 e1
EDGE e2 e3
EDGE e3 e0
EDGE e3 e2
EDGE e3 e4
EDGE e4 e5
QUERY REACH e0 e5
STATE
EMPTY
```

Target:

```text
PATH e0
```

### train/graph_reachability/repair

- ID: `train:graph_reachability:0:repair:1`

Source:

```text
MODE repair
PROBLEM
EDGE e0 e1
EDGE e1 e0
EDGE e1 e2
EDGE e2 e0
EDGE e2 e1
EDGE e2 e3
EDGE e3 e0
EDGE e3 e2
EDGE e3 e4
EDGE e4 e5
QUERY REACH e0 e5
STATE
PATH e5
```

Target:

```text
PATH e0
```

### train/graph_reachability/verify

- ID: `train:graph_reachability:0:verify:valid`

Source:

```text
MODE verify
PROBLEM
EDGE e0 e1
EDGE e1 e0
EDGE e1 e2
EDGE e2 e0
EDGE e2 e1
EDGE e2 e3
EDGE e3 e0
EDGE e3 e2
EDGE e3 e4
EDGE e4 e5
QUERY REACH e0 e5
STATE
PATH e0 e1 e2 e3 e4 e5
```

Target:

```text
VALID
```

### train/implication_chains/complete

- ID: `train:implication_chains:168:complete:0`

Source:

```text
MODE complete
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p0 -> p4
HYP h6 : p3 -> p8
GOAL p4
STATE
EMPTY
```

Target:

```text
DERIVE p0 BY h0
DERIVE p1 BY h1 FROM p0
DERIVE p2 BY h2 FROM p1
DERIVE p3 BY h3 FROM p2
DERIVE p4 BY h4 FROM p3
```

### train/implication_chains/improve

- ID: `train:implication_chains:168:improve:0`

Source:

```text
MODE improve
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p0 -> p4
HYP h6 : p3 -> p8
GOAL p4
STATE
EMPTY
```

Target:

```text
DERIVE p0 BY h0
```

### train/implication_chains/repair

- ID: `train:implication_chains:168:repair:1`

Source:

```text
MODE repair
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p0 -> p4
HYP h6 : p3 -> p8
GOAL p4
STATE
DERIVE p0 BY h999
```

Target:

```text
DERIVE p0 BY h0
```

### train/implication_chains/verify

- ID: `train:implication_chains:168:verify:valid`

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
HYP h6 : p3 -> p8
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

### train/relation_composition/complete

- ID: `train:relation_composition:336:complete:0`

Source:

```text
MODE complete
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e6 e0
FACT r0 e7 e0
FACT r1 e6 e4
QUERY r4 e0 e3
STATE
EMPTY
```

Target:

```text
DERIVE r3 e0 e2 VIA e1
DERIVE r4 e0 e3 VIA e2
```

### train/relation_composition/improve

- ID: `train:relation_composition:336:improve:0`

Source:

```text
MODE improve
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e6 e0
FACT r0 e7 e0
FACT r1 e6 e4
QUERY r4 e0 e3
STATE
EMPTY
```

Target:

```text
DERIVE r3 e0 e2 VIA e1
```

### train/relation_composition/repair

- ID: `train:relation_composition:336:repair:1`

Source:

```text
MODE repair
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e6 e0
FACT r0 e7 e0
FACT r1 e6 e4
QUERY r4 e0 e3
STATE
DERIVE r3 e0 e2 VIA e0
```

Target:

```text
DERIVE r3 e0 e2 VIA e1
```

### train/relation_composition/verify

- ID: `train:relation_composition:336:verify:valid`

Source:

```text
MODE verify
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e6 e0
FACT r0 e7 e0
FACT r1 e6 e4
QUERY r4 e0 e3
STATE
DERIVE r3 e0 e2 VIA e1
DERIVE r4 e0 e3 VIA e2
```

Target:

```text
VALID
```
