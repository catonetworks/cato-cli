"""Tests for catocli_user_guide/examples/auditfeed_incremental.py.

Covers:
- parse_retry_after: delay-seconds, HTTP-date (future/past), missing/garbage forms
- record_identity: flatFields-order stability, distinctness, determinism
- extract_records: single/multi-account, empty input
- graphql_call_with_retries: numeric Retry-After, HTTP-date Retry-After,
  exponential fallback, max-retries bound, non-retryable status, counter increment
- Integration (via mocked graphql_call_with_retries):
  - boundary duplicate suppressed across runs and across restarts
  - mixed duplicate and new records: only new emitted
  - time-frame change resets marker and seenHashes
  - no-progress guard breaks inner loop and writes to stderr
  - run-once exits after drain; paginates until hasMore=false
  - state persisted after each page
  - seenHashes bounded to MAX_SEEN_HASHES
"""
from __future__ import annotations

import email.utils
import importlib.util
import io
import urllib.error
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import pytest

# ── load the standalone script as a module ────────────────────────────────────
_SCRIPT = (
    Path(__file__).parent.parent
    / "catocli_user_guide"
    / "examples"
    / "auditfeed_incremental.py"
)
_spec = importlib.util.spec_from_file_location("auditfeed_incremental", _SCRIPT)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

parse_retry_after = _mod.parse_retry_after
record_identity = _mod.record_identity
extract_records = _mod.extract_records
load_state = _mod.load_state
save_state = _mod.save_state
MAX_SEEN_HASHES = _mod.MAX_SEEN_HASHES


# ── shared test helpers ───────────────────────────────────────────────────────

def _make_response(
    marker: str,
    has_more: bool,
    raw_records: list[dict],
    account_id: str = "12345",
) -> dict:
    """Minimal valid auditFeed GraphQL response."""
    return {
        "data": {
            "auditFeed": {
                "marker": marker,
                "hasMore": has_more,
                "fetchedCount": len(raw_records),
                "from": "2026-06-17T00:00:00Z",
                "to": "2026-06-18T00:00:00Z",
                "accounts": [{"id": account_id, "records": raw_records}],
            }
        }
    }


class FakeHTTPError(urllib.error.HTTPError):
    """urllib.error.HTTPError subclass that avoids complex file-pointer setup."""

    def __init__(self, code: int, retry_after: str | None = None, body: bytes = b"error"):
        self.code = code
        self._body = body
        self.headers = {"Retry-After": retry_after} if retry_after is not None else {}

    def read(self) -> bytes:
        return self._body


def _run_main(
    responses: list[dict],
    state_file: Path,
    extra_args: list[str] | None = None,
    time_frame: str = "last.P1D",
) -> tuple[list[dict], str]:
    """Run main() with --run-once using mocked API.

    Returns (emitted_records, stderr_text).
    graphql_call_with_retries and process_batch are both patched so no real
    network call or stdout write happens.
    """
    responses_iter = iter(responses)
    emitted: list[dict] = []
    stderr_buf = io.StringIO()

    def fake_call(endpoint, token, query, variables, max_retries):
        return next(responses_iter)

    def fake_process_batch(records):
        emitted.extend(records)

    argv = [
        "auditfeed_incremental.py",
        "--token", "fake-token",
        "--account-id", "12345",
        "--time-frame", time_frame,
        "--state-file", str(state_file),
        "--run-once",
    ] + (extra_args or [])

    with (
        patch.object(_mod, "graphql_call_with_retries", fake_call),
        patch.object(_mod, "process_batch", fake_process_batch),
        patch.object(_mod.time, "sleep"),
        patch("sys.argv", argv),
        patch("sys.stderr", stderr_buf),
    ):
        _mod.main()

    return emitted, stderr_buf.getvalue()


# ── parse_retry_after ─────────────────────────────────────────────────────────

