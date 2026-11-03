"""Import summaries must distinguish failed imports from successful completion."""
import contextlib
import io
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from catocli.parsers.custom.import_rules_to_tf import import_rules_to_tf as importer


class ImportFailureTest(unittest.TestCase):
    def test_if_import_reports_unexpected_failure(self):
        args = SimpleNamespace(json_file="unused.json", module_name="policy", verbose=False,
                               rules_only=False, sections_only=False, auto_approve=True,
                               batch_size=10, delay=0)
        policy = {"sections": [], "rules": [{"rule": {"id": "r1", "name": "Rule"}}]}
        with patch.object(importer, "load_json_data", return_value=policy), \
                patch.object(importer, "validate_terraform_environment"), \
                patch.object(importer, "run_terraform_import", return_value=(False, "", "permission denied")), \
                contextlib.redirect_stdout(io.StringIO()):
            result = importer.import_if_rules_to_tf(args, None)
        self.assertIn("other_failures", result[0], result)
        self.assertFalse(result[0]["success"])
        self.assertEqual(result[0]["other_failures"], 1)
