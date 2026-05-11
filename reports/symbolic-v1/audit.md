# Dataset Audit

- Data dir: `data/symbolic-v1`
- Status: `pass`
- Errors: `0`
- Warnings: `0`

## JSONL Summary

### train

- Examples: `1629`
- Problems: `120`
- Families: `{'graph_reachability': 611, 'implication_chains': 614, 'relation_composition': 404}`
- Modes: `{'complete': 463, 'improve': 463, 'repair': 463, 'verify': 240}`
- Verify targets: `{'INVALID BAD_EDGE': 28, 'INVALID BAD_FACT': 40, 'INVALID BAD_PATH_END': 12, 'INVALID BAD_PREMISE': 34, 'INVALID UNKNOWN_HYP': 6, 'VALID': 120}`

### test

- Examples: `504`
- Problems: `36`
- Families: `{'graph_reachability': 183, 'implication_chains': 189, 'relation_composition': 132}`
- Modes: `{'complete': 144, 'improve': 144, 'repair': 144, 'verify': 72}`
- Verify targets: `{'INVALID BAD_EDGE': 9, 'INVALID BAD_FACT': 12, 'INVALID BAD_PATH_END': 3, 'INVALID BAD_PREMISE': 9, 'INVALID UNKNOWN_HYP': 3, 'VALID': 36}`

### ood

- Examples: `891`
- Problems: `36`
- Families: `{'graph_reachability': 330, 'implication_chains': 315, 'relation_composition': 246}`
- Modes: `{'complete': 273, 'improve': 273, 'repair': 273, 'verify': 72}`
- Verify targets: `{'INVALID BAD_EDGE': 12, 'INVALID BAD_FACT': 12, 'INVALID BAD_PREMISE': 11, 'INVALID UNKNOWN_HYP': 1, 'VALID': 36}`

## Difficulty Summary

### graph_reachability

- `extra_edges`: `{'min': 1.0, 'max': 9.0, 'mean': 3.8656583629893237, 'unique': [1, 2, 3, 4, 5, 6, 8, 9]}`
- `num_nodes`: `{'min': 5.0, 'max': 13.0, 'mean': 8.259786476868328, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13]}`
- `path_length`: `{'min': 2.0, 'max': 8.0, 'mean': 4.800711743772242, 'unique': [2, 3, 4, 5, 6, 7, 8]}`
- `require_shortest`: `{True: 1124}`

### implication_chains

- `distractor_hyps`: `{'min': 1.0, 'max': 9.0, 'mean': 3.940071556350626, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9]}`
- `num_props`: `{'min': 5.0, 'max': 13.0, 'mean': 7.979427549194991, 'unique': [5, 6, 7, 8, 9, 10, 11, 13]}`
- `proof_length`: `{'min': 3.0, 'max': 9.0, 'mean': 5.710196779964222, 'unique': [3, 4, 5, 6, 7, 8, 9]}`

### relation_composition

- `composition_depth`: `{'min': 2.0, 'max': 8.0, 'mean': 5.10997442455243, 'unique': [2, 3, 4, 5, 6, 7, 8]}`
- `distractor_facts`: `{'min': 1.0, 'max': 9.0, 'mean': 4.381074168797954, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9]}`
- `num_entities`: `{'min': 5.0, 'max': 13.0, 'mean': 8.423273657289002, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13]}`

## TRM Array Summary

### train

- Inputs shape: `[1629, 257]`
- Labels shape: `[1629, 257]`
- Seq len: `257`
- Vocab size: `97`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1629`

### test

- Inputs shape: `[504, 257]`
- Labels shape: `[504, 257]`
- Seq len: `257`
- Vocab size: `97`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `504`

### ood

- Inputs shape: `[891, 257]`
- Labels shape: `[891, 257]`
- Seq len: `257`
- Vocab size: `97`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `891`

## Samples

### ood/graph_reachability/complete

- ID: `ood:graph_reachability:0:complete:0`

Source:

```text
MODE complete
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e10 e2
EDGE e2 e3
EDGE e3 e4
EDGE e4 e5
EDGE e5 e3
EDGE e5 e6
EDGE e7 e10
EDGE e9 e1
QUERY REACH e0 e6
STATE
EMPTY
```

Target:

```text
PATH e0 e1 e2 e3 e4 e5 e6
```

### ood/graph_reachability/improve

- ID: `ood:graph_reachability:0:improve:0`

Source:

```text
MODE improve
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e10 e2
EDGE e2 e3
EDGE e3 e4
EDGE e4 e5
EDGE e5 e3
EDGE e5 e6
EDGE e7 e10
EDGE e9 e1
QUERY REACH e0 e6
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
EDGE e1 e2
EDGE e10 e2
EDGE e2 e3
EDGE e3 e4
EDGE e4 e5
EDGE e5 e3
EDGE e5 e6
EDGE e7 e10
EDGE e9 e1
QUERY REACH e0 e6
STATE
PATH e6
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
EDGE e1 e2
EDGE e10 e2
EDGE e2 e3
EDGE e3 e4
EDGE e4 e5
EDGE e5 e3
EDGE e5 e6
EDGE e7 e10
EDGE e9 e1
QUERY REACH e0 e6
STATE
PATH e0 e1 e2 e3 e4 e5 e6
```

Target:

```text
VALID
```

### ood/implication_chains/complete

- ID: `ood:implication_chains:12:complete:0`

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
HYP h8 : p0 -> p4
HYP h9 : p2 -> p0
HYP h10 : p6 -> p4
HYP h11 : p7 -> p1
HYP h12 : p7 -> p9
HYP h13 : p8 -> p6
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

- ID: `ood:implication_chains:12:improve:0`

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
HYP h8 : p0 -> p4
HYP h9 : p2 -> p0
HYP h10 : p6 -> p4
HYP h11 : p7 -> p1
HYP h12 : p7 -> p9
HYP h13 : p8 -> p6
GOAL p7
STATE
EMPTY
```

