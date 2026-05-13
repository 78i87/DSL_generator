# Dataset Audit

- Data dir: `data/symbolic-0_49-term-rule-index-actions-alpha`
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

- Inputs shape: `[19827, 1008]`
- Labels shape: `[19827, 1008]`
- Seq len: `1008`
- Vocab size: `473`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `19827`

### test

- Inputs shape: `[1202, 1008]`
- Labels shape: `[1202, 1008]`
- Seq len: `1008`
- Vocab size: `473`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1202`

### ood

- Inputs shape: `[1856, 1008]`
- Labels shape: `[1856, 1008]`
- Seq len: `1008`
- Vocab size: `473`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1856`

## Samples

### ood/graph_reachability/action

- ID: `ood:graph_reachability:0:action:0`

Source:

```text
MODE action
TASK
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX QUERY REACH A C : DONE needs PATH from A to C
SYNTAX EDGE A B : directed step from A to B
SYNTAX PATH A B C : ordered visited nodes
STATE EMPTY means no PATH has started
VALID PATH requires each adjacent pair has EDGE
ACTION APPEND X starts with query start or extends from last node by EDGE
DONE when PATH starts at query start and ends at query target
DEMO EDGE X0 X1 ; EDGE X1 X2 ; QUERY REACH X0 X2 ; EMPTY => APPEND X0 ; PATH X0 => APPEND X1
PROBLEM
EDGE e8 e11
EDGE e11 e5
EDGE e4 e2
EDGE e5 e8
EDGE e5 e7
EDGE e7 e2
EDGE e7 e0
EDGE e2 e1
EDGE e1 e5
EDGE e1 e9
EDGE e9 e3
EDGE e3 e6
EDGE e6 e11
QUERY REACH e8 e6
STATE
EMPTY
```

Target:

```text
APPEND e8
```

### ood/graph_reachability/repair_action

- ID: `ood:graph_reachability:0:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX QUERY REACH A C : DONE needs PATH from A to C
SYNTAX EDGE A B : directed step from A to B
SYNTAX PATH A B C : ordered visited nodes
STATE EMPTY means no PATH has started
VALID PATH requires each adjacent pair has EDGE
ACTION APPEND X starts with query start or extends from last node by EDGE
DONE when PATH starts at query start and ends at query target
DEMO EDGE X0 X1 ; EDGE X1 X2 ; QUERY REACH X0 X2 ; EMPTY => APPEND X0 ; PATH X0 => APPEND X1
PROBLEM
EDGE e8 e11
EDGE e11 e5
EDGE e4 e2
EDGE e5 e8
EDGE e5 e7
EDGE e7 e2
EDGE e7 e0
EDGE e2 e1
EDGE e1 e5
EDGE e1 e9
EDGE e9 e3
EDGE e3 e6
EDGE e6 e11
QUERY REACH e8 e6
STATE
PATH e6
```

Target:

```text
REPLACE ROOT WITH e8
```

### ood/graph_reachability/verify

- ID: `ood:graph_reachability:0:verify:valid`

Source:

```text
MODE verify
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX QUERY REACH A C : DONE needs PATH from A to C
SYNTAX EDGE A B : directed step from A to B
SYNTAX PATH A B C : ordered visited nodes
STATE EMPTY means no PATH has started
VALID PATH requires each adjacent pair has EDGE
ACTION APPEND X starts with query start or extends from last node by EDGE
DONE when PATH starts at query start and ends at query target
DEMO EDGE X0 X1 ; EDGE X1 X2 ; QUERY REACH X0 X2 ; EMPTY => APPEND X0 ; PATH X0 => APPEND X1
PROBLEM
EDGE e8 e11
EDGE e11 e5
EDGE e4 e2
EDGE e5 e8
EDGE e5 e7
EDGE e7 e2
EDGE e7 e0
EDGE e2 e1
EDGE e1 e5
EDGE e1 e9
EDGE e9 e3
EDGE e3 e6
EDGE e6 e11
QUERY REACH e8 e6
STATE
PATH e8 e11 e5 e7 e2 e1 e9 e3 e6
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
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX HYP K : P : K proves fact P
SYNTAX HYP K : P -> Q : K maps known P to Q
SYNTAX GOAL Q : DONE needs Q derived
SYNTAX DERIVE Q BY K FROM P : Q follows by implication K and prior P
ACTION APPLY K adds the derivation licensed by K
VALID proof uses only known facts and prior derived premises
DONE when GOAL proposition is derived
DEMO HYP K20 : X0 ; HYP K21 : X0 -> X1 ; GOAL X1 ; EMPTY => APPLY K20 ; DERIVE X0 BY K20 => APPLY K21
PROBLEM
HYP h3 : p2
HYP h10 : p2 -> p9
HYP h12 : p9 -> p7
HYP h6 : p7 -> p1
HYP h17 : p1 -> p5
HYP h13 : p5 -> p3
HYP h5 : p3 -> p6
HYP h7 : p6 -> p4
HYP h1 : p2 -> p7
HYP h8 : p9 -> p5
HYP h11 : p9 -> p0
HYP h9 : p6 -> p3
HYP h4 : p6 -> p10
HYP h16 : p4 -> p10
HYP h0 : p8 -> p2
HYP h2 : p8 -> p5
HYP h15 : p0 -> p5
HYP h999 : p10 -> p1
GOAL p4
STATE
EMPTY
```

Target:

```text
APPLY h3
```

### ood/implication_chains/repair_action

- ID: `ood:implication_chains:18:repair_action:1`

Source:

```text
MODE repair_action
TASK
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
SYNTAX HYP K : P : K proves fact P
SYNTAX GOAL Q : DONE needs Q derived
SYNTAX HYP K : P -> Q : K maps known P to Q
SYNTAX DERIVE Q BY K FROM P : Q follows by implication K and prior P
ACTION APPLY K adds the derivation licensed by K
VALID proof uses only known facts and prior derived premises
DONE when GOAL proposition is derived
DEMO HYP K10 : N0 ; HYP K11 : N0 -> N1 ; GOAL N1 ; EMPTY => APPLY K10 ; DERIVE N0 BY K10 => APPLY K11
PROBLEM
HYP h3 : p2
HYP h10 : p2 -> p9
HYP h12 : p9 -> p7
HYP h6 : p7 -> p1
HYP h17 : p1 -> p5
HYP h13 : p5 -> p3
HYP h5 : p3 -> p6
HYP h7 : p6 -> p4
HYP h1 : p2 -> p7
HYP h8 : p9 -> p5
HYP h11 : p9 -> p0
HYP h9 : p6 -> p3
HYP h4 : p6 -> p10
HYP h16 : p4 -> p10
HYP h0 : p8 -> p2
HYP h2 : p8 -> p5
HYP h15 : p0 -> p5
HYP h999 : p10 -> p1
GOAL p4
STATE
DERIVE p2 BY h14
```

Target:

```text
REPLACE FIRST HYP h3
```

### ood/implication_chains/verify

