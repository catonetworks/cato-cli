"""
Shared detection/cleaning helpers for Imperva/Incapsula WAF challenge pages.

Context: the Cato API edge sits behind an Imperva/Incapsula WAF. Under rapid
same-IP request bursts (or other bot/rate heuristics), that edge can return
an HTML challenge/block page - e.g. containing "/_Incapsula_Resource?..." and
"Incapsula incident ID: ..." - instead of the expected GraphQL JSON or SCIM
JSON response. This can arrive two ways:

  1. Via a non-2xx HTTP status (commonly 403), which the GraphQL client's
     transport layer turns into an ApiException whose body/message IS the
     raw HTML page.
  2. Via a 2xx HTTP status with an HTML body - no exception is raised by the
     transport layer; a naive JSON decode of the body either throws (and is
     caught/discarded) or silently returns the raw bytes/string instead of a
     dict.

This is normally transient rate-limiting/bot-heuristic throttling and clears
after a short backoff - every call path in catocli that can receive one of
these pages should retry it on this schedule (when retrying is low-risk for
that call site) and otherwise report a short, clean message - NEVER the raw
HTML - to the user. Full HTML is only ever shown under CATO_DEBUG.

This module has zero dependencies on the rest of catocli so it can be
imported from any call path (customLib.makeCall, the generic query/mutation
driver, configure's credential test, the Terraform-import auth check, the
SCIM client, etc.) without import-cycle concerns.
"""

import os
import random
import re
import time

from graphql_client.api_client import ApiException

# Markers that identify an Imperva/Incapsula WAF challenge/block page body,
# as opposed to a real API response.
WAF_CHALLENGE_MARKERS = ("_Incapsula_Resource", "Incapsula incident ID")

# Dedicated backoff schedule (seconds, before jitter) for WAF-challenge
# retries - short and separate from any generic network-error retry
# schedule a given call path may already have, since a WAF challenge
# normally clears quickly and doesn't warrant long waits.
WAF_RETRY_DELAYS = [2, 5, 12]


class WafChallengeError(Exception):
    """Raised/used by callers when the Cato API edge (Imperva/Incapsula)
    returned a WAF challenge/block page instead of a real API response.
    Carries the raw page text (for CATO_DEBUG output only) and the
    extracted incident ID (if present), and formats a clean, HTML-free
    message for everything else."""

    def __init__(self, raw_text):
        self.raw_text = raw_text or ""
        self.incident_id = extract_incapsula_incident_id(self.raw_text)
        super().__init__(clean_waf_error_message(self.raw_text))


def is_waf_challenge(text):
    """True if `text` looks like an Incapsula WAF challenge/block page body
    rather than a normal API response."""
    if not text:
        return False
    return any(marker in text for marker in WAF_CHALLENGE_MARKERS)


def extract_incapsula_incident_id(text):
    """Best-effort extraction of the Incapsula incident ID from a challenge
    page body, for a clearer message. Returns None if not found."""
    if not text:
        return None
    match = re.search(r'incident\s*ID[:\s]+([0-9A-Za-z\-]+)', text, re.IGNORECASE)
    return match.group(1) if match else None


def clean_waf_error_message(text):
    """Short, human-readable, HTML-free message for a terminal WAF-challenge
    failure (retries exhausted, or a call path that doesn't retry)."""
    incident_id = extract_incapsula_incident_id(text)
    incident_part = f", incident ID {incident_id}" if incident_id else ""
    return (
        f"Cato API edge (Imperva/Incapsula) rejected the request{incident_part}; "
        "this is usually transient throttling and should clear on retry"
    )


def waf_retry_warning(raw_text, delay_seconds, attempt_number, max_retries):
    """One-line warning printed before sleeping and retrying a WAF-challenge
    response. Exact wording:

        WARNING: Cato API edge (Imperva/Incapsula) challenge received
        (incident ID <id>) — transient throttling; retrying in <n>s (k/3)
    """
    incident_id = extract_incapsula_incident_id(raw_text)
    incident_part = f"incident ID {incident_id}" if incident_id else "no incident ID"
    return (
        f"WARNING: Cato API edge (Imperva/Incapsula) challenge received "
        f"({incident_part}) — transient throttling; retrying in "
        f"{delay_seconds:.1f}s ({attempt_number}/{max_retries})"
    )


def response_text_if_not_dict(response):
    """If `response` is not a dict (the shape a WAF challenge takes when it
    rides a 2xx status - see module docstring case 2), return its text for
    WAF-marker inspection; otherwise return None. Callers use this right
    after unwrapping a raw API client response, before treating it as a
    JSON result."""
    if isinstance(response, dict):
        return None
    if isinstance(response, (bytes, bytearray)):
        return response.decode('utf-8', 'replace')
    return str(response)


def call_with_waf_retry(call_fn, waf_payload_from_result=None):
    """Execute `call_fn()` (a zero-arg callable that performs one API
    request), detecting and retrying an Imperva/Incapsula WAF challenge
    with the shared backoff schedule (WAF_RETRY_DELAYS) and warning
    wording (waf_retry_warning) - so every call path that adopts this
    helper behaves identically for a WAF challenge, regardless of what
    request it's making.

    call_fn: zero-arg callable. May return a result or raise.
    waf_payload_from_result(result) -> str | None: given a *successful*
        return value from call_fn(), return text to WAF-marker-check (for
        the 2xx-with-HTML-body case - see module docstring case 2), or
        None if the result looks like a normal (non-WAF) response.
        Defaults to response_text_if_not_dict(result).

    Returns call_fn()'s result unchanged on success (including on a
    successful retry). On a non-WAF exception, re-raises it immediately,
    untouched. Once every retry is exhausted while still WAF-challenged,
    raises a plain graphql_client ApiException with a clean, HTML-free
    message - deliberately NOT WafChallengeError - so any caller with an
    existing `except ApiException` clause keeps working completely
    unchanged (this preserves the exception TYPE every existing caller
    already matches on; only the message content changes, from raw HTML
    to a short clean sentence). Raw HTML is never raised/returned from
    this function - it is only ever printed when CATO_DEBUG is set.
    """
    if waf_payload_from_result is None:
        waf_payload_from_result = response_text_if_not_dict

    debug = bool(os.getenv("CATO_DEBUG", False))
    waf_retry_count = 0

    while True:
        status = None
        try:
            result = call_fn()
        except ApiException as e:
            raw_text = str(e)
            if not is_waf_challenge(raw_text):
                raise
            status = getattr(e, 'status', None)
        except WafChallengeError as e:
            raw_text = e.raw_text
            status = None
        else:
            raw_text = waf_payload_from_result(result)
            if raw_text is None or not is_waf_challenge(raw_text):
                return result

        # A WAF challenge was detected, either via an exception or via a
        # successful-looking (2xx) call whose body is actually the
        # challenge page.
        if debug:
            print(f"DEBUG: raw WAF/Incapsula challenge response body:\n{raw_text}")

        if waf_retry_count < len(WAF_RETRY_DELAYS):
            base_delay = WAF_RETRY_DELAYS[waf_retry_count]
            delay = base_delay + random.uniform(0, base_delay * 0.5)
            print(waf_retry_warning(raw_text, delay, waf_retry_count + 1, len(WAF_RETRY_DELAYS)))
            time.sleep(delay)
            waf_retry_count += 1
            continue

        # Retries exhausted - raise a real ApiException (status defaults
        # to 403, the conventional status for an Incapsula block, when the
        # challenge was only ever seen via a 2xx body) with a clean reason.
        raise ApiException(status=status if status is not None else 403, reason=clean_waf_error_message(raw_text))
