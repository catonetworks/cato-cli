## Cursor Cloud specific instructions

### Overview

This is the **CatoCLI** (`catocli`) codebase — a Python CLI tool for the Cato Networks GraphQL API. It is a single-package Python project (not a monorepo). There are no local services, databases, or containers to run. The CLI communicates with the external Cato Networks API at `api.catonetworks.com`.

### Running the CLI

After `pip install -e .`, the `catocli` command is available. Use `catocli -h` for help.

### Testing

Run validation tests (no API credentials required):

```
pytest tests/run_all_tests.py -v
```

Run the full test runner (generated + custom tests require API credentials):

```
python3 tests/run_all_tests.py --skip-generated --skip-custom
```

To run generated/custom tests that hit the actual Cato API, configure credentials first:

```
catocli configure set --cato-token "TOKEN" --account-id "ACCOUNT_ID" --skip-validation
```

### Important notes

- **PATH**: pytest and other pip-installed scripts are in `/home/ubuntu/.local/bin` — ensure it's on PATH (`export PATH="/home/ubuntu/.local/bin:$PATH"`).
- **Test from project root**: Always run `pytest` from `/workspace` (the repo root). Running `run_all_tests.py` from inside `tests/` can cause path resolution differences.
- **No linter configured**: The repo has no configured linter (no flake8, pylint, ruff, or similar config). Python type checking and linting are not part of the project's CI workflow.
- **Local operations**: `catocli query appCategory` works without API credentials (it's a local lookup). Use it to verify the CLI is functional without needing a Cato account.
- **Pre-existing test quirk**: The `test_invalid_json_handling` test may fail when run via `run_all_tests.py` from the `tests/` directory (due to credential check short-circuiting the JSON validation path). It passes when run via `pytest` from the project root.