- ID: `ood:implication_chains:18:verify:valid`

Source:

```text
MODE verify
TASK
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
SYNTAX HYP K : P : K proves fact P
SYNTAX GOAL Q : DONE needs Q derived
SYNTAX HYP K : P -> Q : K maps known P to Q
SYNTAX DERIVE Q BY K FROM P : Q follows by implication K and prior P
ACTION APPLY K adds the derivation licensed by K
VALID proof uses only known facts and prior derived premises
DONE when GOAL proposition is derived
DEMO HYP K10 : N0 ; HYP K11 : N0 -> N1 ; GOAL N1 ; EMPTY => APPLY K10 ; DERIVE N0 BY K10 => APPLY K11
PROBLEM
HYP h3 : p2
HYP h10 : p2 -> p9
HYP h12 : p9 -> p7
HYP h6 : p7 -> p1
HYP h17 : p1 -> p5
HYP h13 : p5 -> p3
HYP h5 : p3 -> p6
HYP h7 : p6 -> p4
HYP h1 : p2 -> p7
HYP h8 : p9 -> p5
HYP h11 : p9 -> p0
HYP h9 : p6 -> p3
HYP h4 : p6 -> p10
HYP h16 : p4 -> p10
HYP h0 : p8 -> p2
HYP h2 : p8 -> p5
HYP h15 : p0 -> p5
HYP h999 : p10 -> p1
GOAL p4
STATE
DERIVE p2 BY h3
DERIVE p9 BY h10 FROM p2
DERIVE p7 BY h12 FROM p9
DERIVE p1 BY h6 FROM p7
DERIVE p5 BY h17 FROM p1
DERIVE p3 BY h13 FROM p5
DERIVE p6 BY h5 FROM p3
DERIVE p4 BY h7 FROM p6
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
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE RC = RA ; RB : compose RA then RB through a shared middle
SYNTAX FACT R A B : relation R holds from A to B
SYNTAX QUERY R A C : DONE needs relation R from A to C
SYNTAX DERIVE R A C VIA B : composed fact uses middle B
ACTION FOLLOW C VIA B adds the next composed fact ending at C
VALID derivation requires matching left fact, right fact, and rule
DONE when queried relation fact is available
DEMO FACT REL20 X0 X1 ; FACT REL21 X1 X2 ; RULE REL22 = REL20 ; REL21 ; QUERY REL22 X0 X2 ; EMPTY => FOLLOW X2 VIA X1
PROBLEM
FACT r4 e9 e4
FACT r3 e4 e6
FACT r10 e6 e2
FACT r5 e2 e7
FACT r6 e7 e0
FACT r8 e0 e10
FACT r11 e10 e11
FACT r1 e11 e1
RULE r0 = r4 ; r3
RULE r12 = r0 ; r10
RULE r13 = r12 ; r5
RULE r2 = r13 ; r6
RULE r9 = r2 ; r8
RULE r7 = r9 ; r11
RULE r14 = r7 ; r1
FACT r4 e9 e8
FACT r10 e0 e1
FACT r6 e1 e5
FACT r8 e4 e0
FACT r8 e7 e3
FACT r11 e1 e2
QUERY r14 e9 e1
STATE
EMPTY
```

Target:

```text
FOLLOW e9 e6 VIA e4
```

### ood/relation_composition/repair_action

- ID: `ood:relation_composition:36:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX FACT R A B : relation R holds from A to B
SYNTAX RULE RC = RA ; RB : compose RA then RB through a shared middle
SYNTAX QUERY R A C : DONE needs relation R from A to C
SYNTAX DERIVE R A C VIA B : composed fact uses middle B
ACTION FOLLOW C VIA B adds the next composed fact ending at C
VALID derivation requires matching left fact, right fact, and rule
DONE when queried relation fact is available
DEMO FACT REL00 A0 A1 ; FACT REL01 A1 A2 ; RULE REL02 = REL00 ; REL01 ; QUERY REL02 A0 A2 ; EMPTY => FOLLOW A2 VIA A1
PROBLEM
FACT r4 e9 e4
FACT r3 e4 e6
FACT r10 e6 e2
FACT r5 e2 e7
FACT r6 e7 e0
FACT r8 e0 e10
FACT r11 e10 e11
FACT r1 e11 e1
RULE r0 = r4 ; r3
RULE r12 = r0 ; r10
RULE r13 = r12 ; r5
RULE r2 = r13 ; r6
RULE r9 = r2 ; r8
RULE r7 = r9 ; r11
RULE r14 = r7 ; r1
FACT r4 e9 e8
FACT r10 e0 e1
FACT r6 e1 e5
FACT r8 e4 e0
FACT r8 e7 e3
FACT r11 e1 e2
QUERY r14 e9 e1
STATE
DERIVE r0 e9 e6 VIA e9
```

Target:

```text
REPLACE FIRST VIA e4
```

### ood/relation_composition/verify

- ID: `ood:relation_composition:36:verify:valid`

Source:

```text
MODE verify
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX FACT R A B : relation R holds from A to B
SYNTAX RULE RC = RA ; RB : compose RA then RB through a shared middle
SYNTAX QUERY R A C : DONE needs relation R from A to C
SYNTAX DERIVE R A C VIA B : composed fact uses middle B
ACTION FOLLOW C VIA B adds the next composed fact ending at C
VALID derivation requires matching left fact, right fact, and rule
DONE when queried relation fact is available
DEMO FACT REL00 A0 A1 ; FACT REL01 A1 A2 ; RULE REL02 = REL00 ; REL01 ; QUERY REL02 A0 A2 ; EMPTY => FOLLOW A2 VIA A1
PROBLEM
FACT r4 e9 e4
FACT r3 e4 e6
FACT r10 e6 e2
FACT r5 e2 e7
FACT r6 e7 e0
FACT r8 e0 e10
FACT r11 e10 e11
FACT r1 e11 e1
RULE r0 = r4 ; r3
RULE r12 = r0 ; r10
RULE r13 = r12 ; r5
RULE r2 = r13 ; r6
RULE r9 = r2 ; r8
RULE r7 = r9 ; r11
RULE r14 = r7 ; r1
FACT r4 e9 e8
FACT r10 e0 e1
FACT r6 e1 e5
FACT r8 e4 e0
FACT r8 e7 e3
FACT r11 e1 e2
QUERY r14 e9 e1
STATE
DERIVE r0 e9 e6 VIA e4
DERIVE r12 e9 e2 VIA e6
DERIVE r13 e9 e7 VIA e2
DERIVE r2 e9 e0 VIA e7
DERIVE r9 e9 e10 VIA e0
DERIVE r7 e9 e11 VIA e10
DERIVE r14 e9 e1 VIA e11
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
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX TERM T : current expression
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
ACTION RW RULE N AT PATH uses RULE line N and rewrites the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K20 : OP20 X0 -> OP21 X0 ; START OP20 X0 ; GOAL OP21 X0 ; TERM OP20 X0 => RW RULE 0 AT ROOT
PROBLEM
RULE r1 : B g31 B g107 B g126 e0 e72 e2 e1 -> U f125 B g107 B g126 e0 e72 e2
RULE r0 : U f125 v1 -> U f124 v1
RULE r14 : U f124 B g107 B g126 e0 e72 e2 -> B g3 B g107 B g126 e0 e72 e2 e1
RULE r10 : B g3 B g107 B g126 e0 e72 e2 e1 -> U f4 B g107 B g126 e0 e72 e2
RULE r4 : U f4 v1 -> U f121 v1
RULE r9 : U f121 B g107 B g126 e0 e72 e2 -> B g7 B g107 B g126 e0 e72 e2 e1
RULE r6 : B g7 B g107 B g126 e0 e72 e2 e1 -> B g120 B g107 B g126 e0 e72 e2 e1
RULE r15 : B g120 B g107 B g126 e0 e72 e2 e1 -> U f128 B g107 B g126 e0 e72 e2
RULE r5 : B g6 v1 v0 -> B g62 v1 v0
RULE r2 : U f105 v1 -> U f2 v1
RULE r16 : U f101 v1 -> U f60 v1
RULE r13 : U f122 v1 -> U f5 v1
RULE r12 : U f123 v1 -> U f104 v1
RULE r3 : U f61 v1 -> U f1 v1
RULE r11 : B g30 v1 v0 -> B g8 v1 v0
RULE r8 : B g100 v1 v0 -> B g0 v1 v0
RULE r7 : U f8 v1 -> U f108 v1
START B g106 U f102 U f103 B g31 B g107 B g126 e0 e72 e2 e1 e3
QUERY NORMAL_FORM
STATE
TERM B g106 U f102 U f103 B g31 B g107 B g126 e0 e72 e2 e1 e3
```

