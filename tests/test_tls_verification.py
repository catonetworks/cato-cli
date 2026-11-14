"""TLS certificate verification: secure defaults, explicit opt-out, CA bundle.

No real API key is needed. The end-to-end tests run the CLI against a local
HTTPS listener with a throwaway self-signed certificate and a dummy token.
"""

import contextlib
import io
import json
import os
import re
import shutil
import ssl
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import certifi

ROOT = Path(__file__).resolve().parents[1]

from catocli.Utils import tls
from catocli.Utils import clidriver


def _ns(**kwargs):
    return SimpleNamespace(**kwargs)


class ResolveTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.bundle = os.path.join(self.tmp.name, "ca.pem")
        Path(self.bundle).write_text("placeholder")

    def tearDown(self):
        self.tmp.cleanup()

    def test_default_is_secure(self):
        s = tls.resolve(None, profile_config={}, environ={})
        self.assertTrue(s.verify)
        self.assertIsNone(s.ca_bundle)
        self.assertIsNone(s.insecure_source)

    def test_insecure_flag(self):
        s = tls.resolve(_ns(insecure=True), profile_config={}, environ={})
        self.assertFalse(s.verify)
        self.assertEqual(s.insecure_source, "--insecure")

    def test_insecure_env(self):
        for value in ("1", "true", "YES", "on"):
            s = tls.resolve(None, profile_config={}, environ={tls.ENV_INSECURE: value})
            self.assertFalse(s.verify, value)

    def test_insecure_env_falsey_values_stay_secure(self):
        for value in ("", "0", "false", "no", "off", "anything"):
            s = tls.resolve(None, profile_config={}, environ={tls.ENV_INSECURE: value})
            self.assertTrue(s.verify, value)

    def test_insecure_env_false_overrides_profile(self):
        profile = {tls.PROFILE_INSECURE: "true"}
        self.assertFalse(tls.resolve(None, profile, {}).verify)
        self.assertTrue(tls.resolve(None, profile, {tls.ENV_INSECURE: "0"}).verify)
        self.assertFalse(tls.resolve(None, profile, {tls.ENV_INSECURE: "  "}).verify)  # blank = unset

    def test_relative_ca_bundle_is_rejected(self):
        with self.assertRaises(tls.TlsConfigError):
            tls.resolve(None, {}, {tls.ENV_CA_BUNDLE: "ca.pem"})

    def test_blank_ca_bundle_falls_through_to_next_source(self):
        s = tls.resolve(_ns(ca_bundle="  "), {tls.PROFILE_CA_BUNDLE: self.bundle}, {tls.ENV_CA_BUNDLE: " "})
        self.assertEqual(s.ca_bundle, self.bundle)

    def test_insecure_profile(self):
        s = tls.resolve(None, profile_config={tls.PROFILE_INSECURE: "true"}, environ={})
        self.assertFalse(s.verify)

    def test_ca_bundle_precedence_flag_env_profile(self):
        other = os.path.join(self.tmp.name, "other.pem")
        Path(other).write_text("placeholder")
        profile = {tls.PROFILE_CA_BUNDLE: other}
        env = {tls.ENV_CA_BUNDLE: other}
        self.assertEqual(tls.resolve(_ns(ca_bundle=self.bundle), profile, env).ca_bundle, self.bundle)
        self.assertEqual(tls.resolve(None, profile, {tls.ENV_CA_BUNDLE: self.bundle}).ca_bundle, self.bundle)
        self.assertEqual(tls.resolve(None, {tls.PROFILE_CA_BUNDLE: self.bundle}, {}).ca_bundle, self.bundle)

    def test_ca_bundle_keeps_verification_on(self):
        s = tls.resolve(_ns(ca_bundle=self.bundle), profile_config={}, environ={})
        self.assertTrue(s.verify)

    def test_missing_ca_bundle_is_an_error(self):
        with self.assertRaises(tls.TlsConfigError):
            tls.resolve(_ns(ca_bundle=os.path.join(self.tmp.name, "missing.pem")), {}, {})

    def test_active_falls_back_to_secure_default_on_bad_settings(self):
        with patch.object(tls, "_active", None), \
                patch.object(tls, "resolve", side_effect=tls.TlsConfigError("bad")):
            self.assertTrue(tls.active().verify)


