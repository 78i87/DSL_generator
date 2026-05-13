# Dataset Audit

- Data dir: `data/symbolic-0_85-extra-hard-15_17-eval-compatible3`
- Status: `fail`
- Errors: `4`
- Warnings: `0`

## Errors

- Missing JSONL file: data/symbolic-0_85-extra-hard-15_17-eval-compatible3/jsonl/train.jsonl
- Missing JSONL file: data/symbolic-0_85-extra-hard-15_17-eval-compatible3/jsonl/test.jsonl
- Missing metadata file: data/symbolic-0_85-extra-hard-15_17-eval-compatible3/train/dataset.json
- Missing metadata file: data/symbolic-0_85-extra-hard-15_17-eval-compatible3/test/dataset.json

## JSONL Summary

### ood

- Examples: `954`
- Problems: `27`
- Families: `{'graph_reachability': 324, 'implication_chains': 306, 'tree_ancestry': 324}`
- Modes: `{'action': 450, 'repair_action': 450, 'verify': 54}`
- Verify targets: `{'INVALID BAD_EDGE': 9, 'INVALID BAD_PARENT': 9, 'INVALID BAD_PREMISE': 9, 'VALID': 27}`

## Difficulty Summary

### graph_reachability

- `extra_edges`: `{'min': 5.0, 'max': 10.0, 'mean': 7.648148148148148, 'unique': [5, 6, 7, 8, 9, 10]}`
- `num_nodes`: `{'min': 20.0, 'max': 23.0, 'mean': 20.80246913580247, 'unique': [20, 21, 22, 23]}`
- `path_length`: `{'min': 15.0, 'max': 17.0, 'mean': 16.037037037037038, 'unique': [15, 16, 17]}`
- `require_shortest`: `{True: 324}`
- `symbol_offset`: `{'min': 0.0, 'max': 0.0, 'mean': 0.0, 'unique': [0]}`

### implication_chains

- `distractor_hyps`: `{'min': 3.0, 'max': 5.0, 'mean': 4.333333333333333, 'unique': [3, 4, 5]}`
- `num_props`: `{'min': 17.0, 'max': 19.0, 'mean': 18.104575163398692, 'unique': [17, 18, 19]}`
- `proof_length`: `{'min': 15.0, 'max': 17.0, 'mean': 16.03921568627451, 'unique': [15, 16, 17]}`
- `symbol_offset`: `{'min': 0.0, 'max': 0.0, 'mean': 0.0, 'unique': [0]}`

### tree_ancestry

- `branching_factor`: `{'min': 2.0, 'max': 3.0, 'mean': 2.5617283950617282, 'unique': [2, 3]}`
- `depth`: `{'min': 15.0, 'max': 17.0, 'mean': 16.037037037037038, 'unique': [15, 16, 17]}`
- `distractor_subtrees`: `{'min': 5.0, 'max': 9.0, 'mean': 7.234567901234568, 'unique': [5, 6, 7, 8, 9]}`
- `symbol_offset`: `{'min': 0.0, 'max': 0.0, 'mean': 0.0, 'unique': [0]}`

## TRM Array Summary

### ood

- Inputs shape: `[954, 430]`
- Labels shape: `[954, 430]`
- Seq len: `430`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `954`

## Samples

### ood/graph_reachability/action

- ID: `ood:graph_reachability:0:action:0`

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
EDGE e10 e0
EDGE e10 e11
EDGE e11 e12
EDGE e12 e13
EDGE e13 e12
EDGE e13 e14
EDGE e14 e15
EDGE e14 e5
EDGE e16 e2
EDGE e17 e19
EDGE e19 e16
EDGE e2 e3
EDGE e3 e17
EDGE e3 e4
EDGE e4 e5
EDGE e5 e17
EDGE e5 e6
EDGE e6 e7
EDGE e7 e18
EDGE e7 e8
EDGE e8 e9
EDGE e9 e10
QUERY REACH e0 e15
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
EDGE e10 e0
EDGE e10 e11
EDGE e11 e12
EDGE e12 e13
EDGE e13 e12
EDGE e13 e14
EDGE e14 e15
EDGE e14 e5
EDGE e16 e2
EDGE e17 e19
EDGE e19 e16
EDGE e2 e3
EDGE e3 e17
EDGE e3 e4
EDGE e4 e5
EDGE e5 e17
EDGE e5 e6
EDGE e6 e7
EDGE e7 e18
EDGE e7 e8
EDGE e8 e9
EDGE e9 e10
QUERY REACH e0 e15
STATE
PATH e15
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
EDGE e10 e0
EDGE e10 e11
EDGE e11 e12
EDGE e12 e13
EDGE e13 e12
EDGE e13 e14
EDGE e14 e15
EDGE e14 e5
EDGE e16 e2
EDGE e17 e19
EDGE e19 e16
EDGE e2 e3
EDGE e3 e17
EDGE e3 e4
EDGE e4 e5
EDGE e5 e17
EDGE e5 e6
EDGE e6 e7
EDGE e7 e18
EDGE e7 e8
EDGE e8 e9
EDGE e9 e10
QUERY REACH e0 e15
STATE
PATH e0 e1 e2 e3 e4 e5 e6 e7 e8 e9 e10 e11 e12 e13 e14 e15
```

Target:

```text
VALID
```

### ood/implication_chains/action

- ID: `ood:implication_chains:9:action:0`

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
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p7 -> p8
HYP h9 : p8 -> p9
HYP h10 : p9 -> p10
HYP h11 : p10 -> p11
HYP h12 : p11 -> p12
HYP h13 : p12 -> p13
HYP h14 : p13 -> p14
HYP h15 : p0 -> p8
HYP h16 : p7 -> p10
HYP h17 : p13 -> p16
HYP h18 : p15 -> p16
GOAL p14
STATE
EMPTY
```