Target:

```text
RW RULE 0
```

### ood/term_rewriting/repair_action

- ID: `ood:term_rewriting:72:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
SYNTAX TERM T : current expression
ACTION RW RULE N AT PATH uses RULE line N and rewrites the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K00 : OP00 A0 -> OP01 A0 ; START OP00 A0 ; GOAL OP01 A0 ; TERM OP00 A0 => RW RULE 0 AT ROOT
PROBLEM
RULE r1 : B g31 B g107 B g126 e0 e72 e2 e1 -> U f125 B g107 B g126 e0 e72 e2
RULE r0 : U f125 v1 -> U f124 v1
RULE r14 : U f124 B g107 B g126 e0 e72 e2 -> B g3 B g107 B g126 e0 e72 e2 e1
RULE r10 : B g3 B g107 B g126 e0 e72 e2 e1 -> U f4 B g107 B g126 e0 e72 e2
RULE r4 : U f4 v1 -> U f121 v1
RULE r9 : U f121 B g107 B g126 e0 e72 e2 -> B g7 B g107 B g126 e0 e72 e2 e1
RULE r6 : B g7 B g107 B g126 e0 e72 e2 e1 -> B g120 B g107 B g126 e0 e72 e2 e1
RULE r15 : B g120 B g107 B g126 e0 e72 e2 e1 -> U f128 B g107 B g126 e0 e72 e2
RULE r5 : B g6 v1 v0 -> B g62 v1 v0
RULE r2 : U f105 v1 -> U f2 v1
RULE r16 : U f101 v1 -> U f60 v1
RULE r13 : U f122 v1 -> U f5 v1
RULE r12 : U f123 v1 -> U f104 v1
RULE r3 : U f61 v1 -> U f1 v1
RULE r11 : B g30 v1 v0 -> B g8 v1 v0
RULE r8 : B g100 v1 v0 -> B g0 v1 v0
RULE r7 : U f8 v1 -> U f108 v1
START B g106 U f102 U f103 B g31 B g107 B g126 e0 e72 e2 e1 e3
QUERY NORMAL_FORM
STATE
TERM B g106 U f102 U f103 B g31 B g107 B g126 e0 e72 e2 e1 e3
RW r1
TERM B g106 U f102 U f103 U f125 B g107 B g126 e0 e2 e2 e3
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
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX TERM T : current expression
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
ACTION RW RULE N AT PATH uses RULE line N and rewrites the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K20 : OP20 X0 -> OP21 X0 ; START OP20 X0 ; GOAL OP21 X0 ; TERM OP20 X0 => RW RULE 0 AT ROOT
PROBLEM
RULE r1 : B g31 B g107 B g126 e0 e72 e2 e1 -> U f125 B g107 B g126 e0 e72 e2
RULE r0 : U f125 v1 -> U f124 v1
RULE r14 : U f124 B g107 B g126 e0 e72 e2 -> B g3 B g107 B g126 e0 e72 e2 e1
RULE r10 : B g3 B g107 B g126 e0 e72 e2 e1 -> U f4 B g107 B g126 e0 e72 e2
RULE r4 : U f4 v1 -> U f121 v1
RULE r9 : U f121 B g107 B g126 e0 e72 e2 -> B g7 B g107 B g126 e0 e72 e2 e1
RULE r6 : B g7 B g107 B g126 e0 e72 e2 e1 -> B g120 B g107 B g126 e0 e72 e2 e1
RULE r15 : B g120 B g107 B g126 e0 e72 e2 e1 -> U f128 B g107 B g126 e0 e72 e2
RULE r5 : B g6 v1 v0 -> B g62 v1 v0
RULE r2 : U f105 v1 -> U f2 v1
RULE r16 : U f101 v1 -> U f60 v1
RULE r13 : U f122 v1 -> U f5 v1
RULE r12 : U f123 v1 -> U f104 v1
RULE r3 : U f61 v1 -> U f1 v1
RULE r11 : B g30 v1 v0 -> B g8 v1 v0
RULE r8 : B g100 v1 v0 -> B g0 v1 v0
RULE r7 : U f8 v1 -> U f108 v1
START B g106 U f102 U f103 B g31 B g107 B g126 e0 e72 e2 e1 e3
QUERY NORMAL_FORM
STATE
TERM B g106 U f102 U f103 B g31 B g107 B g126 e0 e72 e2 e1 e3
RW r1
TERM B g106 U f102 U f103 U f125 B g107 B g126 e0 e72 e2 e3
RW r0
TERM B g106 U f102 U f103 U f124 B g107 B g126 e0 e72 e2 e3
RW r14
TERM B g106 U f102 U f103 B g3 B g107 B g126 e0 e72 e2 e1 e3
RW r10
TERM B g106 U f102 U f103 U f4 B g107 B g126 e0 e72 e2 e3
RW r4
TERM B g106 U f102 U f103 U f121 B g107 B g126 e0 e72 e2 e3
RW r9
TERM B g106 U f102 U f103 B g7 B g107 B g126 e0 e72 e2 e1 e3
RW r6
TERM B g106 U f102 U f103 B g120 B g107 B g126 e0 e72 e2 e1 e3
RW r15
TERM B g106 U f102 U f103 U f128 B g107 B g126 e0 e72 e2 e3
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
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX PARENT A B : A is direct parent of B
SYNTAX QUERY ANCESTOR A C : DONE needs lineage from A to C
SYNTAX LINEAGE A B C : ordered ancestor chain
STATE EMPTY means no lineage has started
VALID LINEAGE starts at query ancestor and follows PARENT steps
ACTION DESCEND X starts with query ancestor or appends a child of last node
DONE when LINEAGE ends at query target
DEMO PARENT A0 A1 ; PARENT A1 A2 ; QUERY ANCESTOR A0 A2 ; EMPTY => DESCEND A0 ; LINEAGE A0 => DESCEND A1
PROBLEM
PARENT e6 e0
PARENT e0 e13
PARENT e0 e5
PARENT e5 e3
PARENT e3 e7
PARENT e7 e12
PARENT e7 e2
PARENT e2 e1
PARENT e2 e4
PARENT e1 e10
PARENT e10 e11
PARENT e10 e8
PARENT e8 e9
QUERY ANCESTOR e6 e8
STATE
EMPTY
```

