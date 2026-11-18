"""`catocli export all` registration and argument-parsing behavior.

Builds just the `export` parser tree in isolation (not through clidriver) via
export_rules_parse(), the same entry point catocli/parsers/custom/__init__.py
uses. Every individual export subcommand's handler function is monkeypatched
to a network-free stub, and the pre-flight credential check
(_preflight_validate_export_all_credentials) is monkeypatched too, so these
tests never touch the Cato API.
"""

import argparse
import os
import tempfile
import unittest

from catocli.parsers.custom.export_rules import export_rules_parse
from catocli.parsers.custom.export_rules import export_rules as export_rules_module


def build_export_parser():
    parser = argparse.ArgumentParser(prog="catocli")
    subparsers = parser.add_subparsers()
    export_rules_parse(subparsers)
    return parser


class ExportAllRegistrationTest(unittest.TestCase):
    def setUp(self):
        self.parser = build_export_parser()
        # Walk down to the 'export' subparser's own subparsers action.
        export_parser = self.parser._subparsers._group_actions[0].choices["export"]
        self.registry = next(
            a for a in export_parser._actions if getattr(a, "choices", None)
        )

    def test_all_is_registered_alongside_every_export_type(self):
        self.assertIn("all", self.registry.choices)
        # 'all' must come after every other type was registered, so its
        # runtime-derived type list (see export_all_to_json) is complete.
        other_types = [name for name in self.registry.choices if name != "all"]
        self.assertGreater(len(other_types), 20)
        for expected in ("if_rules", "wf_rules", "socket_sites", "groups", "static_hosts"):
            self.assertIn(expected, other_types)

    def test_all_parser_exposes_common_and_filter_flags(self):
        all_args = self.parser.parse_args(["export", "all"])
        for attr in (
            "accountID", "output_directory", "types", "fail_fast", "verbose",
            "archive_directory", "no_account_suffix",
        ):
            self.assertTrue(hasattr(all_args, attr), f"missing attribute: {attr}")
        self.assertIsNone(all_args.types)
        self.assertFalse(all_args.fail_fast)
        self.assertFalse(all_args.verbose)
        self.assertIsNone(all_args.archive_directory)
        self.assertFalse(all_args.no_account_suffix)

    def test_all_args_carry_the_live_subparsers_registry(self):
        all_args = self.parser.parse_args(["export", "all"])
        self.assertIs(all_args._export_subparsers, self.registry)
        self.assertIs(all_args.func, export_rules_module.export_all_to_json)


class PreflightStubbedTestCase(unittest.TestCase):
    """Base class that stubs out the live-API pre-flight check so subclasses
    can exercise the per-type loop without any network access. Tests that
    want to exercise the pre-flight check itself override it per-test
    instead (see ExportAllPreflightTest)."""

    def setUp(self):
        self.parser = build_export_parser()
        export_parser = self.parser._subparsers._group_actions[0].choices["export"]
        self.registry = next(
            a for a in export_parser._actions if getattr(a, "choices", None)
        )
        self.called = []
        for name, sub_parser in self.registry.choices.items():
            if name == "all":
                continue
            sub_parser.set_defaults(func=self._make_stub(name))

        self._orig_preflight = export_rules_module._preflight_validate_export_all_credentials
        self._set_preflight(True, "stub: preflight skipped")
        self.addCleanup(self._restore_preflight)

    def _set_preflight(self, ok, message):
        export_rules_module._preflight_validate_export_all_credentials = (
            lambda args, configuration: (ok, message)
        )

    def _restore_preflight(self):
        export_rules_module._preflight_validate_export_all_credentials = self._orig_preflight

    # Failure fixtures used by multiple subclasses.
    ACCESS_DENIED_ERROR = (
        "Unexpected error during API call - API returned errors: Access denied: "
        "The API key does not have sufficient permissions for this operation. "
        "Please verify the associated Admin or Service Principal permissions"
    )

    def _make_stub(self, name):
        def stub(args, configuration):
            self.called.append(name)
            if name == "groups":
                return [{"success": False, "error": "stub failure for groups"}]
            if name == "dia_rules":
                return [{"success": False, "error": self.ACCESS_DENIED_ERROR}]
            return [{"success": True, "output_file": f"config_data/{name}.json"}]
        return stub


