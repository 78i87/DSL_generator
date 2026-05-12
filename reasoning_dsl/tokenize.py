from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from reasoning_dsl.core import Example


TOKEN_RE = re.compile(r"->|[A-Za-z_][A-Za-z0-9_]*|\d+|[:;=]|\S")
SYMBOL_RE = re.compile(r"^([ephrfgv])(\d+)$")

PAD = "<PAD>"
BOS = "<BOS>"
EOS = "<EOS>"
SEP = "<SEP>"
NL = "<NL>"
BLANK = "<BLANK>"

SPECIAL_TOKENS = [PAD, BOS, EOS, SEP, NL, BLANK]
SYMBOL_PREFIX_TOKENS = {
    "e": "SYM_E",
    "p": "SYM_P",
    "h": "SYM_H",
    "r": "SYM_R",
    "f": "SYM_F",
    "g": "SYM_G",
    "v": "SYM_V",
}
SYMBOL_END = "SYM_END"
NUMBER_START = "NUM"
NUMBER_END = "NUM_END"
DIGIT_TOKENS = {str(idx): f"DIGIT_{idx}" for idx in range(10)}
SYMBOL_PART_TOKENS = [
    *SYMBOL_PREFIX_TOKENS.values(),
    SYMBOL_END,
    NUMBER_START,
    NUMBER_END,
    *DIGIT_TOKENS.values(),
]


def tokenize_text(text: str, *, tokenization: str = "whitespace") -> list[str]:
    tokens: list[str] = []
    lines = text.splitlines()
    for line_index, line in enumerate(lines):
        line_tokens = TOKEN_RE.findall(line)
        if tokenization == "symbol_parts":
            tokens.extend(_expand_symbol_parts(line_tokens))
        elif tokenization == "whitespace":
            tokens.extend(line_tokens)
        else:
            raise ValueError(f"Unsupported tokenization: {tokenization}")
        if line_index != len(lines) - 1:
            tokens.append(NL)
    return tokens


def _expand_symbol_parts(tokens: list[str]) -> list[str]:
    expanded: list[str] = []
    for token in tokens:
        match = SYMBOL_RE.fullmatch(token)
        if match:
            prefix, digits = match.groups()
            expanded.append(SYMBOL_PREFIX_TOKENS[prefix])
            expanded.extend(DIGIT_TOKENS[digit] for digit in digits)
            expanded.append(SYMBOL_END)
        elif token.isdigit():
            expanded.append(NUMBER_START)
            expanded.extend(DIGIT_TOKENS[digit] for digit in token)
            expanded.append(NUMBER_END)
        else:
            expanded.append(token)
    return expanded


@dataclass
class Vocab:
    token_to_id: dict[str, int]
    tokenization: str = "whitespace"

    @classmethod
    def build(cls, examples: list[Example], *, tokenization: str = "whitespace") -> "Vocab":
        if tokenization not in {"whitespace", "symbol_parts"}:
            raise ValueError(f"Unsupported tokenization: {tokenization}")
        token_to_id = {token: idx for idx, token in enumerate(SPECIAL_TOKENS)}
        if tokenization == "symbol_parts":
            for token in SYMBOL_PART_TOKENS:
                token_to_id.setdefault(token, len(token_to_id))
        for example in examples:
            for token in tokenize_text(example.source_text(), tokenization=tokenization):
                token_to_id.setdefault(token, len(token_to_id))
            for token in tokenize_text(example.target_text(), tokenization=tokenization):
                token_to_id.setdefault(token, len(token_to_id))
        return cls(token_to_id, tokenization=tokenization)

    @classmethod
    def load(cls, path: str | Path) -> "Vocab":
        with open(path, "r", encoding="utf-8") as f:
            token_to_id = json.load(f)
        if not isinstance(token_to_id, dict):
            raise ValueError(f"Vocab must be a token-to-id object: {path}")
        normalized = {str(token): int(token_id) for token, token_id in token_to_id.items()}
        expected_ids = set(range(len(normalized)))
        actual_ids = set(normalized.values())
        if actual_ids != expected_ids:
            raise ValueError(f"Vocab ids must be contiguous from 0 to {len(normalized) - 1}: {path}")
        for token in SPECIAL_TOKENS:
            if token not in normalized:
                raise ValueError(f"Vocab is missing required special token {token!r}: {path}")
        tokenization = "symbol_parts" if SYMBOL_END in normalized and "SYM_E" in normalized else "whitespace"
        return cls(normalized, tokenization=tokenization)

    @property
    def pad_id(self) -> int:
        return self.token_to_id[PAD]

    @property
    def blank_id(self) -> int:
        return self.token_to_id[BLANK]

    @property
    def vocab_size(self) -> int:
        return len(self.token_to_id)

    def encode(self, text: str) -> list[int]:
        ids = []
        for token in tokenize_text(text, tokenization=self.tokenization):
            if token not in self.token_to_id:
                raise ValueError(f"Token {token!r} is not in the fixed vocabulary")
            ids.append(self.token_to_id[token])
        return ids

    def save(self, path: str | Path) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.token_to_id, f, indent=2, sort_keys=True)
