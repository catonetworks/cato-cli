"""Import summaries must distinguish failed imports from successful completion."""
import contextlib
import io
import json
import tempfile
from pathlib import Path
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

    def test_all_flat_family_imports_report_unexpected_failures(self):
        families = {
            "apc": "applicationControl", "atr": "appTenantRestriction",
            "ts": "terminalServer", "amfh": "antiMalwareFileHash",
            "ssia": "sdpStaticIpAllocation", "dia": "dynamicIpAllocation",
            "cc": "clientConnectivity", "st": "splitTunnel", "rpf": "remotePortFwd",
            "swp": "siteWebProxy", "sb": "socketBypass",
        }
        for prefix, key in families.items():
            with self.subTest(family=prefix), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "export.json"
                path.write_text(json.dumps({"data": {"policy": {key: {"policy": {
                    "sections": [], "rules": [{"rule": {"id": "r1", "name": "Rule"}}]
                }}}}}))
                args = SimpleNamespace(json_file=str(path), module_name="policy", verbose=False,
                                       auto_approve=True, batch_size=10, delay=0)
                with patch.object(importer, "validate_terraform_environment"), \
                        patch.object(importer, "run_terraform_import", return_value=(False, "", "permission denied")), \
                        contextlib.redirect_stdout(io.StringIO()):
                    result = getattr(importer, "import_" + prefix + "_rules_to_tf")(args, None)
                self.assertFalse(result[0]["success"], result)
                self.assertEqual(result[0]["other_failures"], 1)
