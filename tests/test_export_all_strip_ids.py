"""Offline tests for `--strip-ids` support: the shared per-type strip
transforms (export_deps.py, export_sites.py, export_rules.py) and
`catocli export all --strip-ids`'s orchestration (raw-archive-then-strip
ordering, CHECKLIST.md generation, flag interplay).

No network calls anywhere - makeCall/getAccountID/_finalize_export/file I/O
are either monkeypatched or exercised against real temp-directory files (for
the ordering/CHECKLIST tests, which need real files to assert archive vs.
primary content).
"""

import argparse
import json
import os
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from catocli.parsers.custom.export_rules import export_rules_parse
from catocli.parsers.custom.export_rules import export_rules as export_rules_module
from catocli.parsers.custom.export_deps import export_deps
from catocli.parsers.custom.export_sites import export_sites


def build_export_parser():
    parser = argparse.ArgumentParser(prog="catocli")
    subparsers = parser.add_subparsers()
    export_rules_parse(subparsers)
    return parser


# ---------------------------------------------------------------------------
# 1. Native --strip-ids vs. `export all --strip-ids` post-processing:
#    byte-identical equivalence for groups and mailing_lists (the two types
#    called out in the task - name-fallback members / admin-id subtleties).
# ---------------------------------------------------------------------------

def _fake_groups_responses():
    group_list_response = {
        "data": {
            "groups": {
                "groupList": {
                    "items": [{"id": "g1", "name": "Group One", "description": "desc"}],
                    "paging": {"total": 1},
                }
            }
        }
    }
    members_response = {
        "data": {
            "groups": {
                "group": {
                    "members": {
                        "items": [
                            {"id": "m1", "name": "Bob", "type": "user"},
                            {"id": "m2", "name": "Alice", "type": "user"},
                        ],
                        "paging": {"total": 2},
                    }
                }
            }
        }
    }

    def fake_make_call(args, configuration, query):
        if query["operationName"] == "groupsGroupList":
            return group_list_response
        return members_response

    return fake_make_call


def _fake_mailing_lists_response():
    return {
        "data": {
            "notification": {
                "mailingListList": {
                    "items": [
                        {
                            "id": "ml1",
                            "name": "List One",
                            "address": ["b@x.com", "a@x.com"],
                            "admin": [
                                {"id": "u2", "name": "Bob"},
                                {"id": "u1", "name": "Alice"},
                            ],
                        }
                    ]
                }
            }
        }
    }


class DependencyStripEquivalenceTest(unittest.TestCase):
    """`catocli export <type> --strip-ids` and `export all --strip-ids`'s
    post-processing of the raw export must be byte-identical, because both
    call the exact same pure strip_*_ids function - this pins that equality
    for groups (member id/name-fallback) and mailing_lists (admin ids)."""

    def _run_export_groups(self, strip_ids):
        captured = {}

        def fake_finalize(items, args, account_id, default_filename, name_key='name'):
            captured["items"] = items
            return [{"success": True, "output_file": default_filename}]

        args = SimpleNamespace(verbose=False, strip_ids=strip_ids, names=None, merge_into=None)
        with patch.object(export_deps, "makeCall", side_effect=_fake_groups_responses()), \
                patch.object(export_deps, "getAccountID", return_value="12345"), \
                patch.object(export_deps, "_finalize_export", side_effect=fake_finalize):
            export_deps.export_groups_to_json(args, configuration=None)
        return captured["items"]

    def test_groups_native_strip_matches_postprocessed_strip(self):
        native_stripped = self._run_export_groups(strip_ids=True)
        raw = self._run_export_groups(strip_ids=False)
        postprocessed = export_rules_module._strip_exported_payload("groups", raw)

        self.assertEqual(
            json.dumps(native_stripped, sort_keys=True),
            json.dumps(postprocessed, sort_keys=True),
        )
        # Sanity: the raw version actually had ids to strip, so this isn't
        # vacuously true.
        self.assertIn("id", raw[0])
        self.assertNotIn("id", native_stripped[0])
        self.assertNotIn("id", postprocessed[0])

    def _run_export_mailing_lists(self, strip_ids):
        captured = {}

        def fake_finalize(items, args, account_id, default_filename, name_key='name'):
            captured["items"] = items
            return [{"success": True, "output_file": default_filename}]

        args = SimpleNamespace(verbose=False, strip_ids=strip_ids, names=None, merge_into=None)
        with patch.object(export_deps, "makeCall", return_value=_fake_mailing_lists_response()), \
                patch.object(export_deps, "getAccountID", return_value="12345"), \
                patch.object(export_deps, "_finalize_export", side_effect=fake_finalize):
            export_deps.export_mailing_lists_to_json(args, configuration=None)
        return captured["items"]

    def test_mailing_lists_native_strip_matches_postprocessed_strip(self):
        native_stripped = self._run_export_mailing_lists(strip_ids=True)
        raw = self._run_export_mailing_lists(strip_ids=False)
        postprocessed = export_rules_module._strip_exported_payload("mailing_lists", raw)

        self.assertEqual(
            json.dumps(native_stripped, sort_keys=True),
            json.dumps(postprocessed, sort_keys=True),
        )
        self.assertIn("id", raw[0])
        self.assertNotIn("id", native_stripped[0])
        self.assertNotIn("id", postprocessed[0])
        # Admin ids specifically - the subtlety called out in the task.
        self.assertNotIn("id", native_stripped[0]["admin"][0])
        self.assertNotIn("id", postprocessed[0]["admin"][0])