Target:

```text
DESCEND e6
```

### ood/tree_ancestry/repair_action

- ID: `ood:tree_ancestry:54:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX PARENT A B : A is direct parent of B
SYNTAX QUERY ANCESTOR A C : DONE needs lineage from A to C
SYNTAX LINEAGE A B C : ordered ancestor chain
STATE EMPTY means no lineage has started
VALID LINEAGE starts at query ancestor and follows PARENT steps
ACTION DESCEND X starts with query ancestor or appends a child of last node
DONE when LINEAGE ends at query target
DEMO PARENT A0 A1 ; PARENT A1 A2 ; QUERY ANCESTOR A0 A2 ; EMPTY => DESCEND A0 ; LINEAGE A0 => DESCEND A1
PROBLEM
PARENT e6 e0
PARENT e0 e13
PARENT e0 e5
PARENT e5 e3
PARENT e3 e7
PARENT e7 e12
PARENT e7 e2
PARENT e2 e1
PARENT e2 e4
PARENT e1 e10
PARENT e10 e11
PARENT e10 e8
PARENT e8 e9
QUERY ANCESTOR e6 e8
STATE
LINEAGE e8
```

Target:

```text
REPLACE ROOT WITH e6
```

### ood/tree_ancestry/verify

- ID: `ood:tree_ancestry:54:verify:valid`

Source:

```text
MODE verify
TASK
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
SYNTAX QUERY ANCESTOR A C : DONE needs lineage from A to C
SYNTAX PARENT A B : A is direct parent of B
SYNTAX LINEAGE A B C : ordered ancestor chain
STATE EMPTY means no lineage has started
VALID LINEAGE starts at query ancestor and follows PARENT steps
ACTION DESCEND X starts with query ancestor or appends a child of last node
DONE when LINEAGE ends at query target
DEMO PARENT N0 N1 ; PARENT N1 N2 ; QUERY ANCESTOR N0 N2 ; EMPTY => DESCEND N0 ; LINEAGE N0 => DESCEND N1
PROBLEM
PARENT e6 e0
PARENT e0 e13
PARENT e0 e5
PARENT e5 e3
PARENT e3 e7
PARENT e7 e12
PARENT e7 e2
PARENT e2 e1
PARENT e2 e4
PARENT e1 e10
PARENT e10 e11
PARENT e10 e8
PARENT e8 e9
QUERY ANCESTOR e6 e8
STATE
LINEAGE e6 e0 e5 e3 e7 e2 e1 e10 e8
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
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX EDGE A B : directed step from A to B
SYNTAX QUERY REACH A C : DONE needs PATH from A to C
SYNTAX PATH A B C : ordered visited nodes
STATE EMPTY means no PATH has started
VALID PATH requires each adjacent pair has EDGE
ACTION APPEND X starts with query start or extends from last node by EDGE
DONE when PATH starts at query start and ends at query target
DEMO EDGE A0 A1 ; EDGE A1 A2 ; QUERY REACH A0 A2 ; EMPTY => APPEND A0 ; PATH A0 => APPEND A1
PROBLEM
EDGE e7 e4
EDGE e4 e6
EDGE e6 e2
EDGE e6 e1
EDGE e2 e0
EDGE e1 e3
EDGE e1 e5
EDGE e5 e4
EDGE e8 e7
QUERY REACH e7 e0
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
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX EDGE A B : directed step from A to B
SYNTAX QUERY REACH A C : DONE needs PATH from A to C
SYNTAX PATH A B C : ordered visited nodes
STATE EMPTY means no PATH has started
VALID PATH requires each adjacent pair has EDGE
ACTION APPEND X starts with query start or extends from last node by EDGE
DONE when PATH starts at query start and ends at query target
DEMO EDGE A0 A1 ; EDGE A1 A2 ; QUERY REACH A0 A2 ; EMPTY => APPEND A0 ; PATH A0 => APPEND A1
PROBLEM
EDGE e7 e4
EDGE e4 e6
EDGE e6 e2
EDGE e6 e1
EDGE e2 e0
EDGE e1 e3
EDGE e1 e5
EDGE e5 e4
EDGE e8 e7
QUERY REACH e7 e0
STATE
PATH e0
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
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX QUERY REACH A C : DONE needs PATH from A to C
SYNTAX EDGE A B : directed step from A to B
SYNTAX PATH A B C : ordered visited nodes
STATE EMPTY means no PATH has started
VALID PATH requires each adjacent pair has EDGE
ACTION APPEND X starts with query start or extends from last node by EDGE
DONE when PATH starts at query start and ends at query target
DEMO EDGE X0 X1 ; EDGE X1 X2 ; QUERY REACH X0 X2 ; EMPTY => APPEND X0 ; PATH X0 => APPEND X1
PROBLEM
EDGE e7 e4
EDGE e4 e6
EDGE e6 e2
EDGE e6 e1
EDGE e2 e0
EDGE e1 e3
EDGE e1 e5
EDGE e5 e4
EDGE e8 e7
QUERY REACH e7 e0
STATE
PATH e7 e4 e6 e2 e0
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
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX HYP K : P : K proves fact P
SYNTAX HYP K : P -> Q : K maps known P to Q
SYNTAX GOAL Q : DONE needs Q derived
SYNTAX DERIVE Q BY K FROM P : Q follows by implication K and prior P
ACTION APPLY K adds the derivation licensed by K
VALID proof uses only known facts and prior derived premises
DONE when GOAL proposition is derived
DEMO HYP K00 : A0 ; HYP K01 : A0 -> A1 ; GOAL A1 ; EMPTY => APPLY K00 ; DERIVE A0 BY K00 => APPLY K01
PROBLEM
HYP h7 : p2
HYP h0 : p2 -> p3
HYP h6 : p3 -> p0
HYP h999 : p0 -> p1
HYP h2 : p2 -> p0
HYP h5 : p3 -> p2
HYP h4 : p3 -> p1
HYP h3 : p1 -> p3
GOAL p1
STATE
EMPTY
```