class ExportAllTypesFilterTest(PreflightStubbedTestCase):
    def test_unknown_type_is_rejected_without_calling_any_handler(self):
        args = self.parser.parse_args(["export", "all", "--types", "if_rules,bogus_type"])
        result = args.func(args, None)
        self.assertFalse(result[0]["success"])
        self.assertIn("bogus_type", result[0]["error"])
        self.assertEqual(self.called, [])

    def test_types_filter_runs_only_the_requested_subset(self):
        args = self.parser.parse_args(
            ["export", "all", "--types", "if_rules,wf_rules"]
        )
        result = args.func(args, None)
        self.assertTrue(result[0]["success"])
        self.assertEqual(sorted(self.called), ["if_rules", "wf_rules"])

    def test_continue_on_error_by_default_and_nonzero_exit_on_failure(self):
        # (c) a non-access-denied failure (the "groups" stub) does NOT abort
        # the run - wf_rules still runs afterward.
        args = self.parser.parse_args(
            ["export", "all", "--types", "if_rules,groups,wf_rules"]
        )
        with self.assertRaises(SystemExit) as ctx:
            args.func(args, None)
        self.assertEqual(ctx.exception.code, 1)
        self.assertEqual(sorted(self.called), ["groups", "if_rules", "wf_rules"])

    def test_fail_fast_stops_at_the_first_failure(self):
        args = self.parser.parse_args(
            ["export", "all", "--types", "groups,wf_rules", "--fail-fast"]
        )
        with self.assertRaises(SystemExit) as ctx:
            args.func(args, None)
        self.assertEqual(ctx.exception.code, 1)
        self.assertEqual(self.called, ["groups"])


class ExportAllAccessDeniedAbortTest(PreflightStubbedTestCase):
    """(b) A mid-run access-denied failure aborts the whole run immediately,
    regardless of continue-on-error / --fail-fast, and later types are never
    invoked."""

    def test_access_denied_aborts_immediately_and_skips_remaining_types(self):
        args = self.parser.parse_args(
            ["export", "all", "--types", "if_rules,dia_rules,wf_rules,groups"]
        )
        with self.assertRaises(SystemExit) as ctx:
            args.func(args, None)
        self.assertEqual(ctx.exception.code, 1)
        # wf_rules and groups queue after dia_rules's access-denied failure
        # and must never be called, even though continue-on-error is the
        # default behavior for ordinary (non-access-denied) failures.
        self.assertEqual(self.called, ["if_rules", "dia_rules"])

    def test_access_denied_abort_is_not_gated_behind_fail_fast(self):
        # No --fail-fast passed here: proves the abort-on-access-denied
        # behavior is unconditional, not an alias for --fail-fast.
        args = self.parser.parse_args(
            ["export", "all", "--types", "dia_rules,wf_rules"]
        )
        with self.assertRaises(SystemExit) as ctx:
            args.func(args, None)
        self.assertEqual(ctx.exception.code, 1)
        self.assertEqual(self.called, ["dia_rules"])

    def test_access_denied_raised_as_exception_also_aborts(self):
        # Access-denied surfacing as a raised exception (e.g. from makeCall)
        # rather than a returned {"success": False, ...} must abort too.
        def raising_stub(args, configuration):
            self.called.append("dia_rules")
            raise RuntimeError(self.ACCESS_DENIED_ERROR)

        for name, sub_parser in self.registry.choices.items():
            if name == "dia_rules":
                sub_parser.set_defaults(func=raising_stub)

        args = self.parser.parse_args(
            ["export", "all", "--types", "dia_rules,wf_rules"]
        )
        with self.assertRaises(SystemExit) as ctx:
            args.func(args, None)
        self.assertEqual(ctx.exception.code, 1)
        self.assertEqual(self.called, ["dia_rules"])


class ExportAllPreflightTest(PreflightStubbedTestCase):
    """(a) A failing pre-flight credential/permission check exits 1 before
    any type's handler is invoked."""

    def test_preflight_failure_exits_before_any_type_is_exported(self):
        self._set_preflight(False, "Access denied - check account ID and permissions")

        args = self.parser.parse_args(["export", "all"])
        with self.assertRaises(SystemExit) as ctx:
            args.func(args, None)
        self.assertEqual(ctx.exception.code, 1)
        self.assertEqual(self.called, [])

    def test_preflight_success_allows_the_run_to_proceed(self):
        self._set_preflight(True, "Credentials are valid")

        args = self.parser.parse_args(["export", "all", "--types", "if_rules"])
        result = args.func(args, None)
        self.assertTrue(result[0]["success"])
        self.assertEqual(self.called, ["if_rules"])