class TestParseRetryAfter:
    def test_delay_seconds(self):
        assert parse_retry_after("120") == 120.0

    def test_delay_seconds_with_whitespace(self):
        assert parse_retry_after("  45 ") == 45.0

    def test_delay_zero(self):
        assert parse_retry_after("0") == 0.0

    def test_negative_delay_clamped_to_zero(self):
        assert parse_retry_after("-10") == 0.0

    def test_http_date_future(self):
        future = datetime.now(timezone.utc) + timedelta(seconds=60)
        result = parse_retry_after(email.utils.format_datetime(future))
        assert result is not None
        assert 55.0 <= result <= 65.0

    def test_http_date_past_clamped_to_zero(self):
        past = datetime.now(timezone.utc) - timedelta(seconds=60)
        assert parse_retry_after(email.utils.format_datetime(past)) == 0.0

    def test_garbage_returns_none(self):
        assert parse_retry_after("not-a-valid-value") is None

    def test_none_returns_none(self):
        assert parse_retry_after(None) is None

    def test_empty_string_returns_none(self):
        assert parse_retry_after("") is None


# ── record_identity ───────────────────────────────────────────────────────────

class TestRecordIdentity:
    _BASE = {
        "account_id": "12345",
        "time": "2026-06-17T12:54:41Z",
        "fieldsMap": {"admin": "alice", "change_type": "MODIFIED"},
        "flatFields": [["change_type", "MODIFIED"], ["admin", "alice"]],
    }

    def test_stable_across_flatfields_order(self):
        r1 = {**self._BASE, "flatFields": [["admin", "alice"], ["change_type", "MODIFIED"]]}
        r2 = {**self._BASE, "flatFields": [["change_type", "MODIFIED"], ["admin", "alice"]]}
        assert record_identity(r1) == record_identity(r2)

    def test_different_content_gives_different_hash(self):
        r1 = self._BASE
        r2 = {**self._BASE, "time": "2026-06-17T13:00:00Z"}
        assert record_identity(r1) != record_identity(r2)

    def test_deterministic_on_repeated_calls(self):
        assert record_identity(self._BASE) == record_identity(self._BASE)

    def test_handles_none_flatfields(self):
        r = {**self._BASE, "flatFields": None}
        h = record_identity(r)
        assert isinstance(h, str) and len(h) == 64


# ── extract_records ───────────────────────────────────────────────────────────

class TestExtractRecords:
    def test_single_account_single_record(self):
        feed = {
            "accounts": [{
                "id": "12345",
                "records": [{"time": "t1", "fieldsMap": {"a": "1"}, "flatFields": None}],
            }]
        }
        out = extract_records(feed)
        assert len(out) == 1
        assert out[0] == {
            "account_id": "12345",
            "time": "t1",
            "fieldsMap": {"a": "1"},
            "flatFields": None,
        }

    def test_multiple_accounts(self):
        feed = {
            "accounts": [
                {"id": "111", "records": [{"time": "t1", "fieldsMap": {}, "flatFields": None}]},
                {"id": "222", "records": [{"time": "t2", "fieldsMap": {}, "flatFields": None}]},
            ]
        }
        out = extract_records(feed)
        assert {r["account_id"] for r in out} == {"111", "222"}

    def test_empty_accounts_list(self):
        assert extract_records({"accounts": []}) == []

    def test_missing_accounts_key(self):
        assert extract_records({}) == []


# ── graphql_call_with_retries ─────────────────────────────────────────────────

