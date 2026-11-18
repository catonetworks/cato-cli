"""Unit tests for the Imperva/Incapsula WAF-challenge detection and
dedicated retry/backoff logic added to catocli.parsers.custom.customLib.

Context: during `catocli export all`, a rapid same-IP burst of sequential
accountSnapshot POSTs (one per site) tripped the Cato API edge's WAF
rate/bot heuristics, which returned an HTML challenge page ("/_Incapsula_
Resource?...", "Incapsula incident ID: ...") instead of GraphQL JSON. The
raw HTML then leaked into the exception message surfaced to the user.

This fix:
  - detects a WAF challenge page both when it arrives via a non-2xx status
    (raises ApiException whose body/message is the raw HTML), and when it
    arrives via a 2xx status (the GraphQL client's JSON decode silently
    falls back to the raw response bytes, so `response` isn't a dict), and
  - retries it with a dedicated exponential backoff + jitter schedule
    (WAF_RETRY_DELAYS = [2, 5, 12]) separate from the existing generic
    network-error retry budget, and
  - raises a clean, HTML-free error message (with the Incapsula incident ID
    extracted, if present) once retries are exhausted.

All tests here are fully offline: CallApi/ApiClient are monkeypatched to an
in-memory stub, and time.sleep / random.uniform are patched so the tests
run instantly and deterministically.
"""

import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from catocli.parsers.custom import customLib
from graphql_client.api_client import ApiException


INCAPSULA_INCIDENT_ID = "123000160052092904-432895730991301692"

INCAPSULA_HTML = (
    b'<html><body>'
    b'<iframe src="/_Incapsula_Resource?CWUDNSAI=9&incident_id=' + INCAPSULA_INCIDENT_ID.encode() + b'"></iframe>'
    b'Request unsuccessful. Incapsula incident ID: ' + INCAPSULA_INCIDENT_ID.encode() +
    b'</body></html>'
)


class FakeHttpResp:
    """Minimal stand-in for the urllib3-backed QUERYResponse object that
    ApiException(http_resp=...) reads status/reason/data/headers from."""

    def __init__(self, status, data, reason="Forbidden"):
        self.status = status
        self.reason = reason
        self.data = data

    def getheaders(self):
        return {}


class WafChallengeDetectionTest(unittest.TestCase):
    """Pure functions - no API client involved."""

    def test_is_waf_challenge_detects_known_markers(self):
        self.assertTrue(customLib._is_waf_challenge("... /_Incapsula_Resource?x=1 ..."))
        self.assertTrue(customLib._is_waf_challenge("Request unsuccessful. Incapsula incident ID: 123"))
        self.assertTrue(customLib._is_waf_challenge(INCAPSULA_HTML.decode()))

    def test_is_waf_challenge_false_for_ordinary_errors(self):
        self.assertFalse(customLib._is_waf_challenge("502 Bad Gateway"))
        self.assertFalse(customLib._is_waf_challenge("Connection timed out"))
        self.assertFalse(customLib._is_waf_challenge(""))
        self.assertFalse(customLib._is_waf_challenge(None))

    def test_extract_incident_id(self):
        text = "Request unsuccessful. Incapsula incident ID: " + INCAPSULA_INCIDENT_ID
        self.assertEqual(customLib._extract_incapsula_incident_id(text), INCAPSULA_INCIDENT_ID)

    def test_extract_incident_id_returns_none_when_absent(self):
        self.assertIsNone(customLib._extract_incapsula_incident_id("no incident info here"))
        self.assertIsNone(customLib._extract_incapsula_incident_id(""))
        self.assertIsNone(customLib._extract_incapsula_incident_id(None))

    def test_clean_error_message_strips_html_and_keeps_incident_id(self):
        msg = customLib._clean_waf_error_message(INCAPSULA_HTML.decode())
        self.assertNotIn("<html>", msg)
        self.assertNotIn("<iframe", msg)
        self.assertIn(INCAPSULA_INCIDENT_ID, msg)
        self.assertIn("Imperva/Incapsula", msg)
        self.assertIn("transient", msg)

    def test_clean_error_message_without_incident_id_is_still_readable(self):
        msg = customLib._clean_waf_error_message("_Incapsula_Resource but no incident id here")
        self.assertNotIn("<html>", msg)
        self.assertIn("Imperva/Incapsula", msg)


