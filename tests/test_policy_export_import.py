"""Policy export/import regressions without live API or Terraform calls."""

import contextlib
import io
import json
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from catocli.parsers.custom.export_rules import export_rules as exporter
from catocli.parsers.custom.import_rules_to_tf import import_rules_to_tf as importer


class PolicyExportImportTest(unittest.TestCase):
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
        response = {'data': {'policy': {'internetFirewall': {'policy': policy}}}}
        with patch.object(exporter, 'getAccountID', return_value='account'), \
                patch.object(exporter, 'makeCall', return_value=response), \
                patch.object(exporter, 'writeDataToFile', return_value='export.json') as write:
            result = exporter.export_if_rules_to_json(SimpleNamespace(), None)
        self.assertTrue(result[0]['success'], result)
        exported = write.call_args.kwargs['data']['data']['policy']['internetFirewall']['policy']
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
