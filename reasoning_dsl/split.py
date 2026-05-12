from __future__ import annotations

import hashlib
from dataclasses import replace
from typing import Any

from reasoning_dsl.core import Example, Generator, build_examples_for_problem


def stable_seed(*parts: object) -> int:
    text = ":".join(str(part) for part in parts)
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return int(digest[:16], 16) % (2**31 - 1)


def generate_examples(
    *,
    generators: list[Generator],
    config: dict[str, Any],
    root_seed: int,
) -> dict[str, list[Example]]:
    modes = list(config.get("modes", ["improve", "repair", "complete", "verify"]))
    relation_action_format = str(config.get("relation_action_format", "follow"))
    action_reference_format = str(config.get("action_reference_format", "symbol"))
    term_rewrite_action_format = str(config.get("term_rewrite_action_format", "path"))
    term_repair_action_format = str(config.get("term_repair_action_format", "rewrite"))
    tree_repair_action_format = str(config.get("tree_repair_action_format", "index"))
    repair_action_format = str(config.get("repair_action_format", "index"))
    verify_corruption_strategy = str(config.get("verify_corruption_strategy", "default"))
    task_spec_format = str(config.get("task_spec_format", "none"))
    task_spec_variant_count = int(config.get("task_spec_variant_count", 1))
    split_config = config["splits"]
    family_config = config["families"]
    seen_fingerprints: set[str] = set()
    examples_by_split: dict[str, list[Example]] = {}

    for split, split_info in split_config.items():
        split_examples: list[Example] = []
        split_problem_index = 0
        use_slice_seed = "difficulty_mixture" in split_info
        for generator in generators:
            if generator.family not in family_config:
                continue
            if not family_config[generator.family].get("enabled", True):
                continue
            for slice_name, count, difficulty, slice_modes in _difficulty_slices(
                split, split_info, family_config[generator.family], modes, generator.family
            ):
                if generator.family == "term_rewriting":
                    difficulty = {**difficulty, "action_format": term_rewrite_action_format}
                generated = 0
                attempts = 0
                while generated < count:
                    attempts += 1
                    if attempts > count * 100:
                        raise RuntimeError(
                            f"Could not generate enough unique {generator.family} problems for {split}/{slice_name}"
                        )
                    if use_slice_seed:
                        seed = stable_seed(root_seed, split, slice_name, generator.family, generated, attempts)
                    else:
                        seed = stable_seed(root_seed, split, generator.family, generated, attempts)
                    problem = generator.generate(seed, difficulty)
                    if use_slice_seed:
                        problem = replace(problem, meta={**problem.meta, "difficulty_slice": slice_name})
                    global_fingerprint = f"{generator.family}:{problem.fingerprint}"
                    if global_fingerprint in seen_fingerprints:
                        continue
                    seen_fingerprints.add(global_fingerprint)
                    split_examples.extend(
                        build_examples_for_problem(
                            generator=generator,
                            problem=problem,
                            split=split,
                            problem_index=split_problem_index,
                            seed=seed,
                            modes=slice_modes,
                            relation_action_format=relation_action_format,
                            action_reference_format=action_reference_format,
                            tree_repair_action_format=tree_repair_action_format,
                            repair_action_format=repair_action_format,
                            term_repair_action_format=term_repair_action_format,
                            verify_corruption_strategy=verify_corruption_strategy,
                            task_spec_format=task_spec_format,
                            task_spec_variant_count=task_spec_variant_count,
                        )
                    )
                    generated += 1
                    split_problem_index += 1
        examples_by_split[split] = split_examples

    return examples_by_split


def _difficulty_slices(
    split: str,
    split_info: dict[str, Any],
    family_info: dict[str, Any],
    default_modes: list[str],
    family: str,
) -> list[tuple[str, int, dict[str, Any], list[str]]]:
    if "difficulty_mixture" not in split_info:
        count = int(split_info["problems_per_family"])
        difficulty_name = str(split_info.get("difficulty", split))
        return [(difficulty_name, count, dict(family_info[difficulty_name]), list(default_modes))]

    slices: list[tuple[str, int, dict[str, Any], list[str]]] = []
    for item in split_info["difficulty_mixture"]:
        included_families = item.get("families")
        if included_families is not None and family not in set(included_families):
            continue
        name = str(item["name"])
        count = int(item["problems_per_family"])
        difficulty_name = str(item["difficulty"])
        difficulty = dict(family_info[difficulty_name])
        difficulty.update(dict(item.get("difficulty_overrides", {})))
        slice_modes = list(item.get("modes", default_modes))
        slices.append((name, count, difficulty, slice_modes))
    return slices
