from __future__ import annotations

from collections.abc import Iterable


def normalize_lines(lines: Iterable[str]) -> list[str]:
    return [line.strip() for line in lines if line.strip()]


def render_lines(lines: Iterable[str]) -> str:
    return "\n".join(normalize_lines(lines))


def split_line(line: str) -> list[str]:
    return line.strip().split()
