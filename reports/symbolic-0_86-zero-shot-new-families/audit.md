# Dataset Audit

- Data dir: `data/symbolic-0_86-zero-shot-new-families`
- Status: `pass`
- Errors: `0`
- Warnings: `0`

## JSONL Summary

### train

- Examples: `28`
- Problems: `3`
- Families: `{'dfa_simulation_lite': 10, 'equality_rewriting_lite': 8, 'shortest_path_lite': 10}`
- Modes: `{'action': 11, 'repair_action': 11, 'verify': 6}`
- Verify targets: `{'INVALID BAD_FACT': 1, 'INVALID BAD_PATH': 1, 'INVALID BAD_RESULT': 1, 'VALID': 3}`

### test

- Examples: `24`
- Problems: `3`
- Families: `{'dfa_simulation_lite': 8, 'equality_rewriting_lite': 8, 'shortest_path_lite': 8}`
- Modes: `{'action': 9, 'repair_action': 9, 'verify': 6}`
- Verify targets: `{'INVALID BAD_PATH': 2, 'INVALID BAD_RESULT': 1, 'VALID': 3}`

### ood

- Examples: `392`
- Problems: `36`
- Families: `{'dfa_simulation_lite': 138, 'equality_rewriting_lite': 114, 'shortest_path_lite': 140}`
- Modes: `{'action': 160, 'repair_action': 160, 'verify': 72}`
- Verify targets: `{'INVALID BAD_EDGE': 9, 'INVALID BAD_FACT': 8, 'INVALID BAD_PATH': 7, 'INVALID BAD_RESULT': 12, 'VALID': 36}`

## Difficulty Summary

### dfa_simulation_lite

- `distractor_facts`: `{'min': 5.0, 'max': 8.0, 'mean': 6.538461538461538, 'unique': [5, 8]}`
- `input_length`: `{'min': 2.0, 'max': 6.0, 'mean': 3.7948717948717947, 'unique': [2, 3, 4, 5, 6]}`
- `num_states`: `{'min': 8.0, 'max': 12.0, 'mean': 10.051282051282051, 'unique': [8, 12]}`
- `relation_count`: `{'min': 3.0, 'max': 4.0, 'mean': 3.5128205128205128, 'unique': [3, 4]}`
- `symbol_offset`: `{'min': 0.0, 'max': 2.0, 'mean': 1.0256410256410255, 'unique': [0, 2]}`

### equality_rewriting_lite

- `distractor_rules`: `{'min': 3.0, 'max': 4.0, 'mean': 3.5692307692307694, 'unique': [3, 4]}`
- `reversed_rules`: `{'min': 0.0, 'max': 4.0, 'mean': 1.7230769230769232, 'unique': [0, 1, 2, 3, 4]}`
- `rewrite_steps`: `{'min': 2.0, 'max': 6.0, 'mean': 4.092307692307692, 'unique': [2, 3, 4, 5, 6]}`
- `symbol_offset`: `{'min': 0.0, 'max': 0.0, 'mean': 0.0, 'unique': [0]}`

### shortest_path_lite

- `extra_edges`: `{'min': 5.0, 'max': 8.0, 'mean': 6.594936708860759, 'unique': [5, 8]}`
- `num_nodes`: `{'min': 8.0, 'max': 12.0, 'mean': 10.126582278481013, 'unique': [8, 12]}`
- `path_length`: `{'min': 2.0, 'max': 6.0, 'mean': 3.9873417721518987, 'unique': [2, 3, 4, 6]}`
- `symbol_offset`: `{'min': 0.0, 'max': 2.0, 'mean': 1.0632911392405062, 'unique': [0, 2]}`

## TRM Array Summary

### train

- Inputs shape: `[28, 328]`
- Labels shape: `[28, 328]`
- Seq len: `328`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `28`

### test

- Inputs shape: `[24, 328]`
- Labels shape: `[24, 328]`
- Seq len: `328`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `24`

### ood

- Inputs shape: `[392, 328]`
- Labels shape: `[392, 328]`
- Seq len: `328`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `392`

## Samples

### ood/dfa_simulation_lite/action

