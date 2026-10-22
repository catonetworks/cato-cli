"""Behavioral coverage for nested namespaces and GraphQL file uploads."""

import copy
import contextlib
import io
import json
import sys
import tempfile
import unittest
from email.parser import BytesParser
from email.policy import default
from pathlib import Path
from unittest.mock import patch
from urllib3.response import HTTPResponse

from graphql import DirectiveLocation, build_client_schema, parse, validate

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "schema"))
import catolib
from catocli.Utils.graphql_utils import generateGraphqlPayload, renderArgsAndFields, validateArgs
from graphql_client import ApiClient, CallApi, Configuration
from graphql_client.uploads import MAX_UPLOAD_BYTES, encode_uploads


def model(name):
    return json.loads((ROOT / "models" / f"{name}.json").read_text())


class NamespaceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = json.loads((ROOT / "schema/introspection.json").read_text())["data"]
        for directive in data["__schema"]["directives"]:
            directive["locations"] = [v for v in directive["locations"] if v in DirectiveLocation.__members__]
        cls.schema = build_client_schema(data)

    def test_argument_free_operation_has_no_variable_definitions(self):
        name = "query.rateLimit"
        operation = model(name)
        payload = generateGraphqlPayload({}, operation, name,
            renderArgsAndFields_func=lambda r, v, o, d, n, i, a: renderArgsAndFields(r, v, o, d, n, i, a, None))
        document = parse(payload["query"])
        self.assertEqual([], validate(self.schema, document))
        self.assertFalse(document.definitions[0].variable_definitions)
        self.assertEqual("rateLimit", payload["operationName"])
        self.assertEqual({}, payload["variables"])

    def test_independent_rbac_actions(self):
        cases = {
            "mutation.rbac.roleManagement.createRole": {"roleManagementCreateRoleInput": {"name": "example", "permission": []}},
            "mutation.rbac.roleManagement.updateRole": {"roleManagementUpdateRoleInput": {"id": "1", "name": "example"}},
            "mutation.rbac.roleManagement.deleteRole": {"roleManagementDeleteRoleInput": {"id": "1"}},
            "query.rbac.roleManagement.permissionCatalog": {},
            "query.rbac.roleManagement.role": {"id": "1"},
            "query.rbac.roleManagement.roleList": {"roleManagementRoleListInput": {"paging": {"from": 0, "limit": 10}}},
        }
        for name, variables in cases.items():
            with self.subTest(operation=name):
                operation = model(name)
                variables = dict(variables, accountId="123")
                self.assertTrue(validateArgs(variables, operation)[0])
                payload = generateGraphqlPayload(variables, operation, name,
                    renderArgsAndFields_func=lambda r, v, o, d, n, i, a: renderArgsAndFields(r, v, o, d, n, i, a, None))
                self.assertEqual([], validate(self.schema, parse(payload["query"])))
                fields = parse(payload["query"]).definitions[0].selection_set.selections[0].selection_set.selections[0].selection_set.selections
                self.assertEqual([name.split(".")[-1]], [field.name.value for field in fields])

    def test_discovery_reaches_argument_free_catalog(self):
        data = json.loads((ROOT / "schema/introspection.json").read_text())
        settings = json.loads((ROOT / "catocli/clisettings.json").read_text())
        types = {t["name"]: t for t in data["data"]["__schema"]["types"]}
        categories = {"OBJECT": "objects", "INPUT_OBJECT": "input_objects", "ENUM": "enums", "SCALAR": "scalars", "INTERFACE": "interfaces", "UNION": "unions"}
        introspection = {category: {name: t for name, t in types.items() if t["kind"] == kind}
                         for kind, category in categories.items()}
        field = next(f for f in types["Query"]["fields"] if f["name"] == "rbac")
        self.assertTrue(catolib.isChildOperationParent(field, settings["childOperationParent"], settings["childOperationObjects"]))
        schema = {"query": {}, "mutation": {}}
        with patch.dict(catolib.catoApiIntrospection, introspection), patch.object(catolib, "catoApiSchema", schema):
            catolib.getChildOperations("query", copy.deepcopy(field), copy.deepcopy(field), "query.rbac",
                                      settings["childOperationObjects"], settings["childOperationLeafObjects"])
        self.assertEqual({"query.rbac.roleManagement." + name for name in ("permissionCatalog", "role", "roleList")}, set(schema["query"]))

    def test_other_query_namespaces_are_independent(self):
        cases = {
            "query.connectivitySnapshots.ztnaAppConnectorGroupSnapshot": "ztnaAppConnectorGroupSnapshotInput",
            "query.connectivitySnapshots.ztnaAppConnectorSnapshot": "ztnaAppConnectorSnapshotInput",
            "query.connectivitySnapshots.ztnaAppConnectorSnapshotSummary": "ztnaAppConnectorSnapshotSummaryInput",
            "query.customAppData.customApplication": "customApplicationRefInput",
            "query.customAppData.customApplicationList": "customApplicationListInput",
            "query.privateApplication.privateApplication": "privateApplicationRefInput",
            "query.privateApplication.privateApplicationList": "privateApplicationListInput",
            "query.user.userList": "userListInput",
            "query.user.dynamicUserGroupsConfiguration": None,
        }
        for name, input_name in cases.items():
            with self.subTest(operation=name):
                operation = model(name)
                self.assertEqual({"accountId"} | ({input_name} if input_name else set()),
                                 set(operation["operationArgs"]))
                variables = dict(catolib.generateExampleVariables(operation), accountId="123")
                self.assertTrue(validateArgs(variables, operation)[0])
                payload = generateGraphqlPayload(variables, operation, name,
                    renderArgsAndFields_func=lambda r, v, o, d, n, i, a: renderArgsAndFields(r, v, o, d, n, i, a, None))
                self.assertEqual([], validate(self.schema, parse(payload["query"])))
                selection = parse(payload["query"]).definitions[0].selection_set
                for segment in name.split(".")[1:]:
                    self.assertEqual([segment], [field.name.value for field in selection.selections])
                    selection = selection.selections[0].selection_set

    def test_group_list_without_and_with_member_details(self):
        operation = model("query.groups.groupList")
        self.assertFalse(operation["operationArgs"]["groupMembersListInput"]["requiredForOperation"])
        for include_members in (False, True):
            with self.subTest(include_members=include_members):
                variables = {"accountId": "123"}
                if include_members:
                    variables["groupMembersListInput"] = catolib.generateExampleVariables(operation)["groupMembersListInput"]
                self.assertTrue(validateArgs(variables, operation)[0])
                payload = generateGraphqlPayload(variables, copy.deepcopy(operation), "query.groups.groupList",
                    renderArgsAndFields_func=lambda r, v, o, d, n, i, a: renderArgsAndFields(r, v, o, d, n, i, a, None))
                self.assertEqual([], validate(self.schema, parse(payload["query"])))
                self.assertEqual(include_members, "members (" in payload["query"])
                self.assertEqual(include_members, "$groupMembersListInput" in payload["query"])

    def test_group_mutations_do_not_require_returned_member_details(self):
        for action in ("createGroup", "updateGroup", "deleteGroup"):
            name = "mutation.groups." + action
            with self.subTest(operation=name):
                operation = model(name)
                variables = dict(catolib.generateExampleVariables(operation), accountId="123")
                variables.pop("groupMembersListInput", None)
                self.assertTrue(validateArgs(variables, operation)[0])
                payload = generateGraphqlPayload(variables, operation, name,
                    renderArgsAndFields_func=lambda r, v, o, d, n, i, a: renderArgsAndFields(r, v, o, d, n, i, a, None))
                self.assertEqual([], validate(self.schema, parse(payload["query"])))
                self.assertNotIn("$groupMembersListInput", payload["query"])


