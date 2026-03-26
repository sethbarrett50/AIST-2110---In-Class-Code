---
name: Repo boundaries
---

- Do not edit generated files, lockfiles, model artifacts, datasets, or large result files unless explicitly requested.
- Do not rename public interfaces, move files, or change package layout unless explicitly requested.
- Avoid broad refactors in core simulation, training, or drift-monitor code unless the request requires it.
- Preserve CLI flags, config fields, and logging/output formats unless explicitly requested to change them.
- Prefer minimal diffs in research code and experimental pipelines.
- When changing metrics, evaluation, or simulation behavior, call out user-visible behavior changes explicitly.