- ID: `ood:dfa_simulation_lite:12:action:0`

Source:

```text
MODE action
TASK
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX FACT R A B : directed step from A to B
SYNTAX HYP K : R : ordered rule R
SYNTAX START A : initial STATE is A
SYNTAX GOAL C : DONE needs PATH ending C
SYNTAX PATH A B C : ordered visited nodes
ACTION APPEND X starts or extends PATH by next HYP rule
VALID PATH uses each HYP rule with matching FACT
DEMO FACT REL20 X0 X1 ; FACT REL21 X1 X2 ; HYP K20 : REL20 ; HYP K21 : REL21 ; START X0 ; GOAL X2 ; EMPTY => APPEND X0 ; PATH X0 => APPEND X1
PROBLEM
FACT r0 e1 e2
FACT r1 e2 e3
FACT r1 e4 e2
FACT r2 e0 e1
FACT r2 e2 e6
FACT r2 e4 e7
FACT r2 e6 e0
FACT r2 e6 e5
HYP h0 : r2
HYP h1 : r0
HYP h2 : r1
START e0
GOAL e3
STATE
EMPTY
```

Target:

```text
APPEND e0
```

### ood/dfa_simulation_lite/repair_action

- ID: `ood:dfa_simulation_lite:12:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX FACT R A B : directed step from A to B
SYNTAX HYP K : R : ordered rule R
SYNTAX START A : initial STATE is A
SYNTAX GOAL C : DONE needs PATH ending C
SYNTAX PATH A B C : ordered visited nodes
ACTION APPEND X starts or extends PATH by next HYP rule
VALID PATH uses each HYP rule with matching FACT
DEMO FACT REL00 A0 A1 ; FACT REL01 A1 A2 ; HYP K00 : REL00 ; HYP K01 : REL01 ; START A0 ; GOAL A2 ; EMPTY => APPEND A0 ; PATH A0 => APPEND A1
PROBLEM
FACT r0 e1 e2
FACT r1 e2 e3
FACT r1 e4 e2
FACT r2 e0 e1
FACT r2 e2 e6
FACT r2 e4 e7
FACT r2 e6 e0
FACT r2 e6 e5
HYP h0 : r2
HYP h1 : r0
HYP h2 : r1
START e0
GOAL e3
STATE
PATH e3
```

Target:

```text
REPLACE ROOT WITH e0
```

### ood/dfa_simulation_lite/verify

- ID: `ood:dfa_simulation_lite:12:verify:valid`

Source:

```text
MODE verify
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX FACT R A B : directed step from A to B
SYNTAX HYP K : R : ordered rule R
SYNTAX START A : initial STATE is A
SYNTAX GOAL C : DONE needs PATH ending C
SYNTAX PATH A B C : ordered visited nodes
ACTION APPEND X starts or extends PATH by next HYP rule
VALID PATH uses each HYP rule with matching FACT
DEMO FACT REL20 X0 X1 ; FACT REL21 X1 X2 ; HYP K20 : REL20 ; HYP K21 : REL21 ; START X0 ; GOAL X2 ; EMPTY => APPEND X0 ; PATH X0 => APPEND X1
PROBLEM
FACT r0 e1 e2
FACT r1 e2 e3
FACT r1 e4 e2
FACT r2 e0 e1
FACT r2 e2 e6
FACT r2 e4 e7
FACT r2 e6 e0
FACT r2 e6 e5
HYP h0 : r2
HYP h1 : r0
HYP h2 : r1
START e0
GOAL e3
STATE
PATH e0 e1 e2 e3
```

Target:

```text
VALID
```

### ood/equality_rewriting_lite/action

- ID: `ood:equality_rewriting_lite:24:action:0`

Source:

```text
MODE action
TASK
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K maps expression L and R
SYNTAX TERM T : current expression
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs TERM equal GOAL
ACTION RW K AT PATH changes one subterm by RULE K
VALID trace alternates TERM then RW then TERM
DONE when current TERM is GOAL
DEMO RULE K20 : OP20 X0 -> OP21 X0 ; START OP20 X0 ; GOAL OP21 X0 ; TERM OP20 X0 => RW K20 AT ROOT
PROBLEM
RULE r0 : U f1 e0 -> U f0 e0
RULE r1 : U f2 e0 -> U f1 e0
RULE r2 : U f3 e0 -> U f4 e0
RULE r3 : U f4 e0 -> U f5 e0
RULE r4 : U f5 e0 -> U f6 e0
START U f0 e0
GOAL U f2 e0
STATE
TERM U f0 e0
```

Target:

```text
RW r0 AT ROOT
```

### ood/equality_rewriting_lite/repair_action

- ID: `ood:equality_rewriting_lite:24:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K maps expression L and R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs TERM equal GOAL
SYNTAX TERM T : current expression
ACTION RW K AT PATH changes one subterm by RULE K
VALID trace alternates TERM then RW then TERM
DONE when current TERM is GOAL
DEMO RULE K00 : OP00 A0 -> OP01 A0 ; START OP00 A0 ; GOAL OP01 A0 ; TERM OP00 A0 => RW K00 AT ROOT
PROBLEM
RULE r0 : U f1 e0 -> U f0 e0
RULE r1 : U f2 e0 -> U f1 e0
RULE r2 : U f3 e0 -> U f4 e0
RULE r3 : U f4 e0 -> U f5 e0
RULE r4 : U f5 e0 -> U f6 e0
START U f0 e0
GOAL U f2 e0
STATE
TERM U f0 e0
RW r0 AT ROOT
TERM U f13 e0
```

Target:

```text
REPAIR FIRST_BAD
```

### ood/equality_rewriting_lite/verify

- ID: `ood:equality_rewriting_lite:24:verify:valid`

Source:

```text
MODE verify
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K maps expression L and R
SYNTAX TERM T : current expression
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs TERM equal GOAL
ACTION RW K AT PATH changes one subterm by RULE K
VALID trace alternates TERM then RW then TERM
DONE when current TERM is GOAL
DEMO RULE K20 : OP20 X0 -> OP21 X0 ; START OP20 X0 ; GOAL OP21 X0 ; TERM OP20 X0 => RW K20 AT ROOT
PROBLEM
RULE r0 : U f1 e0 -> U f0 e0
RULE r1 : U f2 e0 -> U f1 e0
RULE r2 : U f3 e0 -> U f4 e0
RULE r3 : U f4 e0 -> U f5 e0
RULE r4 : U f5 e0 -> U f6 e0
START U f0 e0
GOAL U f2 e0
STATE
TERM U f0 e0
RW r0 AT ROOT
TERM U f1 e0
RW r1 AT ROOT
TERM U f2 e0
```

Target:

```text
VALID
```

### ood/shortest_path_lite/action

- ID: `ood:shortest_path_lite:0:action:0`

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
EDGE e1 e0
EDGE e1 e2
EDGE e2 e3
EDGE e4 e0
EDGE e5 e6
EDGE e6 e1
EDGE e7 e4
QUERY REACH e0 e3
STATE
EMPTY
```

Target:

```text
APPEND e0
```

### ood/shortest_path_lite/repair_action

- ID: `ood:shortest_path_lite:0:repair_action:1`

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
EDGE e1 e0
EDGE e1 e2
EDGE e2 e3
EDGE e4 e0
EDGE e5 e6
EDGE e6 e1
EDGE e7 e4
QUERY REACH e0 e3
STATE
PATH e3
```

Target:

```text
REPLACE ROOT WITH e0
```

### ood/shortest_path_lite/verify