class TestGraphqlCallWithRetries:
    def test_numeric_retry_after_honored(self, monkeypatch):
        slept: list[float] = []
        calls = [0]

        def fake_call(*_):
            if calls[0] == 0:
                calls[0] += 1
                raise FakeHTTPError(429, retry_after="10")
            return {"data": {}}

        monkeypatch.setattr(_mod, "graphql_call", fake_call)
        monkeypatch.setattr(_mod.time, "sleep", slept.append)

        _mod.graphql_call_with_retries("ep", "tok", "q", {}, max_retries=3)
        assert slept == [10.0]

    def test_http_date_retry_after_honored(self, monkeypatch):
        slept: list[float] = []
        calls = [0]
        future = datetime.now(timezone.utc) + timedelta(seconds=30)
        header = email.utils.format_datetime(future)

        def fake_call(*_):
            if calls[0] == 0:
                calls[0] += 1
                raise FakeHTTPError(429, retry_after=header)
            return {"data": {}}

        monkeypatch.setattr(_mod, "graphql_call", fake_call)
        monkeypatch.setattr(_mod.time, "sleep", slept.append)

        _mod.graphql_call_with_retries("ep", "tok", "q", {}, max_retries=3)
        assert len(slept) == 1
        assert 25.0 <= slept[0] <= 35.0

    def test_missing_retry_after_falls_back_to_exponential_backoff(self, monkeypatch):
        slept: list[float] = []
        calls = [0]

        def fake_call(*_):
            if calls[0] < 2:
                calls[0] += 1
                raise FakeHTTPError(429)
            return {"data": {}}

        monkeypatch.setattr(_mod, "graphql_call", fake_call)
        monkeypatch.setattr(_mod.time, "sleep", slept.append)

        _mod.graphql_call_with_retries("ep", "tok", "q", {}, max_retries=3)
        assert slept == [1.0, 2.0]  # min(2**0, 30), min(2**1, 30)

    def test_raises_after_max_retries_exceeded(self, monkeypatch):
        def always_fail(*_):
            raise FakeHTTPError(500)

        monkeypatch.setattr(_mod, "graphql_call", always_fail)
        monkeypatch.setattr(_mod.time, "sleep", lambda _: None)

        with pytest.raises(RuntimeError, match="HTTP 500"):
            _mod.graphql_call_with_retries("ep", "tok", "q", {}, max_retries=2)

    def test_non_retryable_status_raises_immediately(self, monkeypatch):
        called = [0]

        def fail_with_400(*_):
            called[0] += 1
            raise FakeHTTPError(400)

        monkeypatch.setattr(_mod, "graphql_call", fail_with_400)
        monkeypatch.setattr(_mod.time, "sleep", lambda _: None)

        with pytest.raises(RuntimeError, match="HTTP 400"):
            _mod.graphql_call_with_retries("ep", "tok", "q", {}, max_retries=5)
        assert called[0] == 1  # no retries attempted

    def test_retry_counter_increments_on_every_retry_path(self, monkeypatch):
        """Each retry must increment the counter so --max-retries is always reachable."""
        calls = [0]

        def fail_three_times(*_):
            calls[0] += 1
            if calls[0] <= 3:
                raise FakeHTTPError(503)
            return {"data": {}}

        monkeypatch.setattr(_mod, "graphql_call", fail_three_times)
        monkeypatch.setattr(_mod.time, "sleep", lambda _: None)

        _mod.graphql_call_with_retries("ep", "tok", "q", {}, max_retries=5)
        assert calls[0] == 4  # 3 failures + 1 success


# ── integration: deduplication ────────────────────────────────────────────────

class TestBoundaryDuplicate:
    def test_boundary_record_suppressed_on_second_run(self, tmp_path):
        state_file = tmp_path / "state.json"
        rec_a = {"time": "t1", "fieldsMap": {"k": "A"}, "flatFields": None}
        rec_b = {"time": "t2", "fieldsMap": {"k": "B"}, "flatFields": None}

        # First run: both emitted
        emitted1, _ = _run_main([_make_response("M1", False, [rec_a, rec_b])], state_file)
        assert len(emitted1) == 2

        # Second run: API re-returns B at the boundary → must be suppressed
        emitted2, _ = _run_main([_make_response("M1", False, [rec_b])], state_file)
        assert emitted2 == []

    def test_boundary_record_suppressed_across_process_restarts(self, tmp_path):
        state_file = tmp_path / "state.json"
        rec = {"time": "t1", "fieldsMap": {"k": "A"}, "flatFields": None}

        _run_main([_make_response("M1", False, [rec])], state_file)

        # Simulate process restart with same state file
        emitted, _ = _run_main([_make_response("M1", False, [rec])], state_file)
        assert emitted == []