class ExportAllArchiveDirectoryTest(PreflightStubbedTestCase):
    """--archive-directory: on success, copy the real produced file
    byte-for-byte into the archive dir under the same basename; skip failed
    types; leave the archive untouched when the flag is omitted; and treat
    an archive-copy failure as a non-aborting per-type failure."""

    def setUp(self):
        super().setUp()
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.output_dir = os.path.join(self.tmp.name, "config_data")
        os.makedirs(self.output_dir, exist_ok=True)
        self.archive_dir = os.path.join(self.tmp.name, "config_data_archive")

        # Override the base class's fake-path stubs: these write a real
        # file to args.output_directory (already overridden by
        # export_all_to_json to this run's --output-directory) and return
        # its real path, so the archive step has an actual byte-for-byte
        # source to copy.
        for name, sub_parser in self.registry.choices.items():
            if name == "all":
                continue
            sub_parser.set_defaults(func=self._make_real_file_stub(name))

    def _make_real_file_stub(self, name):
        def stub(args, configuration):
            self.called.append(name)
            if name == "groups":
                return [{"success": False, "error": "stub failure for groups"}]
            if name == "dia_rules":
                return [{"success": False, "error": self.ACCESS_DENIED_ERROR}]
            out_dir = getattr(args, "output_directory", None) or self.output_dir
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, f"{name}.json")
            with open(out_path, "w") as f:
                f.write(f'{{"type": "{name}"}}')
            return [{"success": True, "output_file": out_path}]
        return stub

    def test_archive_files_created_with_identical_content_and_basenames(self):
        args = self.parser.parse_args([
            "export", "all", "--types", "if_rules,wf_rules",
            "--output-directory", self.output_dir,
            "--archive-directory", self.archive_dir,
        ])
        result = args.func(args, None)
        self.assertTrue(result[0]["success"])
        self.assertTrue(os.path.isdir(self.archive_dir))
        for name in ("if_rules", "wf_rules"):
            primary = os.path.join(self.output_dir, f"{name}.json")
            archived = os.path.join(self.archive_dir, f"{name}.json")
            self.assertTrue(os.path.isfile(archived))
            with open(primary) as f1, open(archived) as f2:
                self.assertEqual(f1.read(), f2.read())

    def test_failed_type_leaves_no_archive_file(self):
        args = self.parser.parse_args([
            "export", "all", "--types", "groups,wf_rules",
            "--output-directory", self.output_dir,
            "--archive-directory", self.archive_dir,
        ])
        with self.assertRaises(SystemExit):
            args.func(args, None)
        self.assertFalse(os.path.exists(os.path.join(self.archive_dir, "groups.json")))
        self.assertTrue(os.path.isfile(os.path.join(self.archive_dir, "wf_rules.json")))

    def test_omitted_flag_touches_no_archive_directory(self):
        args = self.parser.parse_args([
            "export", "all", "--types", "if_rules",
            "--output-directory", self.output_dir,
        ])
        result = args.func(args, None)
        self.assertTrue(result[0]["success"])
        self.assertIsNone(result[0]["archive_directory"])
        self.assertFalse(os.path.exists(self.archive_dir))

    def test_archive_copy_failure_marks_type_failed_without_aborting(self):
        # Pre-create the archive's destination filename AS A DIRECTORY, so
        # shutil.copyfile() reliably raises when writing if_rules.json
        # there, without touching anything in customLib/export_sites.
        os.makedirs(self.archive_dir, exist_ok=True)
        os.makedirs(os.path.join(self.archive_dir, "if_rules.json"), exist_ok=True)

        args = self.parser.parse_args([
            "export", "all", "--types", "if_rules,wf_rules",
            "--output-directory", self.output_dir,
            "--archive-directory", self.archive_dir,
        ])
        with self.assertRaises(SystemExit) as ctx:
            args.func(args, None)
        self.assertEqual(ctx.exception.code, 1)
        # Not aborted: wf_rules still ran (and archived) after if_rules's
        # archive-copy failure, which is not an access-denied condition.
        self.assertEqual(self.called, ["if_rules", "wf_rules"])
        self.assertTrue(os.path.isfile(os.path.join(self.archive_dir, "wf_rules.json")))


