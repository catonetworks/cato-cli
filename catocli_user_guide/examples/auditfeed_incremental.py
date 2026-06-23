#!/usr/bin/env python3
"""Incremental Cato auditFeed poller.

Validated against this repo's Cato schema snapshot and query payload:
- introspection.json
- queryPayloads/query.auditFeed.txt

Key behavior:
- auditFeed accepts accountIDs, timeFrame, optional filters, and optional marker
- auditFeed does not expose a limit/page-size argument
- pagination is marker-based; continue while hasMore is true
- only advance the stored marker after the current batch is processed successfully
- the marker boundary is inclusive, so the last record(s) of a drained window are
  re-returned on the next poll; a persisted record-level seen-hash set drops these
  duplicates so each audit record is emitted exactly once
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


# Maximum number of recently-seen record hashes to persist between runs.
# Only records near the time-window boundary can realistically reappear, so a
# few thousand is plenty while keeping the state file small.
MAX_SEEN_HASHES = 5000


GRAPHQL_QUERY = """
query auditFeed(
  $accountIDs: [ID!]
  $timeFrame: TimeFrame!
  $filters: [AuditFieldFilterInput!]
  $marker: String
) {
  auditFeed(
    accountIDs: $accountIDs
    timeFrame: $timeFrame
    filters: $filters
    marker: $marker
  ) {
    from
    to
    marker
    fetchedCount
    hasMore
    accounts {
      id
      records {
        time
        fieldsMap
        flatFields
      }
    }
  }
}
""".strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Incrementally retrieve Cato auditFeed records.")
    parser.add_argument("--endpoint", default="https://api.catonetworks.com/api/v1/graphql2")
    parser.add_argument("--token", required=True, help="Cato API token")
    parser.add_argument("--account-id", required=True, help="Single Cato account ID")
    parser.add_argument(
        "--time-frame",
        required=True,
        help='Cato TimeFrame, for example "last.P1D" or "utc.2026-06-{16/00:00:00--16/23:59:59}"',
    )
    parser.add_argument(
        "--state-file",
        default="./auditfeed_state.json",
        help="Where to persist marker state",
    )
    parser.add_argument(
        "--poll-interval",
        type=float,
        default=30.0,
        help="Seconds to wait between polls after the queue is drained",
    )
    parser.add_argument(
        "--run-once",
        action="store_true",
        help="Fetch until hasMore=false once, then exit",
    )
    parser.add_argument("--max-retries", type=int, default=5, help="Retries for transient API failures")
    parser.add_argument(
        "--filters-json",
        help='Optional JSON array for the GraphQL "filters" argument',
    )
    return parser.parse_args()


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(path: Path, state: dict[str, Any]) -> None:
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_variables(args: argparse.Namespace, marker: str) -> dict[str, Any]:
    variables: dict[str, Any] = {
        "accountIDs": [args.account_id],
        "timeFrame": args.time_frame,
        "marker": marker,
    }
    if args.filters_json:
        variables["filters"] = json.loads(args.filters_json)
    return variables


def graphql_call(endpoint: str, token: str, query: str, variables: dict[str, Any]) -> dict[str, Any]:
    payload = json.dumps(
        {
            "query": query,
            "variables": variables,
            "operationName": "auditFeed",
        }
    ).encode("utf-8")

    request = urllib.request.Request(
        endpoint,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "x-api-key": token,
        },
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def graphql_call_with_retries(
    endpoint: str,
    token: str,
    query: str,
    variables: dict[str, Any],
    max_retries: int,
) -> dict[str, Any]:
    attempt = 0
    while True:
        try:
            return graphql_call(endpoint, token, query, variables)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            if exc.code in {429, 500, 502, 503, 504} and attempt < max_retries:
                retry_after = exc.headers.get("Retry-After")
                delay = float(retry_after) if retry_after else min(2 ** attempt, 30)
                time.sleep(delay)
                attempt += 1
                continue
            raise RuntimeError(f"HTTP {exc.code}: {body}") from exc
        except urllib.error.URLError as exc:
            if attempt < max_retries:
                time.sleep(min(2 ** attempt, 30))
                attempt += 1
                continue
            raise RuntimeError(f"Network error: {exc}") from exc


def extract_records(audit_feed: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for account in audit_feed.get("accounts", []) or []:
        account_id = account.get("id")
        for record in account.get("records", []) or []:
            normalized = {
                "account_id": account_id,
                "time": record.get("time"),
                "fieldsMap": record.get("fieldsMap"),
                "flatFields": record.get("flatFields"),
            }
            records.append(normalized)
    return records


def process_batch(records: list[dict[str, Any]]) -> None:
    for record in records:
        print(json.dumps(record, separators=(",", ":")))


def record_identity(record: dict[str, Any]) -> str:
    """Stable content hash of a single audit record, used for dedup.

    flatFields is sorted so the hash is stable across API calls."""
    r = dict(record)
    flat = r.get("flatFields")
    if isinstance(flat, list):
        r["flatFields"] = sorted(
            flat,
            key=lambda pair: pair[0] if isinstance(pair, list) and pair else "",
        )
    serialized = json.dumps(r, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def main() -> int:
    args = parse_args()
    state_file = Path(args.state_file)

    while True:
        state = load_state(state_file)
        saved_time_frame = state.get("timeFrame")
        marker = state.get("marker", "")
        seen_hashes = state.get("seenHashes") or []
        if not isinstance(seen_hashes, list):
            seen_hashes = []

        # The auditFeed marker (and therefore the dedup state) is scoped to a
        # specific timeFrame; reset both when the time window changes.
        if saved_time_frame and saved_time_frame != args.time_frame:
            marker = ""
            seen_hashes = []

        seen_set = set(seen_hashes)

        while True:
            variables = build_variables(args, marker)
            response = graphql_call_with_retries(
                args.endpoint,
                args.token,
                GRAPHQL_QUERY,
                variables,
                args.max_retries,
            )

            if "errors" in response:
                raise RuntimeError(json.dumps(response["errors"], indent=2))

            audit_feed = response["data"]["auditFeed"]
            records = extract_records(audit_feed)
            next_marker = audit_feed.get("marker", "") or ""
            has_more = bool(audit_feed.get("hasMore"))

            # Record-level dedup: the auditFeed marker boundary is inclusive, so
            # the last record(s) of a drained window are re-returned on the next
            # poll. Drop any record we have already emitted. Robust even if the
            # API changes its boundary/marker behavior in the future.
            new_records = []
            for record in records:
                h = record_identity(record)
                if h in seen_set:
                    continue
                seen_set.add(h)
                seen_hashes.append(h)
                new_records.append(record)

            # bound the persisted dedup set to the most recent entries
            if len(seen_hashes) > MAX_SEEN_HASHES:
                drop = len(seen_hashes) - MAX_SEEN_HASHES
                for old in seen_hashes[:drop]:
                    seen_set.discard(old)
                seen_hashes = seen_hashes[drop:]

            if new_records:
                process_batch(new_records)

            save_state(
                state_file,
                {
                    "accountID": args.account_id,
                    "timeFrame": args.time_frame,
                    "marker": next_marker,
                    "seenHashes": seen_hashes,
                },
            )

            marker = next_marker
            if not has_more:
                break

        if args.run_once:
            return 0

        time.sleep(args.poll_interval)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
