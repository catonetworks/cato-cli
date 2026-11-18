"""Offline tests for Imperva/Incapsula WAF-challenge handling in the generic
`catocli query ...` / `catocli mutation ...` driver path.

Context: catocli.parsers.custom.customLib.makeCall (the custom-export call
path) already detects and retries a WAF challenge page cleanly (see
tests/test_customlib_waf_retry.py). This file covers the OTHER, much more
commonly used path: catocli.parsers.customParserApiClient.createRequest -
the function every plain `catocli query <op> ...` / `catocli mutation <op>
...` invocation runs through. Before this fix, createRequest's
`except ApiException as e: return e` let a raw Incapsula HTML challenge
page reach catocli.Utils.clidriver's `print(response)` untouched.

The fix wraps createRequest's single `instance.call_api(...)` call with the
shared catocli.Utils.waf_detect.call_with_waf_retry() helper - the same
detection markers, backoff schedule (2s/5s/12s with jitter), and one-line
warning wording used everywhere else in catocli - covering both ways a WAF
challenge can arrive:
  - a non-2xx status (commonly 403), raising ApiException whose body IS
    the raw HTML page, and
  - a 2xx status whose body is the HTML page instead of JSON.

These tests are fully offline: CallApi/ApiClient and the operation-model/
GraphQL-payload machinery are all monkeypatched to in-memory stubs. time.sleep
and random.uniform are patched so tests run instantly and deterministically.
"""

import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from catocli.parsers import customParserApiClient
from catocli.Utils import waf_detect
from graphql_client.api_client import ApiException


INCAPSULA_INCIDENT_ID = "123000160052092904-432895730991301692"

INCAPSULA_HTML = (
    b'<html><body>'
    b'<iframe src="/_Incapsula_Resource?CWUDNSAI=9"></iframe>'
    b'Request unsuccessful. Incapsula incident ID: ' + INCAPSULA_INCIDENT_ID.encode() +
    b'</body></html>'
)


class FakeHttpResp:
    """Minimal stand-in for the urllib3-backed response object that
    ApiException(http_resp=...) reads status/reason/data/headers from."""

    def __init__(self, status, data, reason="Forbidden"):
        self.status = status
        self.reason = reason
        self.data = data

    def getheaders(self):
        return {}


