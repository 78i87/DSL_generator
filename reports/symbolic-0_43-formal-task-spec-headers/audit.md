# Dataset Audit

- Data dir: `data/symbolic-0_43-formal-task-spec-headers`
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

- Inputs shape: `[19827, 903]`
- Labels shape: `[19827, 903]`
- Seq len: `903`
- Vocab size: `345`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `19827`

### test

- Inputs shape: `[1202, 903]`
- Labels shape: `[1202, 903]`
- Seq len: `903`
- Vocab size: `345`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1202`

### ood

- Inputs shape: `[1856, 903]`
- Labels shape: `[1856, 903]`
- Seq len: `903`
- Vocab size: `345`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1856`

## Samples

### ood/graph_reachability/action

- ID: `ood:graph_reachability:0:action:0`

Source:

```text
MODE action
TASK
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
VALID ALL_RULES_HOLD
FORM QUERY REACH A C
FORM EDGE A B
FORM PATH A ... C
EMPTY MEANS NO_PATH
VALID PATH USES_EDGE_BETWEEN_NEIGHBORS
APPEND X STARTS_OR_EXTENDS_PATH
DONE PATH_FROM_QUERY_START_TO_TARGET
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e11 e4
EDGE e2 e0
EDGE e2 e3
EDGE e3 e4
EDGE e3 e9
EDGE e4 e5
EDGE e5 e2
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e8 e1
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
TASK
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
VALID ALL_RULES_HOLD
FORM QUERY REACH A C
FORM EDGE A B
FORM PATH A ... C
EMPTY MEANS NO_PATH
VALID PATH USES_EDGE_BETWEEN_NEIGHBORS
APPEND X STARTS_OR_EXTENDS_PATH
DONE PATH_FROM_QUERY_START_TO_TARGET
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e11 e4
EDGE e2 e0
EDGE e2 e3
EDGE e3 e4
EDGE e3 e9
EDGE e4 e5
EDGE e5 e2
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e8 e1
QUERY REACH e0 e8
STATE
PATH e8
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
TASK
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
VALID ALL_RULES_HOLD
FORM QUERY REACH A C
FORM EDGE A B
FORM PATH A ... C
EMPTY MEANS NO_PATH
VALID PATH USES_EDGE_BETWEEN_NEIGHBORS
APPEND X STARTS_OR_EXTENDS_PATH
DONE PATH_FROM_QUERY_START_TO_TARGET
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e11 e4
EDGE e2 e0
EDGE e2 e3
EDGE e3 e4
EDGE e3 e9
EDGE e4 e5
EDGE e5 e2
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e8 e1
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
TASK
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
VALID ALL_RULES_HOLD
FORM HYP K : P
FORM HYP K : P -> Q
FORM GOAL Q
FORM DERIVE Q BY K FROM P
APPLY K ADDS_LICENSED_DERIVATION
VALID DERIVE_USES_KNOWN_FACT_OR_PRIOR_PREMISE
DONE GOAL_DERIVED
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p0 -> p2
HYP h9 : p1 -> p4
HYP h10 : p1 -> p9
HYP h11 : p6 -> p5
HYP h12 : p6 -> p10
HYP h13 : p7 -> p10
HYP h14 : p8 -> p0
HYP h15 : p8 -> p4
HYP h16 : p9 -> p4
HYP h17 : p10 -> p3
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
TASK
VALID ALL_RULES_HOLD
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
FORM HYP K : P
FORM GOAL Q
FORM HYP K : P -> Q
FORM DERIVE Q BY K FROM P
APPLY K ADDS_LICENSED_DERIVATION
VALID DERIVE_USES_KNOWN_FACT_OR_PRIOR_PREMISE
DONE GOAL_DERIVED
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p0 -> p2
HYP h9 : p1 -> p4
HYP h10 : p1 -> p9
HYP h11 : p6 -> p5
HYP h12 : p6 -> p10
HYP h13 : p7 -> p10
HYP h14 : p8 -> p0
HYP h15 : p8 -> p4
HYP h16 : p9 -> p4
HYP h17 : p10 -> p3
GOAL p7
STATE
DERIVE p0 BY h999
```

Target:

```text
REPLACE FIRST HYP h0
```

### ood/implication_chains/verify

- ID: `ood:implication_chains:18:verify:valid`

Source:

```text
MODE verify
TASK
VALID ALL_RULES_HOLD
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
FORM HYP K : P
FORM GOAL Q
FORM HYP K : P -> Q
FORM DERIVE Q BY K FROM P
APPLY K ADDS_LICENSED_DERIVATION
VALID DERIVE_USES_KNOWN_FACT_OR_PRIOR_PREMISE
DONE GOAL_DERIVED
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p0 -> p2
HYP h9 : p1 -> p4
HYP h10 : p1 -> p9
HYP h11 : p6 -> p5
HYP h12 : p6 -> p10
HYP h13 : p7 -> p10
HYP h14 : p8 -> p0
HYP h15 : p8 -> p4
HYP h16 : p9 -> p4
HYP h17 : p10 -> p3
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
TASK
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
VALID ALL_RULES_HOLD
FORM RULE RC = RA ; RB
FORM FACT R A B
FORM QUERY R A C
FORM DERIVE R A C VIA B
FOLLOW C VIA B ADDS_COMPOSED_FACT
VALID NEEDS_LEFT_FACT_RIGHT_FACT_AND_RULE
DONE QUERY_FACT_AVAILABLE
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
FACT r0 e0 e10
FACT r2 e5 e8
FACT r4 e8 e9
FACT r5 e1 e5
FACT r5 e4 e11
FACT r6 e8 e3
QUERY r14 e0 e8
STATE
EMPTY
```

