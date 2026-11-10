"""Offline tests for the remaining direct-API-client call paths that can
receive an Imperva/Incapsula WAF challenge page: configure's credential
test, the Terraform-import auth pre-flight check, and the SCIM client.

See tests/test_customlib_waf_retry.py (customLib.makeCall) and
tests/test_generic_driver_waf_retry.py (the generic query/mutation driver)
for the other two call paths covered by this same fix. All four, plus
clidriver.py's defense-in-depth print guard, now share detection/cleaning/
retry-schedule/warning-wording from catocli.Utils.waf_detect.

Fully offline: network clients are monkeypatched to in-memory stubs; time.sleep
and random.uniform are patched for deterministic, instant tests.
"""

import io
import unittest
import urllib.error
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from catocli.parsers.configure import configure
from catocli.parsers.custom.import_sites_to_tf import import_sites_to_tf
from catocli.parsers.custom.scim.scim_client import CatoSCIMClient
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
    def __init__(self, status, data, reason="Forbidden"):
        self.status = status
        self.reason = reason
        self.data = data

    def getheaders(self):
        return {}


class _WafOfflineTestBase(unittest.TestCase):
    """Shared no-sleep/no-jitter setup for every test in this file."""

    def setUp(self):
        self.sleep_calls = []
        self.sleep_patcher = patch.object(waf_detect.time, "sleep", side_effect=self.sleep_calls.append)
        self.sleep_patcher.start()
        self.addCleanup(self.sleep_patcher.stop)

        self.uniform_patcher = patch.object(waf_detect.random, "uniform", return_value=0.0)
        self.uniform_patcher.start()
        self.addCleanup(self.uniform_patcher.stop)


class ConfigureTestCredentialsWafTest(_WafOfflineTestBase):
    def _patch_api(self, side_effect):
        fake_instance = MagicMock()
        fake_instance.call_api.side_effect = side_effect
        api_client_patcher = patch.object(configure, "ApiClient", return_value=MagicMock())
        call_api_patcher = patch.object(configure, "CallApi", return_value=fake_instance)
        api_client_patcher.start()
        call_api_patcher.start()
        self.addCleanup(api_client_patcher.stop)
        self.addCleanup(call_api_patcher.stop)
        return fake_instance

    def test_waf_challenge_retries_then_validates_successfully(self):
        waf_exc = ApiException(http_resp=FakeHttpResp(403, INCAPSULA_HTML))
        success_response = [{"data": {"entityLookup": {"items": []}}}, 200, {}]
        fake_instance = self._patch_api([waf_exc, success_response])

        with patch("builtins.print"):
            is_valid, message = configure.test_credentials("https://api.example.com", "tok", "15412")

        self.assertTrue(is_valid)
        self.assertEqual(fake_instance.call_api.call_count, 2)

    def test_exhausted_waf_challenge_is_not_mislabeled_as_access_denied(self):
        """A persistent Incapsula 403 must not be reported as 'Access
        denied - check account ID and permissions' - that would send an
        operator chasing the wrong problem."""
        waf_exc = ApiException(http_resp=FakeHttpResp(403, INCAPSULA_HTML))
        fake_instance = self._patch_api([waf_exc, waf_exc, waf_exc, waf_exc])

        with patch("builtins.print"):
            is_valid, message = configure.test_credentials("https://api.example.com", "tok", "15412")

        self.assertFalse(is_valid)
        self.assertNotIn("<html", message.lower())
        self.assertNotIn("_Incapsula_Resource", message)
        self.assertNotIn("Access denied", message)
        self.assertIn("Imperva/Incapsula", message)
        self.assertIn(INCAPSULA_INCIDENT_ID, message)
        self.assertEqual(fake_instance.call_api.call_count, 1 + len(waf_detect.WAF_RETRY_DELAYS))


class ImportSitesAuthWafTest(_WafOfflineTestBase):
    def _patch_api(self, side_effect):
        fake_instance = MagicMock()
        fake_instance.call_api.side_effect = side_effect
        api_client_patcher = patch.object(import_sites_to_tf, "ApiClient", return_value=MagicMock())
        call_api_patcher = patch.object(import_sites_to_tf, "CallApi", return_value=fake_instance)
        api_client_patcher.start()
        call_api_patcher.start()
        self.addCleanup(api_client_patcher.stop)
        self.addCleanup(call_api_patcher.stop)
        return fake_instance

    def test_waf_challenge_retries_then_validates_successfully(self):
        waf_exc = ApiException(http_resp=FakeHttpResp(403, INCAPSULA_HTML))
        success_response = [
            {"data": {"entityLookup": {"items": [], "total": 0}}},
            200,
            {},
        ]
        fake_instance = self._patch_api([waf_exc, success_response])
        configuration = SimpleNamespace(accountID="15412")

        with patch("builtins.print"):
            success, error = import_sites_to_tf.validate_cato_api_auth(configuration, verbose=False)

        self.assertTrue(success)
        self.assertIsNone(error)
        self.assertEqual(fake_instance.call_api.call_count, 2)

    def test_exhausted_waf_challenge_returns_clean_message(self):
        waf_exc = ApiException(http_resp=FakeHttpResp(403, INCAPSULA_HTML))
        fake_instance = self._patch_api([waf_exc, waf_exc, waf_exc, waf_exc])
        configuration = SimpleNamespace(accountID="15412")

        with patch("builtins.print"):
            success, error = import_sites_to_tf.validate_cato_api_auth(configuration, verbose=False)

        self.assertFalse(success)
        self.assertNotIn("<html", error.lower())
        self.assertNotIn("_Incapsula_Resource", error)
        self.assertIn("Imperva/Incapsula", error)