Target:

```text
APPLY h7
```

### test/implication_chains/repair_action

- ID: `test:implication_chains:18:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX HYP K : P : K proves fact P
SYNTAX HYP K : P -> Q : K maps known P to Q
SYNTAX GOAL Q : DONE needs Q derived
SYNTAX DERIVE Q BY K FROM P : Q follows by implication K and prior P
ACTION APPLY K adds the derivation licensed by K
VALID proof uses only known facts and prior derived premises
DONE when GOAL proposition is derived
DEMO HYP K20 : X0 ; HYP K21 : X0 -> X1 ; GOAL X1 ; EMPTY => APPLY K20 ; DERIVE X0 BY K20 => APPLY K21
PROBLEM
HYP h7 : p2
HYP h0 : p2 -> p3
HYP h6 : p3 -> p0
HYP h999 : p0 -> p1
HYP h2 : p2 -> p0
HYP h5 : p3 -> p2
HYP h4 : p3 -> p1
HYP h3 : p1 -> p3
GOAL p1
STATE
DERIVE p2 BY h1
```

Target:

```text
REPLACE FIRST HYP h7
```

### test/implication_chains/verify

- ID: `test:implication_chains:18:verify:valid`

Source:

```text
MODE verify
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX HYP K : P : K proves fact P
SYNTAX HYP K : P -> Q : K maps known P to Q
SYNTAX GOAL Q : DONE needs Q derived
SYNTAX DERIVE Q BY K FROM P : Q follows by implication K and prior P
ACTION APPLY K adds the derivation licensed by K
VALID proof uses only known facts and prior derived premises
DONE when GOAL proposition is derived
DEMO HYP K00 : A0 ; HYP K01 : A0 -> A1 ; GOAL A1 ; EMPTY => APPLY K00 ; DERIVE A0 BY K00 => APPLY K01
PROBLEM
HYP h7 : p2
HYP h0 : p2 -> p3
HYP h6 : p3 -> p0
HYP h999 : p0 -> p1
HYP h2 : p2 -> p0
HYP h5 : p3 -> p2
HYP h4 : p3 -> p1
HYP h3 : p1 -> p3
GOAL p1
STATE
DERIVE p2 BY h7
DERIVE p3 BY h0 FROM p2
DERIVE p0 BY h6 FROM p3
DERIVE p1 BY h999 FROM p0
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
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
SYNTAX FACT R A B : relation R holds from A to B
SYNTAX RULE RC = RA ; RB : compose RA then RB through a shared middle
SYNTAX QUERY R A C : DONE needs relation R from A to C
SYNTAX DERIVE R A C VIA B : composed fact uses middle B
ACTION FOLLOW C VIA B adds the next composed fact ending at C
VALID derivation requires matching left fact, right fact, and rule
DONE when queried relation fact is available
DEMO FACT REL10 N0 N1 ; FACT REL11 N1 N2 ; RULE REL12 = REL10 ; REL11 ; QUERY REL12 N0 N2 ; EMPTY => FOLLOW N2 VIA N1
PROBLEM
FACT r3 e5 e3
FACT r4 e3 e0
FACT r1 e0 e2
FACT r6 e2 e1
FACT r7 e1 e4
RULE r5 = r3 ; r4
RULE r8 = r5 ; r1
RULE r0 = r8 ; r6
RULE r2 = r0 ; r7
FACT r3 e0 e4
FACT r4 e2 e4
FACT r4 e4 e0
FACT r1 e0 e4
FACT r6 e4 e0
QUERY r2 e5 e4
STATE
EMPTY
```

Target:

```text
FOLLOW e5 e0 VIA e3
```

### test/relation_composition/repair_action

- ID: `test:relation_composition:36:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE RC = RA ; RB : compose RA then RB through a shared middle
SYNTAX FACT R A B : relation R holds from A to B
SYNTAX QUERY R A C : DONE needs relation R from A to C
SYNTAX DERIVE R A C VIA B : composed fact uses middle B
ACTION FOLLOW C VIA B adds the next composed fact ending at C
VALID derivation requires matching left fact, right fact, and rule
DONE when queried relation fact is available
DEMO FACT REL20 X0 X1 ; FACT REL21 X1 X2 ; RULE REL22 = REL20 ; REL21 ; QUERY REL22 X0 X2 ; EMPTY => FOLLOW X2 VIA X1
PROBLEM
FACT r3 e5 e3
FACT r4 e3 e0
FACT r1 e0 e2
FACT r6 e2 e1
FACT r7 e1 e4
RULE r5 = r3 ; r4
RULE r8 = r5 ; r1
RULE r0 = r8 ; r6
RULE r2 = r0 ; r7
FACT r3 e0 e4
FACT r4 e2 e4
FACT r4 e4 e0
FACT r1 e0 e4
FACT r6 e4 e0
QUERY r2 e5 e4
STATE
DERIVE r5 e5 e0 VIA e5
```

Target:

```text
REPLACE FIRST VIA e3
```

### test/relation_composition/verify

- ID: `test:relation_composition:36:verify:valid`

Source:

```text
MODE verify
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE RC = RA ; RB : compose RA then RB through a shared middle
SYNTAX FACT R A B : relation R holds from A to B
SYNTAX QUERY R A C : DONE needs relation R from A to C
SYNTAX DERIVE R A C VIA B : composed fact uses middle B
ACTION FOLLOW C VIA B adds the next composed fact ending at C
VALID derivation requires matching left fact, right fact, and rule
DONE when queried relation fact is available
DEMO FACT REL20 X0 X1 ; FACT REL21 X1 X2 ; RULE REL22 = REL20 ; REL21 ; QUERY REL22 X0 X2 ; EMPTY => FOLLOW X2 VIA X1
PROBLEM
FACT r3 e5 e3
FACT r4 e3 e0
FACT r1 e0 e2
FACT r6 e2 e1
FACT r7 e1 e4
RULE r5 = r3 ; r4
RULE r8 = r5 ; r1
RULE r0 = r8 ; r6
RULE r2 = r0 ; r7
FACT r3 e0 e4
FACT r4 e2 e4
FACT r4 e4 e0
FACT r1 e0 e4
FACT r6 e4 e0
QUERY r2 e5 e4
STATE
DERIVE r5 e5 e0 VIA e3
DERIVE r8 e5 e2 VIA e0
DERIVE r0 e5 e1 VIA e2
DERIVE r2 e5 e4 VIA e1
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
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
SYNTAX TERM T : current expression
ACTION RW RULE N AT PATH uses RULE line N and rewrites the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K00 : OP00 A0 -> OP01 A0 ; START OP00 A0 ; GOAL OP01 A0 ; TERM OP00 A0 => RW RULE 0 AT ROOT
PROBLEM
RULE r0 : U f4 v1 -> U f1 v1
RULE r4 : U f1 B g31 e1 e2 -> U f2 B g31 e1 e2
RULE r3 : U f2 B g31 e1 e2 -> B g3 B g31 e1 e2 e0
RULE r5 : B g3 B g31 e1 e2 e0 -> U f0 B g31 e1 e2
RULE r2 : B g60 v1 v0 -> B g120 v1 v0
RULE r1 : B g101 v1 v0 -> B g30 v1 v0
START B g121 U f4 B g31 e1 e2 U f4 B g31 e1 e2
GOAL B g121 U f0 B g31 e1 e2 U f4 B g31 e1 e2
STATE
TERM B g121 U f4 B g31 e1 e2 U f4 B g31 e1 e2
```