Target:

```text
FOLLOW e0 e2 VIA e1
```

### ood/relation_composition/repair_action

- ID: `ood:relation_composition:36:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
VALID ALL_RULES_HOLD
FORM FACT R A B
FORM RULE RC = RA ; RB
FORM QUERY R A C
FORM DERIVE R A C VIA B
FOLLOW C VIA B ADDS_COMPOSED_FACT
VALID NEEDS_LEFT_FACT_RIGHT_FACT_AND_RULE
DONE QUERY_FACT_AVAILABLE
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
FACT r0 e0 e10
FACT r2 e5 e8
FACT r4 e8 e9
FACT r5 e1 e5
FACT r5 e4 e11
FACT r6 e8 e3
QUERY r14 e0 e8
STATE
DERIVE r8 e0 e2 VIA e0
```

Target:

```text
REPLACE FIRST VIA e1
```

### ood/relation_composition/verify

- ID: `ood:relation_composition:36:verify:valid`

Source:

```text
MODE verify
TASK
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
VALID ALL_RULES_HOLD
FORM FACT R A B
FORM RULE RC = RA ; RB
FORM QUERY R A C
FORM DERIVE R A C VIA B
FOLLOW C VIA B ADDS_COMPOSED_FACT
VALID NEEDS_LEFT_FACT_RIGHT_FACT_AND_RULE
DONE QUERY_FACT_AVAILABLE
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
FACT r0 e0 e10
FACT r2 e5 e8
FACT r4 e8 e9
FACT r5 e1 e5
FACT r5 e4 e11
FACT r6 e8 e3
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

### ood/term_rewriting/action

- ID: `ood:term_rewriting:72:action:0`

Source:

```text
MODE action
TASK
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
VALID ALL_RULES_HOLD
FORM RULE K : L -> R
FORM TERM T
FORM START T
FORM GOAL T
FORM QUERY NORMAL_FORM
FORM RW K AT PATH
FORM HALT
RW REPLACES_MATCHING_SUBTERM_AT_PATH
HALT ONLY_WHEN_DONE
VALID TRACE_ALTERNATES_TERM_AND_RW
PROBLEM
RULE r0 : B g0 B g31 B g30 e0 e2 e3 e1 -> U f1 B g31 B g30 e0 e2 e3
RULE r1 : U f1 v0 -> U f2 v0
RULE r2 : U f2 B g31 B g30 e0 e2 e3 -> B g3 B g31 B g30 e0 e2 e3 e1
RULE r3 : B g3 B g31 B g30 e0 e2 e3 e1 -> U f4 B g31 B g30 e0 e2 e3
RULE r4 : U f4 v0 -> U f5 v0
RULE r5 : U f5 B g31 B g30 e0 e2 e3 -> B g6 B g31 B g30 e0 e2 e3 e1
RULE r6 : B g6 B g31 B g30 e0 e2 e3 e1 -> B g7 B g31 B g30 e0 e2 e3 e1
RULE r7 : B g7 B g31 B g30 e0 e2 e3 e1 -> U f8 B g31 B g30 e0 e2 e3
RULE r8 : B g100 v0 v1 -> B g120 v0 v1
RULE r9 : U f101 v0 -> U f121 v0
RULE r10 : U f102 v0 -> U f122 v0
RULE r11 : U f103 v0 -> U f123 v0
RULE r12 : U f104 v0 -> U f124 v0
RULE r13 : U f105 v0 -> U f125 v0
RULE r14 : B g106 v0 v1 -> B g126 v0 v1
RULE r15 : B g107 v0 v1 -> B g127 v0 v1
RULE r16 : U f108 v0 -> U f128 v0
START B g62 U f61 U f60 B g0 B g31 B g30 e0 e2 e3 e1 e72
QUERY NORMAL_FORM
STATE
TERM B g62 U f61 U f60 B g0 B g31 B g30 e0 e2 e3 e1 e72
```

Target:

```text
RW r0
```

### ood/term_rewriting/repair_action

- ID: `ood:term_rewriting:72:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
VALID ALL_RULES_HOLD
FORM RULE K : L -> R
FORM START T
FORM GOAL T
FORM QUERY NORMAL_FORM
FORM TERM T
FORM RW K AT PATH
FORM HALT
RW REPLACES_MATCHING_SUBTERM_AT_PATH
HALT ONLY_WHEN_DONE
VALID TRACE_ALTERNATES_TERM_AND_RW
PROBLEM
RULE r0 : B g0 B g31 B g30 e0 e2 e3 e1 -> U f1 B g31 B g30 e0 e2 e3
RULE r1 : U f1 v0 -> U f2 v0
RULE r2 : U f2 B g31 B g30 e0 e2 e3 -> B g3 B g31 B g30 e0 e2 e3 e1
RULE r3 : B g3 B g31 B g30 e0 e2 e3 e1 -> U f4 B g31 B g30 e0 e2 e3
RULE r4 : U f4 v0 -> U f5 v0
RULE r5 : U f5 B g31 B g30 e0 e2 e3 -> B g6 B g31 B g30 e0 e2 e3 e1
RULE r6 : B g6 B g31 B g30 e0 e2 e3 e1 -> B g7 B g31 B g30 e0 e2 e3 e1
RULE r7 : B g7 B g31 B g30 e0 e2 e3 e1 -> U f8 B g31 B g30 e0 e2 e3
RULE r8 : B g100 v0 v1 -> B g120 v0 v1
RULE r9 : U f101 v0 -> U f121 v0
RULE r10 : U f102 v0 -> U f122 v0
RULE r11 : U f103 v0 -> U f123 v0
RULE r12 : U f104 v0 -> U f124 v0
RULE r13 : U f105 v0 -> U f125 v0
RULE r14 : B g106 v0 v1 -> B g126 v0 v1
RULE r15 : B g107 v0 v1 -> B g127 v0 v1
RULE r16 : U f108 v0 -> U f128 v0
START B g62 U f61 U f60 B g0 B g31 B g30 e0 e2 e3 e1 e72
QUERY NORMAL_FORM
STATE
TERM B g62 U f61 U f60 B g0 B g31 B g30 e0 e2 e3 e1 e72
RW r0
TERM B g62 U f61 U f60 U f1 B g31 B g30 e0 e3 e3 e72
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
TASK
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
VALID ALL_RULES_HOLD
FORM RULE K : L -> R
FORM TERM T
FORM START T
FORM GOAL T
FORM QUERY NORMAL_FORM
FORM RW K AT PATH
FORM HALT
RW REPLACES_MATCHING_SUBTERM_AT_PATH
HALT ONLY_WHEN_DONE
VALID TRACE_ALTERNATES_TERM_AND_RW
PROBLEM
RULE r0 : B g0 B g31 B g30 e0 e2 e3 e1 -> U f1 B g31 B g30 e0 e2 e3
RULE r1 : U f1 v0 -> U f2 v0
RULE r2 : U f2 B g31 B g30 e0 e2 e3 -> B g3 B g31 B g30 e0 e2 e3 e1
RULE r3 : B g3 B g31 B g30 e0 e2 e3 e1 -> U f4 B g31 B g30 e0 e2 e3
RULE r4 : U f4 v0 -> U f5 v0
RULE r5 : U f5 B g31 B g30 e0 e2 e3 -> B g6 B g31 B g30 e0 e2 e3 e1
RULE r6 : B g6 B g31 B g30 e0 e2 e3 e1 -> B g7 B g31 B g30 e0 e2 e3 e1
RULE r7 : B g7 B g31 B g30 e0 e2 e3 e1 -> U f8 B g31 B g30 e0 e2 e3
RULE r8 : B g100 v0 v1 -> B g120 v0 v1
RULE r9 : U f101 v0 -> U f121 v0
RULE r10 : U f102 v0 -> U f122 v0
RULE r11 : U f103 v0 -> U f123 v0
RULE r12 : U f104 v0 -> U f124 v0
RULE r13 : U f105 v0 -> U f125 v0
RULE r14 : B g106 v0 v1 -> B g126 v0 v1
RULE r15 : B g107 v0 v1 -> B g127 v0 v1
RULE r16 : U f108 v0 -> U f128 v0
START B g62 U f61 U f60 B g0 B g31 B g30 e0 e2 e3 e1 e72
QUERY NORMAL_FORM
STATE
TERM B g62 U f61 U f60 B g0 B g31 B g30 e0 e2 e3 e1 e72
RW r0
TERM B g62 U f61 U f60 U f1 B g31 B g30 e0 e2 e3 e72
RW r1
TERM B g62 U f61 U f60 U f2 B g31 B g30 e0 e2 e3 e72
RW r2
TERM B g62 U f61 U f60 B g3 B g31 B g30 e0 e2 e3 e1 e72
RW r3
TERM B g62 U f61 U f60 U f4 B g31 B g30 e0 e2 e3 e72
RW r4
TERM B g62 U f61 U f60 U f5 B g31 B g30 e0 e2 e3 e72
RW r5
TERM B g62 U f61 U f60 B g6 B g31 B g30 e0 e2 e3 e1 e72
RW r6
TERM B g62 U f61 U f60 B g7 B g31 B g30 e0 e2 e3 e1 e72
RW r7
TERM B g62 U f61 U f60 U f8 B g31 B g30 e0 e2 e3 e72
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
TASK
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
VALID ALL_RULES_HOLD
FORM PARENT A B
FORM QUERY ANCESTOR A C
FORM LINEAGE A ... C
EMPTY MEANS NO_LINEAGE
VALID LINEAGE USES_PARENT_BETWEEN_NEIGHBORS
DESCEND X STARTS_OR_EXTENDS_LINEAGE
DONE LINEAGE_FROM_QUERY_START_TO_TARGET
PROBLEM
PARENT e0 e1
PARENT e1 e12
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e4 e10
PARENT e4 e5
PARENT e5 e6
PARENT e5 e9
PARENT e6 e7
PARENT e7 e11
PARENT e7 e8
PARENT e8 e13
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
TASK
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
VALID ALL_RULES_HOLD
FORM PARENT A B
FORM QUERY ANCESTOR A C
FORM LINEAGE A ... C
EMPTY MEANS NO_LINEAGE
VALID LINEAGE USES_PARENT_BETWEEN_NEIGHBORS
DESCEND X STARTS_OR_EXTENDS_LINEAGE
DONE LINEAGE_FROM_QUERY_START_TO_TARGET
PROBLEM
PARENT e0 e1
PARENT e1 e12
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e4 e10
PARENT e4 e5
PARENT e5 e6
PARENT e5 e9
PARENT e6 e7
PARENT e7 e11
PARENT e7 e8
PARENT e8 e13
QUERY ANCESTOR e0 e8
STATE
LINEAGE e8
```

Target:

```text
REPLACE ROOT WITH e0
```

### ood/tree_ancestry/verify

- ID: `ood:tree_ancestry:54:verify:valid`

Source:

```text
MODE verify
TASK
VALID ALL_RULES_HOLD
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
FORM QUERY ANCESTOR A C
FORM PARENT A B
FORM LINEAGE A ... C
EMPTY MEANS NO_LINEAGE
VALID LINEAGE USES_PARENT_BETWEEN_NEIGHBORS
DESCEND X STARTS_OR_EXTENDS_LINEAGE
DONE LINEAGE_FROM_QUERY_START_TO_TARGET
PROBLEM
PARENT e0 e1
PARENT e1 e12
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e4 e10
PARENT e4 e5
PARENT e5 e6
PARENT e5 e9
PARENT e6 e7
PARENT e7 e11
PARENT e7 e8
PARENT e8 e13
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
TASK
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
VALID ALL_RULES_HOLD
FORM EDGE A B
FORM QUERY REACH A C
FORM PATH A ... C
EMPTY MEANS NO_PATH
VALID PATH USES_EDGE_BETWEEN_NEIGHBORS
APPEND X STARTS_OR_EXTENDS_PATH
DONE PATH_FROM_QUERY_START_TO_TARGET
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e2 e3
EDGE e2 e5
EDGE e3 e4
EDGE e5 e6
EDGE e5 e7
EDGE e7 e1
EDGE e8 e0
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
TASK
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
VALID ALL_RULES_HOLD
FORM EDGE A B
FORM QUERY REACH A C
FORM PATH A ... C
EMPTY MEANS NO_PATH
VALID PATH USES_EDGE_BETWEEN_NEIGHBORS
APPEND X STARTS_OR_EXTENDS_PATH
DONE PATH_FROM_QUERY_START_TO_TARGET
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e2 e3
EDGE e2 e5
EDGE e3 e4
EDGE e5 e6
EDGE e5 e7
EDGE e7 e1
EDGE e8 e0
QUERY REACH e0 e4
STATE
PATH e4
```

Target:

```text
REPLACE ROOT WITH e0
```

### test/graph_reachability/verify

- ID: `test:graph_reachability:0:verify:valid`

Source:

```text
MODE verify
TASK
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
VALID ALL_RULES_HOLD
FORM QUERY REACH A C
FORM EDGE A B
FORM PATH A ... C
EMPTY MEANS NO_PATH
VALID PATH USES_EDGE_BETWEEN_NEIGHBORS
APPEND X STARTS_OR_EXTENDS_PATH
DONE PATH_FROM_QUERY_START_TO_TARGET
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e2 e3
EDGE e2 e5
EDGE e3 e4
EDGE e5 e6
EDGE e5 e7
EDGE e7 e1
EDGE e8 e0
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
TASK
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
VALID ALL_RULES_HOLD
FORM HYP K : P
FORM HYP K : P -> Q
FORM GOAL Q
FORM DERIVE Q BY K FROM P
APPLY K ADDS_LICENSED_DERIVATION
VALID DERIVE_USES_KNOWN_FACT_OR_PRIOR_PREMISE
DONE GOAL_DERIVED
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p0 -> p2
HYP h5 : p1 -> p0
HYP h6 : p1 -> p3
HYP h7 : p3 -> p1
GOAL p3
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
TASK
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
VALID ALL_RULES_HOLD
FORM HYP K : P
FORM HYP K : P -> Q
FORM GOAL Q
FORM DERIVE Q BY K FROM P
APPLY K ADDS_LICENSED_DERIVATION
VALID DERIVE_USES_KNOWN_FACT_OR_PRIOR_PREMISE
DONE GOAL_DERIVED
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p0 -> p2
HYP h5 : p1 -> p0
HYP h6 : p1 -> p3
HYP h7 : p3 -> p1
GOAL p3
STATE
DERIVE p0 BY h999
```

Target:

```text
REPLACE FIRST HYP h0
```

### test/implication_chains/verify

- ID: `test:implication_chains:18:verify:valid`

Source:

```text
MODE verify
TASK
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
VALID ALL_RULES_HOLD
FORM HYP K : P
FORM HYP K : P -> Q
FORM GOAL Q
FORM DERIVE Q BY K FROM P
APPLY K ADDS_LICENSED_DERIVATION
VALID DERIVE_USES_KNOWN_FACT_OR_PRIOR_PREMISE
DONE GOAL_DERIVED
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p0 -> p2
HYP h5 : p1 -> p0
HYP h6 : p1 -> p3
HYP h7 : p3 -> p1
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

