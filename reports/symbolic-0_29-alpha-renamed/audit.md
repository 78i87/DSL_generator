# Dataset Audit

- Data dir: `data/symbolic-0_29-alpha-renamed`
- Status: `pass`
- Errors: `0`
- Warnings: `0`

## JSONL Summary

### train

- Examples: `19827`
- Problems: `1776`
- Families: `{'graph_reachability': 4154, 'implication_chains': 3672, 'relation_composition': 4018, 'term_rewriting': 3819, 'tree_ancestry': 4164}`
- Modes: `{'action': 8795, 'repair_action': 9304, 'verify': 1728}`
- Verify targets: `{'INVALID BAD_EDGE': 143, 'INVALID BAD_FACT': 144, 'INVALID BAD_LINEAGE_END': 1, 'INVALID BAD_NOT_GOAL': 31, 'INVALID BAD_NO_MATCH': 74, 'INVALID BAD_PARENT': 143, 'INVALID BAD_PATH': 77, 'INVALID BAD_PATH_END': 1, 'INVALID BAD_PREMATURE_HALT': 42, 'INVALID BAD_PREMISE': 115, 'INVALID BAD_RESULT': 64, 'INVALID UNKNOWN_HYP': 29, 'VALID': 864}`

### test

- Examples: `1202`
- Problems: `90`
- Families: `{'graph_reachability': 268, 'implication_chains': 234, 'relation_composition': 194, 'term_rewriting': 230, 'tree_ancestry': 276}`
- Modes: `{'action': 511, 'repair_action': 511, 'verify': 180}`
- Verify targets: `{'INVALID BAD_EDGE': 18, 'INVALID BAD_FACT': 18, 'INVALID BAD_NOT_GOAL': 1, 'INVALID BAD_NO_MATCH': 4, 'INVALID BAD_PARENT': 18, 'INVALID BAD_PATH': 3, 'INVALID BAD_PREMATURE_HALT': 5, 'INVALID BAD_PREMISE': 11, 'INVALID BAD_RESULT': 5, 'INVALID UNKNOWN_HYP': 7, 'VALID': 90}`

### ood

- Examples: `1856`
- Problems: `90`
- Families: `{'graph_reachability': 396, 'implication_chains': 360, 'relation_composition': 324, 'term_rewriting': 380, 'tree_ancestry': 396}`
- Modes: `{'action': 838, 'repair_action': 838, 'verify': 180}`
- Verify targets: `{'INVALID BAD_EDGE': 18, 'INVALID BAD_FACT': 18, 'INVALID BAD_NOT_GOAL': 1, 'INVALID BAD_NO_MATCH': 6, 'INVALID BAD_PARENT': 18, 'INVALID BAD_PATH': 6, 'INVALID BAD_PREMATURE_HALT': 2, 'INVALID BAD_PREMISE': 14, 'INVALID BAD_RESULT': 3, 'INVALID UNKNOWN_HYP': 4, 'VALID': 90}`

## Difficulty Summary

### graph_reachability