class TestMixedDuplicateAndNew:
    def test_only_new_record_emitted(self, tmp_path):
        state_file = tmp_path / "state.json"
        rec_b = {"time": "t2", "fieldsMap": {"k": "B"}, "flatFields": None}
        rec_c = {"time": "t3", "fieldsMap": {"k": "C"}, "flatFields": None}

        # First run: emit B, persist its hash
        _run_main([_make_response("M1", False, [rec_b])], state_file)

        # Second run: [B, C] → only C is new
        emitted, _ = _run_main([_make_response("M2", False, [rec_b, rec_c])], state_file)
        assert len(emitted) == 1
        assert emitted[0]["fieldsMap"]["k"] == "C"


# ── integration: time-frame reset ─────────────────────────────────────────────

class TestTimeFrameChange:
    def test_marker_and_hashes_reset_when_timeframe_changes(self, tmp_path):
        state_file = tmp_path / "state.json"
        rec = {"time": "t1", "fieldsMap": {"k": "A"}, "flatFields": None}

        # First run with last.P1D
        _run_main([_make_response("M1", False, [rec])], state_file)
        state = load_state(state_file)
        assert state["marker"] == "M1"
        assert len(state["seenHashes"]) == 1

        # Second run with a different time frame: marker and hashes must reset
        seen_marker_sent = []
        responses_iter = iter([_make_response("M2", False, [rec])])

        def fake_call(endpoint, token, query, variables, max_retries):
            seen_marker_sent.append(variables["marker"])
            return next(responses_iter)

        with (
            patch.object(_mod, "graphql_call_with_retries", fake_call),
            patch.object(_mod, "process_batch", lambda _: None),
            patch.object(_mod.time, "sleep"),
            patch("sys.argv", [
                "auditfeed_incremental.py",
                "--token", "fake-token",
                "--account-id", "12345",
                "--time-frame", "last.PT1H",
                "--state-file", str(state_file),
                "--run-once",
            ]),
            patch("sys.stderr", io.StringIO()),
        ):
            _mod.main()

        # Marker must have been sent as "" because the time frame changed
        assert seen_marker_sent == [""]

        # The record should be re-emitted (seenHashes was reset)
        new_state = load_state(state_file)
        assert new_state["timeFrame"] == "last.PT1H"
        assert new_state["marker"] == "M2"


# ── integration: no-progress guard ────────────────────────────────────────────

class TestNoProgressStop:
    def test_breaks_inner_loop_when_marker_stalls(self, tmp_path):
        state_file = tmp_path / "state.json"
        save_state(state_file, {
            "accountID": "12345",
            "timeFrame": "last.P1D",
            "marker": "M_STUCK",
            "seenHashes": [],
        })
        rec = {"time": "t1", "fieldsMap": {"k": "A"}, "flatFields": None}

        # API returns the same marker it received, but hasMore=True
        emitted, stderr = _run_main([_make_response("M_STUCK", True, [rec])], state_file)

        # The new record is still emitted (it wasn't in seenHashes)
        assert len(emitted) == 1
        # The no-progress notice must go to stderr
        assert "marker" in stderr.lower() or "advance" in stderr.lower()

    def test_no_second_api_call_after_stall(self, tmp_path):
        state_file = tmp_path / "state.json"
        save_state(state_file, {
            "accountID": "12345",
            "timeFrame": "last.P1D",
            "marker": "STUCK",
            "seenHashes": [],
        })

        call_count = [0]

        def counting_fake_call(endpoint, token, query, variables, max_retries):
            call_count[0] += 1
            return _make_response("STUCK", True, [])

        with (
            patch.object(_mod, "graphql_call_with_retries", counting_fake_call),
            patch.object(_mod, "process_batch", lambda _: None),
            patch.object(_mod.time, "sleep"),
            patch("sys.argv", [
                "auditfeed_incremental.py",
                "--token", "tok", "--account-id", "12345",
                "--time-frame", "last.P1D",
                "--state-file", str(state_file),
                "--run-once",
            ]),
            patch("sys.stderr", io.StringIO()),
        ):
            _mod.main()

        assert call_count[0] == 1


