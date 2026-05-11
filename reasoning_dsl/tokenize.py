from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from reasoning_dsl.core import Example


TOKEN_RE = re.compile(r"->|[A-Za-z_][A-Za-z0-9_]*|\d+|[:;=]|\S")

PAD = "<PAD>"
BOS = "<BOS>"
EOS = "<EOS>"
SEP = "<SEP>"
NL = "<NL>"
BLANK = "<BLANK>"

SPECIAL_TOKENS = [PAD, BOS, EOS, SEP, NL, BLANK]


def tokenize_text(text: str) -> list[str]:
    tokens: list[str] = []
    lines = text.splitlines()
    for line_index, line in enumerate(lines):
        tokens.extend(TOKEN_RE.findall(line))
        if line_index != len(lines) - 1:
            tokens.append(NL)
    return tokens


@dataclass
class Vocab:
    token_to_id: dict[str, int]

    @classmethod
    def build(cls, examples: list[Example]) -> "Vocab":
        token_to_id = {token: idx for idx, token in enumerate(SPECIAL_TOKENS)}
        for example in examples:
            for token in tokenize_text(example.source_text()):
                token_to_id.setdefault(token, len(token_to_id))
            for token in tokenize_text(example.target_text()):
                token_to_id.setdefault(token, len(token_to_id))
        return cls(token_to_id)

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
        return cls(normalized)

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
        for token in tokenize_text(text):
            if token not in self.token_to_id:
                raise ValueError(f"Token {token!r} is not in the fixed vocabulary")
            ids.append(self.token_to_id[token])
        return ids

    def save(self, path: str | Path) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.token_to_id, f, indent=2, sort_keys=True)