- ID: `test:relation_composition:36:action:0`

Source:

```text
MODE action
TASK
VALID ALL_RULES_HOLD
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
FORM FACT R A B
FORM RULE RC = RA ; RB
FORM QUERY R A C
FORM DERIVE R A C VIA B
FOLLOW C VIA B ADDS_COMPOSED_FACT
VALID NEEDS_LEFT_FACT_RIGHT_FACT_AND_RULE
DONE QUERY_FACT_AVAILABLE
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
FACT r0 e2 e5
FACT r1 e3 e5
FACT r1 e5 e2
FACT r2 e2 e5
FACT r3 e5 e2
QUERY r8 e0 e5
STATE
EMPTY
```

Target:

```text
FOLLOW e0 e2 VIA e1
```

### test/relation_composition/repair_action

- ID: `test:relation_composition:36:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
VALID ALL_RULES_HOLD
FORM RULE RC = RA ; RB
FORM FACT R A B
FORM QUERY R A C
FORM DERIVE R A C VIA B
FOLLOW C VIA B ADDS_COMPOSED_FACT
VALID NEEDS_LEFT_FACT_RIGHT_FACT_AND_RULE
DONE QUERY_FACT_AVAILABLE
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
FACT r0 e2 e5
FACT r1 e3 e5
FACT r1 e5 e2
FACT r2 e2 e5
FACT r3 e5 e2
QUERY r8 e0 e5
STATE
DERIVE r5 e0 e2 VIA e0
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
TASK
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
VALID ALL_RULES_HOLD
FORM RULE RC = RA ; RB
FORM FACT R A B
FORM QUERY R A C
FORM DERIVE R A C VIA B
FOLLOW C VIA B ADDS_COMPOSED_FACT
VALID NEEDS_LEFT_FACT_RIGHT_FACT_AND_RULE
DONE QUERY_FACT_AVAILABLE
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
FACT r0 e2 e5
FACT r1 e3 e5
FACT r1 e5 e2
FACT r2 e2 e5
FACT r3 e5 e2
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

### test/term_rewriting/action

- ID: `test:term_rewriting:72:action:0`

Source:

```text
MODE action
TASK
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
VALID ALL_RULES_HOLD
FORM RULE K : L -> R
FORM START T
FORM GOAL T
FORM QUERY NORMAL_FORM
FORM TERM T
FORM RW K AT PATH
FORM HALT
RW REPLACES_MATCHING_SUBTERM_AT_PATH
HALT ONLY_WHEN_DONE
VALID TRACE_ALTERNATES_TERM_AND_RW
PROBLEM
RULE r0 : U f0 v0 -> U f1 v0
RULE r1 : U f1 B g30 e0 e2 -> U f2 B g30 e0 e2
RULE r2 : U f2 B g30 e0 e2 -> B g3 B g30 e0 e2 e1
RULE r3 : B g3 B g30 e0 e2 e1 -> U f4 B g30 e0 e2
RULE r4 : B g100 v0 v1 -> B g120 v0 v1
RULE r5 : B g101 v0 v1 -> B g121 v0 v1
START B g60 U f0 B g30 e0 e2 U f0 B g30 e0 e2
GOAL B g60 U f4 B g30 e0 e2 U f0 B g30 e0 e2
STATE
TERM B g60 U f0 B g30 e0 e2 U f0 B g30 e0 e2
```

Target:

```text
RW r0
```

### test/term_rewriting/repair_action

- ID: `test:term_rewriting:72:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
VALID ALL_RULES_HOLD
FORM RULE K : L -> R
FORM START T
FORM GOAL T
FORM QUERY NORMAL_FORM
FORM TERM T
FORM RW K AT PATH
FORM HALT
RW REPLACES_MATCHING_SUBTERM_AT_PATH
HALT ONLY_WHEN_DONE
VALID TRACE_ALTERNATES_TERM_AND_RW
PROBLEM
RULE r0 : U f0 v0 -> U f1 v0
RULE r1 : U f1 B g30 e0 e2 -> U f2 B g30 e0 e2
RULE r2 : U f2 B g30 e0 e2 -> B g3 B g30 e0 e2 e1
RULE r3 : B g3 B g30 e0 e2 e1 -> U f4 B g30 e0 e2
RULE r4 : B g100 v0 v1 -> B g120 v0 v1
RULE r5 : B g101 v0 v1 -> B g121 v0 v1
START B g60 U f0 B g30 e0 e2 U f0 B g30 e0 e2
GOAL B g60 U f4 B g30 e0 e2 U f0 B g30 e0 e2
STATE
TERM B g60 U f0 B g30 e0 e2 U f0 B g30 e0 e2
RW r0
TERM B g60 U f1 B g30 e0 e2 U f0 B g31 e0 e2
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
TASK
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
VALID ALL_RULES_HOLD
FORM RULE K : L -> R
FORM START T
FORM GOAL T
FORM QUERY NORMAL_FORM
FORM TERM T
FORM RW K AT PATH
FORM HALT
RW REPLACES_MATCHING_SUBTERM_AT_PATH
HALT ONLY_WHEN_DONE
VALID TRACE_ALTERNATES_TERM_AND_RW
PROBLEM
RULE r0 : U f0 v0 -> U f1 v0
RULE r1 : U f1 B g30 e0 e2 -> U f2 B g30 e0 e2
RULE r2 : U f2 B g30 e0 e2 -> B g3 B g30 e0 e2 e1
RULE r3 : B g3 B g30 e0 e2 e1 -> U f4 B g30 e0 e2
RULE r4 : B g100 v0 v1 -> B g120 v0 v1
RULE r5 : B g101 v0 v1 -> B g121 v0 v1
START B g60 U f0 B g30 e0 e2 U f0 B g30 e0 e2
GOAL B g60 U f4 B g30 e0 e2 U f0 B g30 e0 e2
STATE
TERM B g60 U f0 B g30 e0 e2 U f0 B g30 e0 e2
RW r0
TERM B g60 U f1 B g30 e0 e2 U f0 B g30 e0 e2
RW r1
TERM B g60 U f2 B g30 e0 e2 U f0 B g30 e0 e2
RW r2
TERM B g60 B g3 B g30 e0 e2 e1 U f0 B g30 e0 e2
RW r3
TERM B g60 U f4 B g30 e0 e2 U f0 B g30 e0 e2
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
TASK
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
VALID ALL_RULES_HOLD
FORM PARENT A B
FORM QUERY ANCESTOR A C
FORM LINEAGE A ... C
EMPTY MEANS NO_LINEAGE
VALID LINEAGE USES_PARENT_BETWEEN_NEIGHBORS
DESCEND X STARTS_OR_EXTENDS_LINEAGE
DONE LINEAGE_FROM_QUERY_START_TO_TARGET
PROBLEM
PARENT e0 e1
PARENT e0 e5
PARENT e1 e2
PARENT e1 e6
PARENT e2 e3
PARENT e3 e4
PARENT e4 e7
PARENT e5 e8
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
TASK
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
VALID ALL_RULES_HOLD
FORM PARENT A B
FORM QUERY ANCESTOR A C
FORM LINEAGE A ... C
EMPTY MEANS NO_LINEAGE
VALID LINEAGE USES_PARENT_BETWEEN_NEIGHBORS
DESCEND X STARTS_OR_EXTENDS_LINEAGE
DONE LINEAGE_FROM_QUERY_START_TO_TARGET
PROBLEM
PARENT e0 e1
PARENT e0 e5
PARENT e1 e2
PARENT e1 e6
PARENT e2 e3
PARENT e3 e4
PARENT e4 e7
PARENT e5 e8
QUERY ANCESTOR e0 e4
STATE
LINEAGE e4
```

Target:

```text
REPLACE ROOT WITH e0
```

### test/tree_ancestry/verify

- ID: `test:tree_ancestry:54:verify:valid`

Source:

```text
MODE verify
TASK
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
VALID ALL_RULES_HOLD
FORM PARENT A B
FORM QUERY ANCESTOR A C
FORM LINEAGE A ... C
EMPTY MEANS NO_LINEAGE
VALID LINEAGE USES_PARENT_BETWEEN_NEIGHBORS
DESCEND X STARTS_OR_EXTENDS_LINEAGE
DONE LINEAGE_FROM_QUERY_START_TO_TARGET
PROBLEM
PARENT e0 e1
PARENT e0 e5
PARENT e1 e2
PARENT e1 e6
PARENT e2 e3
PARENT e3 e4
PARENT e4 e7
PARENT e5 e8
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
TASK
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
VALID ALL_RULES_HOLD
FORM EDGE A B
FORM QUERY REACH A C
FORM PATH A ... C
EMPTY MEANS NO_PATH
VALID PATH USES_EDGE_BETWEEN_NEIGHBORS
APPEND X STARTS_OR_EXTENDS_PATH
DONE PATH_FROM_QUERY_START_TO_TARGET
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e2 e3
EDGE e3 e4
EDGE e4 e1
EDGE e4 e5
EDGE e5 e0
EDGE e5 e1
EDGE e5 e4
QUERY REACH e0 e5
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
TASK
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
VALID ALL_RULES_HOLD
FORM QUERY REACH A C
FORM EDGE A B
FORM PATH A ... C
EMPTY MEANS NO_PATH
VALID PATH USES_EDGE_BETWEEN_NEIGHBORS
APPEND X STARTS_OR_EXTENDS_PATH
DONE PATH_FROM_QUERY_START_TO_TARGET
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e2 e3
EDGE e3 e4
EDGE e4 e1
EDGE e4 e5
EDGE e5 e0
EDGE e5 e1
EDGE e5 e4
QUERY REACH e0 e5
STATE
PATH e5
```

Target:

```text
REPLACE ROOT WITH e0
```

### train/graph_reachability/verify

- ID: `train:graph_reachability:0:verify:valid`

Source:

```text
MODE verify
TASK
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
VALID ALL_RULES_HOLD
FORM QUERY REACH A C
FORM EDGE A B
FORM PATH A ... C
EMPTY MEANS NO_PATH
VALID PATH USES_EDGE_BETWEEN_NEIGHBORS
APPEND X STARTS_OR_EXTENDS_PATH
DONE PATH_FROM_QUERY_START_TO_TARGET
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e2 e3
EDGE e3 e4
EDGE e4 e1
EDGE e4 e5
EDGE e5 e0
EDGE e5 e1
EDGE e5 e4
QUERY REACH e0 e5
STATE
PATH e0 e1 e2 e3 e4 e5
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
TASK
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
VALID ALL_RULES_HOLD
FORM HYP K : P
FORM HYP K : P -> Q
FORM GOAL Q
FORM DERIVE Q BY K FROM P
APPLY K ADDS_LICENSED_DERIVATION
VALID DERIVE_USES_KNOWN_FACT_OR_PRIOR_PREMISE
DONE GOAL_DERIVED
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p0 -> p8
HYP h4 : p2 -> p0
HYP h5 : p2 -> p1
GOAL p2
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
TASK
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
VALID ALL_RULES_HOLD
FORM HYP K : P
FORM HYP K : P -> Q
FORM GOAL Q
FORM DERIVE Q BY K FROM P
APPLY K ADDS_LICENSED_DERIVATION
VALID DERIVE_USES_KNOWN_FACT_OR_PRIOR_PREMISE
DONE GOAL_DERIVED
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p0 -> p8
HYP h4 : p2 -> p0
HYP h5 : p2 -> p1
GOAL p2
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
TASK
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
VALID ALL_RULES_HOLD
FORM HYP K : P
FORM HYP K : P -> Q
FORM GOAL Q
FORM DERIVE Q BY K FROM P
APPLY K ADDS_LICENSED_DERIVATION
VALID DERIVE_USES_KNOWN_FACT_OR_PRIOR_PREMISE
DONE GOAL_DERIVED
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p0 -> p8
HYP h4 : p2 -> p0
HYP h5 : p2 -> p1
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