# ── integration: pagination and state ─────────────────────────────────────────

class TestPaginationAndState:
    def test_run_once_exits_after_drain(self, tmp_path):
        state_file = tmp_path / "state.json"
        rec = {"time": "t1", "fieldsMap": {"k": "A"}, "flatFields": None}
        emitted, _ = _run_main([_make_response("M1", False, [rec])], state_file)
        assert len(emitted) == 1
        assert load_state(state_file)["marker"] == "M1"

    def test_paginates_through_all_pages(self, tmp_path):
        state_file = tmp_path / "state.json"
        rec_a = {"time": "t1", "fieldsMap": {"k": "A"}, "flatFields": None}
        rec_b = {"time": "t2", "fieldsMap": {"k": "B"}, "flatFields": None}
        responses = [
            _make_response("M1", True, [rec_a]),   # hasMore → continue
            _make_response("M2", False, [rec_b]),  # drained → stop
        ]
        emitted, _ = _run_main(responses, state_file)
        assert len(emitted) == 2
        assert load_state(state_file)["marker"] == "M2"

    def test_state_persisted_after_first_page(self, tmp_path):
        """Marker must be saved after each page, not only after the full drain."""
        state_file = tmp_path / "state.json"
        rec_a = {"time": "t1", "fieldsMap": {"k": "A"}, "flatFields": None}
        rec_b = {"time": "t2", "fieldsMap": {"k": "B"}, "flatFields": None}

        marker_seen_on_second_call = []
        responses_iter = iter([
            _make_response("M1", True, [rec_a]),
            _make_response("M2", False, [rec_b]),
        ])

        def stateful_fake_call(endpoint, token, query, variables, max_retries):
            resp = next(responses_iter)
            # On the second call the state file should already hold M1
            if variables["marker"] == "M1":
                marker_seen_on_second_call.append(load_state(state_file).get("marker"))
            return resp

        with (
            patch.object(_mod, "graphql_call_with_retries", stateful_fake_call),
            patch.object(_mod, "process_batch", lambda _: None),
            patch.object(_mod.time, "sleep"),
            patch("sys.argv", [
                "auditfeed_incremental.py",
                "--token", "tok", "--account-id", "12345",
                "--time-frame", "last.P1D",
                "--state-file", str(state_file),
                "--run-once",
            ]),
            patch("sys.stderr", io.StringIO()),
        ):
            _mod.main()

        assert marker_seen_on_second_call == ["M1"]

    def test_seen_hashes_bounded_to_max(self, tmp_path):
        state_file = tmp_path / "state.json"
        # Pre-fill to just below the cap
        existing = [f"hash{i:05d}" for i in range(MAX_SEEN_HASHES - 1)]
        save_state(state_file, {
            "accountID": "12345",
            "timeFrame": "last.P1D",
            "marker": "M0",
            "seenHashes": existing,
        })

        # Add 3 new records in one response (pushes total to MAX + 2)
        new_recs = [
            {"time": f"t{i}", "fieldsMap": {"k": str(i)}, "flatFields": None}
            for i in range(3)
        ]
        _run_main([_make_response("M1", False, new_recs)], state_file)

        state = load_state(state_file)
        assert len(state["seenHashes"]) == MAX_SEEN_HASHES
