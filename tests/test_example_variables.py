import datetime
import ipaddress
import json
import shlex
import subprocess
import sys
import unittest
from pathlib import Path
from zoneinfo import ZoneInfo

from graphql import DirectiveLocation, build_client_schema, get_variable_values, parse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "schema"))
import catolib


class ExampleVariablesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = json.loads((ROOT / "schema/introspection.json").read_text())["data"]
        # The API includes a vendor directive location unsupported by graphql-core.
        # Directive locations do not affect variable coercion.
        for directive in data["__schema"]["directives"]:
            directive["locations"] = [
                location for location in directive["locations"]
                if location in DirectiveLocation.__members__
            ]
        cls.schema = build_client_schema(data)

    def test_generated_examples_match_schema_and_checked_in_payloads(self):
        paths = sorted((ROOT / "queryPayloads").glob("*.json"))
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(operation=path.stem):
                payload = json.loads(path.read_text())
                model = json.loads((ROOT / "models" / path.name).read_text())
                variables = catolib.generateExampleVariables(model)
                self.assertEqual(payload["variables"], variables)
                # Account context is injected by the CLI profile.
                variables.update(accountID="12345", accountId="12345")
                definitions = parse(payload["query"]).definitions[0].variable_definitions
                result = get_variable_values(self.schema, definitions, variables)
                self.assertIsInstance(result, dict, result)

    def test_custom_scalar_formats(self):
        def example(name):
            return catolib.renderInputFieldVal({"type": {"name": name, "kind": ["SCALAR"]}})

        self.assertEqual(example("TimeFrame"), "last.P1D")
        datetime.datetime.fromisoformat(example("DateTime"))
        datetime.date.fromisoformat(example("Date"))
        datetime.time.fromisoformat(example("Time"))
        ZoneInfo(example("TimeZone"))
        ipaddress.ip_address(example("IPAddress"))
        ipaddress.ip_network(example("IPSubnet"))
        start, end = example("IPRange").split("-")
        self.assertLess(ipaddress.ip_address(start), ipaddress.ip_address(end))
        self.assertIsInstance(example("Map"), dict)
        for name in ("Port", "Vlan", "Long", "NetworkBandwidth", "ApplicationRisk"):
            self.assertIsInstance(example(name), int)
        self.assertRegex(example("SHA_256"), r"^[0-9a-f]{64}$")

    def test_missing_argument_example_is_shell_ready(self):
        result = subprocess.run(
            [sys.executable, "-m", "catocli", "query", "events"],
            cwd=ROOT, capture_output=True, text=True, timeout=30, check=True,
        )
        example = next(line.removeprefix("Example: ") for line in result.stdout.splitlines()
                       if line.startswith("Example: "))
        command = shlex.split(example)
        self.assertEqual(command[:3], ["catocli", "query", "events"])
        self.assertEqual(len(command), 4)
        variables = json.loads(command[3])
        self.assertEqual(variables["timeFrame"], "last.P1D")
        for name in ("eventsDimension", "eventsFilter", "eventsMeasure", "eventsPostAggFilter", "eventsSort"):
            self.assertIsInstance(variables[name], list)


if __name__ == "__main__":
    unittest.main()