class ConfigurationTest(unittest.TestCase):
    CREDS = {"endpoint": "https://example.invalid/api", "cato_token": "dummy", "account_id": "1"}

    def get_configuration(self, settings):
        with patch.object(clidriver.profile_manager, "migrate_from_environment"), \
                patch.object(clidriver.profile_manager, "get_credentials", return_value=self.CREDS), \
                contextlib.redirect_stderr(io.StringIO()) as err:
            config = clidriver.get_configuration(tls_settings=settings)
        return config, err.getvalue()

    def test_get_configuration_verifies_by_default(self):
        config, err = self.get_configuration(tls.resolve(None, {}, {}))
        self.assertIs(config.verify_ssl, True)
        self.assertEqual(err, "")

    def test_get_configuration_insecure_warns(self):
        config, err = self.get_configuration(tls.resolve(_ns(insecure=True), {}, {}))
        self.assertIs(config.verify_ssl, False)
        self.assertIn("TLS certificate verification is DISABLED", err)

    def test_get_configuration_sets_ca_bundle(self):
        with tempfile.NamedTemporaryFile(suffix=".pem") as f:
            config, _ = self.get_configuration(tls.resolve(_ns(ca_bundle=f.name), {}, {}))
        self.assertTrue(config.verify_ssl)
        self.assertEqual(config.ssl_ca_cert, f.name)

    def test_pool_manager_kwargs_default_secure(self):
        kwargs = tls.pool_manager_kwargs(object())
        self.assertEqual(kwargs["cert_reqs"], "CERT_REQUIRED")
        self.assertEqual(kwargs["ca_certs"], certifi.where())

    def test_pool_manager_kwargs_uses_ca_bundle(self):
        kwargs = tls.pool_manager_kwargs(_ns(verify_ssl=True, ssl_ca_cert="/tmp/x.pem"))
        self.assertEqual(kwargs, {"cert_reqs": "CERT_REQUIRED", "ca_certs": "/tmp/x.pem"})

    def test_pool_manager_kwargs_explicit_opt_out(self):
        self.assertEqual(tls.pool_manager_kwargs(_ns(verify_ssl=False, ssl_ca_cert=None))["cert_reqs"], "CERT_NONE")

    def test_verified_ssl_context_never_disables_verification(self):
        ctx = tls.verified_ssl_context(tls.TlsSettings(verify=False, ca_bundle=None, insecure_source="--insecure"))
        self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
        self.assertTrue(ctx.check_hostname)


