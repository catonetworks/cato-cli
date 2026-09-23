import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "schema"))
sys.path.insert(0, str(ROOT))

import catolib
from catocli.Utils.graphql_utils import generateGraphqlPayload, renderArgsAndFields


def load_introspection():
    with (ROOT / "schema/introspection.json").open(encoding="utf-8") as handle:
        types = json.load(handle)["data"]["__schema"]["types"]

    categories = {
        "OBJECT": "objects",
        "INTERFACE": "interfaces",
        "UNION": "unions",
        "INPUT_OBJECT": "input_objects",
        "ENUM": "enums",
        "SCALAR": "scalars",
    }
    for category in catolib.catoApiIntrospection.values():
        category.clear()
    for type_obj in types:
        category = categories.get(type_obj["kind"])
        if category:
            catolib.catoApiIntrospection[category][type_obj["name"]] = type_obj


def generated_query(operation_name):
    with (ROOT / "models" / f"{operation_name}.json").open(encoding="utf-8") as handle:
        operation = json.load(handle)
    variables = catolib.generateExampleVariables(operation)
    return generateGraphqlPayload(
        variables,
        operation,
        operation_name,
        renderArgsAndFields_func=lambda response, values, current, definition, name, indent, dynamic: renderArgsAndFields(
            response,
            values,
            current,
            definition,
            name,
            indent,
            dynamic,
            None,
        ),
    )["query"]


class GeneratedGraphQLPayloadTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_introspection()

    def test_account_arguments_are_rendered(self):
        remove_account = generated_query("mutation.accountManagement.removeAccount")
        account_snapshot = generated_query("query.accountSnapshot")

        self.assertIn("removeAccount ( accountId:$accountIdToRemove", remove_account)
        self.assertIn("$accountId:ID!", remove_account)
        self.assertIn("$accountIdToRemove:ID!", remove_account)
        self.assertNotIn("accountSnapshot ( )", account_snapshot)
        self.assertIn("accountSnapshot {", account_snapshot)

    def test_union_is_rendered_once(self):
        query = generated_query("query.auditFeed")

        self.assertNotIn("\n\t\t\t\t\t{\n", query)
        self.assertEqual(query.count("... on StringValue"), 1)
        self.assertEqual(query.count("... on DateValue"), 1)
        self.assertEqual(query.count("... on Entity"), 1)

    def test_xdr_complex_fields_and_interface_conflicts(self):
        query = generated_query("query.xdr.stories")

        self.assertIn("... on MicrosoftEndpoint", query)
        self.assertIn("analystFeedback {\n", query)
        self.assertIn("site {\n", query)
        self.assertIn("device {\n", query)
        self.assertIn("alerts {\n", query)
        self.assertIn("statusCatoEndpoint: status", query)
        self.assertIn("statusMicrosoftEndpoint: status", query)
        self.assertEqual(query.count("siteName"), 1)
        self.assertNotIn("\n\t\t\t\t\tanalystFeedback\n", query)
        self.assertNotIn("\n\t\t\t\t\tdevice\n", query)
        self.assertNotIn("\n\t\t\t\t\talerts\n", query)
        self.assertNotRegex(query, r"\.\.\. on \w+ \{\n\s*\}")


if __name__ == "__main__":
    unittest.main()