Target:

```text
APPLY h0
```

### ood/implication_chains/repair_action

- ID: `ood:implication_chains:9:repair_action:1`

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
HYP h0 : p0
HYP h1 : p0 -> p1
HYP h2 : p1 -> p2
HYP h3 : p2 -> p3
HYP h4 : p3 -> p4
HYP h5 : p4 -> p5
HYP h6 : p5 -> p6
HYP h7 : p6 -> p7
HYP h8 : p7 -> p8
HYP h9 : p8 -> p9
HYP h10 : p9 -> p10
HYP h11 : p10 -> p11
HYP h12 : p11 -> p12
HYP h13 : p12 -> p13
HYP h14 : p13 -> p14
HYP h15 : p0 -> p8
HYP h16 : p7 -> p10
HYP h17 : p13 -> p16
HYP h18 : p15 -> p16
GOAL p14
STATE
DERIVE p0 BY h999
```

Target:

```text
REPLACE FIRST HYP h0
```

### ood/implication_chains/verify

- ID: `ood:implication_chains:9:verify:valid`

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
HYP h8 : p7 -> p8
HYP h9 : p8 -> p9
HYP h10 : p9 -> p10
HYP h11 : p10 -> p11
HYP h12 : p11 -> p12
HYP h13 : p12 -> p13
HYP h14 : p13 -> p14
HYP h15 : p0 -> p8
HYP h16 : p7 -> p10
HYP h17 : p13 -> p16
HYP h18 : p15 -> p16
GOAL p14
STATE
DERIVE p0 BY h0
DERIVE p1 BY h1 FROM p0
DERIVE p2 BY h2 FROM p1
DERIVE p3 BY h3 FROM p2
DERIVE p4 BY h4 FROM p3
DERIVE p5 BY h5 FROM p4
DERIVE p6 BY h6 FROM p5
DERIVE p7 BY h7 FROM p6
DERIVE p8 BY h8 FROM p7
DERIVE p9 BY h9 FROM p8
DERIVE p10 BY h10 FROM p9
DERIVE p11 BY h11 FROM p10
DERIVE p12 BY h12 FROM p11
DERIVE p13 BY h13 FROM p12
DERIVE p14 BY h14 FROM p13
```

Target:

```text
VALID
```

### ood/tree_ancestry/action

- ID: `ood:tree_ancestry:18:action:0`

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
PARENT e1 e17
PARENT e1 e2
PARENT e10 e11
PARENT e11 e12
PARENT e11 e16
PARENT e12 e13
PARENT e13 e14
PARENT e14 e15
PARENT e14 e19
PARENT e15 e21
PARENT e18 e22
PARENT e2 e3
PARENT e3 e4
PARENT e4 e5
PARENT e5 e6
PARENT e6 e7
PARENT e7 e8
PARENT e8 e18
PARENT e8 e9
PARENT e9 e10
PARENT e9 e20
QUERY ANCESTOR e0 e15
STATE
EMPTY
```

Target:

```text
DESCEND e0
```

### ood/tree_ancestry/repair_action

- ID: `ood:tree_ancestry:18:repair_action:1`

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
PARENT e1 e17
PARENT e1 e2
PARENT e10 e11
PARENT e11 e12
PARENT e11 e16
PARENT e12 e13
PARENT e13 e14
PARENT e14 e15
PARENT e14 e19
PARENT e15 e21
PARENT e18 e22
PARENT e2 e3
PARENT e3 e4
PARENT e4 e5
PARENT e5 e6
PARENT e6 e7
PARENT e7 e8
PARENT e8 e18
PARENT e8 e9
PARENT e9 e10
PARENT e9 e20
QUERY ANCESTOR e0 e15
STATE
LINEAGE e15
```

Target:

```text
REPLACE ROOT WITH e0
```

### ood/tree_ancestry/verify

- ID: `ood:tree_ancestry:18:verify:valid`

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
PARENT e1 e17
PARENT e1 e2
PARENT e10 e11
PARENT e11 e12
PARENT e11 e16
PARENT e12 e13
PARENT e13 e14
PARENT e14 e15
PARENT e14 e19
PARENT e15 e21
PARENT e18 e22
PARENT e2 e3
PARENT e3 e4
PARENT e4 e5
PARENT e5 e6
PARENT e6 e7
PARENT e7 e8
PARENT e8 e18
PARENT e8 e9
PARENT e9 e10
PARENT e9 e20
QUERY ANCESTOR e0 e15
STATE
LINEAGE e0 e1 e2 e3 e4 e5 e6 e7 e8 e9 e10 e11 e12 e13 e14 e15
```

Target:

```text
VALID
```
