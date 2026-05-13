# Dataset Audit

- Data dir: `data/symbolic-0_54-implication-verify-heavy-finetune`
- Status: `pass`
- Errors: `0`
- Warnings: `0`

## JSONL Summary

### train

- Examples: `2880`
- Problems: `1440`
- Families: `{'implication_chains': 2880}`
- Modes: `{'verify': 2880}`
- Verify targets: `{'INVALID BAD_PREMISE': 1276, 'INVALID UNKNOWN_HYP': 164, 'VALID': 1440}`

### test

- Examples: `1202`
- Problems: `90`
- Families: `{'graph_reachability': 260, 'implication_chains': 238, 'relation_composition': 194, 'term_rewriting': 238, 'tree_ancestry': 272}`
- Modes: `{'action': 511, 'repair_action': 511, 'verify': 180}`
- Verify targets: `{'INVALID BAD_EDGE': 18, 'INVALID BAD_FACT': 18, 'INVALID BAD_NOT_GOAL': 2, 'INVALID BAD_NO_MATCH': 6, 'INVALID BAD_PARENT': 18, 'INVALID BAD_PATH': 4, 'INVALID BAD_PREMATURE_HALT': 3, 'INVALID BAD_PREMISE': 17, 'INVALID BAD_RESULT': 3, 'INVALID UNKNOWN_HYP': 1, 'VALID': 90}`

### ood

- Examples: `1846`
- Problems: `90`
- Families: `{'graph_reachability': 396, 'implication_chains': 360, 'relation_composition': 324, 'term_rewriting': 370, 'tree_ancestry': 396}`
- Modes: `{'action': 833, 'repair_action': 833, 'verify': 180}`
- Verify targets: `{'INVALID BAD_EDGE': 18, 'INVALID BAD_FACT': 18, 'INVALID BAD_NOT_GOAL': 1, 'INVALID BAD_NO_MATCH': 5, 'INVALID BAD_PARENT': 18, 'INVALID BAD_PATH': 6, 'INVALID BAD_PREMATURE_HALT': 4, 'INVALID BAD_PREMISE': 16, 'INVALID BAD_RESULT': 2, 'INVALID UNKNOWN_HYP': 2, 'VALID': 90}`

## Difficulty Summary

### graph_reachability

