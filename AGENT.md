# Agent Instructions

Use pre-1.0 semantic experiment versions going forward.

- Human version labels should look like `0.23`, `0.24`, etc.
- Filesystem names should use `0_23`, `0_24`, etc. Example: `configs/symbolic_0_23_fresh_holdout.json`, `data/symbolic-0_23-fresh-holdout`.
- Do not rename old `v1` through `v22` artifacts; they are historical references used by logs and reports.
- Treat `0.22` as the stable baseline alias for the final `v22` single-error verify run.
- Reserve `1.0` for the first major dataset/DSL release that is intentionally frozen as a public-style baseline.