class ArgumentParsingTest(unittest.TestCase):
    def test_global_flags_parse_before_command(self):
        args = clidriver.parser.parse_args(["--insecure", "--ca-bundle", "/x.pem", "version"])
        self.assertTrue(args.insecure)
        self.assertEqual(args.ca_bundle, "/x.pem")

    def test_insecure_after_command_is_rejected_not_ignored(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as cm:
            clidriver.parser.parse_args(["version", "--insecure"])
        self.assertNotEqual(cm.exception.code, 0)


class NoUnconditionalVerifyOffTest(unittest.TestCase):
    """Regression guard: the generator template and runtime code must not turn verification off."""

    FORBIDDEN = re.compile(
        r"verify_ssl\s*=\s*False"
        r"|['\"]verify_ssl['\"]\s*,\s*False"
        r"|disable_warnings\s*\("
        r"|_create_unverified_context\s*\("
        r"|check_hostname\s*=\s*False"
        r"|CERT_NONE"
    )
    # Files allowed to mention these, and why.
    ALLOWED = {
        # Only disables verification when its caller passes verify_ssl=False, and warns.
        ROOT / "catocli" / "parsers" / "custom" / "scim" / "scim_client.py",
        # Maps the explicit, warned opt-out to cert_reqs='CERT_NONE'.
        ROOT / "catocli" / "Utils" / "tls.py",
    }

    def test_template_and_runtime_code(self):
        files = [ROOT / "schema" / "catolib.py"] + sorted((ROOT / "catocli").rglob("*.py"))
        offenders = []
        for path in files:
            if path in self.ALLOWED:
                continue
            for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                match = self.FORBIDDEN.search(line)
                if not match:
                    continue
                if path.name == "catolib.py" and "_create_unverified_context" in match.group(0):
                    continue  # schema download in build tooling, not the CLI runtime
                offenders.append(f"{path.relative_to(ROOT)}:{lineno}: {line.strip()}")
        self.assertEqual(offenders, [])


class _Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.rfile.read(int(self.headers.get("Content-Length", 0)))
        body = json.dumps({"data": {"entityLookup": {"items": [], "marker": "TLS_CONTROL_OK"}}}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


class _TlsServer(ThreadingHTTPServer):
    """Handshakes in the handler thread with a timeout, so a stalled client can't block accept()."""
    tls_context = None

    def get_request(self):
        sock, addr = self.socket.accept()
        sock.settimeout(10)
        return self.tls_context.wrap_socket(sock, server_side=True, do_handshake_on_connect=False), addr

    def handle_error(self, request, client_address):
        # Rejected handshakes are the expected outcome in several tests; keep the log quiet.
        if isinstance(sys.exc_info()[1], (ssl.SSLError, OSError)):
            return
        super().handle_error(request, client_address)


@unittest.skipUnless(shutil.which("openssl"), "openssl CLI needed to create a test certificate")
class SelfSignedEndpointTest(unittest.TestCase):
    """Positive control: a real TLS handshake against an untrusted certificate."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        d = Path(cls.tmp.name)
        cls.cert, key = str(d / "cert.pem"), str(d / "key.pem")
        result = subprocess.run(
            ["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes", "-days", "1",
             "-subj", "/CN=localhost", "-addext", "subjectAltName=IP:127.0.0.1,DNS:localhost",
             "-keyout", key, "-out", cls.cert],
            capture_output=True,
        )
        if result.returncode != 0:
            cls.tmp.cleanup()
            raise unittest.SkipTest("openssl could not create a test certificate: " + result.stderr.decode()[-200:])
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ctx.load_cert_chain(cls.cert, key)
        cls.server = _TlsServer(("127.0.0.1", 0), _Handler)
        cls.server.tls_context = ctx
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.endpoint = f"https://127.0.0.1:{cls.server.server_address[1]}/api/v1/graphql2"
        cls.home = d / "home"
        cls.home.mkdir()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.tmp.cleanup()

    QUERY = ["query", "entityLookup", '{"type": "country"}']

    def run_cli(self, global_args=(), extra_env=None, home=None, command=None):
        env = {k: v for k, v in os.environ.items() if not k.startswith("CATO_")}
        env["HOME"] = str(home or self.home)  # isolate from the developer's ~/.cato profiles
        env.update(extra_env or {})
        if command is None:
            command = ["--endpoint", self.endpoint, "--api-token", "dummy-token", "--accountID", "1", *self.QUERY]
        cmd = [sys.executable, "-m", "catocli", *global_args, *command]
        return subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True, text=True, timeout=60)

    def make_home(self, profile_lines=()):
        home = Path(tempfile.mkdtemp(dir=self.tmp.name))
        if profile_lines:
            (home / ".cato").mkdir()
            (home / ".cato" / "credentials").write_text("\n".join(["[default]", *profile_lines]) + "\n")
        return home

    def test_configure_set_ca_bundle_validates_and_saves(self):
        home = self.make_home()
        r = self.run_cli(home=home, command=[
            "configure", "set", "--endpoint", self.endpoint, "--cato-token", "dummy-token",
            "--account-id", "1", "--ca-bundle", self.cert])
        self.assertIn("Credentials validated successfully", r.stdout, r.stdout + r.stderr)
        self.assertIn("ca_bundle = " + self.cert, (home / ".cato" / "credentials").read_text())
        # The saved profile is then used with no flags or env vars.
        r = self.run_cli(home=home, command=self.QUERY)
        self.assertIn("TLS_CONTROL_OK", r.stdout, r.stdout + r.stderr)

    def test_configure_set_ca_bundle_check_ignores_insecure(self):
        # A bundle that does not trust the listener must fail the check, even with --insecure.
        home = self.make_home()
        r = self.run_cli(["--insecure"], home=home, command=[
            "configure", "set", "--endpoint", self.endpoint, "--cato-token", "dummy-token",
            "--account-id", "1", "--ca-bundle", certifi.where()])
        out = r.stdout + r.stderr
        self.assertIn("CERTIFICATE_VERIFY_FAILED", out)
        self.assertNotIn("Credentials validated successfully", out)
        self.assertFalse((home / ".cato" / "credentials").exists())

    def test_profile_insecure_setting_connects_and_warns(self):
        home = self.make_home(["endpoint = " + self.endpoint, "cato_token = dummy", "account_id = 1",
                               "insecure_skip_tls_verify = true"])
        r = self.run_cli(home=home, command=self.QUERY)
        self.assertIn("TLS_CONTROL_OK", r.stdout)
        self.assertIn("TLS certificate verification is DISABLED", r.stderr)
        # CATO_INSECURE_SKIP_TLS_VERIFY=0 turns verification back on for one run.
        r = self.run_cli(home=home, command=self.QUERY, extra_env={"CATO_INSECURE_SKIP_TLS_VERIFY": "0"})
        self.assertIn("CERTIFICATE_VERIFY_FAILED", r.stdout + r.stderr)

    def test_stale_profile_ca_bundle_can_still_be_fixed(self):
        home = self.make_home(["endpoint = " + self.endpoint, "cato_token = dummy", "account_id = 1",
                               "ca_bundle = " + str(self.home / "moved.pem")])
        r = self.run_cli(home=home, command=self.QUERY)
        self.assertIn("CA bundle file not found", r.stdout + r.stderr)
        self.assertNotIn("TLS_CONTROL_OK", r.stdout)
        r = self.run_cli(home=home, command=["configure", "show"])
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        r = self.run_cli(home=home, command=["configure", "set", "--ca-bundle", self.cert])
        self.assertIn("Credentials validated successfully", r.stdout, r.stdout + r.stderr)
        r = self.run_cli(home=home, command=self.QUERY)
        self.assertIn("TLS_CONTROL_OK", r.stdout, r.stdout + r.stderr)

    def test_default_rejects_untrusted_certificate(self):
        r = self.run_cli()
        out = r.stdout + r.stderr
        self.assertIn("CERTIFICATE_VERIFY_FAILED", out)
        self.assertNotIn("TLS_CONTROL_OK", out)

    def test_ca_bundle_flag_trusts_certificate(self):
        r = self.run_cli(["--ca-bundle", self.cert])
        out = r.stdout + r.stderr
        self.assertIn("TLS_CONTROL_OK", out)
        self.assertNotIn("DISABLED", out)

    def test_ca_bundle_env_trusts_certificate(self):
        r = self.run_cli(extra_env={"CATO_CA_BUNDLE": self.cert})
        self.assertIn("TLS_CONTROL_OK", r.stdout + r.stderr)

    def test_insecure_connects_and_warns(self):
        r = self.run_cli(["--insecure"])
        self.assertIn("TLS_CONTROL_OK", r.stdout)
        self.assertIn("TLS certificate verification is DISABLED", r.stderr)

    def test_insecure_env_connects_and_warns(self):
        r = self.run_cli(extra_env={"CATO_INSECURE_SKIP_TLS_VERIFY": "1"})
        self.assertIn("TLS_CONTROL_OK", r.stdout)
        self.assertIn("TLS certificate verification is DISABLED", r.stderr)

    def test_missing_ca_bundle_fails_closed(self):
        r = self.run_cli(["--ca-bundle", str(self.home / "nope.pem")])
        out = r.stdout + r.stderr
        self.assertIn("CA bundle file not found", out)
        self.assertNotIn("TLS_CONTROL_OK", out)
        self.assertNotEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
