"""Private boolean flags must not override JSON values when omitted."""

import argparse
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from catocli.parsers import customParserApiClient as client
from catocli.parsers.custom_private import create_private_command_parser


class PrivateBooleanArgumentsTest(unittest.TestCase):
    def setUp(self):
        self.config = {
            "description": "Update administrator login restrictions",
            "arguments": [
                {
                    "name": name,
                    "type": "boolean",
                    "path": [
                        "variables.update.administratorLoginRestrictions." + name
                    ],
                }
                for name in ("enableLoginIps", "enableLoginEgressIps")
            ],
        }
        self.template = {
            "variables": {
                "update": {
                    "administratorLoginRestrictions": {
                        "enableLoginIps": True,
                        "enableLoginEgressIps": False,
                    }
                }
            }
        }

    def parse(self, arguments):
        parser = argparse.ArgumentParser()
        create_private_command_parser(
            parser.add_subparsers(), "accountUpdate", self.config
        )
        return parser.parse_args(["accountUpdate"] + arguments)

    def payload(self, arguments):
        args = self.parse(arguments + ["-t"])
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory:
            settings = Path(directory) / "settings.json"
            settings.write_text('{"autoFetchVersion": false}')
            with patch.object(client, "get_profile_manager") as manager, \
                    patch.object(client.os.path, "expanduser", return_value=str(settings)), \
                    patch.object(client, "load_payload_template", return_value=self.template), \
                    patch.object(client, "sendPrivateRequest") as send, \
                    contextlib.redirect_stdout(output):
                manager.return_value.validate_private_credentials.return_value = (True, None)
                manager.return_value.get_credentials.return_value = {
                    "account_id": "123",
                    "private_endpoint": "https://example.invalid/graphql",
                }
                client.createPrivateRequest(args, SimpleNamespace())
                send.assert_not_called()
        return json.loads(output.getvalue())["variables"]["update"][
            "administratorLoginRestrictions"
        ]

    def test_omitted_flags_are_none(self):
        args = self.parse([])
        self.assertIsNone(args.enableLoginIps)
        self.assertIsNone(args.enableLoginEgressIps)

    def test_json_booleans_are_preserved(self):
        for value in (True, False):
            with self.subTest(value=value):
                values = dict.fromkeys(("enableLoginIps", "enableLoginEgressIps"), value)
                self.assertEqual(values, self.payload([json.dumps(values)]))

    def test_explicit_flag_overrides_only_its_json_value(self):
        values = {"enableLoginIps": False, "enableLoginEgressIps": True}
        self.assertEqual(
            {"enableLoginIps": True, "enableLoginEgressIps": True},
            self.payload([json.dumps(values), "--enableLoginIps"]),
        )

    def test_json_file_booleans_are_preserved(self):
        values = {"enableLoginIps": True, "enableLoginEgressIps": False}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            path.write_text(json.dumps(values))
            self.assertEqual(values, self.payload(["--json-file", str(path)]))

    def test_omitted_values_preserve_template_defaults(self):
        self.assertEqual(
            {"enableLoginIps": True, "enableLoginEgressIps": False},
            self.payload([]),
        )

    def test_omitted_flag_preserves_configured_default(self):
        self.config["arguments"][0]["default"] = True
        self.assertIs(self.payload([])["enableLoginIps"], True)
