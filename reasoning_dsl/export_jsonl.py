from __future__ import annotations

import json
from pathlib import Path

from reasoning_dsl.core import Example


def export_jsonl(examples_by_split: dict[str, list[Example]], output_dir: str | Path) -> None:
    out = Path(output_dir) / "jsonl"
    out.mkdir(parents=True, exist_ok=True)
    for split, examples in examples_by_split.items():
        with open(out / f"{split}.jsonl", "w", encoding="utf-8") as f:
            for example in examples:
                f.write(json.dumps(example.to_json(), sort_keys=True) + "\n")