class UploadTest(unittest.TestCase):
    def test_generated_command_uploads_without_a_live_request(self):
        from catocli.Utils.clidriver import parser
        configuration = Configuration()
        configuration.version = "test"
        configuration.accountID = "123"
        configuration.host = "https://example.invalid/graphql"
        configuration.api_key["x-api-key"] = "test-only"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.keytab"
            path.write_bytes(b"keytab bytes")
            args = parser.parse_args(["mutation", "webProxyConfig", "encryptKeytabFile",
                                      json.dumps({"encryptKeytabFileInput": {"file": str(path)}})])
            with patch("graphql_client.api_client.urllib3.PoolManager.request") as request, contextlib.redirect_stdout(io.StringIO()):
                request.return_value = HTTPResponse(body=b'{"data": {"webProxyConfig": {"encryptKeytabFile": {"encryptedFile": "result"}}}}', status=200)
                args.func(args, configuration)
            self.assertEqual(1, request.call_count)
            self.assertIn("multipart/form-data", request.call_args.kwargs["headers"]["Content-Type"])
            self.assertIn(b"keytab bytes", request.call_args.kwargs["body"])
            path.unlink()
            args.t = True
            with patch("graphql_client.api_client.urllib3.PoolManager.request") as request, contextlib.redirect_stdout(io.StringIO()):
                args.func(args, configuration)
            request.assert_not_called()

    def test_upload_reaches_http_transport_with_file_bytes(self):
        configuration = Configuration()
        configuration.version = "test"
        configuration.host = "https://example.invalid/graphql"
        configuration.api_key["x-api-key"] = "test-only"
        client = ApiClient(configuration)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.keytab"
            path.write_bytes(b"\x00\xffkeytab\x01")
            for name in ("mutation.encryptKeytabFile", "mutation.webProxyConfig.encryptKeytabFile"):
                with self.subTest(operation=name):
                    body = {"query": "mutation example { __typename }", "variables": {"accountId": "123", "encryptKeytabFileInput": {"file": str(path)}}}
                    original = copy.deepcopy(body)
                    with patch.object(client.rest_client.pool_manager, "request") as request:
                        request.return_value = HTTPResponse(body=b'{"data": {}}', status=200)
                        CallApi(client).call_api(body, {"_upload_model": model(name), "trace_id": True})
                    kwargs = request.call_args.kwargs
                    headers = kwargs["headers"]
                    self.assertEqual("test-only", headers["x-api-key"])
                    self.assertEqual("true", headers["x-force-tracing"])
                    message = BytesParser(policy=default).parsebytes(("Content-Type: " + headers["Content-Type"] + "\r\n\r\n").encode() + kwargs["body"])
                    parts = {part.get_param("name", header="content-disposition"): part.get_payload(decode=True) for part in message.iter_parts()}
                    self.assertIsNone(json.loads(parts["operations"])["variables"]["encryptKeytabFileInput"]["file"])
                    self.assertEqual({"0": ["variables.encryptKeytabFileInput.file"]}, json.loads(parts["map"]))
                    self.assertEqual(path.read_bytes(), parts["0"])
                    self.assertEqual(original, body)

    def test_missing_and_oversized_uploads_fail_before_network(self):
        operation = model("mutation.webProxyConfig.encryptKeytabFile")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.keytab"
            body = {"variables": {"encryptKeytabFileInput": {"file": str(path)}}}
            with self.assertRaises(OSError):
                encode_uploads(body, operation)
            with path.open("wb") as handle:
                handle.truncate(MAX_UPLOAD_BYTES + 1)
            with self.assertRaisesRegex(ValueError, "32 MiB"):
                encode_uploads(body, operation)
            body["variables"]["encryptKeytabFileInput"]["file"] = directory
            with self.assertRaisesRegex(ValueError, "regular file"):
                encode_uploads(body, operation)

    def test_regular_string_paths_are_not_uploaded(self):
        self.assertIsNone(encode_uploads({"variables": {"name": "/tmp/file"}}, {"operationArgs": {"name": {"type": {"name": "String", "kind": ["SCALAR"]}}}}))

    def test_upload_lists_use_indexed_paths(self):
        operation = {"operationArgs": {"files": {"type": {"name": "Upload", "kind": ["LIST", "SCALAR"]}}}}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "one.keytab"
            path.write_bytes(b"binary file")
            for values in ([str(path), str(path)], str(path)):
                with self.subTest(values=values):
                    body, content_type = encode_uploads({"variables": {"files": values}}, operation)
                    message = BytesParser(policy=default).parsebytes(("Content-Type: " + content_type + "\r\n\r\n").encode() + body)
                    parts = {part.get_param("name", header="content-disposition"): part.get_payload(decode=True) for part in message.iter_parts()}
                    count = len(values) if isinstance(values, list) else 1
                    self.assertEqual({str(index): [f"variables.files.{index}"] for index in range(count)}, json.loads(parts["map"]))
                    self.assertEqual([None] * count, json.loads(parts["operations"])["variables"]["files"])


if __name__ == "__main__":
    unittest.main()
