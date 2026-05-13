# Dataset Audit

- Data dir: `data/symbolic-0_39-alpha-term-action-only`
- Status: `pass`
- Errors: `0`
- Warnings: `0`

## JSONL Summary

### train

- Examples: `1787`
- Problems: `240`
- Families: `{'term_rewriting': 1787}`
- Modes: `{'action': 1787}`
- Verify targets: `{}`

### test

- Examples: `97`
- Problems: `18`
- Families: `{'term_rewriting': 97}`
- Modes: `{'action': 97}`
- Verify targets: `{}`

### ood

- Examples: `172`
- Problems: `18`
- Families: `{'term_rewriting': 172}`
- Modes: `{'action': 172}`
- Verify targets: `{}`

## Difficulty Summary

### term_rewriting

- `action_format`: `{'rule': 2056}`
- `binary_rules`: `{'min': 1.0, 'max': 10.0, 'mean': 5.750972762645914, 'unique': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `distractor_rules`: `{'min': 0.0, 'max': 16.0, 'mean': 8.42704280155642, 'unique': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}`
- `query_kind`: `{'goal': 1230, 'normal_form': 826}`
- `repeated_subterms`: `{False: 1654, True: 402}`
- `rewrite_steps`: `{'min': 2.0, 'max': 10.0, 'mean': 7.519455252918288, 'unique': [2, 3, 4, 5, 6, 7, 8, 9, 10]}`
- `symbol_offset`: `{'min': 0.0, 'max': 6.0, 'mean': 1.3861867704280155, 'unique': [0, 2, 3, 4, 6]}`
- `term_depth`: `{'min': 1.0, 'max': 8.0, 'mean': 4.046692607003891, 'unique': [1, 2, 3, 4, 5, 6, 7, 8]}`
- `variable_rules`: `{'min': 0.0, 'max': 7.0, 'mean': 2.1921206225680936, 'unique': [0, 1, 2, 3, 4, 5, 6, 7]}`

## TRM Array Summary

### train

- Inputs shape: `[1787, 877]`
- Labels shape: `[1787, 877]`
- Seq len: `877`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `1787`

### test

- Inputs shape: `[97, 877]`
- Labels shape: `[97, 877]`
- Seq len: `877`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `97`

### ood

- Inputs shape: `[172, 877]`
- Labels shape: `[172, 877]`
- Seq len: `877`
- Vocab size: `462`
- Puzzle identifiers unique: `[0]`
- Non-empty target rows: `172`

## Samples

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
ACTION RW K AT PATH applies rule K to the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K20 : OP20 X0 -> OP21 X0 ; START OP20 X0 ; GOAL OP21 X0 ; TERM OP20 X0 => RW K20 AT ROOT
PROBLEM
RULE r9 : B g8 B g107 B g62 e2 e0 e1 e72 -> U f121 B g107 B g62 e2 e0 e1
RULE r3 : U f121 v1 -> U f2 v1
RULE r12 : U f2 B g107 B g62 e2 e0 e1 -> B g6 B g107 B g62 e2 e0 e1 e72
RULE r0 : B g6 B g107 B g62 e2 e0 e1 e72 -> U f108 B g107 B g62 e2 e0 e1
RULE r10 : U f108 v1 -> U f124 v1
RULE r4 : U f124 B g107 B g62 e2 e0 e1 -> B g0 B g107 B g62 e2 e0 e1 e72
RULE r7 : B g0 B g107 B g62 e2 e0 e1 e72 -> B g100 B g107 B g62 e2 e0 e1 e72
RULE r1 : B g100 B g107 B g62 e2 e0 e1 e72 -> U f61 B g107 B g62 e2 e0 e1
RULE r6 : B g31 v1 v0 -> B g120 v1 v0
RULE r14 : U f1 v1 -> U f128 v1
RULE r16 : U f123 v1 -> U f5 v1
RULE r5 : U f102 v1 -> U f101 v1
RULE r11 : U f60 v1 -> U f8 v1
RULE r15 : U f103 v1 -> U f105 v1
RULE r8 : B g30 v1 v0 -> B g127 v1 v0
RULE r2 : B g106 v1 v0 -> B g7 v1 v0
RULE r13 : U f104 v1 -> U f122 v1
START B g3 U f4 U f125 B g8 B g107 B g62 e2 e0 e1 e72 e3
QUERY NORMAL_FORM
STATE
TERM B g3 U f4 U f125 B g8 B g107 B g62 e2 e0 e1 e72 e3
```

Target:

```text
RW r9
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
ACTION RW K AT PATH applies rule K to the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K00 : OP00 A0 -> OP01 A0 ; START OP00 A0 ; GOAL OP01 A0 ; TERM OP00 A0 => RW K00 AT ROOT
PROBLEM
RULE r3 : U f4 v1 -> U f0 v1
RULE r5 : U f0 B g100 e0 e2 -> U f1 B g100 e0 e2
RULE r2 : U f1 B g100 e0 e2 -> B g101 B g100 e0 e2 e3
RULE r4 : B g101 B g100 e0 e2 e3 -> U f2 B g100 e0 e2
RULE r1 : B g31 v1 v0 -> B g3 v1 v0
RULE r0 : B g30 v1 v0 -> B g60 v1 v0
START B g121 U f4 B g100 e0 e2 U f4 B g100 e0 e2
GOAL B g121 U f2 B g100 e0 e2 U f4 B g100 e0 e2
STATE
TERM B g121 U f4 B g100 e0 e2 U f4 B g100 e0 e2
```

Target:

```text
RW r3
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
ACTION RW K AT PATH applies rule K to the subterm at PATH
ACTION HALT stops only when DONE already holds
VALID trace alternates TERM then RW then TERM, with optional final HALT
DEMO RULE K20 : OP20 X0 -> OP21 X0 ; START OP20 X0 ; GOAL OP21 X0 ; TERM OP20 X0 => RW K20 AT ROOT
PROBLEM
RULE r3 : U f1 e1 -> U f121 e1
RULE r6 : U f121 v1 -> U f61 v1
RULE r5 : U f61 v1 -> U f3 v1
RULE r1 : U f3 e1 -> B g5 e1 e0
RULE r4 : B g5 e1 e0 -> U f5 e1
RULE r0 : B g100 v1 v0 -> B g4 v1 v0
RULE r2 : U f0 v1 -> U f2 v1
START U f101 U f1 e1
QUERY NORMAL_FORM
STATE
TERM U f101 U f1 e1
```

Target:

```text
RW r3
```