Target:

```text
RW RULE 0
```

### test/term_rewriting/repair_action

- ID: `test:term_rewriting:72:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
SYNTAX TERM T : current expression
ACTION RW RULE N AT PATH uses RULE line N and rewrites the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K00 : OP00 A0 -> OP01 A0 ; START OP00 A0 ; GOAL OP01 A0 ; TERM OP00 A0 => RW RULE 0 AT ROOT
PROBLEM
RULE r0 : U f4 v1 -> U f1 v1
RULE r4 : U f1 B g31 e1 e2 -> U f2 B g31 e1 e2
RULE r3 : U f2 B g31 e1 e2 -> B g3 B g31 e1 e2 e0
RULE r5 : B g3 B g31 e1 e2 e0 -> U f0 B g31 e1 e2
RULE r2 : B g60 v1 v0 -> B g120 v1 v0
RULE r1 : B g101 v1 v0 -> B g30 v1 v0
START B g121 U f4 B g31 e1 e2 U f4 B g31 e1 e2
GOAL B g121 U f0 B g31 e1 e2 U f4 B g31 e1 e2
STATE
TERM B g121 U f4 B g31 e1 e2 U f4 B g31 e1 e2
RW r0
TERM B g121 U f1 B g31 e1 e2 U f4 B g100 e1 e2
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
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
SYNTAX TERM T : current expression
ACTION RW RULE N AT PATH uses RULE line N and rewrites the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K00 : OP00 A0 -> OP01 A0 ; START OP00 A0 ; GOAL OP01 A0 ; TERM OP00 A0 => RW RULE 0 AT ROOT
PROBLEM
RULE r0 : U f4 v1 -> U f1 v1
RULE r4 : U f1 B g31 e1 e2 -> U f2 B g31 e1 e2
RULE r3 : U f2 B g31 e1 e2 -> B g3 B g31 e1 e2 e0
RULE r5 : B g3 B g31 e1 e2 e0 -> U f0 B g31 e1 e2
RULE r2 : B g60 v1 v0 -> B g120 v1 v0
RULE r1 : B g101 v1 v0 -> B g30 v1 v0
START B g121 U f4 B g31 e1 e2 U f4 B g31 e1 e2
GOAL B g121 U f0 B g31 e1 e2 U f4 B g31 e1 e2
STATE
TERM B g121 U f4 B g31 e1 e2 U f4 B g31 e1 e2
RW r0
TERM B g121 U f1 B g31 e1 e2 U f4 B g31 e1 e2
RW r4
TERM B g121 U f2 B g31 e1 e2 U f4 B g31 e1 e2
RW r3
TERM B g121 B g3 B g31 e1 e2 e0 U f4 B g31 e1 e2
RW r5
TERM B g121 U f0 B g31 e1 e2 U f4 B g31 e1 e2
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
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX PARENT A B : A is direct parent of B
SYNTAX QUERY ANCESTOR A C : DONE needs lineage from A to C
SYNTAX LINEAGE A B C : ordered ancestor chain
STATE EMPTY means no lineage has started
VALID LINEAGE starts at query ancestor and follows PARENT steps
ACTION DESCEND X starts with query ancestor or appends a child of last node
DONE when LINEAGE ends at query target
DEMO PARENT A0 A1 ; PARENT A1 A2 ; QUERY ANCESTOR A0 A2 ; EMPTY => DESCEND A0 ; LINEAGE A0 => DESCEND A1
PROBLEM
PARENT e8 e4
PARENT e8 e5
PARENT e4 e1
PARENT e4 e7
PARENT e1 e6
PARENT e6 e3
PARENT e3 e0
PARENT e5 e2
QUERY ANCESTOR e8 e3
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
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX PARENT A B : A is direct parent of B
SYNTAX QUERY ANCESTOR A C : DONE needs lineage from A to C
SYNTAX LINEAGE A B C : ordered ancestor chain
STATE EMPTY means no lineage has started
VALID LINEAGE starts at query ancestor and follows PARENT steps
ACTION DESCEND X starts with query ancestor or appends a child of last node
DONE when LINEAGE ends at query target
DEMO PARENT X0 X1 ; PARENT X1 X2 ; QUERY ANCESTOR X0 X2 ; EMPTY => DESCEND X0 ; LINEAGE X0 => DESCEND X1
PROBLEM
PARENT e8 e4
PARENT e8 e5
PARENT e4 e1
PARENT e4 e7
PARENT e1 e6
PARENT e6 e3
PARENT e3 e0
PARENT e5 e2
QUERY ANCESTOR e8 e3
STATE
LINEAGE e3
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
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX PARENT A B : A is direct parent of B
SYNTAX QUERY ANCESTOR A C : DONE needs lineage from A to C
SYNTAX LINEAGE A B C : ordered ancestor chain
STATE EMPTY means no lineage has started
VALID LINEAGE starts at query ancestor and follows PARENT steps
ACTION DESCEND X starts with query ancestor or appends a child of last node
DONE when LINEAGE ends at query target
DEMO PARENT X0 X1 ; PARENT X1 X2 ; QUERY ANCESTOR X0 X2 ; EMPTY => DESCEND X0 ; LINEAGE X0 => DESCEND X1
PROBLEM
PARENT e8 e4
PARENT e8 e5
PARENT e4 e1
PARENT e4 e7
PARENT e1 e6
PARENT e6 e3
PARENT e3 e0
PARENT e5 e2
QUERY ANCESTOR e8 e3
STATE
LINEAGE e8 e4 e1 e6 e3
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
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX EDGE A B : directed step from A to B
SYNTAX QUERY REACH A C : DONE needs PATH from A to C
SYNTAX PATH A B C : ordered visited nodes
STATE EMPTY means no PATH has started
VALID PATH requires each adjacent pair has EDGE
ACTION APPEND X starts with query start or extends from last node by EDGE
DONE when PATH starts at query start and ends at query target
DEMO EDGE A0 A1 ; EDGE A1 A2 ; QUERY REACH A0 A2 ; EMPTY => APPEND A0 ; PATH A0 => APPEND A1
PROBLEM
EDGE e4 e2
EDGE e2 e5
EDGE e5 e3
EDGE e3 e0
EDGE e0 e2
EDGE e0 e1
EDGE e1 e4
EDGE e1 e2
EDGE e1 e0
QUERY REACH e4 e1
STATE
EMPTY
```

Target:

```text
APPEND e4
```

### train/graph_reachability/repair_action

