"""Offline tests for the implicit-default-section sentinel and custom-apps sort.

Sentinel convention: rules living in a policy's implicit default section (a
section the API never lists in policy.sections[]) are exported with
section_name "" -- the canonical sentinel. Exporters previously synthesized
the literal "Default Section" on some paths, which made exports internally
inconsistent (two sentinels for one concept) and noisy to validate. These
tests pin the new behavior: "" passes through verbatim and the synthesized
string is gone from the codebase.

Also pins the custom_applications export's deterministic top-level ordering
(sorted by name, case-insensitive), which the docstring always promised but
the code never applied.

No network calls -- makeCall/getAccountID/output writers are monkeypatched.
"""

import json
import os
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from catocli.parsers.custom.export_rules import export_rules
from catocli.parsers.custom.export_deps import export_deps

EXPORT_RULES_SRC = os.path.join(
    os.path.dirname(export_rules.__file__), "export_rules.py"
)


def _fake_tls_response():
    return {
        "data": {
            "policy": {
                "tlsInspect": {
                    "policy": {
                        "enabled": True,
                        "rules": [
                            {
                                "properties": [],
                                "rule": {
                                    "id": "r1",
                                    "name": "Sentinel Rule",
                                    "index": 1,
                                    "section": {"id": "", "name": ""},
                                    "enabled": True,
                                },
                            },
                            {
                                "properties": ["SYSTEM"],
                                "rule": {
                                    "id": "r2",
                                    "name": "System Rule",
                                    "index": 2,
                                    "section": {"id": "", "name": ""},
                                    "enabled": True,
                                },
                            },
                            {
                                "properties": [],
                                "rule": {
                                    "id": "r3",
                                    "name": "Named Rule",
                                    "index": 3,
                                    "section": {"id": "s1", "name": "Named"},
                                    "enabled": True,
                                },
                            },
                        ],
                        "sections": [{"section": {"id": "s1", "name": "Named"}}],
                    }
                }
            }
        }
    }


class TlsSentinelExportTest(unittest.TestCase):
    """Flat-path exporters emit "" for the implicit default section."""

    def _run_export(self):
        captured = {}

        def fake_write(data, args, **kwargs):
            captured["data"] = data
            return {"success": True, "output_file": "unused.json"}

        args = SimpleNamespace(verbose=False)
        with patch.object(export_rules, "makeCall", return_value=_fake_tls_response()), \
                patch.object(export_rules, "getAccountID", return_value="12345"), \
                patch.object(export_rules, "writeDataToFile", side_effect=fake_write):
            export_rules.export_tls_rules_to_json(args, configuration=None)
        return captured["data"]

    def test_empty_section_name_survives_verbatim(self):
        data = self._run_export()
        policy = data["data"]["policy"]["tlsInspect"]["policy"]
        ris = policy["rules_in_sections"]
        by_rule = {row["rule_name"]: row["section_name"] for row in ris}
        self.assertEqual(by_rule["Sentinel Rule"], "")
        self.assertEqual(by_rule["Named Rule"], "Named")
        # SYSTEM rule filtered out entirely
        self.assertNotIn("System Rule", by_rule)

    def test_no_default_section_string_in_output(self):
        data = self._run_export()
        self.assertNotIn("Default Section", json.dumps(data))


class NoSynthesizedSentinelAnywhereTest(unittest.TestCase):
    """The legacy synthesized string is gone from the exporter source, so no
    path (flat, wnw/tls copies, sub-policy main branch) can reintroduce it."""

    def test_default_section_literal_absent_from_export_rules(self):
        with open(EXPORT_RULES_SRC, encoding="utf-8") as fh:
            src = fh.read()
        self.assertNotIn('"Default Section"', src)


def _fake_custom_apps_response():
    return {
        "data": {
            "customAppData": {
                "customApplicationList": {
                    "items": [
                        {
                            "id": "a2",
                            "name": "zeta app",
                            "description": "",
                            "category": [],
                            "criteria": [],
                        },
                        {
                            "id": "a1",
                            "name": "Alpha App",
                            "description": "",
                            "category": [],
                            "criteria": [],
                        },
                        {
                            "id": "a3",
                            "name": "beta app",
                            "description": "",
                            "category": [],
                            "criteria": [],
                        },
                    ],
                    "paging": {"total": 3},
                }
            }
        }
    }


class CustomAppsSortTest(unittest.TestCase):
    def test_apps_sorted_by_name_case_insensitive(self):
        captured = {}

        def fake_finalize(items, args, account_id, default_filename):
            captured["items"] = items
            return {"success": True, "output_file": default_filename}

        args = SimpleNamespace(verbose=False, strip_ids=False)
        with patch.object(export_deps, "makeCall", return_value=_fake_custom_apps_response()), \
                patch.object(export_deps, "getAccountID", return_value="12345"), \
                patch.object(export_deps, "_finalize_export", side_effect=fake_finalize):
            export_deps.export_custom_apps_to_json(args, configuration=None)

        names = [a["name"] for a in captured["items"]]
        self.assertEqual(names, ["Alpha App", "beta app", "zeta app"])


if __name__ == "__main__":
    unittest.main()
