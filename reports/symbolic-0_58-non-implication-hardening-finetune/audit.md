# Dataset Audit

- Data dir: `data/symbolic-0_58-non-implication-hardening-finetune`
- Status: `pass`
- Errors: `0`
- Warnings: `0`

## JSONL Summary

### train

- Examples: `5675`
- Problems: `432`
- Families: `{'graph_reachability': 1440, 'term_rewriting': 1355, 'tree_ancestry': 2880}`
- Modes: `{'action': 2795, 'repair_action': 2880}`
- Verify targets: `{}`

### test

- Examples: `1242`
- Problems: `90`
- Families: `{'graph_reachability': 266, 'implication_chains': 234, 'relation_composition': 208, 'term_rewriting': 258, 'tree_ancestry': 276}`
- Modes: `{'action': 531, 'repair_action': 531, 'verify': 180}`
- Verify targets: `{'INVALID BAD_EDGE': 18, 'INVALID BAD_FACT': 18, 'INVALID BAD_NOT_GOAL': 1, 'INVALID BAD_NO_MATCH': 3, 'INVALID BAD_PARENT': 18, 'INVALID BAD_PATH': 7, 'INVALID BAD_PREMATURE_HALT': 5, 'INVALID BAD_PREMISE': 13, 'INVALID BAD_RESULT': 2, 'INVALID UNKNOWN_HYP': 5, 'VALID': 90}`

### ood

- Examples: `1850`
- Problems: `90`
- Families: `{'graph_reachability': 396, 'implication_chains': 360, 'relation_composition': 324, 'term_rewriting': 374, 'tree_ancestry': 396}`
- Modes: `{'action': 835, 'repair_action': 835, 'verify': 180}`
- Verify targets: `{'INVALID BAD_EDGE': 18, 'INVALID BAD_FACT': 18, 'INVALID BAD_NOT_GOAL': 5, 'INVALID BAD_NO_MATCH': 3, 'INVALID BAD_PARENT': 18, 'INVALID BAD_PATH': 3, 'INVALID BAD_PREMATURE_HALT': 5, 'INVALID BAD_PREMISE': 17, 'INVALID BAD_RESULT': 2, 'INVALID UNKNOWN_HYP': 1, 'VALID': 90}`

## Difficulty Summary

### graph_reachability