- ID: `train:relation_composition:624:action:0`

Source:

```text
MODE action
TASK
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
VALID ALL_RULES_HOLD
FORM RULE RC = RA ; RB
FORM FACT R A B
FORM QUERY R A C
FORM DERIVE R A C VIA B
FOLLOW C VIA B ADDS_COMPOSED_FACT
VALID NEEDS_LEFT_FACT_RIGHT_FACT_AND_RULE
DONE QUERY_FACT_AVAILABLE
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e2 e3
FACT r2 e1 e2
QUERY r4 e0 e3
STATE
EMPTY
```

Target:

```text
FOLLOW e0 e2 VIA e1
```

### train/relation_composition/repair_action

- ID: `train:relation_composition:624:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
VALID ALL_RULES_HOLD
FORM RULE RC = RA ; RB
FORM FACT R A B
FORM QUERY R A C
FORM DERIVE R A C VIA B
FOLLOW C VIA B ADDS_COMPOSED_FACT
VALID NEEDS_LEFT_FACT_RIGHT_FACT_AND_RULE
DONE QUERY_FACT_AVAILABLE
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e2 e3
FACT r2 e1 e2
QUERY r4 e0 e3
STATE
DERIVE r3 e0 e2 VIA e0
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
TASK
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
VALID ALL_RULES_HOLD
FORM RULE RC = RA ; RB
FORM FACT R A B
FORM QUERY R A C
FORM DERIVE R A C VIA B
FOLLOW C VIA B ADDS_COMPOSED_FACT
VALID NEEDS_LEFT_FACT_RIGHT_FACT_AND_RULE
DONE QUERY_FACT_AVAILABLE
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e2 e3
FACT r2 e1 e2
QUERY r4 e0 e3
STATE
DERIVE r3 e0 e2 VIA e1
DERIVE r4 e0 e3 VIA e2
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
TASK
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
VALID ALL_RULES_HOLD
FORM RULE K : L -> R
FORM TERM T
FORM START T
FORM GOAL T
FORM QUERY NORMAL_FORM
FORM RW K AT PATH
FORM HALT
RW REPLACES_MATCHING_SUBTERM_AT_PATH
HALT ONLY_WHEN_DONE
VALID TRACE_ALTERNATES_TERM_AND_RW
PROBLEM
RULE r0 : U f0 e0 -> U f1 e0
RULE r1 : U f1 v0 -> U f2 v0
RULE r2 : U f2 v0 -> U f3 v0
RULE r3 : U f3 e0 -> B g4 e0 e1
RULE r4 : B g4 e0 e1 -> U f5 e0
RULE r5 : B g100 v0 v1 -> B g120 v0 v1
RULE r6 : U f101 v0 -> U f121 v0
START U f60 U f0 e0
QUERY NORMAL_FORM
STATE
TERM U f60 U f0 e0
```

