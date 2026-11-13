"""Regression tests for the accountSnapshot batching fix in export_sites.py.

Context: `catocli export socket_sites` (and `export all`) previously called
getAccountSnapshot() once per site inside a tight per-site loop. For an
account with many sites, that produces a rapid burst of sequential POSTs
from the same IP, which can trip the Cato API edge's Imperva/Incapsula WAF
rate/bot heuristics and return an HTML challenge page instead of GraphQL
JSON (see test_customlib_waf_retry.py for the WAF-detection/retry side of
the fix).

The accountSnapshot GraphQL query already accepts a list of site IDs in a
single call, so the fix batches all site IDs into as few getAccountSnapshot
calls as possible (see getAccountSnapshotSitesMap / ACCOUNT_SNAPSHOT_CHUNK_SIZE
in export_sites.py) instead of calling it once per site.

These tests never touch the network - every dependency of
export_socket_site_to_json / get_processed_site_data other than the
accountSnapshot batching path itself is monkeypatched to an in-memory stub.
"""

import unittest
from types import SimpleNamespace
from unittest.mock import patch

from catocli.parsers.custom.export_sites import export_sites


def _fake_entity_sites(count):
    return [
        {"entity": {"id": str(site_id), "name": f"site{site_id}", "type": "site"}}
        for site_id in range(1, count + 1)
    ]


def _fake_snapshot_response(site_ids):
    """Mimic getAccountSnapshot()'s return shape for the given site_ids."""
    return {
        "data": {
            "accountSnapshot": {
                "sites": [
                    {
                        "id": site_id,
                        "infoSiteSnapshot": {
                            "name": f"site{site_id}",
                            "type": "cloud_dc",  # not in export_by_socket_type -> "cloud site", skipped
                            "connType": "NOT_A_SOCKET_TYPE",
                            "interfaces": [],
                        },
                        "devices": [],
                    }
                    for site_id in site_ids
                ]
            }
        }
    }


class GetAccountSnapshotSitesMapTest(unittest.TestCase):
    """Unit tests for the chunking helper itself."""

    def setUp(self):
        self.args = SimpleNamespace(verbose=False)
        self.configuration = SimpleNamespace()
        self.calls = []

    def _fake_get_account_snapshot(self, args, configuration, account_id, site_ids):
        self.calls.append(list(site_ids))
        return _fake_snapshot_response(site_ids)

    def test_small_site_list_is_a_single_call(self):
        """14 sites (the exact count from the field failure) fits in one
        chunk (ACCOUNT_SNAPSHOT_CHUNK_SIZE=25), so exactly 1 call is made,
        not 14."""
        site_ids = [str(i) for i in range(1, 15)]
        with patch.object(export_sites, "getAccountSnapshot", side_effect=self._fake_get_account_snapshot):
            sites_map = export_sites.getAccountSnapshotSitesMap(
                self.args, self.configuration, "15412", site_ids
            )

        self.assertEqual(len(self.calls), 1)
        self.assertEqual(sorted(self.calls[0]), sorted(site_ids))
        self.assertEqual(len(sites_map), 14)
        for site_id in site_ids:
            self.assertIn(site_id, sites_map)

    def test_large_site_list_is_chunked_not_per_site(self):
        """60 sites with a chunk size of 25 -> 3 calls (25, 25, 10), never 60."""
        site_ids = [str(i) for i in range(1, 61)]
        with patch.object(export_sites, "getAccountSnapshot", side_effect=self._fake_get_account_snapshot):
            sites_map = export_sites.getAccountSnapshotSitesMap(
                self.args, self.configuration, "15412", site_ids
            )

        self.assertEqual(len(self.calls), 3)
        self.assertEqual([len(c) for c in self.calls], [25, 25, 10])
        self.assertEqual(len(sites_map), 60)

    def test_empty_site_list_makes_no_call(self):
        with patch.object(export_sites, "getAccountSnapshot", side_effect=self._fake_get_account_snapshot):
            sites_map = export_sites.getAccountSnapshotSitesMap(
                self.args, self.configuration, "15412", []
            )
        self.assertEqual(self.calls, [])
        self.assertEqual(sites_map, {})


class ExportSocketSiteToJsonCallCountTest(unittest.TestCase):
    """End-to-end (but network-free) regression test: the full
    export_socket_site_to_json loop over N sites must call the underlying
    getAccountSnapshot a number of times bounded by the chunk size, not N."""

    def setUp(self):
        self.snapshot_calls = []

        self.patches = [
            patch.object(export_sites, "getAccountID", return_value="15412"),
            patch.object(
                export_sites,
                "load_cli_settings",
                return_value={"export_by_socket_type": []},  # classify every site as "cloud" -> skip heavy processing
            ),
            patch.object(export_sites, "getDhcpRelayGroups", return_value={}),
            patch.object(export_sites, "getNetworkRangeList", return_value=[]),
            patch.object(export_sites, "writeDataToFile", return_value="config_data/socket_sites_15412.json"),
        ]
        for p in self.patches:
            p.start()
            self.addCleanup(p.stop)

        def fake_get_entity_lookup(args, configuration, account_id, entity_type, entity_ids=None, entity_input=None):
            if entity_type == "site":
                return _fake_entity_sites(14)
            return []  # networkInterface / siteRange: no extra interfaces/ranges needed for this test

        self.entity_lookup_patch = patch.object(export_sites, "getEntityLookup", side_effect=fake_get_entity_lookup)
        self.entity_lookup_patch.start()
        self.addCleanup(self.entity_lookup_patch.stop)

        def fake_get_account_snapshot(args, configuration, account_id, site_ids):
            self.snapshot_calls.append(list(site_ids))
            return _fake_snapshot_response(site_ids)

        self.snapshot_patch = patch.object(export_sites, "getAccountSnapshot", side_effect=fake_get_account_snapshot)
        self.snapshot_patch.start()
        self.addCleanup(self.snapshot_patch.stop)

    def test_fourteen_sites_trigger_one_snapshot_call_not_fourteen(self):
        """This is the exact field scenario: '14 site(s) found...' must now
        result in 1 batched getAccountSnapshot call instead of 14 sequential
        per-site calls."""
        args = SimpleNamespace(verbose=False)
        result = export_sites.export_socket_site_to_json(args, configuration=SimpleNamespace())

        self.assertTrue(result[0]["success"], result[0])
        self.assertEqual(len(self.snapshot_calls), 1)
        self.assertEqual(len(self.snapshot_calls[0]), 14)


if __name__ == "__main__":
    unittest.main()