Target:

```text
DERIVE p0 BY h0
```

### ood/implication_chains/repair

- ID: `ood:implication_chains:12:repair:1`

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
HYP h8 : p0 -> p4
HYP h9 : p2 -> p0
HYP h10 : p6 -> p4
HYP h11 : p7 -> p1
HYP h12 : p7 -> p9
HYP h13 : p8 -> p6
GOAL p7
STATE
DERIVE p0 BY h999
```

Target:

```text
DERIVE p0 BY h0
```

### ood/implication_chains/verify

- ID: `ood:implication_chains:12:verify:valid`

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
HYP h8 : p0 -> p4
HYP h9 : p2 -> p0
HYP h10 : p6 -> p4
HYP h11 : p7 -> p1
HYP h12 : p7 -> p9
HYP h13 : p8 -> p6
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

- ID: `ood:relation_composition:24:complete:0`

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
FACT r0 e0 e6
FACT r0 e11 e8
FACT r4 e0 e6
FACT r5 e0 e1
FACT r6 e9 e7
FACT r6 e11 e9
FACT r7 e3 e6
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

- ID: `ood:relation_composition:24:improve:0`

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
FACT r0 e0 e6
FACT r0 e11 e8
FACT r4 e0 e6
FACT r5 e0 e1
FACT r6 e9 e7
FACT r6 e11 e9
FACT r7 e3 e6
QUERY r14 e0 e8
STATE
EMPTY
```

Target:

```text
DERIVE r8 e0 e2 VIA e1
```

### ood/relation_composition/repair

- ID: `ood:relation_composition:24:repair:1`

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
FACT r0 e0 e6
FACT r0 e11 e8
FACT r4 e0 e6
FACT r5 e0 e1
FACT r6 e9 e7
FACT r6 e11 e9
FACT r7 e3 e6
QUERY r14 e0 e8
STATE
DERIVE r8 e0 e2 VIA e0
```

Target:

```text
DERIVE r8 e0 e2 VIA e1
```

### ood/relation_composition/verify

- ID: `ood:relation_composition:24:verify:valid`

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
FACT r0 e0 e6
FACT r0 e11 e8
FACT r4 e0 e6
FACT r5 e0 e1
FACT r6 e9 e7
FACT r6 e11 e9
FACT r7 e3 e6
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
EDGE e1 e5
EDGE e2 e3
EDGE e2 e7
EDGE e3 e4
EDGE e5 e0
EDGE e6 e0
EDGE e7 e3
QUERY REACH e0 e4
STATE
EMPTY
```

Target:

```text
PATH e0 e1 e2 e3 e4
```

### test/graph_reachability/improve

- ID: `test:graph_reachability:0:improve:0`

Source:

```text
MODE improve
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e1 e5
EDGE e2 e3
EDGE e2 e7
EDGE e3 e4
EDGE e5 e0
EDGE e6 e0
EDGE e7 e3
QUERY REACH e0 e4
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
EDGE e1 e5
EDGE e2 e3
EDGE e2 e7
EDGE e3 e4
EDGE e5 e0
EDGE e6 e0
EDGE e7 e3
QUERY REACH e0 e4
STATE
PATH e4
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
EDGE e1 e5
EDGE e2 e3
EDGE e2 e7
EDGE e3 e4
EDGE e5 e0
EDGE e6 e0
EDGE e7 e3
QUERY REACH e0 e4
STATE
PATH e0 e1 e2 e3 e4
```

Target:

```text
VALID
```

### test/implication_chains/complete

- ID: `test:implication_chains:12:complete:0`

Source:

```text
MODE complete
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p0 -> p2
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

- ID: `test:implication_chains:12:improve:0`

Source:

```text
MODE improve
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p0 -> p2
GOAL p2
STATE
EMPTY
```

Target:

```text
DERIVE p0 BY h0
```

### test/implication_chains/repair

- ID: `test:implication_chains:12:repair:1`

Source:

```text
MODE repair
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p0 -> p2
GOAL p2
STATE
DERIVE p0 BY h999
```

Target:

```text
DERIVE p0 BY h0
```

### test/implication_chains/verify

- ID: `test:implication_chains:12:verify:valid`

Source:

```text
MODE verify
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p0 -> p2
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