# ---------------------------------------------------------------------------
# 2. socket_sites strip field list (ported from migrate_tenant.py).
# ---------------------------------------------------------------------------

class SocketSitesStripFieldsTest(unittest.TestCase):
    def test_strip_socket_site_ids_removes_the_documented_fields_only(self):
        data = {
            "sites": [
                {
                    "id": "site-1",
                    "name": "Branch 1",
                    "license_id": "lic-1",
                    "license_bw": 100,
                    "wan_interfaces": [{"id": "site-1:WAN1", "name": "WAN 1"}],
                    "lan_interfaces": [
                        {
                            "id": "site-1:INT_5",
                            "network_ranges": [{"id": "range-1", "subnet": "10.0.0.0/24"}],
                        }
                    ],
                    "native_range": {"id": "nr-1", "range_id": "range-0", "vlan": 10},
                    "wifi_ssids": [{"id": "ssid-1", "name": "Guest Wi-Fi"}],
                }
            ]
        }

        result = export_sites.strip_socket_site_ids(data)
        site = result["sites"][0]

        self.assertNotIn("id", site)
        self.assertNotIn("license_id", site)
        self.assertNotIn("license_bw", site)
        self.assertNotIn("id", site["wan_interfaces"][0])
        self.assertNotIn("id", site["lan_interfaces"][0])
        self.assertNotIn("id", site["lan_interfaces"][0]["network_ranges"][0])
        self.assertNotIn("id", site["native_range"])
        self.assertNotIn("range_id", site["native_range"])
        self.assertNotIn("id", site["wifi_ssids"][0])

        # Everything else survives untouched.
        self.assertEqual(site["name"], "Branch 1")
        self.assertEqual(site["wan_interfaces"][0]["name"], "WAN 1")
        self.assertEqual(site["lan_interfaces"][0]["network_ranges"][0]["subnet"], "10.0.0.0/24")
        self.assertEqual(site["native_range"]["vlan"], 10)
        self.assertEqual(site["wifi_ssids"][0]["name"], "Guest Wi-Fi")


# ---------------------------------------------------------------------------
# 3. Policy-rules strip: rule.id/section_id/sub_policy_id/scope_rule_id gone;
#    names, rules_in_sections, and the "" sentinel untouched.
# ---------------------------------------------------------------------------

def _fake_if_rules_payload():
    return {
        "data": {
            "policy": {
                "internetFirewall": {
                    "policy": {
                        "enabled": True,
                        "revision": {"id": "rev-1", "name": "rev"},
                        "rules": [
                            {
                                "audit": {},
                                "properties": [],
                                "rule": {
                                    "id": "rule-1",
                                    "name": "Sentinel Rule",
                                    "section": {"name": ""},
                                    "enabled": True,
                                },
                            },
                            {
                                "audit": {},
                                "properties": [],
                                "rule": {
                                    "id": "rule-2",
                                    "name": "Named Rule",
                                    "section": {"name": "Main"},
                                    "enabled": True,
                                },
                            },
                        ],
                        "sections": [
                            {"section_index": 1, "section_name": "Main", "section_id": "sec-1"},
                        ],
                        "rules_in_sections": [
                            {"index_in_section": 1, "section_name": "", "rule_name": "Sentinel Rule"},
                            {"index_in_section": 1, "section_name": "Main", "rule_name": "Named Rule"},
                        ],
                        "sub_policies": [
                            {
                                "sub_policy_name": "SubPolicy A",
                                "sub_policy_id": "sp-1",
                                "scope_rule_id": "scope-rule-1",
                                "description": "",
                                "enabled": True,
                                "scope_enabled": True,
                                "scope": {},
                                "cleanup_rule": {
                                    "audit": {},
                                    "rule": {"id": "cleanup-rule-1", "name": "Cleanup", "section": {"name": ""}},
                                },
                            }
                        ],
                    }
                }
            }
        }
    }


