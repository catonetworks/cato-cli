#!/usr/bin/env python3
"""Run generated API tests with an isolated profile from a shell config file."""

import argparse
import os
import shlex
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlparse

from run_all_tests import AllTestsRunner


PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

ALLOWED_CONFIG_KEYS = {
    "CATO_ACCOUNT_ID",
    "CATO_BASEURL",
    "CATO_BASE_URL",
    "CATO_TOKEN",
}
DEFAULT_ENDPOINT = "https://api.catonetworks.com/api/v1/graphql2"


def load_shell_config(path: Path) -> dict:
    """Parse simple shell assignments without executing the file."""
    values = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        tokens = shlex.split(line, comments=True)
        if not tokens:
            continue
        if tokens[0] == "export":
            tokens = tokens[1:]
        if len(tokens) != 1 or "=" not in tokens[0]:
            raise ValueError(f"Unsupported config syntax on line {line_number}")

        key, value = tokens[0].split("=", 1)
        if key in ALLOWED_CONFIG_KEYS:
            values[key] = value

    missing = {"CATO_ACCOUNT_ID", "CATO_TOKEN"} - values.keys()
    if missing:
        raise ValueError(f"Missing required config keys: {', '.join(sorted(missing))}")
    return values


def validate_endpoint(endpoint: str) -> str:
    """Require an absolute HTTPS API endpoint."""
    parsed = urlparse(endpoint)
    if parsed.scheme != "https" or not parsed.netloc:
        raise ValueError("CATO_BASEURL must be an absolute HTTPS URL")
    return endpoint


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run generated tests using credentials from a shell config file."
    )
    parser.add_argument("--config", required=True, type=Path, help="Shell config file path")
    parser.add_argument("--operation", help="Run operations matching this value")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-x", "--stop-on-fail", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = args.config.expanduser().resolve()
    if not config_path.is_file():
        print(f"Config file not found: {config_path}", file=sys.stderr)
        return 2

    try:
        config = load_shell_config(config_path)
        endpoint = validate_endpoint(
            config.get("CATO_BASEURL") or config.get("CATO_BASE_URL") or DEFAULT_ENDPOINT
        )
    except (OSError, ValueError) as error:
        print(f"Invalid config: {error}", file=sys.stderr)
        return 2

    original_home = os.environ.get("HOME")
    try:
        with tempfile.TemporaryDirectory(prefix="cato-cli-tests-") as temporary_home:
            os.environ["HOME"] = temporary_home

            from catocli.Utils.profile_manager import ProfileManager

            ProfileManager().create_profile(
                "default",
                endpoint=endpoint,
                cato_token=config["CATO_TOKEN"],
                account_id=config["CATO_ACCOUNT_ID"],
            )

            runner = AllTestsRunner(verbose=args.verbose, stop_on_fail=args.stop_on_fail)
            passed = runner.run_generated_tests(args.operation)
            return 0 if passed else 1
    finally:
        if original_home is None:
            os.environ.pop("HOME", None)
        else:
            os.environ["HOME"] = original_home


if __name__ == "__main__":
    raise SystemExit(main())
