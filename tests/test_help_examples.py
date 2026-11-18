"""Validate that every generated operation's -h output has functional examples.

Rules:
- Every operation must render at least a basic `catocli <command>` usage line.
- An operation with required arguments (beyond accountId) must include at least
  one runnable JSON example, and every JSON example shown must parse.
- No-argument operations are fine with just the plain usage lines.
- The literal `'{...}'` placeholder (used in curated docs to illustrate output
  flags) is not treated as a JSON example.
"""

import contextlib
import io
import json
import os
import re
import sys

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(REPO_ROOT, "models")
sys.path.insert(0, REPO_ROOT)

from catocli.Utils.help_formatter import get_universal_help  # noqa: E402

OPERATIONS = sorted(f[:-5] for f in os.listdir(MODELS_DIR) if f.endswith(".json"))


def _extract_json_examples(help_text, command_name):
    """Brace-balanced extraction of catocli <cmd> '<json>' examples."""
    blobs = []
    for m in re.finditer(r"catocli " + re.escape(command_name) + r" '", help_text):
        i = m.end()
        if i >= len(help_text) or help_text[i] != "{":
            continue
        if help_text[i:i + 5] == "{...}":  # documentation placeholder
            continue
        depth, j, in_str, esc = 0, i, False, False
        while j < len(help_text):
            c = help_text[j]
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = not in_str
            elif not in_str:
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        break
            j += 1
        blobs.append(help_text[i:j + 1])
    return blobs


@pytest.mark.parametrize("operation", OPERATIONS)
def test_operation_help_has_functional_examples(operation):
    with open(os.path.join(MODELS_DIR, operation + ".json")) as f:
        model = json.load(f)
    args = model.get("operationArgs", {}) or {}
    required_args = [
        name for name, d in args.items()
        if name.lower() != "accountid" and isinstance(d, dict)
        and d.get("required") and d.get("requiredForOperation", True)
    ]

    parser_path = operation.replace(".", "_")
    command_name = parser_path.replace("_", " ")
    with contextlib.redirect_stdout(io.StringIO()):
        help_text = get_universal_help(parser_path, "auto")

    assert f"catocli {command_name}" in help_text, (
        f"{operation}: -h output has no usage line at all"
    )

    examples = _extract_json_examples(help_text, command_name)
    if required_args:
        assert examples, (
            f"{operation}: has required args {required_args} "
            f"but -h shows no runnable JSON example"
        )
    for blob in examples:
        try:
            json.loads(blob)
        except ValueError as e:
            pytest.fail(f"{operation}: example JSON does not parse: {e}")