class CreateRequestWafRetryTest(unittest.TestCase):
    def setUp(self):
        self.args = SimpleNamespace(
            operation_name="query.test.op",
            t=False,
            skip_validation=True,   # bypass validateArgs - not under test here
            raw_output=True,        # forces the simplest (raw) response-formatting branch
        )
        self.configuration = SimpleNamespace(accountID="12345")

        self.sleep_calls = []
        self.sleep_patcher = patch.object(waf_detect.time, "sleep", side_effect=self.sleep_calls.append)
        self.sleep_patcher.start()
        self.addCleanup(self.sleep_patcher.stop)

        self.uniform_patcher = patch.object(waf_detect.random, "uniform", return_value=0.0)
        self.uniform_patcher.start()
        self.addCleanup(self.uniform_patcher.stop)

        # Stub out the operation-model / GraphQL-payload machinery so this
        # test exercises only the API-call + WAF-retry path, not the real
        # schema introspection/rendering pipeline.
        def fake_load_json(path):
            if path.endswith("clisettings.json"):
                return {}
            return {"operationArgs": {}}

        self.load_json_patcher = patch.object(customParserApiClient, "loadJSON", side_effect=fake_load_json)
        self.load_json_patcher.start()
        self.addCleanup(self.load_json_patcher.stop)

        self.payload_patcher = patch.object(
            customParserApiClient,
            "generateGraphqlPayload",
            return_value={"query": "query test { x }", "variables": {}, "operationName": "test"},
        )
        self.payload_patcher.start()
        self.addCleanup(self.payload_patcher.stop)

    def _patch_api(self, side_effect):
        fake_instance = MagicMock()
        fake_instance.call_api.side_effect = side_effect

        api_client_patcher = patch.object(customParserApiClient, "ApiClient", return_value=MagicMock())
        call_api_patcher = patch.object(customParserApiClient, "CallApi", return_value=fake_instance)
        api_client_patcher.start()
        call_api_patcher.start()
        self.addCleanup(api_client_patcher.stop)
        self.addCleanup(call_api_patcher.stop)
        return fake_instance

    def test_403_html_challenge_retries_then_succeeds_with_no_html_in_output(self):
        waf_exc = ApiException(http_resp=FakeHttpResp(403, INCAPSULA_HTML))
        success_response = [{"data": {"ok": True}}, 200, {}]
        fake_instance = self._patch_api([waf_exc, success_response])

        with patch("builtins.print") as mock_print:
            result = customParserApiClient.createRequest(self.args, self.configuration)

        self.assertEqual(result, {"data": {"ok": True}})
        self.assertEqual(fake_instance.call_api.call_count, 2)
        self.assertEqual(self.sleep_calls, waf_detect.WAF_RETRY_DELAYS[:1])

        printed = "\n".join(str(c.args[0]) for c in mock_print.call_args_list if c.args)
        self.assertNotIn("<html", printed.lower())
        self.assertNotIn("_Incapsula_Resource", printed)
        self.assertIn("WARNING: Cato API edge (Imperva/Incapsula) challenge received", printed)
        self.assertIn(INCAPSULA_INCIDENT_ID, printed)  # incident ID is fine to show - it's not HTML
        self.assertIn("retrying in", printed)

    def test_200_html_body_challenge_retries_then_succeeds_with_no_html_in_output(self):
        """A WAF challenge riding a 2xx status never raises ApiException -
        the response body is just the HTML page instead of JSON."""
        success_response = [{"data": {"ok": True}}, 200, {}]
        fake_instance = self._patch_api([[INCAPSULA_HTML, 200, {}], success_response])

        with patch("builtins.print") as mock_print:
            result = customParserApiClient.createRequest(self.args, self.configuration)

        self.assertEqual(result, {"data": {"ok": True}})
        self.assertEqual(fake_instance.call_api.call_count, 2)

        printed = "\n".join(str(c.args[0]) for c in mock_print.call_args_list if c.args)
        self.assertNotIn("<html", printed.lower())
        self.assertNotIn("_Incapsula_Resource", printed)
        self.assertIn("WARNING: Cato API edge (Imperva/Incapsula) challenge received", printed)

    def test_exhausted_waf_retries_return_clean_apiexception_with_no_html(self):
        waf_exc = ApiException(http_resp=FakeHttpResp(403, INCAPSULA_HTML))
        fake_instance = self._patch_api([waf_exc, waf_exc, waf_exc, waf_exc])

        with patch("builtins.print") as mock_print:
            result = customParserApiClient.createRequest(self.args, self.configuration)

        self.assertIsInstance(result, ApiException)
        message = str(result)
        self.assertNotIn("<html", message.lower())
        self.assertNotIn("_Incapsula_Resource", message)
        self.assertIn("Imperva/Incapsula", message)
        self.assertIn(INCAPSULA_INCIDENT_ID, message)

        # 1 initial attempt + len(WAF_RETRY_DELAYS) retries, all exhausted.
        self.assertEqual(fake_instance.call_api.call_count, 1 + len(waf_detect.WAF_RETRY_DELAYS))

        printed = "\n".join(str(c.args[0]) for c in mock_print.call_args_list if c.args)
        self.assertNotIn("<html", printed.lower())
        self.assertNotIn("_Incapsula_Resource", printed)

    def test_debug_mode_prints_raw_html_default_mode_does_not(self):
        waf_exc = ApiException(http_resp=FakeHttpResp(403, INCAPSULA_HTML))
        success_response = [{"data": {"ok": True}}, 200, {}]

        # Default (CATO_DEBUG unset): no raw HTML anywhere in output.
        self._patch_api([waf_exc, success_response])
        with patch.dict(waf_detect.os.environ, {}, clear=False):
            waf_detect.os.environ.pop("CATO_DEBUG", None)
            with patch("builtins.print") as mock_print:
                customParserApiClient.createRequest(self.args, self.configuration)
        printed_default = "\n".join(str(c.args[0]) for c in mock_print.call_args_list if c.args)
        self.assertNotIn("<html", printed_default.lower())
        self.assertNotIn("_Incapsula_Resource", printed_default)

        # CATO_DEBUG set: raw HTML is now allowed in the debug line.
        self._patch_api([waf_exc, success_response])
        with patch.dict(waf_detect.os.environ, {"CATO_DEBUG": "True"}):
            with patch("builtins.print") as mock_print:
                customParserApiClient.createRequest(self.args, self.configuration)
        printed_debug = "\n".join(str(c.args[0]) for c in mock_print.call_args_list if c.args)
        self.assertIn("_Incapsula_Resource", printed_debug)


if __name__ == "__main__":
    unittest.main()
