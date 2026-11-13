"""Offline tests for `catocli export webhooks` (notification.integration.
webhookList) - the standalone webhook-list export added alongside the
existing `--strip-ids` work. No network calls - makeCall/getAccountID/
_finalize_export are monkeypatched, mirroring the conventions in
tests/test_export_sentinel_and_sort.py and tests/test_export_all_strip_ids.py.
"""

import json
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from catocli.parsers.custom.export_deps import export_deps
from catocli.parsers.custom.export_rules import export_rules as export_rules_module
from catocli.parsers.custom.export_rules import export_rules_parse
import argparse


def _fake_webhook_list_response():
    return {
        "data": {
            "notification": {
                "integration": {
                    "webhookList": {
                        "items": [
                            {
                                "id": "wh2",
                                "name": "zeta webhook",
                                "enabled": True,
                                "url": "https://example.com/zeta",
                                "requestMethod": "POST",
                                "relatedWebhookId": None,
                            },
                            {
                                "id": "wh1",
                                "name": "Alpha Webhook",
                                "enabled": False,
                                "url": "https://example.com/alpha",
                                "requestMethod": "POST",
                                "relatedWebhookId": "wh2",
                            },
                        ],
                        "paging": {"total": 2},
                    }
                }
            }
        }
    }


class ExportWebhooksToJsonTest(unittest.TestCase):
    def _run(self, strip_ids):
        captured = {}

        def fake_finalize(items, args, account_id, default_filename, name_key='name'):
            captured["items"] = items
            captured["default_filename"] = default_filename
            return [{"success": True, "output_file": default_filename}]

        args = SimpleNamespace(verbose=False, strip_ids=strip_ids, names=None, merge_into=None)
        with patch.object(export_deps, "makeCall", return_value=_fake_webhook_list_response()), \
                patch.object(export_deps, "getAccountID", return_value="12345"), \
                patch.object(export_deps, "_finalize_export", side_effect=fake_finalize):
            export_deps.export_webhooks_to_json(args, configuration=None)
        return captured

    def test_canonical_filename_is_account_agnostic(self):
        captured = self._run(strip_ids=False)
        self.assertEqual(captured["default_filename"], "webhooks.json")

    def test_fields_and_no_secret_fields_present(self):
        captured = self._run(strip_ids=False)
        item = next(i for i in captured["items"] if i["name"] == "Alpha Webhook")
        self.assertEqual(item["id"], "wh1")
        self.assertEqual(item["enabled"], False)
        self.assertEqual(item["url"], "https://example.com/alpha")
        self.assertEqual(item["requestMethod"], "POST")
        self.assertEqual(item["relatedWebhookId"], "wh2")
        for secret_field in ("auth", "header", "body", "responseMapping"):
            self.assertNotIn(secret_field, item)

    def test_strip_ids_removes_top_level_id_but_keeps_related_webhook_id(self):
        captured = self._run(strip_ids=True)
        item = next(i for i in captured["items"] if i["name"] == "Alpha Webhook")
        self.assertNotIn("id", item)
        self.assertEqual(item["relatedWebhookId"], "wh2")


class StripWebhooksIdsUnitTest(unittest.TestCase):
    def test_strips_only_top_level_id(self):
        webhooks = [
            {"id": "wh1", "name": "A", "enabled": True, "url": "u", "requestMethod": "POST", "relatedWebhookId": "wh2"},
        ]
        stripped = export_deps.strip_webhooks_ids(webhooks)
        self.assertNotIn("id", stripped[0])
        self.assertEqual(stripped[0]["relatedWebhookId"], "wh2")
        self.assertEqual(stripped[0]["name"], "A")
        # Pure - input untouched.
        self.assertIn("id", webhooks[0])


class WebhooksNativeVsPostprocessedEquivalenceTest(unittest.TestCase):
    """Same equivalence guarantee as groups/mailing_lists: `export webhooks
    --strip-ids` and `export all --strip-ids`'s post-processing must produce
    byte-identical output, since both call strip_webhooks_ids."""

    def _run(self, strip_ids):
        captured = {}

        def fake_finalize(items, args, account_id, default_filename, name_key='name'):
            captured["items"] = items
            return [{"success": True, "output_file": default_filename}]

        args = SimpleNamespace(verbose=False, strip_ids=strip_ids, names=None, merge_into=None)
        with patch.object(export_deps, "makeCall", return_value=_fake_webhook_list_response()), \
                patch.object(export_deps, "getAccountID", return_value="12345"), \
                patch.object(export_deps, "_finalize_export", side_effect=fake_finalize):
            export_deps.export_webhooks_to_json(args, configuration=None)
        return captured["items"]

    def test_native_strip_matches_postprocessed_strip(self):
        native_stripped = self._run(strip_ids=True)
        raw = self._run(strip_ids=False)
        postprocessed = export_rules_module._strip_exported_payload("webhooks", raw)

        self.assertEqual(
            json.dumps(native_stripped, sort_keys=True),
            json.dumps(postprocessed, sort_keys=True),
        )
        self.assertIn("id", raw[0])
        self.assertNotIn("id", native_stripped[0])
        self.assertNotIn("id", postprocessed[0])


class WebhooksRegistrationTest(unittest.TestCase):
    """`webhooks` must be picked up automatically by `export all`'s
    runtime-derived type registry (no second hardcoded type list)."""

    def test_webhooks_is_registered_and_reachable_via_export_all_registry(self):
        parser = argparse.ArgumentParser(prog="catocli")
        subparsers = parser.add_subparsers()
        export_rules_parse(subparsers)

        export_parser = parser._subparsers._group_actions[0].choices["export"]
        registry = next(a for a in export_parser._actions if getattr(a, "choices", None))
        self.assertIn("webhooks", registry.choices)

        all_args = parser.parse_args(["export", "all", "--types", "webhooks"])
        self.assertIs(all_args.func, export_rules_module.export_all_to_json)
        self.assertIn("webhooks", all_args._export_subparsers.choices)


if __name__ == "__main__":
    unittest.main()