- ID: `ood:shortest_path_lite:0:verify:valid`

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
EDGE e1 e0
EDGE e1 e2
EDGE e2 e3
EDGE e4 e0
EDGE e5 e6
EDGE e6 e1
EDGE e7 e4
QUERY REACH e0 e3
STATE
PATH e0 e1 e2 e3
```

Target:

```text
VALID
```

### test/dfa_simulation_lite/action

- ID: `test:dfa_simulation_lite:1:action:0`

Source:

```text
MODE action
TASK
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX FACT R A B : directed step from A to B
SYNTAX HYP K : R : ordered rule R
SYNTAX START A : initial STATE is A
SYNTAX GOAL C : DONE needs PATH ending C
SYNTAX PATH A B C : ordered visited nodes
ACTION APPEND X starts or extends PATH by next HYP rule
VALID PATH uses each HYP rule with matching FACT
DEMO FACT REL20 X0 X1 ; FACT REL21 X1 X2 ; HYP K20 : REL20 ; HYP K21 : REL21 ; START X0 ; GOAL X2 ; EMPTY => APPEND X0 ; PATH X0 => APPEND X1
PROBLEM
FACT r0 e6 e1
FACT r1 e0 e1
FACT r1 e1 e2
FACT r1 e3 e6
FACT r2 e1 e2
FACT r2 e3 e5
FACT r2 e3 e6
HYP h0 : r1
HYP h1 : r2
START e0
GOAL e2
STATE
EMPTY
```

Target:

```text
APPEND e0
```

### test/dfa_simulation_lite/repair_action

- ID: `test:dfa_simulation_lite:1:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX FACT R A B : directed step from A to B
SYNTAX HYP K : R : ordered rule R
SYNTAX START A : initial STATE is A
SYNTAX GOAL C : DONE needs PATH ending C
SYNTAX PATH A B C : ordered visited nodes
ACTION APPEND X starts or extends PATH by next HYP rule
VALID PATH uses each HYP rule with matching FACT
DEMO FACT REL20 X0 X1 ; FACT REL21 X1 X2 ; HYP K20 : REL20 ; HYP K21 : REL21 ; START X0 ; GOAL X2 ; EMPTY => APPEND X0 ; PATH X0 => APPEND X1
PROBLEM
FACT r0 e6 e1
FACT r1 e0 e1
FACT r1 e1 e2
FACT r1 e3 e6
FACT r2 e1 e2
FACT r2 e3 e5
FACT r2 e3 e6
HYP h0 : r1
HYP h1 : r2
START e0
GOAL e2
STATE
PATH e2
```

Target:

```text
REPLACE ROOT WITH e0
```

### test/dfa_simulation_lite/verify

- ID: `test:dfa_simulation_lite:1:verify:valid`

Source:

```text
MODE verify
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX FACT R A B : directed step from A to B
SYNTAX HYP K : R : ordered rule R
SYNTAX START A : initial STATE is A
SYNTAX GOAL C : DONE needs PATH ending C
SYNTAX PATH A B C : ordered visited nodes
ACTION APPEND X starts or extends PATH by next HYP rule
VALID PATH uses each HYP rule with matching FACT
DEMO FACT REL20 X0 X1 ; FACT REL21 X1 X2 ; HYP K20 : REL20 ; HYP K21 : REL21 ; START X0 ; GOAL X2 ; EMPTY => APPEND X0 ; PATH X0 => APPEND X1
PROBLEM
FACT r0 e6 e1
FACT r1 e0 e1
FACT r1 e1 e2
FACT r1 e3 e6
FACT r2 e1 e2
FACT r2 e3 e5
FACT r2 e3 e6
HYP h0 : r1
HYP h1 : r2
START e0
GOAL e2
STATE
PATH e0 e1 e2
```

Target:

```text
VALID
```

### test/equality_rewriting_lite/action

- ID: `test:equality_rewriting_lite:2:action:0`

Source:

```text
MODE action
TASK
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
SYNTAX RULE K : L -> R : K maps expression L and R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs TERM equal GOAL
SYNTAX TERM T : current expression
ACTION RW K AT PATH changes one subterm by RULE K
VALID trace alternates TERM then RW then TERM
DONE when current TERM is GOAL
DEMO RULE K10 : OP10 N0 -> OP11 N0 ; START OP10 N0 ; GOAL OP11 N0 ; TERM OP10 N0 => RW K10 AT ROOT
PROBLEM
RULE r0 : U f1 e0 -> U f0 e0
RULE r1 : U f2 e0 -> U f1 e0
RULE r2 : U f3 e0 -> U f2 e0
RULE r3 : U f4 e0 -> U f5 e0
RULE r4 : U f5 e0 -> U f6 e0
RULE r5 : U f6 e0 -> U f7 e0
START U f0 e0
GOAL U f3 e0
STATE
TERM U f0 e0
```

Target:

```text
RW r0 AT ROOT
```

### test/equality_rewriting_lite/repair_action

- ID: `test:equality_rewriting_lite:2:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K maps expression L and R
SYNTAX TERM T : current expression
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs TERM equal GOAL
ACTION RW K AT PATH changes one subterm by RULE K
VALID trace alternates TERM then RW then TERM
DONE when current TERM is GOAL
DEMO RULE K20 : OP20 X0 -> OP21 X0 ; START OP20 X0 ; GOAL OP21 X0 ; TERM OP20 X0 => RW K20 AT ROOT
PROBLEM
RULE r0 : U f1 e0 -> U f0 e0
RULE r1 : U f2 e0 -> U f1 e0
RULE r2 : U f3 e0 -> U f2 e0
RULE r3 : U f4 e0 -> U f5 e0
RULE r4 : U f5 e0 -> U f6 e0
RULE r5 : U f6 e0 -> U f7 e0
START U f0 e0
GOAL U f3 e0
STATE
TERM U f0 e0
RW r0 AT ROOT
TERM U f13 e0
```

Target:

```text
REPAIR FIRST_BAD
```

### test/equality_rewriting_lite/verify

- ID: `test:equality_rewriting_lite:2:verify:valid`

Source:

```text
MODE verify
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K maps expression L and R
SYNTAX TERM T : current expression
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs TERM equal GOAL
ACTION RW K AT PATH changes one subterm by RULE K
VALID trace alternates TERM then RW then TERM
DONE when current TERM is GOAL
DEMO RULE K20 : OP20 X0 -> OP21 X0 ; START OP20 X0 ; GOAL OP21 X0 ; TERM OP20 X0 => RW K20 AT ROOT
PROBLEM
RULE r0 : U f1 e0 -> U f0 e0
RULE r1 : U f2 e0 -> U f1 e0
RULE r2 : U f3 e0 -> U f2 e0
RULE r3 : U f4 e0 -> U f5 e0
RULE r4 : U f5 e0 -> U f6 e0
RULE r5 : U f6 e0 -> U f7 e0
START U f0 e0
GOAL U f3 e0
STATE
TERM U f0 e0
RW r0 AT ROOT
TERM U f1 e0
RW r1 AT ROOT
TERM U f2 e0
RW r2 AT ROOT
TERM U f3 e0
```

Target:

```text
VALID
```

### test/shortest_path_lite/action

- ID: `test:shortest_path_lite:0:action:0`

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
EDGE e0 e5
EDGE e0 e6
EDGE e1 e2
EDGE e2 e3
EDGE e5 e1
EDGE e7 e4
QUERY REACH e0 e2
STATE
EMPTY
```

