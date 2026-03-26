---
name: Pytest and Ruff
---

- Prefer targeted pytest runs over the full suite.
- Prefer running tests only for the touched module or the closest relevant test file.
- Prefer ruff check on touched files before broad lint runs.
- Prefer ruff format only on edited files unless explicitly requested.
- Do not add or change test dependencies unless explicitly requested.
- When proposing verification commands, use uv run if the repository uses uv.
- State clearly which checks were run and which were not run.