- `extra_edges`: `{'min': 2.0, 'max': 16.0, 'mean': 10.9790675547098, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `num_nodes`: `{'min': 5.0, 'max': 19.0, 'mean': 14.498097050428164, 'unique': [5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `path_length`: `{'min': 2.0, 'max': 10.0, 'mean': 8.649857278782113, 'unique': [2, 3, 4, 6, 7, 8, 9, 10]}`
- `require_shortest`: `{True: 2102}`
- `symbol_offset`: `{'min': 0.0, 'max': 4.0, 'mean': 1.2787821122740248, 'unique': [0, 2, 4]}`

### implication_chains

- `distractor_hyps`: `{'min': 1.0, 'max': 11.0, 'mean': 6.8686868686868685, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}`
- `num_props`: `{'min': 5.0, 'max': 16.0, 'mean': 12.232323232323232, 'unique': [5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `proof_length`: `{'min': 2.0, 'max': 10.0, 'mean': 7.824915824915825, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 0.0, 'mean': 0.0, 'unique': [0]}`

### relation_composition

- `composition_depth`: `{'min': 3.0, 'max': 10.0, 'mean': 7.879699248120301, 'unique': [3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_facts`: `{'min': 1.0, 'max': 10.0, 'mean': 6.796992481203008, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `num_entities`: `{'min': 5.0, 'max': 15.0, 'mean': 12.097744360902256, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]}`
- `symbol_offset`: `{'min': 0.0, 'max': 0.0, 'mean': 0.0, 'unique': [0]}`

### term_rewriting

- `action_format`: `{'rule': 1987}`
- `binary_rules`: `{'min': 1.0, 'max': 10.0, 'mean': 7.021137393054857, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_rules`: `{'min': 3.0, 'max': 16.0, 'mean': 10.869149471565173, 'unique': [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `query_kind`: `{'goal': 1153, 'normal_form': 834}`
- `repeated_subterms`: `{False: 1492, True: 495}`
- `rewrite_steps`: `{'min': 3.0, 'max': 10.0, 'mean': 8.669854051333669, 'unique': [3, 4, 5, 6, 7, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 4.0, 'mean': 1.2692501258178157, 'unique': [0, 2, 4]}`
- `term_depth`: `{'min': 1.0, 'max': 9.0, 'mean': 4.637141419224962, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9]}`
- `variable_rules`: `{'min': 0.0, 'max': 8.0, 'mean': 2.720181177654756, 'unique': [0, 1, 2, 3, 4, 5, 6, 7, 8]}`

### tree_ancestry

- `branching_factor`: `{'min': 2.0, 'max': 4.0, 'mean': 2.9155405405405403, 'unique': [2, 3, 4]}`
- `depth`: `{'min': 3.0, 'max': 10.0, 'mean': 8.818693693693694, 'unique': [3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_subtrees`: `{'min': 1.0, 'max': 16.0, 'mean': 11.813626126126126, 'unique': [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `symbol_offset`: `{'min': 0.0, 'max': 4.0, 'mean': 1.5135135135135136, 'unique': [0, 2, 4]}`

## TRM Array Summary

### train

- Inputs shape: `[5675, 941]`
- Labels shape: `[5675, 941]`
- Seq len: `941`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `5675`

### test

- Inputs shape: `[1242, 941]`
- Labels shape: `[1242, 941]`
- Seq len: `941`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1242`

### ood

- Inputs shape: `[1850, 941]`
- Labels shape: `[1850, 941]`
- Seq len: `941`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1850`

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
SYNTAX EDGE A B : directed step from A to B
SYNTAX QUERY REACH A C : DONE needs PATH from A to C
SYNTAX PATH A B C : ordered visited nodes
STATE EMPTY means no PATH has started
VALID PATH requires each adjacent pair has EDGE
ACTION APPEND X starts with query start or extends from last node by EDGE
DONE when PATH starts at query start and ends at query target
DEMO EDGE A0 A1 ; EDGE A1 A2 ; QUERY REACH A0 A2 ; EMPTY => APPEND A0 ; PATH A0 => APPEND A1
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e10 e8
EDGE e2 e3
EDGE e3 e11
EDGE e3 e4
EDGE e4 e5
EDGE e5 e3
EDGE e5 e6
EDGE e6 e10
EDGE e6 e7
EDGE e7 e4
EDGE e7 e8
EDGE e8 e11
EDGE e8 e2
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
EDGE e0 e1
EDGE e1 e2
EDGE e10 e8
EDGE e2 e3
EDGE e3 e11
EDGE e3 e4
EDGE e4 e5
EDGE e5 e3
EDGE e5 e6
EDGE e6 e10
EDGE e6 e7
EDGE e7 e4
EDGE e7 e8
EDGE e8 e11
EDGE e8 e2
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
EDGE e0 e1
EDGE e1 e2
EDGE e10 e8
EDGE e2 e3
EDGE e3 e11
EDGE e3 e4
EDGE e4 e5
EDGE e5 e3
EDGE e5 e6
EDGE e6 e10
EDGE e6 e7
EDGE e7 e4
EDGE e7 e8
EDGE e8 e11
EDGE e8 e2
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
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
SYNTAX HYP K : P : K proves fact P
SYNTAX GOAL Q : DONE needs Q derived
SYNTAX HYP K : P -> Q : K maps known P to Q
SYNTAX DERIVE Q BY K FROM P : Q follows by implication K and prior P
ACTION APPLY K adds the derivation licensed by K
VALID proof uses only known facts and prior derived premises
DONE when GOAL proposition is derived
DEMO HYP K10 : N0 ; HYP K11 : N0 -> N1 ; GOAL N1 ; EMPTY => APPLY K10 ; DERIVE N0 BY K10 => APPLY K11
PROBLEM
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p3 -> p1
HYP h9 : p7 -> p5
HYP h10 : p7 -> p14
HYP h11 : p14 -> p5
HYP h12 : p14 -> p12
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
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p3 -> p1
HYP h9 : p7 -> p5
HYP h10 : p7 -> p14
HYP h11 : p14 -> p5
HYP h12 : p14 -> p12
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
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p3 -> p1
HYP h9 : p7 -> p5
HYP h10 : p7 -> p14
HYP h11 : p14 -> p5
HYP h12 : p14 -> p12
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
FACT r2 e4 e3
FACT r2 e5 e1
FACT r3 e6 e4
FACT r4 e3 e0
FACT r4 e6 e8
FACT r6 e2 e1
FACT r6 e4 e8
FACT r6 e8 e6
FACT r7 e3 e7
FACT r7 e7 e5
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
FACT r2 e4 e3
FACT r2 e5 e1
FACT r3 e6 e4
FACT r4 e3 e0
FACT r4 e6 e8
FACT r6 e2 e1
FACT r6 e4 e8
FACT r6 e8 e6
FACT r7 e3 e7
FACT r7 e7 e5
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
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
SYNTAX FACT R A B : relation R holds from A to B
SYNTAX RULE RC = RA ; RB : compose RA then RB through a shared middle
SYNTAX QUERY R A C : DONE needs relation R from A to C
SYNTAX DERIVE R A C VIA B : composed fact uses middle B
ACTION FOLLOW C VIA B adds the next composed fact ending at C
VALID derivation requires matching left fact, right fact, and rule
DONE when queried relation fact is available
DEMO FACT REL10 N0 N1 ; FACT REL11 N1 N2 ; RULE REL12 = REL10 ; REL11 ; QUERY REL12 N0 N2 ; EMPTY => FOLLOW N2 VIA N1
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
FACT r2 e4 e3
FACT r2 e5 e1
FACT r3 e6 e4
FACT r4 e3 e0
FACT r4 e6 e8
FACT r6 e2 e1
FACT r6 e4 e8
FACT r6 e8 e6
FACT r7 e3 e7
FACT r7 e7 e5
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
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
SYNTAX TERM T : current expression
ACTION RW K AT PATH applies rule K to the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K10 : OP10 N0 -> OP11 N0 ; START OP10 N0 ; GOAL OP11 N0 ; TERM OP10 N0 => RW K10 AT ROOT
PROBLEM
RULE r0 : B g0 B g31 U f30 e0 e3 e1 -> U f1 B g31 U f30 e0 e3
RULE r1 : U f1 v0 -> U f2 v0
RULE r2 : U f2 v0 -> U f3 v0
RULE r3 : U f3 B g31 U f30 e0 e3 -> B g4 B g31 U f30 e0 e3 e1
RULE r4 : B g4 v0 v1 -> B g5 v0 v1
RULE r5 : B g5 B g31 U f30 e0 e3 e1 -> U f6 B g31 U f30 e0 e3
RULE r6 : U f6 B g31 U f30 e0 e3 -> B g7 B g31 U f30 e0 e3 e1
RULE r7 : B g7 B g31 U f30 e0 e3 e1 -> B g8 B g31 U f30 e0 e3 e1
RULE r8 : U f100 v0 -> U f120 v0
RULE r9 : U f101 v0 -> U f121 v0
RULE r10 : B g102 v0 v1 -> B g122 v0 v1
RULE r11 : B g103 v0 v1 -> B g123 v0 v1
RULE r12 : B g104 v0 v1 -> B g124 v0 v1
RULE r13 : U f105 v0 -> U f125 v0
RULE r14 : U f106 v0 -> U f126 v0
RULE r15 : B g107 v0 v1 -> B g127 v0 v1
RULE r16 : U f108 v0 -> U f128 v0
RULE r17 : U f109 v0 -> U f129 v0
START B g61 e71 B g60 B g0 B g31 U f30 e0 e3 e1 B g0 B g31 U f30 e0 e3 e1
GOAL B g61 e71 B g60 B g8 B g31 U f30 e0 e3 e1 B g0 B g31 U f30 e0 e3 e1
STATE
TERM B g61 e71 B g60 B g0 B g31 U f30 e0 e3 e1 B g0 B g31 U f30 e0 e3 e1
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
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
SYNTAX TERM T : current expression
ACTION RW K AT PATH applies rule K to the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K00 : OP00 A0 -> OP01 A0 ; START OP00 A0 ; GOAL OP01 A0 ; TERM OP00 A0 => RW K00 AT ROOT
PROBLEM
RULE r0 : B g0 B g31 U f30 e0 e3 e1 -> U f1 B g31 U f30 e0 e3
RULE r1 : U f1 v0 -> U f2 v0
RULE r2 : U f2 v0 -> U f3 v0
RULE r3 : U f3 B g31 U f30 e0 e3 -> B g4 B g31 U f30 e0 e3 e1
RULE r4 : B g4 v0 v1 -> B g5 v0 v1
RULE r5 : B g5 B g31 U f30 e0 e3 e1 -> U f6 B g31 U f30 e0 e3
RULE r6 : U f6 B g31 U f30 e0 e3 -> B g7 B g31 U f30 e0 e3 e1
RULE r7 : B g7 B g31 U f30 e0 e3 e1 -> B g8 B g31 U f30 e0 e3 e1
RULE r8 : U f100 v0 -> U f120 v0
RULE r9 : U f101 v0 -> U f121 v0
RULE r10 : B g102 v0 v1 -> B g122 v0 v1
RULE r11 : B g103 v0 v1 -> B g123 v0 v1
RULE r12 : B g104 v0 v1 -> B g124 v0 v1
RULE r13 : U f105 v0 -> U f125 v0
RULE r14 : U f106 v0 -> U f126 v0
RULE r15 : B g107 v0 v1 -> B g127 v0 v1
RULE r16 : U f108 v0 -> U f128 v0
RULE r17 : U f109 v0 -> U f129 v0
START B g61 e71 B g60 B g0 B g31 U f30 e0 e3 e1 B g0 B g31 U f30 e0 e3 e1
GOAL B g61 e71 B g60 B g8 B g31 U f30 e0 e3 e1 B g0 B g31 U f30 e0 e3 e1
STATE
TERM B g61 e71 B g60 B g0 B g31 U f30 e0 e3 e1 B g0 B g31 U f30 e0 e3 e1
RW r0
TERM B g61 e71 B g60 U f2 B g31 U f30 e0 e3 B g0 B g31 U f30 e0 e3 e1
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
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
SYNTAX TERM T : current expression
ACTION RW K AT PATH applies rule K to the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K10 : OP10 N0 -> OP11 N0 ; START OP10 N0 ; GOAL OP11 N0 ; TERM OP10 N0 => RW K10 AT ROOT
PROBLEM
RULE r0 : B g0 B g31 U f30 e0 e3 e1 -> U f1 B g31 U f30 e0 e3
RULE r1 : U f1 v0 -> U f2 v0
RULE r2 : U f2 v0 -> U f3 v0
RULE r3 : U f3 B g31 U f30 e0 e3 -> B g4 B g31 U f30 e0 e3 e1
RULE r4 : B g4 v0 v1 -> B g5 v0 v1
RULE r5 : B g5 B g31 U f30 e0 e3 e1 -> U f6 B g31 U f30 e0 e3
RULE r6 : U f6 B g31 U f30 e0 e3 -> B g7 B g31 U f30 e0 e3 e1
RULE r7 : B g7 B g31 U f30 e0 e3 e1 -> B g8 B g31 U f30 e0 e3 e1
RULE r8 : U f100 v0 -> U f120 v0
RULE r9 : U f101 v0 -> U f121 v0
RULE r10 : B g102 v0 v1 -> B g122 v0 v1
RULE r11 : B g103 v0 v1 -> B g123 v0 v1
RULE r12 : B g104 v0 v1 -> B g124 v0 v1
RULE r13 : U f105 v0 -> U f125 v0
RULE r14 : U f106 v0 -> U f126 v0
RULE r15 : B g107 v0 v1 -> B g127 v0 v1
RULE r16 : U f108 v0 -> U f128 v0
RULE r17 : U f109 v0 -> U f129 v0
START B g61 e71 B g60 B g0 B g31 U f30 e0 e3 e1 B g0 B g31 U f30 e0 e3 e1
GOAL B g61 e71 B g60 B g8 B g31 U f30 e0 e3 e1 B g0 B g31 U f30 e0 e3 e1
STATE
TERM B g61 e71 B g60 B g0 B g31 U f30 e0 e3 e1 B g0 B g31 U f30 e0 e3 e1
RW r0
TERM B g61 e71 B g60 U f1 B g31 U f30 e0 e3 B g0 B g31 U f30 e0 e3 e1
RW r1
TERM B g61 e71 B g60 U f2 B g31 U f30 e0 e3 B g0 B g31 U f30 e0 e3 e1
RW r2
TERM B g61 e71 B g60 U f3 B g31 U f30 e0 e3 B g0 B g31 U f30 e0 e3 e1
RW r3
TERM B g61 e71 B g60 B g4 B g31 U f30 e0 e3 e1 B g0 B g31 U f30 e0 e3 e1
RW r4
TERM B g61 e71 B g60 B g5 B g31 U f30 e0 e3 e1 B g0 B g31 U f30 e0 e3 e1
RW r5
TERM B g61 e71 B g60 U f6 B g31 U f30 e0 e3 B g0 B g31 U f30 e0 e3 e1
RW r6
TERM B g61 e71 B g60 B g7 B g31 U f30 e0 e3 e1 B g0 B g31 U f30 e0 e3 e1
RW r7
TERM B g61 e71 B g60 B g8 B g31 U f30 e0 e3 e1 B g0 B g31 U f30 e0 e3 e1
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
DEMO PARENT X0 X1 ; PARENT X1 X2 ; QUERY ANCESTOR X0 X2 ; EMPTY => DESCEND X0 ; LINEAGE X0 => DESCEND X1
PROBLEM
PARENT e0 e1
PARENT e0 e11
PARENT e0 e14
PARENT e1 e2
PARENT e2 e10
PARENT e2 e3
PARENT e3 e13
PARENT e3 e4
PARENT e4 e12
PARENT e4 e5
PARENT e5 e6
PARENT e5 e9
PARENT e6 e7
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
TASK
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
SYNTAX QUERY ANCESTOR A C : DONE needs lineage from A to C
SYNTAX PARENT A B : A is direct parent of B
SYNTAX LINEAGE A B C : ordered ancestor chain
STATE EMPTY means no lineage has started
VALID LINEAGE starts at query ancestor and follows PARENT steps
ACTION DESCEND X starts with query ancestor or appends a child of last node
DONE when LINEAGE ends at query target
DEMO PARENT N0 N1 ; PARENT N1 N2 ; QUERY ANCESTOR N0 N2 ; EMPTY => DESCEND N0 ; LINEAGE N0 => DESCEND N1
PROBLEM
PARENT e0 e1
PARENT e0 e11
PARENT e0 e14
PARENT e1 e2
PARENT e2 e10
PARENT e2 e3
PARENT e3 e13
PARENT e3 e4
PARENT e4 e12
PARENT e4 e5
PARENT e5 e6
PARENT e5 e9
PARENT e6 e7
PARENT e7 e8
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
PARENT e0 e1
PARENT e0 e11
PARENT e0 e14
PARENT e1 e2
PARENT e2 e10
PARENT e2 e3
PARENT e3 e13
PARENT e3 e4
PARENT e4 e12
PARENT e4 e5
PARENT e5 e6
PARENT e5 e9
PARENT e6 e7
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
EDGE e0 e1
EDGE e1 e2
EDGE e2 e3
EDGE e3 e4
EDGE e4 e6
EDGE e5 e1
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
EDGE e0 e1
EDGE e1 e2
EDGE e2 e3
EDGE e3 e4
EDGE e4 e6
EDGE e5 e1
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
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
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
EDGE e0 e1
EDGE e1 e2
EDGE e2 e3
EDGE e3 e4
EDGE e4 e6
EDGE e5 e1
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
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p0
HYP h4 : p2 -> p3
HYP h5 : p5 -> p1
HYP h6 : p5 -> p2
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
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p0
HYP h4 : p2 -> p3
HYP h5 : p5 -> p1
HYP h6 : p5 -> p2
GOAL p1
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
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p0
HYP h4 : p2 -> p3
HYP h5 : p5 -> p1
HYP h6 : p5 -> p2
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
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e0 e3
FACT r0 e2 e1
QUERY r4 e0 e3
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
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e0 e3
FACT r0 e2 e1
QUERY r4 e0 e3
STATE
DERIVE r3 e0 e2 VIA e0
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
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
SYNTAX FACT R A B : relation R holds from A to B
SYNTAX RULE RC = RA ; RB : compose RA then RB through a shared middle
SYNTAX QUERY R A C : DONE needs relation R from A to C
SYNTAX DERIVE R A C VIA B : composed fact uses middle B
ACTION FOLLOW C VIA B adds the next composed fact ending at C
VALID derivation requires matching left fact, right fact, and rule
DONE when queried relation fact is available
DEMO FACT REL10 N0 N1 ; FACT REL11 N1 N2 ; RULE REL12 = REL10 ; REL11 ; QUERY REL12 N0 N2 ; EMPTY => FOLLOW N2 VIA N1
PROBLEM
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
RULE r3 = r0 ; r1
RULE r4 = r3 ; r2
FACT r0 e0 e3
FACT r0 e2 e1
QUERY r4 e0 e3
STATE
DERIVE r3 e0 e2 VIA e1
DERIVE r4 e0 e3 VIA e2
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
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
SYNTAX TERM T : current expression
ACTION RW K AT PATH applies rule K to the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K10 : OP10 N0 -> OP11 N0 ; START OP10 N0 ; GOAL OP11 N0 ; TERM OP10 N0 => RW K10 AT ROOT
PROBLEM
RULE r0 : U f0 U f30 e0 -> B g1 U f30 e0 e1
RULE r1 : B g1 U f30 e0 e1 -> U f2 U f30 e0
RULE r2 : U f2 U f30 e0 -> U f3 U f30 e0
RULE r3 : U f3 U f30 e0 -> B g4 U f30 e0 e1
RULE r4 : B g4 U f30 e0 e1 -> U f5 U f30 e0
RULE r5 : U f100 v0 -> U f120 v0
RULE r6 : B g101 v0 v1 -> B g121 v0 v1
RULE r7 : U f102 v0 -> U f122 v0
RULE r8 : B g103 v0 v1 -> B g123 v0 v1
START U f0 U f30 e0
GOAL U f5 U f30 e0
STATE
TERM U f0 U f30 e0
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
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
SYNTAX TERM T : current expression
ACTION RW K AT PATH applies rule K to the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K10 : OP10 N0 -> OP11 N0 ; START OP10 N0 ; GOAL OP11 N0 ; TERM OP10 N0 => RW K10 AT ROOT
PROBLEM
RULE r0 : U f0 U f30 e0 -> B g1 U f30 e0 e1
RULE r1 : B g1 U f30 e0 e1 -> U f2 U f30 e0
RULE r2 : U f2 U f30 e0 -> U f3 U f30 e0
RULE r3 : U f3 U f30 e0 -> B g4 U f30 e0 e1
RULE r4 : B g4 U f30 e0 e1 -> U f5 U f30 e0
RULE r5 : U f100 v0 -> U f120 v0
RULE r6 : B g101 v0 v1 -> B g121 v0 v1
RULE r7 : U f102 v0 -> U f122 v0
RULE r8 : B g103 v0 v1 -> B g123 v0 v1
START U f0 U f30 e0
GOAL U f5 U f30 e0
STATE
TERM U f0 U f30 e0
RW r0
TERM B g1 U f30 e1 e1
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
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
SYNTAX RULE K : L -> R : K replaces a matching L subterm with R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
SYNTAX TERM T : current expression
ACTION RW K AT PATH applies rule K to the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K10 : OP10 N0 -> OP11 N0 ; START OP10 N0 ; GOAL OP11 N0 ; TERM OP10 N0 => RW K10 AT ROOT
PROBLEM
RULE r0 : U f0 U f30 e0 -> B g1 U f30 e0 e1
RULE r1 : B g1 U f30 e0 e1 -> U f2 U f30 e0
RULE r2 : U f2 U f30 e0 -> U f3 U f30 e0
RULE r3 : U f3 U f30 e0 -> B g4 U f30 e0 e1
RULE r4 : B g4 U f30 e0 e1 -> U f5 U f30 e0
RULE r5 : U f100 v0 -> U f120 v0
RULE r6 : B g101 v0 v1 -> B g121 v0 v1
RULE r7 : U f102 v0 -> U f122 v0
RULE r8 : B g103 v0 v1 -> B g123 v0 v1
START U f0 U f30 e0
GOAL U f5 U f30 e0
STATE
TERM U f0 U f30 e0
RW r0
TERM B g1 U f30 e0 e1
RW r1
TERM U f2 U f30 e0
RW r2
TERM U f3 U f30 e0
RW r3
TERM B g4 U f30 e0 e1
RW r4
TERM U f5 U f30 e0
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
PARENT e0 e1
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e3 e6
PARENT e4 e5
PARENT e4 e7
PARENT e5 e8
PARENT e5 e9
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
PARENT e0 e1
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e3 e6
PARENT e4 e5
PARENT e4 e7
PARENT e5 e8
PARENT e5 e9
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
PARENT e0 e1
PARENT e1 e2
PARENT e2 e3
PARENT e3 e4
PARENT e3 e6
PARENT e4 e5
PARENT e4 e7
PARENT e5 e8
PARENT e5 e9
QUERY ANCESTOR e0 e4
STATE
LINEAGE e0 e1 e2 e3 e4
```

Target:

```text
VALID
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
EDGE e10 e11
EDGE e10 e13
EDGE e11 e12
EDGE e11 e18
EDGE e13 e17
EDGE e14 e4
EDGE e15 e9
EDGE e16 e4
EDGE e4 e16
EDGE e4 e5
EDGE e5 e14
EDGE e5 e16
EDGE e5 e6
EDGE e6 e7
EDGE e7 e8
EDGE e8 e13
EDGE e8 e6
EDGE e8 e9
EDGE e9 e10
EDGE e9 e13
EDGE e9 e7
QUERY REACH e4 e12
STATE
PATH e12
```

Target:

```text
REPLACE ROOT WITH e4
```

### train/term_rewriting/action

- ID: `train:term_rewriting:288:action:0`

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
ACTION RW K AT PATH applies rule K to the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K20 : OP20 X0 -> OP21 X0 ; START OP20 X0 ; GOAL OP21 X0 ; TERM OP20 X0 => RW K20 AT ROOT
PROBLEM
RULE r4 : U f4 v0 -> U f5 v0
RULE r5 : U f5 v0 -> U f6 v0
RULE r6 : U f6 U f35 U f34 e4 -> B g7 U f35 U f34 e4 e5
RULE r7 : B g7 U f35 U f34 e4 e5 -> B g8 U f35 U f34 e4 e5
RULE r8 : B g8 v0 v1 -> B g9 v0 v1
RULE r9 : B g9 U f35 U f34 e4 e5 -> U f10 U f35 U f34 e4
RULE r10 : U f10 U f35 U f34 e4 -> B g11 U f35 U f34 e4 e5
RULE r11 : B g11 U f35 U f34 e4 e5 -> U f12 U f35 U f34 e4
RULE r12 : B g104 v0 v1 -> B g124 v0 v1
RULE r13 : U f105 v0 -> U f125 v0
RULE r14 : B g106 v0 v1 -> B g126 v0 v1
RULE r15 : U f107 v0 -> U f127 v0
RULE r16 : U f108 v0 -> U f128 v0
RULE r17 : U f109 v0 -> U f129 v0
RULE r18 : B g110 v0 v1 -> B g130 v0 v1
RULE r19 : B g111 v0 v1 -> B g131 v0 v1
START B g65 e75 B g64 e74 U f4 U f35 U f34 e4
QUERY NORMAL_FORM
STATE
TERM B g65 e75 B g64 e74 U f4 U f35 U f34 e4
```

Target:

```text
RW r4
```

### train/tree_ancestry/action

- ID: `train:tree_ancestry:144:action:0`

Source:

```text
MODE action
TASK
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
SYNTAX QUERY ANCESTOR A C : DONE needs lineage from A to C
SYNTAX PARENT A B : A is direct parent of B
SYNTAX LINEAGE A B C : ordered ancestor chain
STATE EMPTY means no lineage has started
VALID LINEAGE starts at query ancestor and follows PARENT steps
ACTION DESCEND X starts with query ancestor or appends a child of last node
DONE when LINEAGE ends at query target
DEMO PARENT N0 N1 ; PARENT N1 N2 ; QUERY ANCESTOR N0 N2 ; EMPTY => DESCEND N0 ; LINEAGE N0 => DESCEND N1
PROBLEM
PARENT e10 e11
PARENT e10 e14
PARENT e11 e12
PARENT e12 e18
PARENT e12 e20
PARENT e15 e23
PARENT e16 e19
PARENT e18 e22
PARENT e4 e13
PARENT e4 e5
PARENT e5 e21
PARENT e5 e6
PARENT e6 e16
PARENT e6 e7
PARENT e7 e24
PARENT e7 e8
PARENT e8 e15
PARENT e8 e9
PARENT e9 e10
PARENT e9 e17
QUERY ANCESTOR e4 e12
STATE
EMPTY
```

Target:

```text
DESCEND e4
```

### train/tree_ancestry/repair_action

- ID: `train:tree_ancestry:144:repair_action:1`

Source:

```text
MODE repair_action
TASK
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
SYNTAX QUERY ANCESTOR A C : DONE needs lineage from A to C
SYNTAX PARENT A B : A is direct parent of B
SYNTAX LINEAGE A B C : ordered ancestor chain
STATE EMPTY means no lineage has started
VALID LINEAGE starts at query ancestor and follows PARENT steps
ACTION DESCEND X starts with query ancestor or appends a child of last node
DONE when LINEAGE ends at query target
DEMO PARENT N0 N1 ; PARENT N1 N2 ; QUERY ANCESTOR N0 N2 ; EMPTY => DESCEND N0 ; LINEAGE N0 => DESCEND N1
PROBLEM
PARENT e10 e11
PARENT e10 e14
PARENT e11 e12
PARENT e12 e18
PARENT e12 e20
PARENT e15 e23
PARENT e16 e19
PARENT e18 e22
PARENT e4 e13
PARENT e4 e5
PARENT e5 e21
PARENT e5 e6
PARENT e6 e16
PARENT e6 e7
PARENT e7 e24
PARENT e7 e8
PARENT e8 e15
PARENT e8 e9
PARENT e9 e10
PARENT e9 e17
QUERY ANCESTOR e4 e12
STATE
LINEAGE e12
```

Target:

```text
REPLACE ROOT WITH e4
```