def _http_error(status, body):
    return urllib.error.HTTPError(
        url="https://scimservice.catonetworks.com:4443/scim/v2/15412/abc123/Users",
        code=status,
        msg="Forbidden",
        hdrs={},
        fp=io.BytesIO(body),
    )


class FakeUrlResponse:
    def __init__(self, body, status=200, reason="OK"):
        self._body = body
        self.status = status
        self.reason = reason

    def read(self):
        return self._body


class ScimClientSendWafTest(_WafOfflineTestBase):
    def _make_client(self):
        return CatoSCIMClient(
            scim_url="https://scimservice.catonetworks.com:4443/scim/v2/15412/abc123",
            scim_token="faketoken",
            verify_ssl=True,
            verbose=False,
        )

    def test_403_html_challenge_retries_then_succeeds(self):
        client = self._make_client()
        success_body = b'{"Resources": []}'

        with patch("urllib.request.urlopen", side_effect=[_http_error(403, INCAPSULA_HTML), FakeUrlResponse(success_body)]) as mock_urlopen, \
             patch("builtins.print") as mock_print:
            ok, result = client.send(method="GET", path="/Users")

        self.assertTrue(ok)
        self.assertEqual(result, {"Resources": []})
        self.assertEqual(mock_urlopen.call_count, 2)

        printed = "\n".join(str(c.args[0]) for c in mock_print.call_args_list if c.args)
        self.assertNotIn("<html", printed.lower())
        self.assertNotIn("_Incapsula_Resource", printed)
        self.assertIn("WARNING: Cato API edge (Imperva/Incapsula) challenge received", printed)

    def test_200_html_body_challenge_retries_then_succeeds(self):
        """A WAF challenge riding a 2xx status surfaces as a JSON decode
        failure on an HTML body, not an HTTPError."""
        client = self._make_client()
        success_body = b'{"Resources": []}'

        with patch("urllib.request.urlopen", side_effect=[FakeUrlResponse(INCAPSULA_HTML), FakeUrlResponse(success_body)]) as mock_urlopen, \
             patch("builtins.print") as mock_print:
            ok, result = client.send(method="GET", path="/Users")

        self.assertTrue(ok)
        self.assertEqual(result, {"Resources": []})
        self.assertEqual(mock_urlopen.call_count, 2)

        printed = "\n".join(str(c.args[0]) for c in mock_print.call_args_list if c.args)
        self.assertNotIn("<html", printed.lower())
        self.assertIn("WARNING: Cato API edge (Imperva/Incapsula) challenge received", printed)

    def test_exhausted_waf_challenge_returns_clean_error_tuple(self):
        client = self._make_client()
        errors = [_http_error(403, INCAPSULA_HTML) for _ in range(1 + len(waf_detect.WAF_RETRY_DELAYS))]

        with patch("urllib.request.urlopen", side_effect=errors) as mock_urlopen, \
             patch("builtins.print") as mock_print:
            ok, result = client.send(method="GET", path="/Users")

        self.assertFalse(ok)
        self.assertNotIn("<html", result["error"].lower())
        self.assertNotIn("_Incapsula_Resource", result["error"])
        self.assertIn("Imperva/Incapsula", result["error"])
        self.assertEqual(mock_urlopen.call_count, 1 + len(waf_detect.WAF_RETRY_DELAYS))

        printed = "\n".join(str(c.args[0]) for c in mock_print.call_args_list if c.args)
        self.assertNotIn("<html", printed.lower())

    def test_non_waf_http_error_is_unaffected(self):
        """A plain (non-WAF) 404 must still behave exactly as before -
        returned immediately, no retry, body passed through untouched."""
        client = self._make_client()
        plain_body = b'{"detail": "not found"}'

        with patch("urllib.request.urlopen", side_effect=[_http_error(404, plain_body)]) as mock_urlopen:
            ok, result = client.send(method="GET", path="/Users/doesnotexist")

        self.assertFalse(ok)
        self.assertEqual(result["status"], 404)
        self.assertEqual(result["error"], plain_body.decode())
        self.assertEqual(mock_urlopen.call_count, 1)
        self.assertEqual(self.sleep_calls, [])


if __name__ == "__main__":
    unittest.main()
