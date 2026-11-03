"""Policy export/import regressions without live API or Terraform calls."""

import ast
import contextlib
import copy
import io
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from catocli.parsers.custom.export_rules import export_rules as exporter
from catocli.parsers.custom.import_rules_to_tf import import_rules_to_tf as importer


class PolicyExportImportTest(unittest.TestCase):
    def test_flat_family_exports_preserve_import_ids_and_filter_unmanaged_rules(self):
        families = {
            "apc": "applicationControl", "atr": "appTenantRestriction",
            "ts": "terminalServer", "amfh": "antiMalwareFileHash",
            "ssia": "sdpStaticIpAllocation", "dia": "dynamicIpAllocation",
            "cc": "clientConnectivity", "st": "splitTunnel", "rpf": "remotePortFwd",
            "swp": "siteWebProxy", "sb": "socketBypass",
        }
        for prefix, key in families.items():
            with self.subTest(family=prefix):
                section = {"id": "s1", "name": 'Office\\Network "A"', "subPolicyId": None}
                rules = [{"rule": {"id": "r1", "name": 'Rule "A"', "index": 3,
                                    "section": section, "enabled": False, "ruleType": "APPLICATION",
                                    "applicationRule": {}}, "properties": []}]
                for property_name in ("SYSTEM", "LOCKED"):
                    rules.append({"rule": {"id": property_name, "name": property_name,
                                           "section": section}, "properties": [property_name]})
                original = {"data": {"policy": {key: {"policy": {
                    "sections": [{"section": section}], "rules": rules,
                }}}}}
                before = copy.deepcopy(original)
                with patch.object(exporter, "getAccountID", return_value="account"), \
                        patch.object(exporter, "makeCall", return_value=original), \
                        patch.object(exporter, "writeDataToFile", return_value="export.json") as write:
                    result = getattr(exporter, "export_" + prefix + "_rules_to_json")(SimpleNamespace(), None)
                self.assertTrue(result[0]["success"], result)
                policy = write.call_args.kwargs["data"]["data"]["policy"][key]["policy"]
                self.assertEqual([row["rule"]["id"] for row in policy["rules"]], ["r1"])
                self.assertEqual(policy["sections"][0]["section_id"], "s1")
                self.assertEqual(policy["rules_in_sections"][0]["section_name"], section["name"])
                self.assertEqual(original, before)

    def test_backslash_sub_policy_keeps_child_and_cleanup_ownership(self):
        name = 'Corp\\Office'
        def row(rule_id, rule_name, index, rule_type='POLICY_RULE'):
            result = {
                'rule': {'id': rule_id, 'name': rule_name, 'index': index,
                         'section': {'id': 'section', 'name': 'Managed', 'subPolicyId': None}},
                'ruleType': rule_type, 'properties': [],
            }
            if rule_type != 'SUB_POLICY_SCOPE':
                result['subPolicy'] = {'id': 'sub', 'name': name}
            return result
        policy = {
            'sections': [{'section': {'id': 'default', 'name': 'Default', 'subPolicyId': None}},
                         {'section': {'id': 'section', 'name': 'Managed', 'subPolicyId': None}}],
            'subPolicies': [{'policy': {'id': 'sub', 'name': name, 'description': '', 'enabled': True}}],
            'rules': [row('scope', name, 1, 'SUB_POLICY_SCOPE'),
                      row('child', 'Allow', 2), row('cleanup', 'Cleanup', 3)],
        }
        self.check_sub_policy_export('internetFirewall', exporter.export_if_rules_to_json, policy, name)
        self.check_sub_policy_export('wanFirewall', exporter.export_wf_rules_to_json, policy, name)

    def check_sub_policy_export(self, key, export, policy, name):
        response = {'data': {'policy': {key: {'policy': policy}}}}
        with patch.object(exporter, 'getAccountID', return_value='account'), \
                patch.object(exporter, 'makeCall', return_value=response), \
                patch.object(exporter, 'writeDataToFile', return_value='export.json') as write:
            result = export(SimpleNamespace(), None)
        self.assertTrue(result[0]['success'], result)
        exported = write.call_args.kwargs['data']['data']['policy'][key]['policy']
        self.assertEqual(exported['rules'][0]['sub_policy_name'], name)
        self.assertEqual(exported['sub_policies'][0]['cleanup_rule']['rule']['id'], 'cleanup')
        self.assertEqual(exported['rules_in_sections'][1]['sub_policy_name'], name)

    def test_import_escapes_terraform_instance_keys(self):
        name = 'Corp\\Office "Allow"'
        with patch.object(importer, 'run_terraform_import', return_value=(True, '', '')) as run, \
                contextlib.redirect_stdout(io.StringIO()):
            importer.import_sub_policies([{'sub_policy_name': name, 'sub_policy_id': 'sub'}], 'policy')
            self.assertEqual(run.call_args.args[0],
                             'module.policy.cato_if_sub_policy.sub_policies[' + json.dumps(name) + ']')
            importer.import_sub_rules([{'sub_policy_name': name, 'name': name, 'id': 'rule'}], 'policy')
            self.assertTrue(run.call_args.args[0].endswith('[' + json.dumps(name + '::' + name) + ']'))

    def test_flat_import_escapes_instance_keys(self):
        name = 'Office\\Network "Allow"'
        with patch.object(importer, 'run_terraform_import', return_value=(True, '', '')) as run, \
                contextlib.redirect_stdout(io.StringIO()):
            importer.import_lan_items([{'name': name, 'id': 'rule'}], 'policy',
                                      'cato_socket_bypass_rule', 'rules', 'name', 'id', 'Rule')
        self.assertEqual(run.call_args.args[0],
                         'module.policy.cato_socket_bypass_rule.rules[' + json.dumps(name) + ']')

    def test_all_export_queries_validate_against_schema(self):
        from graphql import parse, validate
        from schema_utils import load_test_schema
        schema = load_test_schema()
        tree = ast.parse(Path(exporter.__file__).read_text())
        queries = [node for node in ast.walk(tree)
                   if isinstance(node, ast.Constant) and isinstance(node.value, str)
                   and node.value.startswith('query policy ')]
        self.assertGreaterEqual(len(queries), 9)
        for query in queries:
            with self.subTest(line=query.lineno):
                self.assertEqual(validate(schema, parse(query.value)), [])