class PolicyRulesStripTest(unittest.TestCase):
    def test_import_key_ids_stripped_names_and_ordering_untouched(self):
        raw = _fake_if_rules_payload()
        stripped = export_rules_module._strip_exported_payload("if_rules", raw)
        policy = stripped["data"]["policy"]["internetFirewall"]["policy"]

        # rule.id gone on every rule, including the sub-policy's cleanup_rule.
        for rule_wrapper in policy["rules"]:
            self.assertNotIn("id", rule_wrapper["rule"])
        self.assertNotIn("id", policy["sub_policies"][0]["cleanup_rule"]["rule"])

        # section_id / sub_policy_id / scope_rule_id gone.
        self.assertNotIn("section_id", policy["sections"][0])
        self.assertNotIn("sub_policy_id", policy["sub_policies"][0])
        self.assertNotIn("scope_rule_id", policy["sub_policies"][0])

        # Names, rules_in_sections, and the "" sentinel are untouched.
        self.assertEqual(policy["rules"][0]["rule"]["name"], "Sentinel Rule")
        self.assertEqual(policy["rules"][0]["rule"]["section"]["name"], "")
        self.assertEqual(policy["rules"][1]["rule"]["name"], "Named Rule")
        self.assertEqual(policy["sections"][0]["section_name"], "Main")
        self.assertEqual(
            policy["rules_in_sections"],
            [
                {"index_in_section": 1, "section_name": "", "rule_name": "Sentinel Rule"},
                {"index_in_section": 1, "section_name": "Main", "rule_name": "Named Rule"},
            ],
        )
        self.assertEqual(policy["sub_policies"][0]["sub_policy_name"], "SubPolicy A")
        self.assertEqual(policy["sub_policies"][0]["cleanup_rule"]["rule"]["name"], "Cleanup")

        # Original is untouched (pure transform - caller may still need the
        # raw version, e.g. for archiving).
        raw_policy = raw["data"]["policy"]["internetFirewall"]["policy"]
        self.assertEqual(raw_policy["rules"][0]["rule"]["id"], "rule-1")
        self.assertEqual(raw_policy["sections"][0]["section_id"], "sec-1")

    def test_unrecognized_type_passes_through_unchanged(self):
        raw = {"some": "shape", "with": ["no", "policy", "node"]}
        result = export_rules_module._strip_exported_payload("future_type", raw)
        self.assertEqual(result, raw)


# ---------------------------------------------------------------------------
# 4. `export all --strip-ids` orchestration: raw-archived-then-stripped-
#    primary ordering, single API call per type, and CHECKLIST.md only
#    written when --strip-ids is set.
# ---------------------------------------------------------------------------