Target:

```text
APPEND e0
```

### test/shortest_path_lite/repair_action

- ID: `test:shortest_path_lite:0:repair_action:1`

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
EDGE e0 e5
EDGE e0 e6
EDGE e1 e2
EDGE e2 e3
EDGE e5 e1
EDGE e7 e4
QUERY REACH e0 e2
STATE
PATH e2
```

Target:

```text
REPLACE ROOT WITH e0
```

### test/shortest_path_lite/verify

- ID: `test:shortest_path_lite:0:verify:valid`

Source:

```text
MODE verify
TASK
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
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
EDGE e0 e5
EDGE e0 e6
EDGE e1 e2
EDGE e2 e3
EDGE e5 e1
EDGE e7 e4
QUERY REACH e0 e2
STATE
PATH e0 e1 e2
```

Target:

```text
VALID
```

### train/dfa_simulation_lite/action

- ID: `train:dfa_simulation_lite:1:action:0`

Source:

```text
MODE action
TASK
VALID means all rules hold; INVALID CODE names the first failed rule
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
SYNTAX HYP K : R : ordered rule R
SYNTAX FACT R A B : directed step from A to B
SYNTAX START A : initial STATE is A
SYNTAX GOAL C : DONE needs PATH ending C
SYNTAX PATH A B C : ordered visited nodes
ACTION APPEND X starts or extends PATH by next HYP rule
VALID PATH uses each HYP rule with matching FACT
DEMO FACT REL10 N0 N1 ; FACT REL11 N1 N2 ; HYP K10 : REL10 ; HYP K11 : REL11 ; START N0 ; GOAL N2 ; EMPTY => APPEND N0 ; PATH N0 => APPEND N1
PROBLEM
FACT r0 e1 e7
FACT r0 e2 e3
FACT r1 e0 e1
FACT r1 e2 e3
FACT r1 e5 e1
FACT r1 e7 e6
FACT r2 e1 e2
FACT r2 e7 e4
HYP h0 : r1
HYP h1 : r2
HYP h2 : r0
START e0
GOAL e3
STATE
EMPTY
```

Target:

```text
APPEND e0
```

### train/dfa_simulation_lite/repair_action

- ID: `train:dfa_simulation_lite:1:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX FACT R A B : directed step from A to B
SYNTAX HYP K : R : ordered rule R
SYNTAX START A : initial STATE is A
SYNTAX GOAL C : DONE needs PATH ending C
SYNTAX PATH A B C : ordered visited nodes
ACTION APPEND X starts or extends PATH by next HYP rule
VALID PATH uses each HYP rule with matching FACT
DEMO FACT REL00 A0 A1 ; FACT REL01 A1 A2 ; HYP K00 : REL00 ; HYP K01 : REL01 ; START A0 ; GOAL A2 ; EMPTY => APPEND A0 ; PATH A0 => APPEND A1
PROBLEM
FACT r0 e1 e7
FACT r0 e2 e3
FACT r1 e0 e1
FACT r1 e2 e3
FACT r1 e5 e1
FACT r1 e7 e6
FACT r2 e1 e2
FACT r2 e7 e4
HYP h0 : r1
HYP h1 : r2
HYP h2 : r0
START e0
GOAL e3
STATE
PATH e3
```

Target:

```text
REPLACE ROOT WITH e0
```

### train/dfa_simulation_lite/verify

- ID: `train:dfa_simulation_lite:1:verify:valid`

Source:

```text
MODE verify
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX FACT R A B : directed step from A to B
SYNTAX HYP K : R : ordered rule R
SYNTAX START A : initial STATE is A
SYNTAX GOAL C : DONE needs PATH ending C
SYNTAX PATH A B C : ordered visited nodes
ACTION APPEND X starts or extends PATH by next HYP rule
VALID PATH uses each HYP rule with matching FACT
DEMO FACT REL20 X0 X1 ; FACT REL21 X1 X2 ; HYP K20 : REL20 ; HYP K21 : REL21 ; START X0 ; GOAL X2 ; EMPTY => APPEND X0 ; PATH X0 => APPEND X1
PROBLEM
FACT r0 e1 e7
FACT r0 e2 e3
FACT r1 e0 e1
FACT r1 e2 e3
FACT r1 e5 e1
FACT r1 e7 e6
FACT r2 e1 e2
FACT r2 e7 e4
HYP h0 : r1
HYP h1 : r2
HYP h2 : r0
START e0
GOAL e3
STATE
PATH e0 e1 e2 e3
```

Target:

```text
VALID
```

### train/equality_rewriting_lite/action

- ID: `train:equality_rewriting_lite:2:action:0`

Source:

```text
MODE action
TASK
OUTPUT exactly one primitive action line
ACTION changes STATE by one valid step toward DONE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K maps expression L and R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs TERM equal GOAL
SYNTAX TERM T : current expression
ACTION RW K AT PATH changes one subterm by RULE K
VALID trace alternates TERM then RW then TERM
DONE when current TERM is GOAL
DEMO RULE K00 : OP00 A0 -> OP01 A0 ; START OP00 A0 ; GOAL OP01 A0 ; TERM OP00 A0 => RW K00 AT ROOT
PROBLEM
RULE r0 : U f0 e0 -> U f1 e0
RULE r1 : U f1 e0 -> U f2 e0
RULE r2 : U f2 e0 -> U f3 e0
RULE r3 : U f4 e0 -> U f5 e0
RULE r4 : U f5 e0 -> U f6 e0
RULE r5 : U f6 e0 -> U f7 e0
START U f0 e0
GOAL U f3 e0
STATE
TERM U f0 e0
```

Target:

```text
RW r0 AT ROOT
```

### train/equality_rewriting_lite/repair_action

- ID: `train:equality_rewriting_lite:2:repair_action:1`

Source:

```text
MODE repair_action
TASK
OUTPUT exactly one local repair action line
REPAIR changes corrupted STATE into the intended STATE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K maps expression L and R
SYNTAX TERM T : current expression
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs TERM equal GOAL
ACTION RW K AT PATH changes one subterm by RULE K
VALID trace alternates TERM then RW then TERM
DONE when current TERM is GOAL
DEMO RULE K20 : OP20 X0 -> OP21 X0 ; START OP20 X0 ; GOAL OP21 X0 ; TERM OP20 X0 => RW K20 AT ROOT
PROBLEM
RULE r0 : U f0 e0 -> U f1 e0
RULE r1 : U f1 e0 -> U f2 e0
RULE r2 : U f2 e0 -> U f3 e0
RULE r3 : U f4 e0 -> U f5 e0
RULE r4 : U f5 e0 -> U f6 e0
RULE r5 : U f6 e0 -> U f7 e0
START U f0 e0
GOAL U f3 e0
STATE
TERM U f0 e0
RW r0 AT ROOT
TERM U f13 e0
```

Target:

```text
REPAIR FIRST_BAD
```

### train/equality_rewriting_lite/verify

- ID: `train:equality_rewriting_lite:2:verify:valid`

Source:

```text
MODE verify
TASK
OUTPUT VALID when STATE satisfies all rules
OUTPUT INVALID CODE when the first broken rule has CODE
VALID means all rules hold; INVALID CODE names the first failed rule
SYNTAX RULE K : L -> R : K maps expression L and R
SYNTAX START T : initial TERM is T
SYNTAX GOAL T : DONE needs TERM equal GOAL
SYNTAX TERM T : current expression
ACTION RW K AT PATH changes one subterm by RULE K
VALID trace alternates TERM then RW then TERM
DONE when current TERM is GOAL
DEMO RULE K00 : OP00 A0 -> OP01 A0 ; START OP00 A0 ; GOAL OP01 A0 ; TERM OP00 A0 => RW K00 AT ROOT
PROBLEM
RULE r0 : U f0 e0 -> U f1 e0
RULE r1 : U f1 e0 -> U f2 e0
RULE r2 : U f2 e0 -> U f3 e0
RULE r3 : U f4 e0 -> U f5 e0
RULE r4 : U f5 e0 -> U f6 e0
RULE r5 : U f6 e0 -> U f7 e0
START U f0 e0
GOAL U f3 e0
STATE
TERM U f0 e0
RW r0 AT ROOT
TERM U f1 e0
RW r1 AT ROOT
TERM U f2 e0
RW r2 AT ROOT
TERM U f3 e0
```

Target:

```text
VALID
```

### train/shortest_path_lite/action

- ID: `train:shortest_path_lite:0:action:0`

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
EDGE e2 e3
EDGE e2 e6
EDGE e3 e2
EDGE e3 e7
EDGE e7 e3
EDGE e7 e6
QUERY REACH e0 e3
STATE
EMPTY
```

Target:

```text
APPEND e0
```

### train/shortest_path_lite/repair_action

- ID: `train:shortest_path_lite:0:repair_action:1`

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
EDGE e2 e3
EDGE e2 e6
EDGE e3 e2
EDGE e3 e7
EDGE e7 e3
EDGE e7 e6
QUERY REACH e0 e3
STATE
PATH e3
```

Target:

```text
REPLACE ROOT WITH e0
```

### train/shortest_path_lite/verify

- ID: `train:shortest_path_lite:0:verify:valid`

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
EDGE e2 e6
EDGE e3 e2
EDGE e3 e7
EDGE e7 e3
EDGE e7 e6
QUERY REACH e0 e3
STATE
PATH e0 e1 e2 e3
```

Target:

```text
VALID
```
