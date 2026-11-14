"""
TLS certificate verification settings for the Cato CLI.

Verification is always on unless the user opts out explicitly. Settings are
resolved in this order, first match wins:

    1. command-line flags   --insecure / --ca-bundle PATH
    2. environment          CATO_INSECURE_SKIP_TLS_VERIFY=1 / CATO_CA_BUNDLE=PATH
    3. active profile       insecure_skip_tls_verify = true / ca_bundle = PATH
                            (in ~/.cato/credentials)

The CA bundle replaces the default certifi bundle, in the same way as
curl --cacert. Use it on networks with TLS inspection, where the inspection
root CA is not in the public bundle.

The insecure opt-out applies only to Cato API calls. Connections to third
parties (the Azure Sentinel upload, the GitHub and PyPI update check) are
always verified, using the CA bundle when one is configured.
"""

import os
import ssl
import sys
from collections import namedtuple

import certifi

ENV_INSECURE = "CATO_INSECURE_SKIP_TLS_VERIFY"
ENV_CA_BUNDLE = "CATO_CA_BUNDLE"
PROFILE_INSECURE = "insecure_skip_tls_verify"
PROFILE_CA_BUNDLE = "ca_bundle"

_TRUTHY = {"1", "true", "yes", "on"}

TlsSettings = namedtuple("TlsSettings", ["verify", "ca_bundle", "insecure_source"])

_DEFAULT = TlsSettings(verify=True, ca_bundle=None, insecure_source=None)
_active = None


class TlsConfigError(ValueError):
    """Raised when the TLS settings are unusable, for example a missing CA bundle."""


def _clean(value):
    return str(value or "").strip()


def truthy(value):
    return _clean(value).lower() in _TRUTHY


def check_ca_bundle(path, source="--ca-bundle"):
    """Return the expanded CA bundle path, or raise TlsConfigError.

    Relative paths are rejected so the trust anchor never depends on the
    current working directory.
    """
    path = os.path.expanduser(_clean(path))
    if not os.path.isabs(path):
        raise TlsConfigError("CA bundle path must be absolute (" + source + "): " + path)
    if not os.path.isfile(path):
        raise TlsConfigError("CA bundle file not found (" + source + "): " + path)
    return path


def _current_profile_config():
    # Imported here so this module has no import-time dependency on the profile store.
    from .profile_manager import get_profile_manager
    pm = get_profile_manager()
    return pm.get_profile_config(pm.get_current_profile()) or {}


def resolve(args=None, profile_config=None, environ=None):
    """Return the TlsSettings for this invocation.

    args           argparse namespace (may be None); reads .insecure and .ca_bundle
    profile_config dict of the active profile; loaded from ~/.cato/credentials if None
    environ        mapping used instead of os.environ (for tests)
    """
    if environ is None:
        environ = os.environ
    if profile_config is None:
        profile_config = _current_profile_config()

    env_insecure = _clean(environ.get(ENV_INSECURE))
    if getattr(args, "insecure", False):
        insecure_source = "--insecure"
    elif env_insecure:
        # A set env var decides either way, so CATO_INSECURE_SKIP_TLS_VERIFY=0 overrides the profile.
        insecure_source = ENV_INSECURE if truthy(env_insecure) else None
    elif truthy(profile_config.get(PROFILE_INSECURE)):
        insecure_source = "profile setting " + PROFILE_INSECURE
    else:
        insecure_source = None

    for source, value in (
        ("--ca-bundle", getattr(args, "ca_bundle", None)),
        (ENV_CA_BUNDLE, environ.get(ENV_CA_BUNDLE)),
        ("profile setting " + PROFILE_CA_BUNDLE, profile_config.get(PROFILE_CA_BUNDLE)),
    ):
        value = _clean(value)
        if value:
            ca_bundle = check_ca_bundle(value, source)
            break
    else:
        ca_bundle = None

    return TlsSettings(verify=insecure_source is None, ca_bundle=ca_bundle,
                       insecure_source=insecure_source)


def set_active(settings):
    """Record the settings resolved for this invocation."""
    global _active
    _active = settings


def active():
    """Settings for this invocation, or the env/profile settings if none were recorded.

    Falls back to secure defaults if the env/profile settings are unusable, so
    background callers such as the update check never silently disable verification.
    """
    if _active is not None:
        return _active
    try:
        return resolve()
    except Exception:
        return _DEFAULT


def warn_insecure(settings, stream=None):
    """Print the opt-out warning to stderr. Called on every insecure invocation."""
    if settings.verify:
        return
    stream = stream or sys.stderr
    print(
        "WARNING: TLS certificate verification is DISABLED for Cato API calls "
        "(" + settings.insecure_source + "). Anyone on the network path can "
        "impersonate the API and capture your API key. On networks with TLS "
        "inspection, use --ca-bundle or " + ENV_CA_BUNDLE + " instead.",
        file=stream,
    )


def apply_to_configuration(configuration, settings):
    """Apply settings to a graphql_client Configuration and warn if insecure."""
    configuration.verify_ssl = settings.verify
    if settings.ca_bundle:
        configuration.ssl_ca_cert = settings.ca_bundle
    warn_insecure(settings)
    return configuration


def pool_manager_kwargs(configuration):
    """cert_reqs/ca_certs for a urllib3.PoolManager built from a Configuration.

    A configuration without verify_ssl is treated as secure.
    """
    verify = getattr(configuration, "verify_ssl", True)
    return {
        "cert_reqs": "CERT_REQUIRED" if verify else "CERT_NONE",
        "ca_certs": getattr(configuration, "ssl_ca_cert", None) or certifi.where(),
    }


def verified_ssl_context(settings=None):
    """A verifying SSLContext for third-party HTTPS calls. Never disables verification."""
    settings = settings or active()
    return ssl.create_default_context(cafile=settings.ca_bundle or certifi.where())
