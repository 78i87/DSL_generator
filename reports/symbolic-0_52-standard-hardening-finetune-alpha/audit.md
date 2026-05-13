# Dataset Audit

- Data dir: `data/symbolic-0_52-standard-hardening-finetune-alpha`
- Status: `pass`
- Errors: `0`
- Warnings: `0`

## JSONL Summary

### train

- Examples: `5960`
- Problems: `576`
- Families: `{'graph_reachability': 1440, 'implication_chains': 288, 'term_rewriting': 1352, 'tree_ancestry': 2880}`
- Modes: `{'action': 2792, 'repair_action': 2880, 'verify': 288}`
- Verify targets: `{'INVALID BAD_PREMISE': 125, 'INVALID UNKNOWN_HYP': 19, 'VALID': 144}`

### test

- Examples: `1188`
- Problems: `90`
- Families: `{'graph_reachability': 274, 'implication_chains': 228, 'relation_composition': 186, 'term_rewriting': 234, 'tree_ancestry': 266}`
- Modes: `{'action': 504, 'repair_action': 504, 'verify': 180}`
- Verify targets: `{'INVALID BAD_EDGE': 18, 'INVALID BAD_FACT': 18, 'INVALID BAD_NOT_GOAL': 3, 'INVALID BAD_NO_MATCH': 3, 'INVALID BAD_PARENT': 18, 'INVALID BAD_PATH': 7, 'INVALID BAD_PREMATURE_HALT': 2, 'INVALID BAD_PREMISE': 14, 'INVALID BAD_RESULT': 3, 'INVALID UNKNOWN_HYP': 4, 'VALID': 90}`

### ood

- Examples: `1846`
- Problems: `90`
- Families: `{'graph_reachability': 396, 'implication_chains': 360, 'relation_composition': 324, 'term_rewriting': 370, 'tree_ancestry': 396}`
- Modes: `{'action': 833, 'repair_action': 833, 'verify': 180}`
- Verify targets: `{'INVALID BAD_EDGE': 18, 'INVALID BAD_FACT': 18, 'INVALID BAD_NOT_GOAL': 3, 'INVALID BAD_NO_MATCH': 4, 'INVALID BAD_PARENT': 18, 'INVALID BAD_PATH': 2, 'INVALID BAD_PREMATURE_HALT': 5, 'INVALID BAD_PREMISE': 16, 'INVALID BAD_RESULT': 4, 'INVALID UNKNOWN_HYP': 2, 'VALID': 90}`

## Difficulty Summary

### graph_reachability