- ID: `test:relation_composition:24:complete:0`

Source:

```text
MODE complete
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
FACT r0 e5 e4
FACT r2 e1 e4
FACT r2 e2 e1
FACT r4 e3 e5
QUERY r8 e0 e5
STATE
EMPTY
```

Target:

```text
DERIVE r5 e0 e2 VIA e1
DERIVE r6 e0 e3 VIA e2
DERIVE r7 e0 e4 VIA e3
DERIVE r8 e0 e5 VIA e4
```

### test/relation_composition/improve

- ID: `test:relation_composition:24:improve:0`

Source:

```text
MODE improve
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
FACT r0 e5 e4
FACT r2 e1 e4
FACT r2 e2 e1
FACT r4 e3 e5
QUERY r8 e0 e5
STATE
EMPTY
```

Target:

```text
DERIVE r5 e0 e2 VIA e1
```

### test/relation_composition/repair

- ID: `test:relation_composition:24:repair:1`

Source:

```text
MODE repair
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
FACT r0 e5 e4
FACT r2 e1 e4
FACT r2 e2 e1
FACT r4 e3 e5
QUERY r8 e0 e5
STATE
DERIVE r5 e0 e2 VIA e0
```

Target:

```text
DERIVE r5 e0 e2 VIA e1
```

### test/relation_composition/verify

- ID: `test:relation_composition:24:verify:valid`

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
FACT r0 e5 e4
FACT r2 e1 e4
FACT r2 e2 e1
FACT r4 e3 e5
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

### train/graph_reachability/complete

- ID: `train:graph_reachability:0:complete:0`

Source:

```text
MODE complete
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e6 e0
EDGE e6 e4
QUERY REACH e0 e2
STATE
EMPTY
```

Target:

```text
PATH e0 e1 e2
```

### train/graph_reachability/improve

- ID: `train:graph_reachability:0:improve:0`

Source:

```text
MODE improve
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e6 e0
EDGE e6 e4
QUERY REACH e0 e2
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
EDGE e1 e2
EDGE e6 e0
EDGE e6 e4
QUERY REACH e0 e2
STATE
PATH e2
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
EDGE e1 e2
EDGE e6 e0
EDGE e6 e4
QUERY REACH e0 e2
STATE
PATH e0 e1 e2
```

Target:

```text
VALID
```

### train/implication_chains/complete

- ID: `train:implication_chains:40:complete:0`

Source:

```text
MODE complete
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p4 -> p3
GOAL p3
STATE
EMPTY
```

Target:

```text
DERIVE p0 BY h0
DERIVE p1 BY h1 FROM p0
DERIVE p2 BY h2 FROM p1
DERIVE p3 BY h3 FROM p2
```

### train/implication_chains/improve

- ID: `train:implication_chains:40:improve:0`

Source:

```text
MODE improve
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p4 -> p3
GOAL p3
STATE
EMPTY
```

Target:

```text
DERIVE p0 BY h0
```

### train/implication_chains/repair

- ID: `train:implication_chains:40:repair:1`

Source:

```text
MODE repair
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p4 -> p3
GOAL p3
STATE
DERIVE p0 BY h999
```

Target:

```text
DERIVE p0 BY h0
```

### train/implication_chains/verify

- ID: `train:implication_chains:40:verify:valid`

Source:

```text
MODE verify
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p4 -> p3
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

### train/relation_composition/complete

- ID: `train:relation_composition:80:complete:0`

Source:

```text
MODE complete
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
FACT r0 e4 e0
FACT r1 e2 e5
FACT r2 e3 e1
FACT r3 e5 e6
QUERY r8 e0 e5
STATE
EMPTY
```

Target:

```text
DERIVE r5 e0 e2 VIA e1
DERIVE r6 e0 e3 VIA e2
DERIVE r7 e0 e4 VIA e3
DERIVE r8 e0 e5 VIA e4
```

### train/relation_composition/improve

- ID: `train:relation_composition:80:improve:0`

Source:

```text
MODE improve
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
FACT r0 e4 e0
FACT r1 e2 e5
FACT r2 e3 e1
FACT r3 e5 e6
QUERY r8 e0 e5
STATE
EMPTY
```

Target:

```text
DERIVE r5 e0 e2 VIA e1
```

### train/relation_composition/repair

- ID: `train:relation_composition:80:repair:1`

Source:

```text
MODE repair
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
FACT r0 e4 e0
FACT r1 e2 e5
FACT r2 e3 e1
FACT r3 e5 e6
QUERY r8 e0 e5
STATE
DERIVE r5 e0 e2 VIA e0
```

Target:

```text
DERIVE r5 e0 e2 VIA e1
```

### train/relation_composition/verify

- ID: `train:relation_composition:80:verify:valid`

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
FACT r0 e4 e0
FACT r1 e2 e5
FACT r2 e3 e1
FACT r3 e5 e6
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