class ExportAllStripIdsOrderingTest(unittest.TestCase):
    """Stubs write REAL id-bearing JSON content per type (a dependency-shaped
    list for 'groups', a policy-shaped payload for 'if_rules'), so stripping
    has real, assertable effect."""

    def setUp(self):
        self.parser = build_export_parser()
        export_parser = self.parser._subparsers._group_actions[0].choices["export"]
        self.registry = next(
            a for a in export_parser._actions if getattr(a, "choices", None)
        )
        self.call_counts = {}

        for name, sub_parser in self.registry.choices.items():
            if name == "all":
                continue
            sub_parser.set_defaults(func=self._make_stub(name))

        self._orig_preflight = export_rules_module._preflight_validate_export_all_credentials
        export_rules_module._preflight_validate_export_all_credentials = (
            lambda args, configuration: (True, "stub: preflight skipped")
        )
        self.addCleanup(self._restore_preflight)

        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.output_dir = os.path.join(self.tmp.name, "config_data")
        os.makedirs(self.output_dir, exist_ok=True)
        self.archive_dir = os.path.join(self.tmp.name, "config_data_archive")

    def _restore_preflight(self):
        export_rules_module._preflight_validate_export_all_credentials = self._orig_preflight

    def _make_stub(self, name):
        def stub(args, configuration):
            self.call_counts[name] = self.call_counts.get(name, 0) + 1
            out_dir = getattr(args, "output_directory", None) or self.output_dir
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, f"{name}.json")
            if name == "groups":
                content = [{"id": "g1", "name": "Group One", "members": [{"id": "m1", "type": "user", "name": "Bob"}]}]
            elif name == "if_rules":
                content = _fake_if_rules_payload()
            else:
                content = {"type": name}
            with open(out_path, "w") as f:
                json.dump(content, f)
            return [{"success": True, "output_file": out_path}]
        return stub

    def test_archive_keeps_raw_ids_primary_is_stripped_single_call_per_type(self):
        args = self.parser.parse_args([
            "export", "all", "--types", "groups,if_rules",
            "--output-directory", self.output_dir,
            "--archive-directory", self.archive_dir,
            "--strip-ids",
        ])
        result = args.func(args, None)
        self.assertTrue(result[0]["success"])

        # Exactly one call per type - the strip is pure post-processing of
        # the file already on disk, never a second API call.
        self.assertEqual(self.call_counts, {"groups": 1, "if_rules": 1})

        # Archive: raw, id-bearing.
        with open(os.path.join(self.archive_dir, "groups.json")) as f:
            archived_groups = json.load(f)
        self.assertEqual(archived_groups[0]["id"], "g1")
        self.assertEqual(archived_groups[0]["members"][0]["id"], "m1")

        with open(os.path.join(self.archive_dir, "if_rules.json")) as f:
            archived_if_rules = json.load(f)
        archived_policy = archived_if_rules["data"]["policy"]["internetFirewall"]["policy"]
        self.assertEqual(archived_policy["rules"][0]["rule"]["id"], "rule-1")
        self.assertEqual(archived_policy["sections"][0]["section_id"], "sec-1")

        # Primary: stripped.
        with open(os.path.join(self.output_dir, "groups.json")) as f:
            primary_groups = json.load(f)
        self.assertNotIn("id", primary_groups[0])
        self.assertNotIn("id", primary_groups[0]["members"][0])
        self.assertEqual(primary_groups[0]["name"], "Group One")

        with open(os.path.join(self.output_dir, "if_rules.json")) as f:
            primary_if_rules = json.load(f)
        primary_policy = primary_if_rules["data"]["policy"]["internetFirewall"]["policy"]
        self.assertNotIn("id", primary_policy["rules"][0]["rule"])
        self.assertNotIn("section_id", primary_policy["sections"][0])
        self.assertEqual(primary_policy["rules"][0]["rule"]["name"], "Sentinel Rule")
        self.assertEqual(primary_policy["rules"][0]["rule"]["section"]["name"], "")

    def test_without_strip_ids_primary_keeps_ids(self):
        args = self.parser.parse_args([
            "export", "all", "--types", "groups",
            "--output-directory", self.output_dir,
        ])
        result = args.func(args, None)
        self.assertTrue(result[0]["success"])
        with open(os.path.join(self.output_dir, "groups.json")) as f:
            primary_groups = json.load(f)
        self.assertEqual(primary_groups[0]["id"], "g1")


class ExportAllChecklistTest(ExportAllStripIdsOrderingTest):
    """CHECKLIST.md is written only when --strip-ids is set, into the
    primary --output-directory, and lists the files this run produced."""

    def test_checklist_written_with_strip_ids(self):
        args = self.parser.parse_args([
            "export", "all", "--types", "groups,if_rules",
            "--output-directory", self.output_dir,
            "--strip-ids",
        ])
        result = args.func(args, None)
        self.assertTrue(result[0]["success"])

        checklist_path = os.path.join(self.output_dir, "CHECKLIST.md")
        self.assertTrue(os.path.isfile(checklist_path))
        self.assertEqual(result[0]["checklist_path"], checklist_path)
        with open(checklist_path) as f:
            content = f.read()
        self.assertIn("catocli export all --strip-ids", content)
        self.assertIn("groups.json", content)
        self.assertIn("if_rules.json", content)
        self.assertIn("Wi-Fi PSKs", content)

    def test_checklist_not_written_without_strip_ids(self):
        args = self.parser.parse_args([
            "export", "all", "--types", "groups",
            "--output-directory", self.output_dir,
        ])
        result = args.func(args, None)
        self.assertTrue(result[0]["success"])
        self.assertIsNone(result[0]["checklist_path"])
        self.assertFalse(os.path.isfile(os.path.join(self.output_dir, "CHECKLIST.md")))


if __name__ == "__main__":
    unittest.main()