class ExportAllNoAccountSuffixTest(PreflightStubbedTestCase):
    """--no-account-suffix: strips the literal '_<accountID>' suffix from
    each type's produced filename before the extension; off by default;
    composes with --archive-directory (the archive basename is also
    unsuffixed, since archiving copies the already-renamed file)."""

    ACCOUNT_ID = "15412"

    def setUp(self):
        super().setUp()
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.output_dir = os.path.join(self.tmp.name, "config_data")
        os.makedirs(self.output_dir, exist_ok=True)
        self.archive_dir = os.path.join(self.tmp.name, "config_data_archive")

        # Stubs write a real file using the same account-suffixed naming
        # convention the real handlers use (all_<type>_<account_id>.json),
        # so the rename-based suffix stripping has a real suffix to strip.
        for name, sub_parser in self.registry.choices.items():
            if name == "all":
                continue
            sub_parser.set_defaults(func=self._make_suffixed_stub(name))

    def _make_suffixed_stub(self, name):
        def stub(args, configuration):
            self.called.append(name)
            if name == "groups":
                return [{"success": False, "error": "stub failure for groups"}]
            if name == "dia_rules":
                return [{"success": False, "error": self.ACCESS_DENIED_ERROR}]
            out_dir = getattr(args, "output_directory", None) or self.output_dir
            os.makedirs(out_dir, exist_ok=True)
            account_id = getattr(args, "accountID", None) or self.ACCOUNT_ID
            out_path = os.path.join(out_dir, f"all_{name}_{account_id}.json")
            with open(out_path, "w") as f:
                f.write(f'{{"type": "{name}"}}')
            return [{"success": True, "output_file": out_path}]
        return stub

    def test_flag_off_keeps_the_account_suffixed_filename(self):
        args = self.parser.parse_args([
            "export", "all", "--types", "if_rules",
            "-accountID", self.ACCOUNT_ID,
            "--output-directory", self.output_dir,
        ])
        result = args.func(args, None)
        self.assertTrue(result[0]["success"])
        expected = os.path.join(self.output_dir, f"all_if_rules_{self.ACCOUNT_ID}.json")
        self.assertTrue(os.path.isfile(expected))

    def test_flag_on_strips_the_literal_account_suffix(self):
        args = self.parser.parse_args([
            "export", "all", "--types", "if_rules,wf_rules",
            "-accountID", self.ACCOUNT_ID,
            "--output-directory", self.output_dir,
            "--no-account-suffix",
        ])
        result = args.func(args, None)
        self.assertTrue(result[0]["success"])
        for name in ("if_rules", "wf_rules"):
            stripped = os.path.join(self.output_dir, f"all_{name}.json")
            suffixed = os.path.join(self.output_dir, f"all_{name}_{self.ACCOUNT_ID}.json")
            self.assertTrue(os.path.isfile(stripped), f"missing {stripped}")
            self.assertFalse(os.path.exists(suffixed), f"leftover suffixed file {suffixed}")

    def test_flag_on_composes_with_archive_directory(self):
        args = self.parser.parse_args([
            "export", "all", "--types", "if_rules",
            "-accountID", self.ACCOUNT_ID,
            "--output-directory", self.output_dir,
            "--archive-directory", self.archive_dir,
            "--no-account-suffix",
        ])
        result = args.func(args, None)
        self.assertTrue(result[0]["success"])
        stripped_primary = os.path.join(self.output_dir, "all_if_rules.json")
        stripped_archive = os.path.join(self.archive_dir, "all_if_rules.json")
        self.assertTrue(os.path.isfile(stripped_primary))
        self.assertTrue(os.path.isfile(stripped_archive))
        # Archive basename must be the already-suffix-stripped name, not
        # the original account-suffixed one.
        self.assertFalse(
            os.path.exists(os.path.join(self.archive_dir, f"all_if_rules_{self.ACCOUNT_ID}.json"))
        )


if __name__ == "__main__":
    unittest.main()
