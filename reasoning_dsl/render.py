from __future__ import annotations

from reasoning_dsl.core import Example


def render_source(example: Example) -> str:
    return example.source_text()


def render_target(example: Example) -> str:
    return example.target_text()