- ID: `train:graph_reachability:0:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX QUERY REACH A C : DONE needs PATH from A to C
SYNTAX EDGE A B : directed step from A to B
SYNTAX PATH A B C : ordered visited nodes
STATE EMPTY means no PATH has started
VALID PATH requires each adjacent pair has EDGE
ACTION APPEND X starts with query start or extends from last node by EDGE
DONE when PATH starts at query start and ends at query target
DEMO EDGE X0 X1 ; EDGE X1 X2 ; QUERY REACH X0 X2 ; EMPTY => APPEND X0 ; PATH X0 => APPEND X1
PROBLEM
EDGE e4 e2
EDGE e2 e5
EDGE e5 e3
EDGE e3 e0
EDGE e0 e2
EDGE e0 e1
EDGE e1 e4
EDGE e1 e2
EDGE e1 e0
QUERY REACH e4 e1
STATE
PATH e1
```

Target:

```text
REPLACE ROOT WITH e4
```

### train/graph_reachability/verify

- ID: `train:graph_reachability:0:verify:valid`

Source:

```text
MODE verify
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX QUERY REACH A C : DONE needs PATH from A to C
SYNTAX EDGE A B : directed step from A to B
SYNTAX PATH A B C : ordered visited nodes
STATE EMPTY means no PATH has started
VALID PATH requires each adjacent pair has EDGE
ACTION APPEND X starts with query start or extends from last node by EDGE
DONE when PATH starts at query start and ends at query target
DEMO EDGE X0 X1 ; EDGE X1 X2 ; QUERY REACH X0 X2 ; EMPTY => APPEND X0 ; PATH X0 => APPEND X1
PROBLEM
EDGE e4 e2
EDGE e2 e5
EDGE e5 e3
EDGE e3 e0
EDGE e0 e2
EDGE e0 e1
EDGE e1 e4
EDGE e1 e2
EDGE e1 e0
QUERY REACH e4 e1
STATE
PATH e4 e2 e5 e3 e0 e1
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
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX HYP K : P : K proves fact P
SYNTAX HYP K : P -> Q : K maps known P to Q
SYNTAX GOAL Q : DONE needs Q derived
SYNTAX DERIVE Q BY K FROM P : Q follows by implication K and prior P
ACTION APPLY K adds the derivation licensed by K
VALID proof uses only known facts and prior derived premises
DONE when GOAL proposition is derived
DEMO HYP K00 : A0 ; HYP K01 : A0 -> A1 ; GOAL A1 ; EMPTY => APPLY K00 ; DERIVE A0 BY K00 => APPLY K01
PROBLEM
HYP h2 : p0
HYP h0 : p0 -> p8
HYP h5 : p8 -> p2
HYP h1 : p0 -> p1
HYP h999 : p2 -> p0
HYP h3 : p2 -> p8
GOAL p2
STATE
EMPTY
```

Target:

```text
APPLY h2
```

### train/implication_chains/repair_action

- ID: `train:implication_chains:312:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX HYP K : P : K proves fact P
SYNTAX HYP K : P -> Q : K maps known P to Q
SYNTAX GOAL Q : DONE needs Q derived
SYNTAX DERIVE Q BY K FROM P : Q follows by implication K and prior P
ACTION APPLY K adds the derivation licensed by K
VALID proof uses only known facts and prior derived premises
DONE when GOAL proposition is derived
DEMO HYP K00 : A0 ; HYP K01 : A0 -> A1 ; GOAL A1 ; EMPTY => APPLY K00 ; DERIVE A0 BY K00 => APPLY K01
PROBLEM
HYP h2 : p0
HYP h0 : p0 -> p8
HYP h5 : p8 -> p2
HYP h1 : p0 -> p1
HYP h999 : p2 -> p0
HYP h3 : p2 -> p8
GOAL p2
STATE
DERIVE p0 BY h4
```

Target:

```text
REPLACE FIRST HYP h2
```

### train/implication_chains/verify

- ID: `train:implication_chains:312:verify:valid`

Source:

```text
MODE verify
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX HYP K : P : K proves fact P
SYNTAX HYP K : P -> Q : K maps known P to Q
SYNTAX GOAL Q : DONE needs Q derived
SYNTAX DERIVE Q BY K FROM P : Q follows by implication K and prior P
ACTION APPLY K adds the derivation licensed by K
VALID proof uses only known facts and prior derived premises
DONE when GOAL proposition is derived
DEMO HYP K20 : X0 ; HYP K21 : X0 -> X1 ; GOAL X1 ; EMPTY => APPLY K20 ; DERIVE X0 BY K20 => APPLY K21
PROBLEM
HYP h2 : p0
HYP h0 : p0 -> p8
HYP h5 : p8 -> p2
HYP h1 : p0 -> p1
HYP h999 : p2 -> p0
HYP h3 : p2 -> p8
GOAL p2
STATE
DERIVE p0 BY h2
DERIVE p8 BY h0 FROM p0
DERIVE p2 BY h5 FROM p8
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
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE RC = RA ; RB : compose RA then RB through a shared middle
SYNTAX FACT R A B : relation R holds from A to B
SYNTAX QUERY R A C : DONE needs relation R from A to C
SYNTAX DERIVE R A C VIA B : composed fact uses middle B
ACTION FOLLOW C VIA B adds the next composed fact ending at C
VALID derivation requires matching left fact, right fact, and rule
DONE when queried relation fact is available
DEMO FACT REL20 X0 X1 ; FACT REL21 X1 X2 ; RULE REL22 = REL20 ; REL21 ; QUERY REL22 X0 X2 ; EMPTY => FOLLOW X2 VIA X1
PROBLEM
FACT r2 e2 e3
FACT r3 e3 e0
FACT r1 e0 e1
RULE r4 = r2 ; r3
RULE r0 = r4 ; r1
FACT r2 e0 e1
FACT r1 e3 e0
QUERY r0 e2 e1
STATE
EMPTY
```

Target:

```text
FOLLOW e2 e0 VIA e3
```

### train/relation_composition/repair_action

- ID: `train:relation_composition:624:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE RC = RA ; RB : compose RA then RB through a shared middle
SYNTAX FACT R A B : relation R holds from A to B
SYNTAX QUERY R A C : DONE needs relation R from A to C
SYNTAX DERIVE R A C VIA B : composed fact uses middle B
ACTION FOLLOW C VIA B adds the next composed fact ending at C
VALID derivation requires matching left fact, right fact, and rule
DONE when queried relation fact is available
DEMO FACT REL20 X0 X1 ; FACT REL21 X1 X2 ; RULE REL22 = REL20 ; REL21 ; QUERY REL22 X0 X2 ; EMPTY => FOLLOW X2 VIA X1
PROBLEM
FACT r2 e2 e3
FACT r3 e3 e0
FACT r1 e0 e1
RULE r4 = r2 ; r3
RULE r0 = r4 ; r1
FACT r2 e0 e1
FACT r1 e3 e0
QUERY r0 e2 e1
STATE
DERIVE r4 e2 e0 VIA e2
```