- `extra_edges`: `{'min': 1.0, 'max': 16.0, 'mean': 8.58530510585305, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `num_nodes`: `{'min': 5.0, 'max': 19.0, 'mean': 12.590909090909092, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `path_length`: `{'min': 2.0, 'max': 10.0, 'mean': 7.455790784557908, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `require_shortest`: `{True: 4818}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.3349937733499377, 'unique': [0, 2, 3, 4, 6]}`

### implication_chains

- `distractor_hyps`: `{'min': 1.0, 'max': 12.0, 'mean': 7.533052039381153, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}`
- `num_props`: `{'min': 5.0, 'max': 19.0, 'mean': 12.290201593999063, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `proof_length`: `{'min': 2.0, 'max': 10.0, 'mean': 7.500234411626817, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.3389592123769338, 'unique': [0, 2, 3, 4, 6]}`

### relation_composition

- `composition_depth`: `{'min': 2.0, 'max': 10.0, 'mean': 7.699294532627866, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_facts`: `{'min': 1.0, 'max': 16.0, 'mean': 9.079585537918872, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `num_entities`: `{'min': 5.0, 'max': 19.0, 'mean': 13.000661375661375, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.3333333333333333, 'unique': [0, 2, 3, 4, 6]}`

### term_rewriting

- `action_format`: `{'rule': 4429}`
- `binary_rules`: `{'min': 1.0, 'max': 10.0, 'mean': 5.7724091216979, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_rules`: `{'min': 0.0, 'max': 16.0, 'mean': 8.513208399187176, 'unique': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `query_kind`: `{'goal': 2725, 'normal_form': 1704}`
- `repeated_subterms`: `{False: 3528, True: 901}`
- `rewrite_steps`: `{'min': 2.0, 'max': 10.0, 'mean': 7.553172273650937, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.4170241589523596, 'unique': [0, 2, 3, 4, 6]}`
- `term_depth`: `{'min': 1.0, 'max': 9.0, 'mean': 4.096410024836306, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9]}`
- `variable_rules`: `{'min': 0.0, 'max': 7.0, 'mean': 2.2056897719575526, 'unique': [0, 1, 2, 3, 4, 5, 6, 7]}`

### tree_ancestry

- `branching_factor`: `{'min': 2.0, 'max': 4.0, 'mean': 2.6439205955334986, 'unique': [2, 3, 4]}`
- `depth`: `{'min': 2.0, 'max': 10.0, 'mean': 7.459884201819686, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_subtrees`: `{'min': 1.0, 'max': 16.0, 'mean': 8.485732009925558, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.3300248138957815, 'unique': [0, 2, 3, 4, 6]}`

## TRM Array Summary

### train

- Inputs shape: `[19827, 850]`
- Labels shape: `[19827, 850]`
- Seq len: `850`
- Vocab size: `304`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `19827`

### test

- Inputs shape: `[1202, 850]`
- Labels shape: `[1202, 850]`
- Seq len: `850`
- Vocab size: `304`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1202`

### ood

- Inputs shape: `[1856, 850]`
- Labels shape: `[1856, 850]`
- Seq len: `850`
- Vocab size: `304`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1856`

## Samples

### ood/graph_reachability/action

- ID: `ood:graph_reachability:0:action:0`

Source:

```text
MODE action
PROBLEM
EDGE e5 e11
EDGE e11 e3
EDGE e7 e1
EDGE e3 e5
EDGE e3 e0
EDGE e0 e1
EDGE e0 e4
EDGE e1 e9
EDGE e9 e3
EDGE e9 e8
EDGE e8 e2
EDGE e2 e6
EDGE e6 e11
QUERY REACH e5 e6
STATE
EMPTY
```

Target:

```text
APPEND e5
```

### ood/graph_reachability/repair_action

- ID: `ood:graph_reachability:0:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
EDGE e5 e11
EDGE e11 e3
EDGE e7 e1
EDGE e3 e5
EDGE e3 e0
EDGE e0 e1
EDGE e0 e4
EDGE e1 e9
EDGE e9 e3
EDGE e9 e8
EDGE e8 e2
EDGE e2 e6
EDGE e6 e11
QUERY REACH e5 e6
STATE
PATH e6
```

Target:

```text
REPLACE ROOT WITH e5
```

### ood/graph_reachability/verify

- ID: `ood:graph_reachability:0:verify:valid`

Source:

```text
MODE verify
PROBLEM
EDGE e5 e11
EDGE e11 e3
EDGE e7 e1
EDGE e3 e5
EDGE e3 e0
EDGE e0 e1
EDGE e0 e4
EDGE e1 e9
EDGE e9 e3
EDGE e9 e8
EDGE e8 e2
EDGE e2 e6
EDGE e6 e11
QUERY REACH e5 e6
STATE
PATH e5 e11 e3 e0 e1 e9 e8 e2 e6
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
HYP h15 : p0
HYP h8 : p0 -> p5
HYP h16 : p5 -> p9
HYP h12 : p9 -> p3
HYP h2 : p3 -> p6
HYP h7 : p6 -> p2
HYP h5 : p2 -> p7
HYP h11 : p7 -> p4
HYP h17 : p0 -> p9
HYP h1 : p5 -> p6
HYP h13 : p5 -> p10
HYP h0 : p7 -> p2
HYP h3 : p7 -> p8
HYP h999 : p4 -> p8
HYP h14 : p1 -> p0
HYP h4 : p1 -> p6
HYP h9 : p10 -> p6
HYP h6 : p8 -> p3
GOAL p4
STATE
EMPTY
```

Target:

```text
APPLY h15
```

### ood/implication_chains/repair_action

- ID: `ood:implication_chains:18:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
HYP h15 : p0
HYP h8 : p0 -> p5
HYP h16 : p5 -> p9
HYP h12 : p9 -> p3
HYP h2 : p3 -> p6
HYP h7 : p6 -> p2
HYP h5 : p2 -> p7
HYP h11 : p7 -> p4
HYP h17 : p0 -> p9
HYP h1 : p5 -> p6
HYP h13 : p5 -> p10
HYP h0 : p7 -> p2
HYP h3 : p7 -> p8
HYP h999 : p4 -> p8
HYP h14 : p1 -> p0
HYP h4 : p1 -> p6
HYP h9 : p10 -> p6
HYP h6 : p8 -> p3
GOAL p4
STATE
DERIVE p0 BY h10
```

Target:

```text
REPLACE FIRST HYP h15
```

### ood/implication_chains/verify

- ID: `ood:implication_chains:18:verify:valid`

Source:

```text
MODE verify
PROBLEM
HYP h15 : p0
HYP h8 : p0 -> p5
HYP h16 : p5 -> p9
HYP h12 : p9 -> p3
HYP h2 : p3 -> p6
HYP h7 : p6 -> p2
HYP h5 : p2 -> p7
HYP h11 : p7 -> p4
HYP h17 : p0 -> p9
HYP h1 : p5 -> p6
HYP h13 : p5 -> p10
HYP h0 : p7 -> p2
HYP h3 : p7 -> p8
HYP h999 : p4 -> p8
HYP h14 : p1 -> p0
HYP h4 : p1 -> p6
HYP h9 : p10 -> p6
HYP h6 : p8 -> p3
GOAL p4
STATE
DERIVE p0 BY h15
DERIVE p5 BY h8 FROM p0
DERIVE p9 BY h16 FROM p5
DERIVE p3 BY h12 FROM p9
DERIVE p6 BY h2 FROM p3
DERIVE p2 BY h7 FROM p6
DERIVE p7 BY h5 FROM p2
DERIVE p4 BY h11 FROM p7
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
FACT r5 e7 e5
FACT r11 e5 e9
FACT r4 e9 e0
FACT r3 e0 e11
FACT r10 e11 e6
FACT r0 e6 e8
FACT r6 e8 e10
FACT r9 e10 e3
RULE r14 = r5 ; r11
RULE r2 = r14 ; r4
RULE r7 = r2 ; r3
RULE r12 = r7 ; r10
RULE r13 = r12 ; r0
RULE r8 = r13 ; r6
RULE r1 = r8 ; r9
FACT r5 e7 e4
FACT r4 e6 e3
FACT r10 e3 e2
FACT r0 e5 e6
FACT r0 e11 e1
FACT r6 e3 e0
QUERY r1 e7 e3
STATE
EMPTY
```

Target:

```text
FOLLOW e7 e9 VIA e5
```

### ood/relation_composition/repair_action

- ID: `ood:relation_composition:36:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
FACT r5 e7 e5
FACT r11 e5 e9
FACT r4 e9 e0
FACT r3 e0 e11
FACT r10 e11 e6
FACT r0 e6 e8
FACT r6 e8 e10
FACT r9 e10 e3
RULE r14 = r5 ; r11
RULE r2 = r14 ; r4
RULE r7 = r2 ; r3
RULE r12 = r7 ; r10
RULE r13 = r12 ; r0
RULE r8 = r13 ; r6
RULE r1 = r8 ; r9
FACT r5 e7 e4
FACT r4 e6 e3
FACT r10 e3 e2
FACT r0 e5 e6
FACT r0 e11 e1
FACT r6 e3 e0
QUERY r1 e7 e3
STATE
DERIVE r14 e7 e9 VIA e7
```

Target:

```text
REPLACE FIRST VIA e5
```

### ood/relation_composition/verify

- ID: `ood:relation_composition:36:verify:valid`

Source:

```text
MODE verify
PROBLEM
FACT r5 e7 e5
FACT r11 e5 e9
FACT r4 e9 e0
FACT r3 e0 e11
FACT r10 e11 e6
FACT r0 e6 e8
FACT r6 e8 e10
FACT r9 e10 e3
RULE r14 = r5 ; r11
RULE r2 = r14 ; r4
RULE r7 = r2 ; r3
RULE r12 = r7 ; r10
RULE r13 = r12 ; r0
RULE r8 = r13 ; r6
RULE r1 = r8 ; r9
FACT r5 e7 e4
FACT r4 e6 e3
FACT r10 e3 e2
FACT r0 e5 e6
FACT r0 e11 e1
FACT r6 e3 e0
QUERY r1 e7 e3
STATE
DERIVE r14 e7 e9 VIA e5
DERIVE r2 e7 e0 VIA e9
DERIVE r7 e7 e11 VIA e0
DERIVE r12 e7 e6 VIA e11
DERIVE r13 e7 e8 VIA e6
DERIVE r8 e7 e10 VIA e8
DERIVE r1 e7 e3 VIA e10
```

Target:

```text
VALID
```

### ood/term_rewriting/action

- ID: `ood:term_rewriting:72:action:0`

Source:

```text
MODE action
PROBLEM
RULE r6 : B g8 B g100 B g3 e72 e3 e1 e0 -> U f60 B g100 B g3 e72 e3 e1
RULE r13 : U f60 v1 -> U f105 v1
RULE r4 : U f105 B g100 B g3 e72 e3 e1 -> B g0 B g100 B g3 e72 e3 e1 e0
RULE r14 : B g0 B g100 B g3 e72 e3 e1 e0 -> U f101 B g100 B g3 e72 e3 e1
RULE r11 : U f101 v1 -> U f124 v1
RULE r8 : U f124 B g100 B g3 e72 e3 e1 -> B g63 B g100 B g3 e72 e3 e1 e0
RULE r12 : B g63 B g100 B g3 e72 e3 e1 e0 -> B g107 B g100 B g3 e72 e3 e1 e0
RULE r5 : B g107 B g100 B g3 e72 e3 e1 e0 -> U f102 B g100 B g3 e72 e3 e1
RULE r7 : B g62 v1 v0 -> B g6 v1 v0
RULE r3 : U f108 v1 -> U f121 v1
RULE r9 : U f61 v1 -> U f122 v1
RULE r2 : U f103 v1 -> U f125 v1
RULE r10 : U f1 v1 -> U f2 v1
RULE r16 : U f5 v1 -> U f8 v1
RULE r0 : B g120 v1 v0 -> B g31 v1 v0
RULE r15 : B g30 v1 v0 -> B g127 v1 v0
RULE r1 : U f128 v1 -> U f104 v1
START B g106 U f123 U f4 B g8 B g100 B g3 e72 e3 e1 e0 e2
QUERY NORMAL_FORM
STATE
TERM B g106 U f123 U f4 B g8 B g100 B g3 e72 e3 e1 e0 e2
```

Target:

```text
RW r6
```

### ood/term_rewriting/repair_action

- ID: `ood:term_rewriting:72:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
RULE r6 : B g8 B g100 B g3 e72 e3 e1 e0 -> U f60 B g100 B g3 e72 e3 e1
RULE r13 : U f60 v1 -> U f105 v1
RULE r4 : U f105 B g100 B g3 e72 e3 e1 -> B g0 B g100 B g3 e72 e3 e1 e0
RULE r14 : B g0 B g100 B g3 e72 e3 e1 e0 -> U f101 B g100 B g3 e72 e3 e1
RULE r11 : U f101 v1 -> U f124 v1
RULE r8 : U f124 B g100 B g3 e72 e3 e1 -> B g63 B g100 B g3 e72 e3 e1 e0
RULE r12 : B g63 B g100 B g3 e72 e3 e1 e0 -> B g107 B g100 B g3 e72 e3 e1 e0
RULE r5 : B g107 B g100 B g3 e72 e3 e1 e0 -> U f102 B g100 B g3 e72 e3 e1
RULE r7 : B g62 v1 v0 -> B g6 v1 v0
RULE r3 : U f108 v1 -> U f121 v1
RULE r9 : U f61 v1 -> U f122 v1
RULE r2 : U f103 v1 -> U f125 v1
RULE r10 : U f1 v1 -> U f2 v1
RULE r16 : U f5 v1 -> U f8 v1
RULE r0 : B g120 v1 v0 -> B g31 v1 v0
RULE r15 : B g30 v1 v0 -> B g127 v1 v0
RULE r1 : U f128 v1 -> U f104 v1
START B g106 U f123 U f4 B g8 B g100 B g3 e72 e3 e1 e0 e2
QUERY NORMAL_FORM
STATE
TERM B g106 U f123 U f4 B g8 B g100 B g3 e72 e3 e1 e0 e2
RW r6
TERM B g106 U f123 U f4 U f60 B g100 B g3 e72 e1 e1 e2
```

Target:

```text
REPAIR FIRST_BAD
```

### ood/term_rewriting/verify

- ID: `ood:term_rewriting:72:verify:valid`

Source:

```text
MODE verify
PROBLEM
RULE r6 : B g8 B g100 B g3 e72 e3 e1 e0 -> U f60 B g100 B g3 e72 e3 e1
RULE r13 : U f60 v1 -> U f105 v1
RULE r4 : U f105 B g100 B g3 e72 e3 e1 -> B g0 B g100 B g3 e72 e3 e1 e0
RULE r14 : B g0 B g100 B g3 e72 e3 e1 e0 -> U f101 B g100 B g3 e72 e3 e1
RULE r11 : U f101 v1 -> U f124 v1
RULE r8 : U f124 B g100 B g3 e72 e3 e1 -> B g63 B g100 B g3 e72 e3 e1 e0
RULE r12 : B g63 B g100 B g3 e72 e3 e1 e0 -> B g107 B g100 B g3 e72 e3 e1 e0
RULE r5 : B g107 B g100 B g3 e72 e3 e1 e0 -> U f102 B g100 B g3 e72 e3 e1
RULE r7 : B g62 v1 v0 -> B g6 v1 v0
RULE r3 : U f108 v1 -> U f121 v1
RULE r9 : U f61 v1 -> U f122 v1
RULE r2 : U f103 v1 -> U f125 v1
RULE r10 : U f1 v1 -> U f2 v1
RULE r16 : U f5 v1 -> U f8 v1
RULE r0 : B g120 v1 v0 -> B g31 v1 v0
RULE r15 : B g30 v1 v0 -> B g127 v1 v0
RULE r1 : U f128 v1 -> U f104 v1
START B g106 U f123 U f4 B g8 B g100 B g3 e72 e3 e1 e0 e2
QUERY NORMAL_FORM
STATE
TERM B g106 U f123 U f4 B g8 B g100 B g3 e72 e3 e1 e0 e2
RW r6
TERM B g106 U f123 U f4 U f60 B g100 B g3 e72 e3 e1 e2
RW r13
TERM B g106 U f123 U f4 U f105 B g100 B g3 e72 e3 e1 e2
RW r4
TERM B g106 U f123 U f4 B g0 B g100 B g3 e72 e3 e1 e0 e2
RW r14
TERM B g106 U f123 U f4 U f101 B g100 B g3 e72 e3 e1 e2
RW r11
TERM B g106 U f123 U f4 U f124 B g100 B g3 e72 e3 e1 e2
RW r8
TERM B g106 U f123 U f4 B g63 B g100 B g3 e72 e3 e1 e0 e2
RW r12
TERM B g106 U f123 U f4 B g107 B g100 B g3 e72 e3 e1 e0 e2
RW r5
TERM B g106 U f123 U f4 U f102 B g100 B g3 e72 e3 e1 e2
HALT
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
PARENT e2 e8
PARENT e8 e1
PARENT e8 e13
PARENT e13 e11
PARENT e11 e7
PARENT e7 e4
PARENT e7 e10
PARENT e10 e5
PARENT e10 e12
PARENT e5 e3
PARENT e3 e6
PARENT e3 e9
PARENT e9 e0
QUERY ANCESTOR e2 e9
STATE
EMPTY
```

Target:

```text
DESCEND e2
```

### ood/tree_ancestry/repair_action

- ID: `ood:tree_ancestry:54:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
PARENT e2 e8
PARENT e8 e1
PARENT e8 e13
PARENT e13 e11
PARENT e11 e7
PARENT e7 e4
PARENT e7 e10
PARENT e10 e5
PARENT e10 e12
PARENT e5 e3
PARENT e3 e6
PARENT e3 e9
PARENT e9 e0
QUERY ANCESTOR e2 e9
STATE
LINEAGE e9
```

Target:

```text
REPLACE ROOT WITH e2
```

### ood/tree_ancestry/verify

- ID: `ood:tree_ancestry:54:verify:valid`

Source:

```text
MODE verify
PROBLEM
PARENT e2 e8
PARENT e8 e1
PARENT e8 e13
PARENT e13 e11
PARENT e11 e7
PARENT e7 e4
PARENT e7 e10
PARENT e10 e5
PARENT e10 e12
PARENT e5 e3
PARENT e3 e6
PARENT e3 e9
PARENT e9 e0
QUERY ANCESTOR e2 e9
STATE
LINEAGE e2 e8 e13 e11 e7 e10 e5 e3 e9
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
EDGE e7 e1
EDGE e1 e3
EDGE e3 e6
EDGE e3 e2
EDGE e6 e4
EDGE e2 e8
EDGE e2 e5
EDGE e5 e1
EDGE e0 e7
QUERY REACH e7 e4
STATE
EMPTY
```

Target:

```text
APPEND e7
```

### test/graph_reachability/repair_action

- ID: `test:graph_reachability:0:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
EDGE e7 e1
EDGE e1 e3
EDGE e3 e6
EDGE e3 e2
EDGE e6 e4
EDGE e2 e8
EDGE e2 e5
EDGE e5 e1
EDGE e0 e7
QUERY REACH e7 e4
STATE
PATH e4
```

Target:

```text
REPLACE ROOT WITH e7
```

### test/graph_reachability/verify

- ID: `test:graph_reachability:0:verify:valid`

Source:

```text
MODE verify
PROBLEM
EDGE e7 e1
EDGE e1 e3
EDGE e3 e6
EDGE e3 e2
EDGE e6 e4
EDGE e2 e8
EDGE e2 e5
EDGE e5 e1
EDGE e0 e7
QUERY REACH e7 e4
STATE
PATH e7 e1 e3 e6 e4
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
HYP h2 : p2
HYP h1 : p2 -> p3
HYP h3 : p3 -> p0
HYP h5 : p0 -> p1
HYP h6 : p2 -> p0
HYP h0 : p3 -> p2
HYP h4 : p3 -> p1
HYP h999 : p1 -> p3
GOAL p1
STATE
EMPTY
```

Target:

```text
APPLY h2
```

### test/implication_chains/repair_action

- ID: `test:implication_chains:18:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
HYP h2 : p2
HYP h1 : p2 -> p3
HYP h3 : p3 -> p0
HYP h5 : p0 -> p1
HYP h6 : p2 -> p0
HYP h0 : p3 -> p2
HYP h4 : p3 -> p1
HYP h999 : p1 -> p3
GOAL p1
STATE
DERIVE p2 BY h7
```

Target:

```text
REPLACE FIRST HYP h2
```

### test/implication_chains/verify

- ID: `test:implication_chains:18:verify:valid`

Source:

```text
MODE verify
PROBLEM
HYP h2 : p2
HYP h1 : p2 -> p3
HYP h3 : p3 -> p0
HYP h5 : p0 -> p1
HYP h6 : p2 -> p0
HYP h0 : p3 -> p2
HYP h4 : p3 -> p1
HYP h999 : p1 -> p3
GOAL p1
STATE
DERIVE p2 BY h2
DERIVE p3 BY h1 FROM p2
DERIVE p0 BY h3 FROM p3
DERIVE p1 BY h5 FROM p0
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
FACT r5 e2 e1
FACT r8 e1 e4
FACT r0 e4 e3
FACT r4 e3 e0
FACT r6 e0 e5
RULE r3 = r5 ; r8
RULE r7 = r3 ; r0
RULE r2 = r7 ; r4
RULE r1 = r2 ; r6
FACT r5 e4 e5
FACT r8 e3 e5
FACT r8 e5 e4
FACT r0 e4 e5
FACT r4 e5 e4
QUERY r1 e2 e5
STATE
EMPTY
```

Target:

```text
FOLLOW e2 e4 VIA e1
```

### test/relation_composition/repair_action

- ID: `test:relation_composition:36:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
FACT r5 e2 e1
FACT r8 e1 e4
FACT r0 e4 e3
FACT r4 e3 e0
FACT r6 e0 e5
RULE r3 = r5 ; r8
RULE r7 = r3 ; r0
RULE r2 = r7 ; r4
RULE r1 = r2 ; r6
FACT r5 e4 e5
FACT r8 e3 e5
FACT r8 e5 e4
FACT r0 e4 e5
FACT r4 e5 e4
QUERY r1 e2 e5
STATE
DERIVE r3 e2 e4 VIA e2
```

Target:

```text
REPLACE FIRST VIA e1
```

### test/relation_composition/verify

- ID: `test:relation_composition:36:verify:valid`

Source:

```text
MODE verify
PROBLEM
FACT r5 e2 e1
FACT r8 e1 e4
FACT r0 e4 e3
FACT r4 e3 e0
FACT r6 e0 e5
RULE r3 = r5 ; r8
RULE r7 = r3 ; r0
RULE r2 = r7 ; r4
RULE r1 = r2 ; r6
FACT r5 e4 e5
FACT r8 e3 e5
FACT r8 e5 e4
FACT r0 e4 e5
FACT r4 e5 e4
QUERY r1 e2 e5
STATE
DERIVE r3 e2 e4 VIA e1
DERIVE r7 e2 e3 VIA e4
DERIVE r2 e2 e0 VIA e3
DERIVE r1 e2 e5 VIA e0
```

Target:

```text
VALID
```

### test/term_rewriting/action

- ID: `test:term_rewriting:72:action:0`

Source:

```text
MODE action
PROBLEM
RULE r5 : U f0 v1 -> U f4 v1
RULE r1 : U f4 B g31 e3 e1 -> U f2 B g31 e3 e1
RULE r0 : U f2 B g31 e3 e1 -> B g121 B g31 e3 e1 e2
RULE r4 : B g121 B g31 e3 e1 e2 -> U f1 B g31 e3 e1
RULE r3 : B g60 v1 v0 -> B g3 v1 v0
RULE r2 : B g101 v1 v0 -> B g120 v1 v0
START B g30 U f0 B g31 e3 e1 U f0 B g31 e3 e1
GOAL B g30 U f1 B g31 e3 e1 U f0 B g31 e3 e1
STATE
TERM B g30 U f0 B g31 e3 e1 U f0 B g31 e3 e1
```

Target:

```text
RW r5
```

### test/term_rewriting/repair_action

- ID: `test:term_rewriting:72:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
RULE r5 : U f0 v1 -> U f4 v1
RULE r1 : U f4 B g31 e3 e1 -> U f2 B g31 e3 e1
RULE r0 : U f2 B g31 e3 e1 -> B g121 B g31 e3 e1 e2
RULE r4 : B g121 B g31 e3 e1 e2 -> U f1 B g31 e3 e1
RULE r3 : B g60 v1 v0 -> B g3 v1 v0
RULE r2 : B g101 v1 v0 -> B g120 v1 v0
START B g30 U f0 B g31 e3 e1 U f0 B g31 e3 e1
GOAL B g30 U f1 B g31 e3 e1 U f0 B g31 e3 e1
STATE
TERM B g30 U f0 B g31 e3 e1 U f0 B g31 e3 e1
RW r5
TERM B g30 U f4 B g31 e3 e1 U f0 B g100 e3 e1
```

Target:

```text
REPAIR FIRST_BAD
```

### test/term_rewriting/verify

- ID: `test:term_rewriting:72:verify:valid`

Source:

```text
MODE verify
PROBLEM
RULE r5 : U f0 v1 -> U f4 v1
RULE r1 : U f4 B g31 e3 e1 -> U f2 B g31 e3 e1
RULE r0 : U f2 B g31 e3 e1 -> B g121 B g31 e3 e1 e2
RULE r4 : B g121 B g31 e3 e1 e2 -> U f1 B g31 e3 e1
RULE r3 : B g60 v1 v0 -> B g3 v1 v0
RULE r2 : B g101 v1 v0 -> B g120 v1 v0
START B g30 U f0 B g31 e3 e1 U f0 B g31 e3 e1
GOAL B g30 U f1 B g31 e3 e1 U f0 B g31 e3 e1
STATE
TERM B g30 U f0 B g31 e3 e1 U f0 B g31 e3 e1
RW r5
TERM B g30 U f4 B g31 e3 e1 U f0 B g31 e3 e1
RW r1
TERM B g30 U f2 B g31 e3 e1 U f0 B g31 e3 e1
RW r0
TERM B g30 B g121 B g31 e3 e1 e2 U f0 B g31 e3 e1
RW r4
TERM B g30 U f1 B g31 e3 e1 U f0 B g31 e3 e1
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
PARENT e8 e3
PARENT e8 e7
PARENT e3 e6
PARENT e3 e4
PARENT e6 e2
PARENT e2 e1
PARENT e1 e0
PARENT e7 e5
QUERY ANCESTOR e8 e1
STATE
EMPTY
```

Target:

```text
DESCEND e8
```

### test/tree_ancestry/repair_action

- ID: `test:tree_ancestry:54:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
PARENT e8 e3
PARENT e8 e7
PARENT e3 e6
PARENT e3 e4
PARENT e6 e2
PARENT e2 e1
PARENT e1 e0
PARENT e7 e5
QUERY ANCESTOR e8 e1
STATE
LINEAGE e1
```

Target:

```text
REPLACE ROOT WITH e8
```

### test/tree_ancestry/verify

- ID: `test:tree_ancestry:54:verify:valid`

Source:

```text
MODE verify
PROBLEM
PARENT e8 e3
PARENT e8 e7
PARENT e3 e6
PARENT e3 e4
PARENT e6 e2
PARENT e2 e1
PARENT e1 e0
PARENT e7 e5
QUERY ANCESTOR e8 e1
STATE
LINEAGE e8 e3 e6 e2 e1
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
EDGE e2 e3
EDGE e3 e0
EDGE e0 e5
EDGE e5 e1
EDGE e1 e3
EDGE e1 e4
EDGE e4 e2
EDGE e4 e3
EDGE e4 e1
QUERY REACH e2 e4
STATE
EMPTY
```

Target:

```text
APPEND e2
```

### train/graph_reachability/repair_action

- ID: `train:graph_reachability:0:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
EDGE e2 e3
EDGE e3 e0
EDGE e0 e5
EDGE e5 e1
EDGE e1 e3
EDGE e1 e4
EDGE e4 e2
EDGE e4 e3
EDGE e4 e1
QUERY REACH e2 e4
STATE
PATH e4
```

Target:

```text
REPLACE ROOT WITH e2
```

### train/graph_reachability/verify

- ID: `train:graph_reachability:0:verify:valid`

Source:

```text
MODE verify
PROBLEM
EDGE e2 e3
EDGE e3 e0
EDGE e0 e5
EDGE e5 e1
EDGE e1 e3
EDGE e1 e4
EDGE e4 e2
EDGE e4 e3
EDGE e4 e1
QUERY REACH e2 e4
STATE
PATH e2 e3 e0 e5 e1 e4
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
HYP h2 : p0 -> p2
HYP h1 : p2 -> p1
HYP h4 : p0 -> p8
HYP h3 : p1 -> p0
HYP h5 : p1 -> p2
GOAL p1
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
HYP h2 : p0 -> p2
HYP h1 : p2 -> p1
HYP h4 : p0 -> p8
HYP h3 : p1 -> p0
HYP h5 : p1 -> p2
GOAL p1
STATE
DERIVE p0 BY h999
```

Target:

```text
REPLACE FIRST HYP h0
```

### train/implication_chains/verify

- ID: `train:implication_chains:312:verify:valid`

Source:

```text
MODE verify
PROBLEM
HYP h0 : p0
HYP h2 : p0 -> p2
HYP h1 : p2 -> p1
HYP h4 : p0 -> p8
HYP h3 : p1 -> p0
HYP h5 : p1 -> p2
GOAL p1
STATE
DERIVE p0 BY h0
DERIVE p2 BY h2 FROM p0
DERIVE p1 BY h1 FROM p2
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
FACT r4 e2 e1
FACT r2 e1 e3
FACT r1 e3 e0
RULE r0 = r4 ; r2
RULE r3 = r0 ; r1
FACT r4 e3 e0
FACT r1 e1 e3
QUERY r3 e2 e0
STATE
EMPTY
```

Target:

```text
FOLLOW e2 e3 VIA e1
```

### train/relation_composition/repair_action

- ID: `train:relation_composition:624:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
FACT r4 e2 e1
FACT r2 e1 e3
FACT r1 e3 e0
RULE r0 = r4 ; r2
RULE r3 = r0 ; r1
FACT r4 e3 e0
FACT r1 e1 e3
QUERY r3 e2 e0
STATE
DERIVE r0 e2 e3 VIA e2
```

Target:

```text
REPLACE FIRST VIA e1
```

### train/relation_composition/verify

- ID: `train:relation_composition:624:verify:valid`

Source:

```text
MODE verify
PROBLEM
FACT r4 e2 e1
FACT r2 e1 e3
FACT r1 e3 e0
RULE r0 = r4 ; r2
RULE r3 = r0 ; r1
FACT r4 e3 e0
FACT r1 e1 e3
QUERY r3 e2 e0
STATE
DERIVE r0 e2 e3 VIA e1
DERIVE r3 e2 e0 VIA e3
```

Target:

```text
VALID
```

### train/term_rewriting/action

- ID: `train:term_rewriting:1368:action:0`

Source:

```text
MODE action
PROBLEM
RULE r4 : U f2 e1 -> U f60 e1
RULE r3 : U f60 v1 -> U f61 v1
RULE r2 : U f61 v1 -> U f1 v1
RULE r5 : U f1 e1 -> B g5 e1 e0
RULE r1 : B g5 e1 e0 -> U f101 e1
RULE r6 : B g100 v1 v0 -> B g120 v1 v0
RULE r0 : U f121 v1 -> U f3 v1
START U f0 U f2 e1
QUERY NORMAL_FORM
STATE
TERM U f0 U f2 e1
```

Target:

```text
RW r4
```

### train/term_rewriting/repair_action

- ID: `train:term_rewriting:1368:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
RULE r4 : U f2 e1 -> U f60 e1
RULE r3 : U f60 v1 -> U f61 v1
RULE r2 : U f61 v1 -> U f1 v1
RULE r5 : U f1 e1 -> B g5 e1 e0
RULE r1 : B g5 e1 e0 -> U f101 e1
RULE r6 : B g100 v1 v0 -> B g120 v1 v0
RULE r0 : U f121 v1 -> U f3 v1
START U f0 U f2 e1
QUERY NORMAL_FORM
STATE
TERM U f0 U f2 e1
RW r4
TERM U f5 U f60 e1
```

Target:

```text
REPAIR FIRST_BAD
```

### train/term_rewriting/verify

- ID: `train:term_rewriting:1368:verify:valid`

Source:

```text
MODE verify
PROBLEM
RULE r4 : U f2 e1 -> U f60 e1
RULE r3 : U f60 v1 -> U f61 v1
RULE r2 : U f61 v1 -> U f1 v1
RULE r5 : U f1 e1 -> B g5 e1 e0
RULE r1 : B g5 e1 e0 -> U f101 e1
RULE r6 : B g100 v1 v0 -> B g120 v1 v0
RULE r0 : U f121 v1 -> U f3 v1
START U f0 U f2 e1
QUERY NORMAL_FORM
STATE
TERM U f0 U f2 e1
RW r4
TERM U f0 U f60 e1
RW r3
TERM U f0 U f61 e1
RW r2
TERM U f0 U f1 e1
RW r5
TERM U f0 B g5 e1 e0
RW r1
TERM U f0 U f101 e1
HALT
```

Target:

```text
VALID
```

### train/tree_ancestry/action

- ID: `train:tree_ancestry:1056:action:0`

Source:

```text
MODE action
PROBLEM
PARENT e6 e0
PARENT e0 e1
PARENT e1 e4
PARENT e1 e5
PARENT e4 e7
PARENT e7 e3
PARENT e3 e2
QUERY ANCESTOR e6 e7
STATE
EMPTY
```

Target:

```text
DESCEND e6
```

### train/tree_ancestry/repair_action

- ID: `train:tree_ancestry:1056:repair_action:1`

Source:

```text
MODE repair_action
PROBLEM
PARENT e6 e0
PARENT e0 e1
PARENT e1 e4
PARENT e1 e5
PARENT e4 e7
PARENT e7 e3
PARENT e3 e2
QUERY ANCESTOR e6 e7
STATE
LINEAGE e7
```

Target:

```text
REPLACE ROOT WITH e6
```

### train/tree_ancestry/verify

- ID: `train:tree_ancestry:1056:verify:valid`

Source:

```text
MODE verify
PROBLEM
PARENT e6 e0
PARENT e0 e1
PARENT e1 e4
PARENT e1 e5
PARENT e4 e7
PARENT e7 e3
PARENT e3 e2
QUERY ANCESTOR e6 e7
STATE
LINEAGE e6 e0 e1 e4 e7
```

Target:

```text
VALID
```