- `extra_edges`: `{'min': 1.0, 'max': 10.0, 'mean': 6.658536585365853, 'unique': [1, 2, 4, 5, 6, 7, 8, 9, 10]}`
- `num_nodes`: `{'min': 5.0, 'max': 16.0, 'mean': 12.390243902439025, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `path_length`: `{'min': 2.0, 'max': 10.0, 'mean': 7.7439024390243905, 'unique': [2, 4, 6, 7, 8, 9, 10]}`
- `require_shortest`: `{True: 656}`
- `symbol_offset`: `{'min': 0.0, 'max': 0.0, 'mean': 0.0, 'unique': [0]}`

### implication_chains

- `distractor_hyps`: `{'min': 1.0, 'max': 12.0, 'mean': 9.423231742380679, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}`
- `num_props`: `{'min': 5.0, 'max': 19.0, 'mean': 14.866014951121334, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `proof_length`: `{'min': 2.0, 'max': 10.0, 'mean': 8.79815986198965, 'unique': [2, 3, 5, 6, 7, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 4.0, 'mean': 1.6561242093156987, 'unique': [0, 2, 4]}`

### relation_composition

- `composition_depth`: `{'min': 2.0, 'max': 10.0, 'mean': 7.888030888030888, 'unique': [2, 3, 4, 6, 7, 8, 9, 10]}`
- `distractor_facts`: `{'min': 2.0, 'max': 10.0, 'mean': 7.305019305019305, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `num_entities`: `{'min': 5.0, 'max': 16.0, 'mean': 12.436293436293436, 'unique': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `symbol_offset`: `{'min': 0.0, 'max': 0.0, 'mean': 0.0, 'unique': [0]}`

### term_rewriting

- `action_format`: `{'rule': 608}`
- `binary_rules`: `{'min': 1.0, 'max': 10.0, 'mean': 5.911184210526316, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_rules`: `{'min': 0.0, 'max': 16.0, 'mean': 9.3125, 'unique': [0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `query_kind`: `{'goal': 454, 'normal_form': 154}`
- `repeated_subterms`: `{False: 398, True: 210}`
- `rewrite_steps`: `{'min': 2.0, 'max': 10.0, 'mean': 7.8256578947368425, 'unique': [2, 4, 5, 6, 7, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 0.0, 'mean': 0.0, 'unique': [0]}`
- `term_depth`: `{'min': 1.0, 'max': 7.0, 'mean': 4.328947368421052, 'unique': [1, 2, 3, 4, 5, 6, 7]}`
- `variable_rules`: `{'min': 0.0, 'max': 6.0, 'mean': 2.3651315789473686, 'unique': [0, 1, 2, 3, 4, 5, 6]}`

### tree_ancestry

- `branching_factor`: `{'min': 2.0, 'max': 3.0, 'mean': 2.4011976047904193, 'unique': [2, 3]}`
- `depth`: `{'min': 2.0, 'max': 10.0, 'mean': 7.766467065868263, 'unique': [2, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_subtrees`: `{'min': 2.0, 'max': 10.0, 'mean': 6.808383233532934, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 0.0, 'mean': 0.0, 'unique': [0]}`

## TRM Array Summary

### train

- Inputs shape: `[2880, 935]`
- Labels shape: `[2880, 935]`
- Seq len: `935`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `2880`

### test

- Inputs shape: `[1202, 935]`
- Labels shape: `[1202, 935]`
- Seq len: `935`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1202`

### ood

- Inputs shape: `[1846, 935]`
- Labels shape: `[1846, 935]`
- Seq len: `935`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1846`

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
EDGE e0 e1
EDGE e1 e2
EDGE e11 e10
EDGE e12 e1
EDGE e2 e10
EDGE e2 e3
EDGE e3 e4
EDGE e3 e9
EDGE e4 e5
EDGE e5 e4
EDGE e5 e6
EDGE e6 e0
EDGE e6 e5
EDGE e6 e7
EDGE e7 e8
EDGE e8 e6
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
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
SYNTAX EDGE A B : directed step from A to B
SYNTAX QUERY REACH A C : DONE needs PATH from A to C
SYNTAX PATH A B C : ordered visited nodes
STATE EMPTY means no PATH has started
VALID PATH requires each adjacent pair has EDGE
ACTION APPEND X starts with query start or extends from last node by EDGE
DONE when PATH starts at query start and ends at query target
DEMO EDGE N0 N1 ; EDGE N1 N2 ; QUERY REACH N0 N2 ; EMPTY => APPEND N0 ; PATH N0 => APPEND N1
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e11 e10
EDGE e12 e1
EDGE e2 e10
EDGE e2 e3
EDGE e3 e4
EDGE e3 e9
EDGE e4 e5
EDGE e5 e4
EDGE e5 e6
EDGE e6 e0
EDGE e6 e5
EDGE e6 e7
EDGE e7 e8
EDGE e8 e6
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
EDGE e11 e10
EDGE e12 e1
EDGE e2 e10
EDGE e2 e3
EDGE e3 e4
EDGE e3 e9
EDGE e4 e5
EDGE e5 e4
EDGE e5 e6
EDGE e6 e0
EDGE e6 e5
EDGE e6 e7
EDGE e7 e8
EDGE e8 e6
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
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p0 -> p4
HYP h9 : p1 -> p6
HYP h10 : p1 -> p7
HYP h11 : p2 -> p7
HYP h12 : p4 -> p2
HYP h13 : p7 -> p5
HYP h14 : p10 -> p4
HYP h15 : p10 -> p6
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
HYP h8 : p0 -> p4
HYP h9 : p1 -> p6
HYP h10 : p1 -> p7
HYP h11 : p2 -> p7
HYP h12 : p4 -> p2
HYP h13 : p7 -> p5
HYP h14 : p10 -> p4
HYP h15 : p10 -> p6
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
HYP h8 : p0 -> p4
HYP h9 : p1 -> p6
HYP h10 : p1 -> p7
HYP h11 : p2 -> p7
HYP h12 : p4 -> p2
HYP h13 : p7 -> p5
HYP h14 : p10 -> p4
HYP h15 : p10 -> p6
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
FACT r0 e12 e3
FACT r1 e6 e4
FACT r2 e2 e0
FACT r2 e3 e6
FACT r2 e9 e5
FACT r2 e9 e7
FACT r3 e1 e0
FACT r4 e5 e6
FACT r4 e5 e9
FACT r4 e7 e6
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
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
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
FACT r0 e12 e3
FACT r1 e6 e4
FACT r2 e2 e0
FACT r2 e3 e6
FACT r2 e9 e5
FACT r2 e9 e7
FACT r3 e1 e0
FACT r4 e5 e6
FACT r4 e5 e9
FACT r4 e7 e6
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
FACT r0 e12 e3
FACT r1 e6 e4
FACT r2 e2 e0
FACT r2 e3 e6
FACT r2 e9 e5
FACT r2 e9 e7
FACT r3 e1 e0
FACT r4 e5 e6
FACT r4 e5 e9
FACT r4 e7 e6
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
RULE r0 : U f0 U f31 U f30 e0 -> B g1 U f31 U f30 e0 e1
RULE r1 : B g1 U f31 U f30 e0 e1 -> B g2 U f31 U f30 e0 e1
RULE r2 : B g2 U f31 U f30 e0 e1 -> U f3 U f31 U f30 e0
RULE r3 : U f3 U f31 U f30 e0 -> B g4 U f31 U f30 e0 e1
RULE r4 : B g4 U f31 U f30 e0 e1 -> U f5 U f31 U f30 e0
RULE r5 : U f5 U f31 U f30 e0 -> B g6 U f31 U f30 e0 e1
RULE r6 : B g6 U f31 U f30 e0 e1 -> U f7 U f31 U f30 e0
RULE r7 : U f7 v0 -> U f8 v0
RULE r8 : U f100 v0 -> U f120 v0
RULE r9 : U f101 v0 -> U f121 v0
RULE r10 : B g102 v0 v1 -> B g122 v0 v1
RULE r11 : U f103 v0 -> U f123 v0
RULE r12 : B g104 v0 v1 -> B g124 v0 v1
RULE r13 : B g105 v0 v1 -> B g125 v0 v1
RULE r14 : U f106 v0 -> U f126 v0
RULE r15 : U f107 v0 -> U f127 v0
RULE r16 : B g108 v0 v1 -> B g128 v0 v1
START B g61 U f60 U f0 U f31 U f30 e0 e71
GOAL B g61 U f60 U f8 U f31 U f30 e0 e71
STATE
TERM B g61 U f60 U f0 U f31 U f30 e0 e71
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
RULE r0 : U f0 U f31 U f30 e0 -> B g1 U f31 U f30 e0 e1
RULE r1 : B g1 U f31 U f30 e0 e1 -> B g2 U f31 U f30 e0 e1
RULE r2 : B g2 U f31 U f30 e0 e1 -> U f3 U f31 U f30 e0
RULE r3 : U f3 U f31 U f30 e0 -> B g4 U f31 U f30 e0 e1
RULE r4 : B g4 U f31 U f30 e0 e1 -> U f5 U f31 U f30 e0
RULE r5 : U f5 U f31 U f30 e0 -> B g6 U f31 U f30 e0 e1
RULE r6 : B g6 U f31 U f30 e0 e1 -> U f7 U f31 U f30 e0
RULE r7 : U f7 v0 -> U f8 v0
RULE r8 : U f100 v0 -> U f120 v0
RULE r9 : U f101 v0 -> U f121 v0
RULE r10 : B g102 v0 v1 -> B g122 v0 v1
RULE r11 : U f103 v0 -> U f123 v0
RULE r12 : B g104 v0 v1 -> B g124 v0 v1
RULE r13 : B g105 v0 v1 -> B g125 v0 v1
RULE r14 : U f106 v0 -> U f126 v0
RULE r15 : U f107 v0 -> U f127 v0
RULE r16 : B g108 v0 v1 -> B g128 v0 v1
START B g61 U f60 U f0 U f31 U f30 e0 e71
GOAL B g61 U f60 U f8 U f31 U f30 e0 e71
STATE
TERM B g61 U f60 U f0 U f31 U f30 e0 e71
RW r0
TERM B g61 U f60 B g1 U f32 U f30 e0 e1 e71
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
RULE r0 : U f0 U f31 U f30 e0 -> B g1 U f31 U f30 e0 e1
RULE r1 : B g1 U f31 U f30 e0 e1 -> B g2 U f31 U f30 e0 e1
RULE r2 : B g2 U f31 U f30 e0 e1 -> U f3 U f31 U f30 e0
RULE r3 : U f3 U f31 U f30 e0 -> B g4 U f31 U f30 e0 e1
RULE r4 : B g4 U f31 U f30 e0 e1 -> U f5 U f31 U f30 e0
RULE r5 : U f5 U f31 U f30 e0 -> B g6 U f31 U f30 e0 e1
RULE r6 : B g6 U f31 U f30 e0 e1 -> U f7 U f31 U f30 e0
RULE r7 : U f7 v0 -> U f8 v0
RULE r8 : U f100 v0 -> U f120 v0
RULE r9 : U f101 v0 -> U f121 v0
RULE r10 : B g102 v0 v1 -> B g122 v0 v1
RULE r11 : U f103 v0 -> U f123 v0
RULE r12 : B g104 v0 v1 -> B g124 v0 v1
RULE r13 : B g105 v0 v1 -> B g125 v0 v1
RULE r14 : U f106 v0 -> U f126 v0
RULE r15 : U f107 v0 -> U f127 v0
RULE r16 : B g108 v0 v1 -> B g128 v0 v1
START B g61 U f60 U f0 U f31 U f30 e0 e71
GOAL B g61 U f60 U f8 U f31 U f30 e0 e71
STATE
TERM B g61 U f60 U f0 U f31 U f30 e0 e71
RW r0
TERM B g61 U f60 B g1 U f31 U f30 e0 e1 e71
RW r1
TERM B g61 U f60 B g2 U f31 U f30 e0 e1 e71
RW r2
TERM B g61 U f60 U f3 U f31 U f30 e0 e71
RW r3
TERM B g61 U f60 B g4 U f31 U f30 e0 e1 e71
RW r4
TERM B g61 U f60 U f5 U f31 U f30 e0 e71
RW r5
TERM B g61 U f60 B g6 U f31 U f30 e0 e1 e71
RW r6
TERM B g61 U f60 U f7 U f31 U f30 e0 e71
RW r7
TERM B g61 U f60 U f8 U f31 U f30 e0 e71
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
PARENT e0 e1
PARENT e0 e9
PARENT e1 e10
PARENT e1 e2
PARENT e11 e12
PARENT e13 e15
PARENT e2 e3
PARENT e3 e4
PARENT e4 e16
PARENT e4 e5
PARENT e5 e11
PARENT e5 e6
PARENT e6 e7
PARENT e7 e14
PARENT e7 e8
PARENT e8 e17
PARENT e9 e13
PARENT e9 e18
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
PARENT e0 e9
PARENT e1 e10
PARENT e1 e2
PARENT e11 e12
PARENT e13 e15
PARENT e2 e3
PARENT e3 e4
PARENT e4 e16
PARENT e4 e5
PARENT e5 e11
PARENT e5 e6
PARENT e6 e7
PARENT e7 e14
PARENT e7 e8
PARENT e8 e17
PARENT e9 e13
PARENT e9 e18
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
PARENT e0 e9
PARENT e1 e10
PARENT e1 e2
PARENT e11 e12
PARENT e13 e15
PARENT e2 e3
PARENT e3 e4
PARENT e4 e16
PARENT e4 e5
PARENT e5 e11
PARENT e5 e6
PARENT e6 e7
PARENT e7 e14
PARENT e7 e8
PARENT e8 e17
PARENT e9 e13
PARENT e9 e18
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
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
SYNTAX EDGE A B : directed step from A to B
SYNTAX QUERY REACH A C : DONE needs PATH from A to C
SYNTAX PATH A B C : ordered visited nodes
STATE EMPTY means no PATH has started
VALID PATH requires each adjacent pair has EDGE
ACTION APPEND X starts with query start or extends from last node by EDGE
DONE when PATH starts at query start and ends at query target
DEMO EDGE N0 N1 ; EDGE N1 N2 ; QUERY REACH N0 N2 ; EMPTY => APPEND N0 ; PATH N0 => APPEND N1
PROBLEM
EDGE e0 e1
EDGE e1 e2
EDGE e3 e4
QUERY REACH e0 e2
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
EDGE e3 e4
QUERY REACH e0 e2
STATE
PATH e2
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
EDGE e3 e4
QUERY REACH e0 e2
STATE
PATH e0 e1 e2
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
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p0 -> p5
HYP h4 : p1 -> p3
HYP h5 : p2 -> p0
HYP h6 : p4 -> p0
HYP h7 : p5 -> p1
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
HYP h3 : p0 -> p5
HYP h4 : p1 -> p3
HYP h5 : p2 -> p0
HYP h6 : p4 -> p0
HYP h7 : p5 -> p1
GOAL p2
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
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p0 -> p5
HYP h4 : p1 -> p3
HYP h5 : p2 -> p0
HYP h6 : p4 -> p0
HYP h7 : p5 -> p1
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
TASK
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
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
RULE r4 = r0 ; r1
RULE r5 = r4 ; r2
RULE r6 = r5 ; r3
FACT r1 e1 e3
FACT r2 e0 e4
FACT r3 e1 e3
QUERY r6 e0 e4
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
FACT r3 e3 e4
RULE r4 = r0 ; r1
RULE r5 = r4 ; r2
RULE r6 = r5 ; r3
FACT r1 e1 e3
FACT r2 e0 e4
FACT r3 e1 e3
QUERY r6 e0 e4
STATE
DERIVE r4 e0 e2 VIA e0
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
FACT r0 e0 e1
FACT r1 e1 e2
FACT r2 e2 e3
FACT r3 e3 e4
RULE r4 = r0 ; r1
RULE r5 = r4 ; r2
RULE r6 = r5 ; r3
FACT r1 e1 e3
FACT r2 e0 e4
FACT r3 e1 e3
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
SYNTAX TERM T : current expression
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
ACTION RW K AT PATH applies rule K to the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K20 : OP20 X0 -> OP21 X0 ; START OP20 X0 ; GOAL OP21 X0 ; TERM OP20 X0 => RW K20 AT ROOT
PROBLEM
RULE r0 : B g0 e0 e1 -> B g1 e0 e1
RULE r1 : B g1 e0 e1 -> U f2 e0
RULE r2 : U f2 v0 -> U f3 v0
RULE r3 : U f3 e0 -> B g4 e0 e1
RULE r4 : B g4 e0 e1 -> U f5 e0
RULE r5 : U f100 v0 -> U f120 v0
START B g0 e0 e1
GOAL U f5 e0
STATE
TERM B g0 e0 e1
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
RULE r0 : B g0 e0 e1 -> B g1 e0 e1
RULE r1 : B g1 e0 e1 -> U f2 e0
RULE r2 : U f2 v0 -> U f3 v0
RULE r3 : U f3 e0 -> B g4 e0 e1
RULE r4 : B g4 e0 e1 -> U f5 e0
RULE r5 : U f100 v0 -> U f120 v0
START B g0 e0 e1
GOAL U f5 e0
STATE
TERM B g0 e0 e1
RW r0
TERM B g1 e0 e2
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
ACTION RW K AT PATH applies rule K to the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K00 : OP00 A0 -> OP01 A0 ; START OP00 A0 ; GOAL OP01 A0 ; TERM OP00 A0 => RW K00 AT ROOT
PROBLEM
RULE r0 : B g0 e0 e1 -> B g1 e0 e1
RULE r1 : B g1 e0 e1 -> U f2 e0
RULE r2 : U f2 v0 -> U f3 v0
RULE r3 : U f3 e0 -> B g4 e0 e1
RULE r4 : B g4 e0 e1 -> U f5 e0
RULE r5 : U f100 v0 -> U f120 v0
START B g0 e0 e1
GOAL U f5 e0
STATE
TERM B g0 e0 e1
RW r0
TERM B g1 e0 e1
RW r1
TERM U f2 e0
RW r2
TERM U f3 e0
RW r3
TERM B g4 e0 e1
RW r4
TERM U f5 e0
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
DEMO PARENT X0 X1 ; PARENT X1 X2 ; QUERY ANCESTOR X0 X2 ; EMPTY => DESCEND X0 ; LINEAGE X0 => DESCEND X1
PROBLEM
PARENT e0 e1
PARENT e0 e3
PARENT e1 e2
PARENT e2 e4
PARENT e2 e6
PARENT e3 e5
QUERY ANCESTOR e0 e2
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
DEMO PARENT X0 X1 ; PARENT X1 X2 ; QUERY ANCESTOR X0 X2 ; EMPTY => DESCEND X0 ; LINEAGE X0 => DESCEND X1
PROBLEM
PARENT e0 e1
PARENT e0 e3
PARENT e1 e2
PARENT e2 e4
PARENT e2 e6
PARENT e3 e5
QUERY ANCESTOR e0 e2
STATE
LINEAGE e2
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
PARENT e0 e3
PARENT e1 e2
PARENT e2 e4
PARENT e2 e6
PARENT e3 e5
QUERY ANCESTOR e0 e2
STATE
LINEAGE e0 e1 e2
```

Target:

```text
VALID
```

### train/implication_chains/verify

- ID: `train:implication_chains:0:verify:valid`

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
HYP h4 : p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p7 -> p8
HYP h9 : p8 -> p9
HYP h10 : p9 -> p10
HYP h11 : p10 -> p11
HYP h12 : p6 -> p5
HYP h13 : p8 -> p11
HYP h14 : p8 -> p15
HYP h15 : p9 -> p6
HYP h16 : p9 -> p17
HYP h17 : p12 -> p17
HYP h18 : p13 -> p6
HYP h19 : p13 -> p14
HYP h20 : p14 -> p16
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