- `extra_edges`: `{'min': 1.0, 'max': 16.0, 'mean': 10.911374407582938, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `num_nodes`: `{'min': 5.0, 'max': 19.0, 'mean': 14.644075829383887, 'unique': [5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `path_length`: `{'min': 2.0, 'max': 10.0, 'mean': 8.653080568720378, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `require_shortest`: `{True: 2110}`
- `symbol_offset`: `{'min': 0.0, 'max': 4.0, 'mean': 1.2739336492890996, 'unique': [0, 2, 4]}`

### implication_chains

- `distractor_hyps`: `{'min': 1.0, 'max': 12.0, 'mean': 8.17123287671233, 'unique': [1, 4, 5, 6, 7, 8, 9, 10, 11, 12]}`
- `num_props`: `{'min': 6.0, 'max': 19.0, 'mean': 13.422374429223744, 'unique': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`
- `proof_length`: `{'min': 2.0, 'max': 10.0, 'mean': 8.19634703196347, 'unique': [2, 3, 4, 6, 7, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 4.0, 'mean': 0.6575342465753424, 'unique': [0, 2, 4]}`

### relation_composition

- `composition_depth`: `{'min': 2.0, 'max': 10.0, 'mean': 7.925490196078432, 'unique': [2, 3, 4, 6, 7, 8, 9, 10]}`
- `distractor_facts`: `{'min': 1.0, 'max': 10.0, 'mean': 6.956862745098039, 'unique': [1, 4, 5, 6, 7, 8, 9, 10]}`
- `num_entities`: `{'min': 5.0, 'max': 16.0, 'mean': 12.568627450980392, 'unique': [5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `symbol_offset`: `{'min': 0.0, 'max': 0.0, 'mean': 0.0, 'unique': [0]}`

### term_rewriting

- `action_format`: `{'rule': 1956}`
- `binary_rules`: `{'min': 1.0, 'max': 10.0, 'mean': 6.741820040899795, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_rules`: `{'min': 0.0, 'max': 16.0, 'mean': 11.1579754601227, 'unique': [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `query_kind`: `{'goal': 1219, 'normal_form': 737}`
- `repeated_subterms`: `{False: 1500, True: 456}`
- `rewrite_steps`: `{'min': 2.0, 'max': 10.0, 'mean': 8.681492842535787, 'unique': [2, 3, 4, 6, 7, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 4.0, 'mean': 1.2750511247443763, 'unique': [0, 2, 4]}`
- `term_depth`: `{'min': 1.0, 'max': 9.0, 'mean': 4.736707566462168, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9]}`
- `variable_rules`: `{'min': 0.0, 'max': 7.0, 'mean': 2.9473415132924337, 'unique': [0, 1, 2, 3, 4, 5, 6, 7]}`

### tree_ancestry

- `branching_factor`: `{'min': 2.0, 'max': 4.0, 'mean': 2.876341050254094, 'unique': [2, 3, 4]}`
- `depth`: `{'min': 2.0, 'max': 10.0, 'mean': 8.822699040090344, 'unique': [2, 3, 5, 6, 7, 8, 9, 10]}`
- `distractor_subtrees`: `{'min': 1.0, 'max': 16.0, 'mean': 11.79107848673066, 'unique': [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `symbol_offset`: `{'min': 0.0, 'max': 4.0, 'mean': 1.517786561264822, 'unique': [0, 2, 4]}`

## TRM Array Summary

### train

- Inputs shape: `[5960, 970]`
- Labels shape: `[5960, 970]`
- Seq len: `970`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `5960`

### test

- Inputs shape: `[1188, 970]`
- Labels shape: `[1188, 970]`
- Seq len: `970`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1188`

### ood

- Inputs shape: `[1846, 970]`
- Labels shape: `[1846, 970]`
- Seq len: `970`
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
EDGE e4 e0
EDGE e0 e5
EDGE e10 e3
EDGE e5 e2
EDGE e2 e3
EDGE e3 e0
EDGE e3 e1
EDGE e1 e3
EDGE e1 e6
EDGE e6 e8
EDGE e8 e9
EDGE e9 e0
EDGE e9 e3
EDGE e7 e0
QUERY REACH e4 e9
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
EDGE e4 e0
EDGE e0 e5
EDGE e10 e3
EDGE e5 e2
EDGE e2 e3
EDGE e3 e0
EDGE e3 e1
EDGE e1 e3
EDGE e1 e6
EDGE e6 e8
EDGE e8 e9
EDGE e9 e0
EDGE e9 e3
EDGE e7 e0
QUERY REACH e4 e9
STATE
PATH e9
```

Target:

```text
REPLACE ROOT WITH e4
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
EDGE e4 e0
EDGE e0 e5
EDGE e10 e3
EDGE e5 e2
EDGE e2 e3
EDGE e3 e0
EDGE e3 e1
EDGE e1 e3
EDGE e1 e6
EDGE e6 e8
EDGE e8 e9
EDGE e9 e0
EDGE e9 e3
EDGE e7 e0
QUERY REACH e4 e9
STATE
PATH e4 e0 e5 e2 e3 e1 e6 e8 e9
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
HYP h8 : p0
HYP h7 : p0 -> p1
HYP h11 : p1 -> p7
HYP h999 : p7 -> p6
HYP h6 : p6 -> p9
HYP h1 : p9 -> p12
HYP h12 : p12 -> p4
HYP h3 : p4 -> p3
HYP h18 : p6 -> p1
HYP h15 : p9 -> p3
HYP h4 : p12 -> p2
HYP h17 : p4 -> p1
HYP h9 : p4 -> p9
HYP h16 : p4 -> p11
HYP h5 : p8 -> p12
HYP h10 : p8 -> p2
HYP h0 : p5 -> p6
HYP h14 : p5 -> p4
HYP h2 : p11 -> p1
GOAL p3
STATE
EMPTY
```

Target:

```text
APPLY h8
```

### ood/implication_chains/repair_action

- ID: `ood:implication_chains:18:repair_action:1`

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
HYP h8 : p0
HYP h7 : p0 -> p1
HYP h11 : p1 -> p7
HYP h999 : p7 -> p6
HYP h6 : p6 -> p9
HYP h1 : p9 -> p12
HYP h12 : p12 -> p4
HYP h3 : p4 -> p3
HYP h18 : p6 -> p1
HYP h15 : p9 -> p3
HYP h4 : p12 -> p2
HYP h17 : p4 -> p1
HYP h9 : p4 -> p9
HYP h16 : p4 -> p11
HYP h5 : p8 -> p12
HYP h10 : p8 -> p2
HYP h0 : p5 -> p6
HYP h14 : p5 -> p4
HYP h2 : p11 -> p1
GOAL p3
STATE
DERIVE p0 BY h13
```

Target:

```text
REPLACE FIRST HYP h8
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
HYP h8 : p0
HYP h7 : p0 -> p1
HYP h11 : p1 -> p7
HYP h999 : p7 -> p6
HYP h6 : p6 -> p9
HYP h1 : p9 -> p12
HYP h12 : p12 -> p4
HYP h3 : p4 -> p3
HYP h18 : p6 -> p1
HYP h15 : p9 -> p3
HYP h4 : p12 -> p2
HYP h17 : p4 -> p1
HYP h9 : p4 -> p9
HYP h16 : p4 -> p11
HYP h5 : p8 -> p12
HYP h10 : p8 -> p2
HYP h0 : p5 -> p6
HYP h14 : p5 -> p4
HYP h2 : p11 -> p1
GOAL p3
STATE
DERIVE p0 BY h8
DERIVE p1 BY h7 FROM p0
DERIVE p7 BY h11 FROM p1
DERIVE p6 BY h999 FROM p7
DERIVE p9 BY h6 FROM p6
DERIVE p12 BY h1 FROM p9
DERIVE p4 BY h12 FROM p12
DERIVE p3 BY h3 FROM p4
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
FACT r2 e4 e12
FACT r6 e12 e8
FACT r5 e8 e0
FACT r7 e0 e11
FACT r14 e11 e6
FACT r12 e6 e3
FACT r8 e3 e7
FACT r10 e7 e5
RULE r0 = r2 ; r6
RULE r3 = r0 ; r5
RULE r1 = r3 ; r7
RULE r4 = r1 ; r14
RULE r11 = r4 ; r12
RULE r9 = r11 ; r8
RULE r13 = r9 ; r10
FACT r2 e12 e7
FACT r2 e6 e0
FACT r6 e12 e5
FACT r7 e12 e6
FACT r7 e5 e2
FACT r14 e1 e7
FACT r12 e2 e6
FACT r8 e12 e2
FACT r8 e11 e8
QUERY r13 e4 e5
STATE
EMPTY
```

Target:

```text
FOLLOW e4 e8 VIA e12
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
FACT r2 e4 e12
FACT r6 e12 e8
FACT r5 e8 e0
FACT r7 e0 e11
FACT r14 e11 e6
FACT r12 e6 e3
FACT r8 e3 e7
FACT r10 e7 e5
RULE r0 = r2 ; r6
RULE r3 = r0 ; r5
RULE r1 = r3 ; r7
RULE r4 = r1 ; r14
RULE r11 = r4 ; r12
RULE r9 = r11 ; r8
RULE r13 = r9 ; r10
FACT r2 e12 e7
FACT r2 e6 e0
FACT r6 e12 e5
FACT r7 e12 e6
FACT r7 e5 e2
FACT r14 e1 e7
FACT r12 e2 e6
FACT r8 e12 e2
FACT r8 e11 e8
QUERY r13 e4 e5
STATE
DERIVE r0 e4 e8 VIA e4
```

Target:

```text
REPLACE FIRST VIA e12
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
FACT r2 e4 e12
FACT r6 e12 e8
FACT r5 e8 e0
FACT r7 e0 e11
FACT r14 e11 e6
FACT r12 e6 e3
FACT r8 e3 e7
FACT r10 e7 e5
RULE r0 = r2 ; r6
RULE r3 = r0 ; r5
RULE r1 = r3 ; r7
RULE r4 = r1 ; r14
RULE r11 = r4 ; r12
RULE r9 = r11 ; r8
RULE r13 = r9 ; r10
FACT r2 e12 e7
FACT r2 e6 e0
FACT r6 e12 e5
FACT r7 e12 e6
FACT r7 e5 e2
FACT r14 e1 e7
FACT r12 e2 e6
FACT r8 e12 e2
FACT r8 e11 e8
QUERY r13 e4 e5
STATE
DERIVE r0 e4 e8 VIA e12
DERIVE r3 e4 e0 VIA e8
DERIVE r1 e4 e11 VIA e0
DERIVE r4 e4 e6 VIA e11
DERIVE r11 e4 e3 VIA e6
DERIVE r9 e4 e7 VIA e3
DERIVE r13 e4 e5 VIA e7
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
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs current TERM equal T
SYNTAX QUERY NORMAL_FORM : DONE needs no RULE applicable
SYNTAX TERM T : current expression
ACTION RW K AT PATH applies rule K to the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K00 : OP00 A0 -> OP01 A0 ; START OP00 A0 ; GOAL OP01 A0 ; TERM OP00 A0 => RW K00 AT ROOT
PROBLEM
RULE r12 : B g63 U f100 U f124 e0 e72 -> U f111 U f100 U f124 e0
RULE r3 : U f111 U f100 U f124 e0 -> B g5 U f100 U f124 e0 e72
RULE r13 : B g5 U f100 U f124 e0 e72 -> U f3 U f100 U f124 e0
RULE r8 : U f3 U f100 U f124 e0 -> B g122 U f100 U f124 e0 e72
RULE r10 : B g122 v1 v0 -> B g127 v1 v0
RULE r7 : B g127 U f100 U f124 e0 e72 -> U f120 U f100 U f124 e0
RULE r5 : U f120 U f100 U f124 e0 -> B g60 U f100 U f124 e0 e72
RULE r9 : B g60 v1 v0 -> B g103 v1 v0
RULE r17 : U f32 v1 -> U f30 v1
RULE r15 : B g61 v1 v0 -> B g2 v1 v0
RULE r18 : B g102 v1 v0 -> B g8 v1 v0
RULE r1 : B g4 v1 v0 -> B g121 v1 v0
RULE r14 : U f104 v1 -> U f108 v1
RULE r2 : B g130 v1 v0 -> B g0 v1 v0
RULE r6 : B g107 v1 v0 -> B g7 v1 v0
RULE r16 : B g106 v1 v0 -> B g125 v1 v0
RULE r0 : U f61 v1 -> U f31 v1
RULE r4 : U f109 v1 -> U f129 v1
RULE r19 : B g126 v1 v0 -> B g105 v1 v0
RULE r11 : U f6 v1 -> U f131 v1
START B g62 e71 U f128 B g110 B g63 U f100 U f124 e0 e72 e1
GOAL B g62 e71 U f128 B g110 B g103 U f100 U f124 e0 e72 e1
STATE
TERM B g62 e71 U f128 B g110 B g63 U f100 U f124 e0 e72 e1
```

Target:

```text
RW r12
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
RULE r12 : B g63 U f100 U f124 e0 e72 -> U f111 U f100 U f124 e0
RULE r3 : U f111 U f100 U f124 e0 -> B g5 U f100 U f124 e0 e72
RULE r13 : B g5 U f100 U f124 e0 e72 -> U f3 U f100 U f124 e0
RULE r8 : U f3 U f100 U f124 e0 -> B g122 U f100 U f124 e0 e72
RULE r10 : B g122 v1 v0 -> B g127 v1 v0
RULE r7 : B g127 U f100 U f124 e0 e72 -> U f120 U f100 U f124 e0
RULE r5 : U f120 U f100 U f124 e0 -> B g60 U f100 U f124 e0 e72
RULE r9 : B g60 v1 v0 -> B g103 v1 v0
RULE r17 : U f32 v1 -> U f30 v1
RULE r15 : B g61 v1 v0 -> B g2 v1 v0
RULE r18 : B g102 v1 v0 -> B g8 v1 v0
RULE r1 : B g4 v1 v0 -> B g121 v1 v0
RULE r14 : U f104 v1 -> U f108 v1
RULE r2 : B g130 v1 v0 -> B g0 v1 v0
RULE r6 : B g107 v1 v0 -> B g7 v1 v0
RULE r16 : B g106 v1 v0 -> B g125 v1 v0
RULE r0 : U f61 v1 -> U f31 v1
RULE r4 : U f109 v1 -> U f129 v1
RULE r19 : B g126 v1 v0 -> B g105 v1 v0
RULE r11 : U f6 v1 -> U f131 v1
START B g62 e71 U f128 B g110 B g63 U f100 U f124 e0 e72 e1
GOAL B g62 e71 U f128 B g110 B g103 U f100 U f124 e0 e72 e1
STATE
TERM B g62 e71 U f128 B g110 B g63 U f100 U f124 e0 e72 e1
RW r12
TERM B g62 e71 U f128 B g110 U f111 U f1 U f124 e0 e1
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
ACTION RW K AT PATH applies rule K to the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K20 : OP20 X0 -> OP21 X0 ; START OP20 X0 ; GOAL OP21 X0 ; TERM OP20 X0 => RW K20 AT ROOT
PROBLEM
RULE r12 : B g63 U f100 U f124 e0 e72 -> U f111 U f100 U f124 e0
RULE r3 : U f111 U f100 U f124 e0 -> B g5 U f100 U f124 e0 e72
RULE r13 : B g5 U f100 U f124 e0 e72 -> U f3 U f100 U f124 e0
RULE r8 : U f3 U f100 U f124 e0 -> B g122 U f100 U f124 e0 e72
RULE r10 : B g122 v1 v0 -> B g127 v1 v0
RULE r7 : B g127 U f100 U f124 e0 e72 -> U f120 U f100 U f124 e0
RULE r5 : U f120 U f100 U f124 e0 -> B g60 U f100 U f124 e0 e72
RULE r9 : B g60 v1 v0 -> B g103 v1 v0
RULE r17 : U f32 v1 -> U f30 v1
RULE r15 : B g61 v1 v0 -> B g2 v1 v0
RULE r18 : B g102 v1 v0 -> B g8 v1 v0
RULE r1 : B g4 v1 v0 -> B g121 v1 v0
RULE r14 : U f104 v1 -> U f108 v1
RULE r2 : B g130 v1 v0 -> B g0 v1 v0
RULE r6 : B g107 v1 v0 -> B g7 v1 v0
RULE r16 : B g106 v1 v0 -> B g125 v1 v0
RULE r0 : U f61 v1 -> U f31 v1
RULE r4 : U f109 v1 -> U f129 v1
RULE r19 : B g126 v1 v0 -> B g105 v1 v0
RULE r11 : U f6 v1 -> U f131 v1
START B g62 e71 U f128 B g110 B g63 U f100 U f124 e0 e72 e1
GOAL B g62 e71 U f128 B g110 B g103 U f100 U f124 e0 e72 e1
STATE
TERM B g62 e71 U f128 B g110 B g63 U f100 U f124 e0 e72 e1
RW r12
TERM B g62 e71 U f128 B g110 U f111 U f100 U f124 e0 e1
RW r3
TERM B g62 e71 U f128 B g110 B g5 U f100 U f124 e0 e72 e1
RW r13
TERM B g62 e71 U f128 B g110 U f3 U f100 U f124 e0 e1
RW r8
TERM B g62 e71 U f128 B g110 B g122 U f100 U f124 e0 e72 e1
RW r10
TERM B g62 e71 U f128 B g110 B g127 U f100 U f124 e0 e72 e1
RW r7
TERM B g62 e71 U f128 B g110 U f120 U f100 U f124 e0 e1
RW r5
TERM B g62 e71 U f128 B g110 B g60 U f100 U f124 e0 e72 e1
RW r9
TERM B g62 e71 U f128 B g110 B g103 U f100 U f124 e0 e72 e1
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
PARENT e5 e8
PARENT e5 e16
PARENT e8 e11
PARENT e7 e4
PARENT e7 e10
PARENT e4 e3
PARENT e11 e15
PARENT e11 e13
PARENT e13 e6
PARENT e6 e2
PARENT e2 e1
PARENT e2 e9
PARENT e9 e12
PARENT e12 e14
PARENT e14 e7
PARENT e14 e0
QUERY ANCESTOR e5 e14
STATE
EMPTY
```

Target:

```text
DESCEND e5
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
PARENT e5 e8
PARENT e5 e16
PARENT e8 e11
PARENT e7 e4
PARENT e7 e10
PARENT e4 e3
PARENT e11 e15
PARENT e11 e13
PARENT e13 e6
PARENT e6 e2
PARENT e2 e1
PARENT e2 e9
PARENT e9 e12
PARENT e12 e14
PARENT e14 e7
PARENT e14 e0
QUERY ANCESTOR e5 e14
STATE
LINEAGE e14
```

Target:

```text
REPLACE ROOT WITH e5
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
DEMO PARENT A0 A1 ; PARENT A1 A2 ; QUERY ANCESTOR A0 A2 ; EMPTY => DESCEND A0 ; LINEAGE A0 => DESCEND A1
PROBLEM
PARENT e5 e8
PARENT e5 e16
PARENT e8 e11
PARENT e7 e4
PARENT e7 e10
PARENT e4 e3
PARENT e11 e15
PARENT e11 e13
PARENT e13 e6
PARENT e6 e2
PARENT e2 e1
PARENT e2 e9
PARENT e9 e12
PARENT e12 e14
PARENT e14 e7
PARENT e14 e0
QUERY ANCESTOR e5 e14
STATE
LINEAGE e5 e8 e11 e13 e6 e2 e9 e12 e14
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
EDGE e2 e0
EDGE e0 e8
EDGE e8 e6
EDGE e3 e1
QUERY REACH e2 e6
STATE
EMPTY
```

Target:

```text
APPEND e2
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
EDGE e2 e0
EDGE e0 e8
EDGE e8 e6
EDGE e3 e1
QUERY REACH e2 e6
STATE
PATH e6
```

Target:

```text
REPLACE ROOT WITH e2
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
EDGE e2 e0
EDGE e0 e8
EDGE e8 e6
EDGE e3 e1
QUERY REACH e2 e6
STATE
PATH e2 e0 e8 e6
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
HYP h4 : p4
HYP h8 : p4 -> p0
HYP h999 : p0 -> p5
HYP h2 : p5 -> p6
HYP h5 : p4 -> p6
HYP h1 : p0 -> p2
HYP h0 : p1 -> p2
HYP h3 : p2 -> p6
HYP h7 : p3 -> p0
GOAL p6
STATE
EMPTY
```

Target:

```text
APPLY h4
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
HYP h4 : p4
HYP h8 : p4 -> p0
HYP h999 : p0 -> p5
HYP h2 : p5 -> p6
HYP h5 : p4 -> p6
HYP h1 : p0 -> p2
HYP h0 : p1 -> p2
HYP h3 : p2 -> p6
HYP h7 : p3 -> p0
GOAL p6
STATE
DERIVE p4 BY h6
```

Target:

```text
REPLACE FIRST HYP h4
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
HYP h4 : p4
HYP h8 : p4 -> p0
HYP h999 : p0 -> p5
HYP h2 : p5 -> p6
HYP h5 : p4 -> p6
HYP h1 : p0 -> p2
HYP h0 : p1 -> p2
HYP h3 : p2 -> p6
HYP h7 : p3 -> p0
GOAL p6
STATE
DERIVE p4 BY h4
DERIVE p0 BY h8 FROM p4
DERIVE p5 BY h999 FROM p0
DERIVE p6 BY h2 FROM p5
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
FACT r1 e1 e0
FACT r2 e0 e3
RULE r0 = r1 ; r2
FACT r1 e1 e2
FACT r2 e5 e3
FACT r2 e2 e3
FACT r2 e6 e4
QUERY r0 e1 e3
STATE
EMPTY
```

Target:

```text
FOLLOW e1 e3 VIA e0
```

### test/relation_composition/repair_action

- ID: `test:relation_composition:36:repair_action:1`

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
FACT r1 e1 e0
FACT r2 e0 e3
RULE r0 = r1 ; r2
FACT r1 e1 e2
FACT r2 e5 e3
FACT r2 e2 e3
FACT r2 e6 e4
QUERY r0 e1 e3
STATE
DERIVE r0 e1 e3 VIA e1
```

Target:

```text
REPLACE FIRST VIA e0
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
FACT r1 e1 e0
FACT r2 e0 e3
RULE r0 = r1 ; r2
FACT r1 e1 e2
FACT r2 e5 e3
FACT r2 e2 e3
FACT r2 e6 e4
QUERY r0 e1 e3
STATE
DERIVE r0 e1 e3 VIA e0
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
RULE r3 : B g121 U f1 U f30 e1 e0 -> U f100 U f1 U f30 e1
RULE r0 : U f100 U f1 U f30 e1 -> U f61 U f1 U f30 e1
RULE r1 : U f61 U f1 U f30 e1 -> U f60 U f1 U f30 e1
RULE r4 : U f122 v1 -> U f3 v1
RULE r5 : B g0 v1 v0 -> B g101 v1 v0
RULE r2 : U f102 v1 -> U f120 v1
START U f2 B g121 U f1 U f30 e1 e0
GOAL U f2 U f60 U f1 U f30 e1
STATE
TERM U f2 B g121 U f1 U f30 e1 e0
```

Target:

```text
RW r3
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
RULE r3 : B g121 U f1 U f30 e1 e0 -> U f100 U f1 U f30 e1
RULE r0 : U f100 U f1 U f30 e1 -> U f61 U f1 U f30 e1
RULE r1 : U f61 U f1 U f30 e1 -> U f60 U f1 U f30 e1
RULE r4 : U f122 v1 -> U f3 v1
RULE r5 : B g0 v1 v0 -> B g101 v1 v0
RULE r2 : U f102 v1 -> U f120 v1
START U f2 B g121 U f1 U f30 e1 e0
GOAL U f2 U f60 U f1 U f30 e1
STATE
TERM U f2 B g121 U f1 U f30 e1 e0
RW r3
TERM U f31 U f100 U f1 U f30 e1
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
RULE r3 : B g121 U f1 U f30 e1 e0 -> U f100 U f1 U f30 e1
RULE r0 : U f100 U f1 U f30 e1 -> U f61 U f1 U f30 e1
RULE r1 : U f61 U f1 U f30 e1 -> U f60 U f1 U f30 e1
RULE r4 : U f122 v1 -> U f3 v1
RULE r5 : B g0 v1 v0 -> B g101 v1 v0
RULE r2 : U f102 v1 -> U f120 v1
START U f2 B g121 U f1 U f30 e1 e0
GOAL U f2 U f60 U f1 U f30 e1
STATE
TERM U f2 B g121 U f1 U f30 e1 e0
RW r3
TERM U f2 U f100 U f1 U f30 e1
RW r0
TERM U f2 U f61 U f1 U f30 e1
RW r1
TERM U f2 U f60 U f1 U f30 e1
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
PARENT e2 e4
PARENT e4 e3
PARENT e3 e1
PARENT e3 e0
QUERY ANCESTOR e2 e1
STATE
EMPTY
```

Target:

```text
DESCEND e2
```

### test/tree_ancestry/repair_action

- ID: `test:tree_ancestry:54:repair_action:1`

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
PARENT e2 e4
PARENT e4 e3
PARENT e3 e1
PARENT e3 e0
QUERY ANCESTOR e2 e1
STATE
LINEAGE e1
```

Target:

```text
REPLACE ROOT WITH e2
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
DEMO PARENT A0 A1 ; PARENT A1 A2 ; QUERY ANCESTOR A0 A2 ; EMPTY => DESCEND A0 ; LINEAGE A0 => DESCEND A1
PROBLEM
PARENT e2 e4
PARENT e4 e3
PARENT e3 e1
PARENT e3 e0
QUERY ANCESTOR e2 e1
STATE
LINEAGE e2 e4 e3 e1
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
SYNTAX EDGE A B : directed step from A to B
SYNTAX QUERY REACH A C : DONE needs PATH from A to C
SYNTAX PATH A B C : ordered visited nodes
STATE EMPTY means no PATH has started
VALID PATH requires each adjacent pair has EDGE
ACTION APPEND X starts with query start or extends from last node by EDGE
DONE when PATH starts at query start and ends at query target
DEMO EDGE A0 A1 ; EDGE A1 A2 ; QUERY REACH A0 A2 ; EMPTY => APPEND A0 ; PATH A0 => APPEND A1
PROBLEM
EDGE e14 e15
EDGE e14 e16
EDGE e14 e13
EDGE e14 e10
EDGE e15 e6
EDGE e16 e7
EDGE e17 e8
EDGE e17 e10
EDGE e8 e14
EDGE e8 e16
EDGE e4 e14
EDGE e5 e6
EDGE e5 e10
EDGE e12 e9
EDGE e9 e7
EDGE e7 e11
EDGE e11 e17
EDGE e11 e12
EDGE e11 e13
EDGE e13 e9
EDGE e13 e10
EDGE e10 e14
QUERY REACH e12 e6
STATE
PATH e6
```

Target:

```text
REPLACE ROOT WITH e12
```

### train/implication_chains/verify

- ID: `train:implication_chains:144:verify:valid`

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
HYP h9 : p14
HYP h12 : p14 -> p12
HYP h10 : p12 -> p10
HYP h15 : p10 -> p13
HYP h11 : p13 -> p4
HYP h17 : p4 -> p16
HYP h8 : p16 -> p6
HYP h5 : p6 -> p7
HYP h13 : p12 -> p7
HYP h19 : p10 -> p6
HYP h16 : p9 -> p15
HYP h18 : p15 -> p13
HYP h6 : p15 -> p8
HYP h7 : p8 -> p12
HYP h14 : p11 -> p4
HYP h4 : p5 -> p13
GOAL p7
STATE
DERIVE p14 BY h9
DERIVE p12 BY h12 FROM p14
DERIVE p10 BY h10 FROM p12
DERIVE p13 BY h15 FROM p10
DERIVE p4 BY h11 FROM p13
DERIVE p16 BY h17 FROM p4
DERIVE p6 BY h8 FROM p16
DERIVE p7 BY h5 FROM p6
```

Target:

```text
VALID
```

### train/term_rewriting/action

- ID: `train:term_rewriting:432:action:0`

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
RULE r15 : U f130 U f110 U f107 e5 -> B g6 U f110 U f107 e5 e4
RULE r6 : B g6 U f110 U f107 e5 e4 -> B g9 U f110 U f107 e5 e4
RULE r11 : B g9 v1 v0 -> B g133 v1 v0
RULE r13 : B g133 U f110 U f107 e5 e4 -> U f34 U f110 U f107 e5
RULE r19 : U f34 U f110 U f107 e5 -> B g106 U f110 U f107 e5 e4
RULE r5 : B g106 U f110 U f107 e5 e4 -> U f35 U f110 U f107 e5
RULE r7 : U f35 U f110 U f107 e5 -> B g11 U f110 U f107 e5 e4
RULE r23 : B g11 U f110 U f107 e5 e4 -> U f8 U f110 U f107 e5
RULE r22 : U f131 v1 -> U f105 v1
RULE r21 : U f111 v1 -> U f12 v1
RULE r12 : B g135 v1 v0 -> B g128 v1 v0
RULE r17 : U f104 v1 -> U f10 v1
RULE r16 : B g5 v1 v0 -> B g115 v1 v0
RULE r4 : B g126 v1 v0 -> B g108 v1 v0
RULE r10 : U f4 v1 -> U f124 v1
RULE r14 : U f127 v1 -> U f125 v1
RULE r8 : B g114 v1 v0 -> B g129 v1 v0
RULE r9 : B g134 v1 v0 -> B g113 v1 v0
RULE r18 : B g109 v1 v0 -> B g132 v1 v0
RULE r20 : B g112 v1 v0 -> B g7 v1 v0
START U f130 U f110 U f107 e5
GOAL U f8 U f110 U f107 e5
STATE
TERM U f130 U f110 U f107 e5
```

Target:

```text
RW r15
```

### train/tree_ancestry/action

- ID: `train:tree_ancestry:288:action:0`

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
PARENT e10 e12
PARENT e10 e20
PARENT e10 e18
PARENT e10 e15
PARENT e12 e13
PARENT e13 e4
PARENT e16 e21
PARENT e14 e24
PARENT e21 e9
PARENT e8 e25
PARENT e7 e23
PARENT e7 e5
PARENT e5 e16
PARENT e5 e17
PARENT e5 e6
PARENT e6 e14
PARENT e6 e11
PARENT e11 e22
PARENT e22 e8
PARENT e22 e19
PARENT e19 e10
QUERY ANCESTOR e7 e13
STATE
EMPTY
```

Target:

```text
DESCEND e7
```

### train/tree_ancestry/repair_action

- ID: `train:tree_ancestry:288:repair_action:1`

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
PARENT e10 e12
PARENT e10 e20
PARENT e10 e18
PARENT e10 e15
PARENT e12 e13
PARENT e13 e4
PARENT e16 e21
PARENT e14 e24
PARENT e21 e9
PARENT e8 e25
PARENT e7 e23
PARENT e7 e5
PARENT e5 e16
PARENT e5 e17
PARENT e5 e6
PARENT e6 e14
PARENT e6 e11
PARENT e11 e22
PARENT e22 e8
PARENT e22 e19
PARENT e19 e10
QUERY ANCESTOR e7 e13
STATE
LINEAGE e13
```

Target:

```text
REPLACE ROOT WITH e7
```