Target:

```text
REPLACE FIRST VIA e3
```

### train/relation_composition/verify

- ID: `train:relation_composition:624:verify:valid`

Source:

```text
MODE verify
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE RC = RA ; RB : compose RA then RB through a shared middle
SYNTAX FACT R A B : relation R holds from A to B
SYNTAX QUERY R A C : DONE needs relation R from A to C
SYNTAX DERIVE R A C VIA B : composed fact uses middle B
ACTION FOLLOW C VIA B adds the next composed fact ending at C
VALID derivation requires matching left fact, right fact, and rule
DONE when queried relation fact is available
DEMO FACT REL20 X0 X1 ; FACT REL21 X1 X2 ; RULE REL22 = REL20 ; REL21 ; QUERY REL22 X0 X2 ; EMPTY => FOLLOW X2 VIA X1
PROBLEM
FACT r2 e2 e3
FACT r3 e3 e0
FACT r1 e0 e1
RULE r4 = r2 ; r3
RULE r0 = r4 ; r1
FACT r2 e0 e1
FACT r1 e3 e0
QUERY r0 e2 e1
STATE
DERIVE r4 e2 e0 VIA e3
DERIVE r0 e2 e1 VIA e0
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
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX TERM T : current expression
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
ACTION RW RULE N AT PATH uses RULE line N and rewrites the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K20 : OP20 X0 -> OP21 X0 ; START OP20 X0 ; GOAL OP21 X0 ; TERM OP20 X0 => RW RULE 0 AT ROOT
PROBLEM
RULE r3 : U f2 e1 -> U f0 e1
RULE r4 : U f0 v1 -> U f5 v1
RULE r0 : U f5 v1 -> U f61 v1
RULE r1 : U f61 e1 -> B g4 e1 e0
RULE r5 : B g4 e1 e0 -> U f60 e1
RULE r2 : B g5 v1 v0 -> B g120 v1 v0
RULE r6 : U f3 v1 -> U f1 v1
START U f121 U f2 e1
QUERY NORMAL_FORM
STATE
TERM U f121 U f2 e1
```

Target:

```text
RW RULE 0
```

### train/term_rewriting/repair_action

- ID: `train:term_rewriting:1368:repair_action:1`

Source:

```text
MODE repair_action
TASK
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
SYNTAX TERM T : current expression
ACTION RW RULE N AT PATH uses RULE line N and rewrites the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K10 : OP10 N0 -> OP11 N0 ; START OP10 N0 ; GOAL OP11 N0 ; TERM OP10 N0 => RW RULE 0 AT ROOT
PROBLEM
RULE r3 : U f2 e1 -> U f0 e1
RULE r4 : U f0 v1 -> U f5 v1
RULE r0 : U f5 v1 -> U f61 v1
RULE r1 : U f61 e1 -> B g4 e1 e0
RULE r5 : B g4 e1 e0 -> U f60 e1
RULE r2 : B g5 v1 v0 -> B g120 v1 v0
RULE r6 : U f3 v1 -> U f1 v1
START U f121 U f2 e1
QUERY NORMAL_FORM
STATE
TERM U f121 U f2 e1
RW r3
TERM U f101 U f0 e1
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
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
SYNTAX TERM T : current expression
ACTION RW RULE N AT PATH uses RULE line N and rewrites the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K10 : OP10 N0 -> OP11 N0 ; START OP10 N0 ; GOAL OP11 N0 ; TERM OP10 N0 => RW RULE 0 AT ROOT
PROBLEM
RULE r3 : U f2 e1 -> U f0 e1
RULE r4 : U f0 v1 -> U f5 v1
RULE r0 : U f5 v1 -> U f61 v1
RULE r1 : U f61 e1 -> B g4 e1 e0
RULE r5 : B g4 e1 e0 -> U f60 e1
RULE r2 : B g5 v1 v0 -> B g120 v1 v0
RULE r6 : U f3 v1 -> U f1 v1
START U f121 U f2 e1
QUERY NORMAL_FORM
STATE
TERM U f121 U f2 e1
RW r3
TERM U f121 U f0 e1
RW r4
TERM U f121 U f5 e1
RW r0
TERM U f121 U f61 e1
RW r1
TERM U f121 B g4 e1 e0
RW r5
TERM U f121 U f60 e1
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
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX PARENT A B : A is direct parent of B
SYNTAX QUERY ANCESTOR A C : DONE needs lineage from A to C
SYNTAX LINEAGE A B C : ordered ancestor chain
STATE EMPTY means no lineage has started
VALID LINEAGE starts at query ancestor and follows PARENT steps
ACTION DESCEND X starts with query ancestor or appends a child of last node
DONE when LINEAGE ends at query target
DEMO PARENT A0 A1 ; PARENT A1 A2 ; QUERY ANCESTOR A0 A2 ; EMPTY => DESCEND A0 ; LINEAGE A0 => DESCEND A1
PROBLEM
PARENT e6 e5
PARENT e5 e2
PARENT e2 e1
PARENT e2 e4
PARENT e1 e3
PARENT e3 e7
PARENT e7 e0
QUERY ANCESTOR e6 e3
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
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX PARENT A B : A is direct parent of B
SYNTAX QUERY ANCESTOR A C : DONE needs lineage from A to C
SYNTAX LINEAGE A B C : ordered ancestor chain
STATE EMPTY means no lineage has started
VALID LINEAGE starts at query ancestor and follows PARENT steps
ACTION DESCEND X starts with query ancestor or appends a child of last node
DONE when LINEAGE ends at query target
DEMO PARENT X0 X1 ; PARENT X1 X2 ; QUERY ANCESTOR X0 X2 ; EMPTY => DESCEND X0 ; LINEAGE X0 => DESCEND X1
PROBLEM
PARENT e6 e5
PARENT e5 e2
PARENT e2 e1
PARENT e2 e4
PARENT e1 e3
PARENT e3 e7
PARENT e7 e0
QUERY ANCESTOR e6 e3
STATE
LINEAGE e3
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
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX PARENT A B : A is direct parent of B
SYNTAX QUERY ANCESTOR A C : DONE needs lineage from A to C
SYNTAX LINEAGE A B C : ordered ancestor chain
STATE EMPTY means no lineage has started
VALID LINEAGE starts at query ancestor and follows PARENT steps
ACTION DESCEND X starts with query ancestor or appends a child of last node
DONE when LINEAGE ends at query target
DEMO PARENT X0 X1 ; PARENT X1 X2 ; QUERY ANCESTOR X0 X2 ; EMPTY => DESCEND X0 ; LINEAGE X0 => DESCEND X1
PROBLEM
PARENT e6 e5
PARENT e5 e2
PARENT e2 e1
PARENT e2 e4
PARENT e1 e3
PARENT e3 e7
PARENT e7 e0
QUERY ANCESTOR e6 e3
STATE
LINEAGE e6 e5 e2 e1 e3
```

Target:

```text
VALID
```
