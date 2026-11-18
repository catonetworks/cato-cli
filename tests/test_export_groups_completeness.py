"""Diagnostic/regression tests for the groups-export completeness question:

the reference-architecture repo's config_data/groups.json exports only 4
groups from the refarch tenant, while its policy-rule JSON files reference
11 distinct group names via rule source/destination `group` fields (e.g.
`.data.policy.wanNetwork.policy.rules[6].rule.source.group[0] ->
{"name": "Branch Locations"}`).

Schema investigation (schema/introspection.json), offline, no network calls:

  1. `GroupListFilterInput` (the only filter `groups.groupList` accepts) has
     fields {freeText, id, name, member, audit} - there is NO "type"/"kind"
     field to distinguish "system" vs "user-defined" groups. The `Group`
     object type itself (id, name, description, audit, members,
     membersCount, membersCountPerType) also carries no such field. So
     there is no addressable filter argument this exporter could be passing
     (or failing to pass) that would explain a 4-vs-11 split.

  2. The `group` field referenced in rule criteria (e.g.
     `InternetFirewallSource.group`, `WanNetworkRuleSource.group`) resolves
     to `[GroupRef!]!` where `GroupRef = {id, name}` - the SAME entity
     `groups.groupList`/`groups.group` exposes. This is a DIFFERENT type
     from `SystemGroupRef` (also `{id, name}`, used by a separate
     `systemGroup` field on the same criteria objects) - and crucially,
     `SystemGroupRef` has NO associated list query anywhere in the schema
     (`GroupsQueries` only exposes `group`, `whereUsed`, `groupList`). Every
     missing-group occurrence found in config_data/*.json keys off `group`,
     never `systemGroup` - confirmed by walking the actual JSON (see the
     path above). So the missing names are not a different, unexported
     object type; they are `Group` entities, the exact type groups.json
     claims to export in full.

  3. `GroupListInput.sort` is NON_NULL but has a schema-level default
     ({name: {direction: ASC, priority: 1}}), so GROUP_LIST_QUERY's
     omission of `sort` is schema-compliant, not a bug. `paging.limit`
     defaults to 100 but the exporter always passes PAGE_LIMIT (1000)
     explicitly, comfortably covering any realistic group count in one
     page.

Conclusion: this task's second test class below proves the existing
pagination/aggregation logic in export_groups_to_json is NOT the cause - it
correctly aggregates everything a (possibly multi-page) groupList response
returns, with no default filter ever sent. Given no fixable filter/arg gap
exists and the group entity type is confirmed identical, the live 4-vs-11
discrepancy most likely reflects actual tenant data (e.g. rule criteria
retaining the plain-text name of a `Group` that was later deleted - once
strip_ids_recursive drops an {id, name}-only GroupRef's id at export time,
only the name survives, forever, even if the group itself no longer exists)
rather than a defect in this exporter. Confirming that definitively (vs. an
account/credential-scoped visibility difference on the live API not visible
in the checked-in schema) requires a live diagnostic run against the refarch
tenant (e.g. `CATO_PROFILE=refarch catocli export groups -v`, comparing the
printed "Retrieved N groups (offset: 0, total: X)" line against X=11) - out
of scope here (no real API calls permitted).
"""

import unittest
from types import SimpleNamespace
from unittest.mock import patch

from catocli.parsers.custom.export_deps import export_deps


def _group_list_page(items, total, offset):
    return {
        "data": {
            "groups": {
                "groupList": {
                    "items": items,
                    "paging": {"total": total},
                }
            }
        }
    }


def _empty_members_response():
    return {
        "data": {
            "groups": {
                "group": {
                    "members": {"items": [], "paging": {"total": 0}}
                }
            }
        }
    }


ALL_ELEVEN_NAMES = [
    "Admin Networks", "Azure AKS_AVD", "Cloud Sites", "Corporate SItes",
    "Branch Locations", "Company-APP1", "EU-Sites", "Guest Network",
    "NAM-Sites", "Printers", "Quarantine Hosts Group",
]


class GroupListPaginationAggregatesEveryPageTest(unittest.TestCase):
    """If the live API DOES paginate groupList (e.g. a tenant with >1000
    groups, or a server-side page cap smaller than the requested limit),
    export_groups_to_json must still return every group across every page.
    This is a stubbed multi-page response (4 groups on page 1, matching the
    live groups.json count; the remaining 7 on page 2, matching the 7 names
    missing from it) - proving the aggregation loop itself is not the
    reason groups would be dropped."""

    def test_multi_page_response_yields_all_eleven_groups(self):
        page1_items = [{"id": f"g{i}", "name": name} for i, name in enumerate(ALL_ELEVEN_NAMES[:4])]
        page2_items = [{"id": f"g{i+4}", "name": name} for i, name in enumerate(ALL_ELEVEN_NAMES[4:])]

        call_log = []

        def fake_make_call(args, configuration, query):
            if query["operationName"] == "groupsGroupList":
                offset = query["variables"]["groupListInput"]["paging"]["from"]
                call_log.append(("groupList", offset))
                if offset == 0:
                    return _group_list_page(page1_items, total=11, offset=0)
                return _group_list_page(page2_items, total=11, offset=offset)
            call_log.append(("members", None))
            return _empty_members_response()

        captured = {}

        def fake_finalize(items, args, account_id, default_filename, name_key='name'):
            captured["items"] = items
            return [{"success": True, "output_file": default_filename}]

        args = SimpleNamespace(verbose=False, strip_ids=False, names=None, merge_into=None)
        with patch.object(export_deps, "makeCall", side_effect=fake_make_call), \
                patch.object(export_deps, "getAccountID", return_value="12345"), \
                patch.object(export_deps, "_finalize_export", side_effect=fake_finalize):
            result = export_deps.export_groups_to_json(args, configuration=None)

        self.assertTrue(result[0]["success"] if isinstance(result, list) else True)
        names = {g["name"] for g in captured["items"]}
        self.assertEqual(names, set(ALL_ELEVEN_NAMES))
        self.assertEqual(len(captured["items"]), 11)
        # Pagination actually walked two pages (offset 0 then 1000), proving
        # this isn't a single-page-only aggregation.
        self.assertIn(("groupList", 0), call_log)
        self.assertIn(("groupList", export_deps.PAGE_LIMIT), call_log)


class GroupListQuerySendsNoDefaultFilterTest(unittest.TestCase):
    """export_groups_to_json must never send a `filter` that could silently
    exclude a subset of groups - GROUP_LIST_QUERY/groupListInput should only
    ever carry `paging` (no `filter`, no implicit "type"/"kind" scoping),
    since GroupListFilterInput/Group expose no such field to filter on in
    the first place (see this module's docstring)."""

    def test_group_list_input_carries_only_paging(self):
        seen_variables = []

        def fake_make_call(args, configuration, query):
            if query["operationName"] == "groupsGroupList":
                seen_variables.append(query["variables"]["groupListInput"])
                return _group_list_page([{"id": "g1", "name": "Only Group"}], total=1, offset=0)
            return _empty_members_response()

        args = SimpleNamespace(verbose=False, strip_ids=False, names=None, merge_into=None)
        with patch.object(export_deps, "makeCall", side_effect=fake_make_call), \
                patch.object(export_deps, "getAccountID", return_value="12345"), \
                patch.object(export_deps, "_finalize_export", side_effect=lambda items, *a, **k: [{"success": True}]):
            export_deps.export_groups_to_json(args, configuration=None)

        self.assertEqual(len(seen_variables), 1)
        self.assertEqual(set(seen_variables[0].keys()), {"paging"})


if __name__ == "__main__":
    unittest.main()