Target:

```text
RW r0
```

### train/term_rewriting/repair_action

- ID: `train:term_rewriting:1368:repair_action:1`

Source:

```text
MODE repair_action
TASK
VALID ALL_RULES_HOLD
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
FORM RULE K : L -> R
FORM START T
FORM GOAL T
FORM QUERY NORMAL_FORM
FORM TERM T
FORM RW K AT PATH
FORM HALT
RW REPLACES_MATCHING_SUBTERM_AT_PATH
HALT ONLY_WHEN_DONE
VALID TRACE_ALTERNATES_TERM_AND_RW
PROBLEM
RULE r0 : U f0 e0 -> U f1 e0
RULE r1 : U f1 v0 -> U f2 v0
RULE r2 : U f2 v0 -> U f3 v0
RULE r3 : U f3 e0 -> B g4 e0 e1
RULE r4 : B g4 e0 e1 -> U f5 e0
RULE r5 : B g100 v0 v1 -> B g120 v0 v1
RULE r6 : U f101 v0 -> U f121 v0
START U f60 U f0 e0
QUERY NORMAL_FORM
STATE
TERM U f60 U f0 e0
RW r0
TERM U f61 U f1 e0
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
TASK
VALID ALL_RULES_HOLD
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
FORM RULE K : L -> R
FORM START T
FORM GOAL T
FORM QUERY NORMAL_FORM
FORM TERM T
FORM RW K AT PATH
FORM HALT
RW REPLACES_MATCHING_SUBTERM_AT_PATH
HALT ONLY_WHEN_DONE
VALID TRACE_ALTERNATES_TERM_AND_RW
PROBLEM
RULE r0 : U f0 e0 -> U f1 e0
RULE r1 : U f1 v0 -> U f2 v0
RULE r2 : U f2 v0 -> U f3 v0
RULE r3 : U f3 e0 -> B g4 e0 e1
RULE r4 : B g4 e0 e1 -> U f5 e0
RULE r5 : B g100 v0 v1 -> B g120 v0 v1
RULE r6 : U f101 v0 -> U f121 v0
START U f60 U f0 e0
QUERY NORMAL_FORM
STATE
TERM U f60 U f0 e0
RW r0
TERM U f60 U f1 e0
RW r1
TERM U f60 U f2 e0
RW r2
TERM U f60 U f3 e0
RW r3
TERM U f60 B g4 e0 e1
RW r4
TERM U f60 U f5 e0
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
TASK
OUT ONE_ACTION
ONE_ACTION MAKES_ONE_VALID_STEP
VALID ALL_RULES_HOLD
FORM PARENT A B
FORM QUERY ANCESTOR A C
FORM LINEAGE A ... C
EMPTY MEANS NO_LINEAGE
VALID LINEAGE USES_PARENT_BETWEEN_NEIGHBORS
DESCEND X STARTS_OR_EXTENDS_LINEAGE
DONE LINEAGE_FROM_QUERY_START_TO_TARGET
PROBLEM
PARENT e0 e1
PARENT e1 e2
PARENT e2 e3
PARENT e2 e5
PARENT e3 e4
PARENT e4 e6
PARENT e6 e7
QUERY ANCESTOR e0 e4
STATE
EMPTY
```