class MakeCallWafRetryTest(unittest.TestCase):
    def setUp(self):
        self.args = SimpleNamespace(verbose=False)
        self.configuration = SimpleNamespace()
        self.sleep_calls = []

        self.sleep_patcher = patch.object(customLib.time, "sleep", side_effect=self.sleep_calls.append)
        self.sleep_patcher.start()
        self.addCleanup(self.sleep_patcher.stop)

        self.uniform_patcher = patch.object(customLib.random, "uniform", return_value=0.0)
        self.uniform_patcher.start()
        self.addCleanup(self.uniform_patcher.stop)

    def _patch_api(self, side_effect):
        """Monkeypatch customLib's CallApi/ApiClient so makeCall() never
        touches the network; `side_effect` is handed straight to the fake
        CallApi instance's call_api() mock (list of return values and/or
        exceptions to raise, in call order)."""
        fake_instance = MagicMock()
        fake_instance.call_api.side_effect = side_effect

        api_client_patcher = patch.object(customLib, "ApiClient", return_value=MagicMock())
        call_api_patcher = patch.object(customLib, "CallApi", return_value=fake_instance)
        api_client_patcher.start()
        call_api_patcher.start()
        self.addCleanup(api_client_patcher.stop)
        self.addCleanup(call_api_patcher.stop)
        return fake_instance

    def test_retries_on_waf_challenge_via_non_2xx_then_succeeds(self):
        """Incapsula returning e.g. 403 raises ApiException whose body is
        the raw HTML - makeCall must retry (not immediately raise) and
        eventually return the successful GraphQL response."""
        waf_exc = ApiException(http_resp=FakeHttpResp(403, INCAPSULA_HTML))
        success_response = [{"data": {"ok": True}}]
        fake_instance = self._patch_api([waf_exc, waf_exc, success_response])

        result = customLib.makeCall(self.args, self.configuration, {"query": "..."})

        self.assertEqual(result, {"data": {"ok": True}})
        self.assertEqual(fake_instance.call_api.call_count, 3)
        # Two WAF retries consumed -> backoff before retry 1 and retry 2,
        # using WAF_RETRY_DELAYS[0] and WAF_RETRY_DELAYS[1] (jitter=0 here).
        self.assertEqual(self.sleep_calls, customLib.WAF_RETRY_DELAYS[:2])

    def test_retries_on_waf_challenge_via_2xx_html_body_then_succeeds(self):
        """A WAF challenge returned with a 2xx status doesn't raise
        ApiException - the response comes back as raw bytes instead of a
        dict (see deserialize()'s json.loads ValueError fallback). makeCall
        must detect that case too."""
        success_response = [{"data": {"ok": True}}]
        fake_instance = self._patch_api([[INCAPSULA_HTML], success_response])

        result = customLib.makeCall(self.args, self.configuration, {"query": "..."})

        self.assertEqual(result, {"data": {"ok": True}})
        self.assertEqual(fake_instance.call_api.call_count, 2)
        self.assertEqual(self.sleep_calls, customLib.WAF_RETRY_DELAYS[:1])

    def test_raises_clean_message_with_no_html_after_exhausting_waf_retries(self):
        waf_exc = ApiException(http_resp=FakeHttpResp(403, INCAPSULA_HTML))
        fake_instance = self._patch_api([waf_exc, waf_exc, waf_exc, waf_exc])

        with self.assertRaises(Exception) as ctx:
            customLib.makeCall(self.args, self.configuration, {"query": "..."})

        message = str(ctx.exception)
        self.assertNotIn("<html>", message)
        self.assertNotIn("<iframe", message)
        self.assertNotIn("_Incapsula_Resource", message)
        self.assertIn("Imperva/Incapsula", message)
        self.assertIn(INCAPSULA_INCIDENT_ID, message)

        # 1 initial attempt + len(WAF_RETRY_DELAYS) retries, all exhausted.
        self.assertEqual(fake_instance.call_api.call_count, 1 + len(customLib.WAF_RETRY_DELAYS))
        self.assertEqual(self.sleep_calls, customLib.WAF_RETRY_DELAYS)

    def test_debug_mode_prints_raw_html_but_default_mode_does_not(self):
        waf_exc = ApiException(http_resp=FakeHttpResp(403, INCAPSULA_HTML))
        success_response = [{"data": {"ok": True}}]

        # Default (CATO_DEBUG unset): raw HTML must not be printed.
        self._patch_api([waf_exc, success_response])
        with patch.dict(customLib.os.environ, {}, clear=False):
            customLib.os.environ.pop("CATO_DEBUG", None)
            with patch("builtins.print") as mock_print:
                customLib.makeCall(self.args, self.configuration, {"query": "..."})
        printed = "\n".join(str(call.args[0]) for call in mock_print.call_args_list if call.args)
        self.assertNotIn("<html>", printed)
        self.assertNotIn("_Incapsula_Resource", printed)
        self.assertIn("WARNING: Cato API edge (Imperva/Incapsula) challenge received", printed)
        self.assertIn(INCAPSULA_INCIDENT_ID, printed)  # incident ID is fine to show - it's not HTML
        self.assertIn("retrying in", printed)

    def test_debug_mode_prints_raw_html(self):
        waf_exc = ApiException(http_resp=FakeHttpResp(403, INCAPSULA_HTML))
        success_response = [{"data": {"ok": True}}]
        self._patch_api([waf_exc, success_response])

        with patch.dict(customLib.os.environ, {"CATO_DEBUG": "True"}):
            with patch("builtins.print") as mock_print:
                customLib.makeCall(self.args, self.configuration, {"query": "..."})
        printed = "\n".join(str(call.args[0]) for call in mock_print.call_args_list if call.args)
        self.assertIn("_Incapsula_Resource", printed)

    def test_generic_retryable_network_error_uses_its_own_budget_and_delays(self):
        """Non-WAF transient errors (timeout/502/503/rate limit) must keep
        working exactly as before - a separate retry budget/schedule from
        the WAF-specific one."""
        timeout_exc = ApiException(status=0, reason="Read timed out")
        success_response = [{"data": {"ok": True}}]
        fake_instance = self._patch_api([timeout_exc, success_response])

        result = customLib.makeCall(self.args, self.configuration, {"query": "..."})

        self.assertEqual(result, {"data": {"ok": True}})
        self.assertEqual(fake_instance.call_api.call_count, 2)
        self.assertEqual(self.sleep_calls, [15])  # generic retry_delays[1], not a WAF delay

    def test_non_retryable_error_raises_immediately_without_sleeping(self):
        err = ApiException(status=400, reason="Bad Request")
        fake_instance = self._patch_api([err])

        with self.assertRaises(Exception):
            customLib.makeCall(self.args, self.configuration, {"query": "..."})

        self.assertEqual(fake_instance.call_api.call_count, 1)
        self.assertEqual(self.sleep_calls, [])


if __name__ == "__main__":
    unittest.main()