Target:

```text
DESCEND e0
```

### train/tree_ancestry/repair_action

- ID: `train:tree_ancestry:1056:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUT ONE_REPAIR_ACTION
ONE_REPAIR_ACTION FIXES_LOCAL_CORRUPTION
VALID ALL_RULES_HOLD
FORM PARENT A B
FORM QUERY ANCESTOR A C
FORM LINEAGE A ... C
EMPTY MEANS NO_LINEAGE
VALID LINEAGE USES_PARENT_BETWEEN_NEIGHBORS
DESCEND X STARTS_OR_EXTENDS_LINEAGE
DONE LINEAGE_FROM_QUERY_START_TO_TARGET
PROBLEM
PARENT e0 e1
PARENT e1 e2
PARENT e2 e3
PARENT e2 e5
PARENT e3 e4
PARENT e4 e6
PARENT e6 e7
QUERY ANCESTOR e0 e4
STATE
LINEAGE e4
```

Target:

```text
REPLACE ROOT WITH e0
```

### train/tree_ancestry/verify

- ID: `train:tree_ancestry:1056:verify:valid`

Source:

```text
MODE verify
TASK
OUT VALID_OR_INVALID_CODE
INVALID_CODE IS_FIRST_BROKEN_RULE
VALID ALL_RULES_HOLD
FORM PARENT A B
FORM QUERY ANCESTOR A C
FORM LINEAGE A ... C
EMPTY MEANS NO_LINEAGE
VALID LINEAGE USES_PARENT_BETWEEN_NEIGHBORS
DESCEND X STARTS_OR_EXTENDS_LINEAGE
DONE LINEAGE_FROM_QUERY_START_TO_TARGET
PROBLEM
PARENT e0 e1
PARENT e1 e2
PARENT e2 e3
PARENT e2 e5
PARENT e3 e4
PARENT e4 e6
PARENT e6 e7
QUERY ANCESTOR e0 e4
STATE
LINEAGE e0 e1 e2 e3 e4
```

Target:

```text
VALID
```
