# auditfeed_incremental.py Specification

## Purpose

This specification defines the required behavior for `catocli_user_guide/examples/auditfeed_incremental.py`, an incremental Cato `auditFeed` poller example.

The implementation must retrieve Cato audit records from the `auditFeed` GraphQL API, paginate with the returned marker, persist state between runs, and emit each audit record exactly once even when Cato re-returns records at the marker boundary.

## Scope

In scope:

- Direct Cato GraphQL `auditFeed` requests.
- Long-option CLI interface for endpoint, token, account ID, time frame, state file, filters, retry count, polling interval, and run-once mode.
- Marker persistence and reuse.
- Time-frame-scoped marker reset.
- Record-level deduplication persisted across process restarts.
- Newline-delimited compact JSON output to stdout.
- Retry behavior for transient API failures and rate limits.

Out of scope:

- TCP streaming.
- Microsoft Sentinel output.
- Short option compatibility with `auditFeed.py`.
- Automatic time-window generation.
- Multi-process state-file locking.
- Guaranteeing exactly-once output when multiple script instances share the same state file concurrently.

## API Contract

### Endpoint

Default endpoint:

```text
https://api.catonetworks.com/api/v1/graphql2
```

The script must use HTTP `POST`.

### Authentication

The Cato API token must be supplied in the `x-api-key` HTTP header.

Security requirements:

- The token must be accepted via `--token`.
- The token must not be hardcoded.
- The token must not be written to the state file.
- The token must not be printed in normal output or error messages.

### GraphQL Query

The script must use a parameterized GraphQL request with variables.

```graphql
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
```

Example request body:

```json
{
  "query": "query auditFeed(...) { ... }",
  "operationName": "auditFeed",
  "variables": {
    "accountIDs": ["12345"],
    "timeFrame": "last.P1D",
    "marker": "",
    "filters": [
      {
        "fieldNameInput": {
          "AuditFieldName": "change_type"
        },
        "operator": "is",
        "values": ["CREATED"]
      }
    ]
  }
}
```

### Parameters

Required:

- `accountIDs`: list of Cato account IDs. The CLI accepts one `--account-id` and sends it as a one-item array.
- `timeFrame`: Cato `TimeFrame`, for example `last.P1D` or `utc.2026-06-{16/00:00:00--16/23:59:59}`.

Optional:

- `marker`: pagination marker from the previous response.
- `filters`: JSON array supplied with `--filters-json`.

Not supported:

- `limit`, `pageSize`, or explicit batch size. `auditFeed` pagination is controlled by `marker` and `hasMore`.

## CLI Contract

Required arguments:

- `--token`: Cato API token.
- `--account-id`: single Cato account ID.
- `--time-frame`: Cato `TimeFrame`.

Optional arguments:

- `--endpoint`: GraphQL endpoint. Default `https://api.catonetworks.com/api/v1/graphql2`.
- `--state-file`: state file path. Default `./auditfeed_state.json`.
- `--poll-interval`: seconds to wait between drained polls. Default `30.0`.
- `--run-once`: fetch until `hasMore=false` once, then exit.
- `--max-retries`: retries for transient API failures. Default `5`.
- `--filters-json`: optional JSON array for GraphQL `filters`.

Example commands:

```bash
python3 auditfeed_incremental.py \
  --token "$CATO_API_TOKEN" \
  --account-id 12345 \
  --time-frame last.P1D \
  --run-once
```

```bash
python3 auditfeed_incremental.py \
  --token "$CATO_API_TOKEN" \
  --account-id 12345 \
  --time-frame "utc.2026-06-{16/00:00:00--16/23:59:59}" \
  --state-file ./auditfeed_state.json \
  --run-once
```

```bash
python3 auditfeed_incremental.py \
  --token "$CATO_API_TOKEN" \
  --account-id 12345 \
  --time-frame last.P1D \
  --filters-json '[{"fieldNameInput":{"AuditFieldName":"change_type"},"operator":"is","values":["CREATED"]}]'
```

## Filter Contract

`--filters-json` must be a JSON array compatible with GraphQL `[AuditFieldFilterInput!]`.

Example:

```json
[
  {
    "fieldNameInput": {
      "AuditFieldName": "change_type"
    },
    "operator": "is",
    "values": ["CREATED"]
  }
]
```

Rules:

- Invalid JSON must fail before the API call.
- The script must pass filters through GraphQL variables.
- The script must not interpolate filter JSON into the query string.

## State File Contract

The state file must be JSON.

Schema:

```json
{
  "accountID": "12345",
  "timeFrame": "last.P1D",
  "marker": "1781883741985_",
  "seenHashes": [
    "sha256-record-hash"
  ]
}
```

Compatibility:

- Older state files containing `lastBatchHash` may be read.
- `lastBatchHash` is ignored.
- If `seenHashes` is missing or not a list, it must be treated as an empty list.

Security requirements:

- The state file must never contain the Cato API token.
- The state file must not contain raw audit records.
- The state file may contain audit record hashes.

## Marker Semantics

Observed `auditFeed` behavior:

- The marker is scoped to the requested `timeFrame`.
- A marker from one time frame must not be reused for a different time frame.
- The marker boundary is inclusive: after a drained response with `hasMore=false`, a later call using the returned marker may return the last record again.
- The returned marker may not advance when the API re-returns only a boundary record.

Required behavior:

- Load `marker` from the state file at the start of each poll cycle.
- Send the loaded marker in GraphQL variables.
- After the response is processed and output succeeds, persist the response marker.
- If stored `timeFrame` differs from requested `--time-frame`, reset `marker` to `""` and reset `seenHashes`.
- Do not compute or mutate Cato markers locally.
- If the response marker equals the marker that was just sent while `hasMore` is true, stop the current drain pass, because continuing would refetch the same records (all deduplicated to nothing) forever. See Termination Guarantees.

## Polling Sequence

For each outer poll cycle:

1. Load state from `--state-file`.
2. Read `timeFrame`, `marker`, and `seenHashes`.
3. If stored `timeFrame` differs from requested `--time-frame`, reset marker and dedup state.
4. Build GraphQL variables from account ID, time frame, marker, and filters.
5. Call `auditFeed`.
6. Fail without advancing marker if the HTTP call fails permanently or GraphQL `errors` are present.
7. Extract records from `data.auditFeed.accounts[*].records`.
8. Deduplicate records using persisted `seenHashes`.
9. Emit only new records to stdout.
10. Persist `accountID`, `timeFrame`, response `marker`, and updated `seenHashes`.
11. If `hasMore` is true and the marker advanced, repeat from step 4 using the persisted response marker.
12. If `hasMore` is true but the marker did not advance, end the current drain pass (no-progress guard) and treat it like a drained queue. See Termination Guarantees.
13. If the drain pass ended and `--run-once` is set, exit.
14. If the drain pass ended and `--run-once` is not set, sleep `--poll-interval` seconds and begin a new outer poll cycle.

Important invariant:

- Marker state must be persisted only after the current batch is processed and emitted successfully. This avoids skipping records after a failure.

## Record Extraction

For each account in `auditFeed.accounts`:

- Read `account.id`.
- For each `record` in `account.records`, produce an object with:
  - `account_id`: account ID from the containing account.
  - `time`: `record.time`.
  - `fieldsMap`: `record.fieldsMap`.
  - `flatFields`: `record.flatFields`.

Output must be compact JSON:

```python
print(json.dumps(record, separators=(",", ":")))
```

## Exactly-Once Deduplication

Problem:

- `auditFeed` can re-return record(s) at the marker boundary.
- This can happen across process restarts.
- Future API behavior may change, so the implementation must not rely only on `hasMore`, marker equality, or full-batch equality.

Required solution:

- Compute a stable identity hash for each individual extracted record.
- Keep a bounded, persisted list of recently emitted record hashes in `seenHashes`.
- Before stdout output, drop records whose hash is already in `seenHashes`.
- Add newly emitted records to `seenHashes`.
- Persist updated `seenHashes` after successful output.
- Bound `seenHashes` to `MAX_SEEN_HASHES`.
- Canonical `MAX_SEEN_HASHES` value: `5000`.

Canonical identity:

```python
def record_identity(record: dict[str, Any]) -> str:
    r = dict(record)
    flat = r.get("flatFields")
    if isinstance(flat, list):
        r["flatFields"] = sorted(
            flat,
            key=lambda pair: pair[0] if isinstance(pair, list) and pair else "",
        )
    serialized = json.dumps(r, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()
```

Why `flatFields` is sorted:

- Cato may return the same logical record with `flatFields` in different list orders.
- Sorting prevents ordering-only changes from bypassing deduplication.

Caveat:

- If Cato returns two genuinely distinct audit records with byte-identical extracted content, the content hash will suppress the second. If Cato exposes a stable unique audit record ID in the future, prefer that as the identity key.

## Retry and Error Handling

Required behavior:

- Retry transient HTTP errors: `429`, `500`, `502`, `503`, and `504`.
- Honor `Retry-After` when present (see Retry-After parsing below).
- Otherwise use exponential backoff, capped at 30 seconds.
- Retry transient network errors up to `--max-retries`.
- On final failure, raise a clear error and do not update the state file.
- If the GraphQL response contains `errors`, raise and do not update the state file.
- Every retry path must increment the retry counter so the `--max-retries` bound is always reachable. A retry path that sleeps and continues without incrementing the counter is a defect, because the bound can never be reached and the script spins forever.

### Retry-After parsing

RFC 7231 defines two permitted forms for the `Retry-After` response header:

- *delay-seconds* – a non-negative decimal integer, e.g. `"120"`. Converted directly to `float`.
- *HTTP-date* – a full date-time string, e.g. `"Wed, 24 Jun 2026 11:30:00 GMT"`. Converted by computing `max(0, target_utc - now_utc)` in seconds.

Rules:

- Negative delay-seconds must be clamped to `0.0`.
- HTTP-dates in the past must produce `0.0` (retry immediately without extra delay).
- Naive datetimes in HTTP-date form must be treated as UTC.
- If the header is absent, empty, or cannot be parsed as either form, return `None` so the caller falls back to exponential backoff.

Canonical implementation:

```python
def parse_retry_after(retry_after: str | None) -> float | None:
    if not retry_after:
        return None
    retry_after = retry_after.strip()
    try:
        return max(0.0, float(retry_after))
    except ValueError:
        pass
    try:
        parsed_date = email.utils.parsedate_to_datetime(retry_after)
    except (TypeError, ValueError):
        return None
    if parsed_date is None:
        return None
    if parsed_date.tzinfo is None:
        parsed_date = parsed_date.replace(tzinfo=timezone.utc)
    return max(0.0, (parsed_date - datetime.now(timezone.utc)).total_seconds())
```

Security requirements:

- Do not include API token values in raised errors or output.
- Error output may include HTTP status and response body, but must avoid logging request headers.

## Termination Guarantees

The script must always make progress or stop. Every retry or pagination loop must have a bound that is guaranteed to be reached.

Required behavior:

- Every retry loop must increment its retry counter on every retry path (HTTP error status and network error) and must raise once `--max-retries` is exceeded.
- The inner pagination loop must end the current drain pass when the response marker equals the marker just sent while `hasMore` is true (no-progress guard), so a stuck or misbehaving feed cannot loop forever.
- The inner pagination loop must also end on `hasMore=false`.
- The no-progress guard must behave like a drained queue: in `--run-once` mode the script exits, otherwise it sleeps `--poll-interval` and starts a new outer poll cycle.
- The no-progress notice must be written to stderr, never to stdout, so it does not corrupt the newline-delimited JSON record stream.

Rationale:

- A retry path that does not increment the counter, or a pagination loop with no no-progress guard, can run forever and is treated as a defect.

## Acceptance Criteria

### Initial API request

- Given an empty or missing state file.
- When running with `--account-id 12345 --time-frame last.P1D`.
- Then variables contain `accountIDs: ["12345"]`, `timeFrame: "last.P1D"`, and marker `""`.
- Then no `limit` or `pageSize` is sent.

### Pagination

- Given a response with `hasMore: true` and marker `M1`.
- Then the next API request uses marker `M1`.
- Then the state file is updated only after records from the first response are emitted.

### Drained run

- Given a response with `hasMore: false`.
- When `--run-once` is set.
- Then the script exits after persisting the response marker and seen hashes.

### Continuous polling

- Given a response with `hasMore: false`.
- When `--run-once` is not set.
- Then the script sleeps for `--poll-interval` and starts a new outer poll cycle using the persisted state.

### Time-frame change

- Given state contains `timeFrame: "last.P1D"`, marker `M1`, and non-empty `seenHashes`.
- When the script starts with `--time-frame last.PT1H`.
- Then marker is reset to `""`.
- And `seenHashes` is reset to `[]`.

### Boundary duplicate

- Given run 1 emits records `[A, B]`, persists marker `M`, and stores hashes for `A` and `B`.
- And run 2 calls `auditFeed` with marker `M` and receives `[B]`.
- Then run 2 emits no records.
- And state remains valid with marker from run 2 and hashes for `A` and `B`.

### Mixed duplicate and new record

- Given state contains hash for `B`.
- And the next response contains `[B, C]`.
- Then the script emits only `C`.
- And state contains hashes for `B` and `C`.

### Restart persistence

- Given the script emitted record `B` and persisted its hash.
- And the process exits.
- When it starts again with the same state file and Cato returns `B`.
- Then `B` is dropped as a duplicate.

### API behavior change

- Given Cato stops re-returning boundary records.
- And the next response contains only new records.
- Then the dedup layer emits all returned records and does not change correct behavior.

### No-progress pagination stop

- Given a response with `hasMore: true` and a marker equal to the marker just sent.
- Then the script ends the current drain pass instead of issuing another identical request.
- And the no-progress notice is written to stderr, not stdout.
- And in `--run-once` mode the script exits, otherwise it sleeps `--poll-interval` and re-polls.

### Bounded retries

- Given the API repeatedly returns a retryable failure.
- Then each retry increments the retry counter.
- And the script raises and stops once `--max-retries` is exceeded, rather than looping forever.

### Retry-After delay-seconds form

- Given the API returns `429` with `Retry-After: 10`.
- Then `parse_retry_after("10")` returns `10.0`.
- And the script sleeps `10.0` seconds before retrying.

### Retry-After HTTP-date form

- Given the API returns `429` with `Retry-After` set to an HTTP-date approximately 30 seconds in the future.
- Then `parse_retry_after` parses the date, computes the remaining seconds, and returns approximately `30.0`.
- And the script sleeps for that duration before retrying without raising.

### Retry-After unparseable or absent

- Given `Retry-After` is `None`, empty, or an unrecognised string (e.g. `"not-a-date"`).
- Then `parse_retry_after` returns `None`.
- And the retry falls back to exponential backoff `min(2 ** attempt, 30)`.

### Retry-After past HTTP-date clamped to zero

- Given `Retry-After` is an HTTP-date in the past.
- Then `parse_retry_after` returns `0.0` (clamp, do not produce a negative delay).

## Implementation Checklist

- [ ] Use parameterized GraphQL query and variables.
- [ ] Require `--token`, `--account-id`, and `--time-frame`.
- [ ] Send `x-api-key` header and never persist the token.
- [ ] Parse `--filters-json` as JSON and pass it through variables.
- [ ] Load `marker`, `timeFrame`, and `seenHashes` from the state file.
- [ ] Treat missing or invalid `seenHashes` as empty.
- [ ] Reset marker and dedup state when `timeFrame` changes.
- [ ] Extract records with `account_id`, `time`, `fieldsMap`, and `flatFields`.
- [ ] Compute per-record identity hashes with sorted `flatFields`.
- [ ] Drop records already present in `seenHashes`.
- [ ] Emit only new records to stdout.
- [ ] Persist response marker and updated `seenHashes` after successful output.
- [ ] Bound `seenHashes` to `MAX_SEEN_HASHES = 5000`.
- [ ] Retry transient HTTP/network failures with `Retry-After` (parsed per RFC 7231 via `parse_retry_after`) or exponential backoff.
- [ ] Increment the retry counter on every retry path so the `--max-retries` bound is always reachable.
- [ ] End the drain pass when the marker does not advance while `hasMore` is true, writing the notice to stderr.
- [ ] Do not update state on permanent API, GraphQL, or output failures.
- [ ] Add tests for: `parse_retry_after` (delay-seconds, HTTP-date future/past, missing/garbage), retry counter increment, boundary duplicate, mixed duplicate/new page, time-frame reset, restart persistence, and no-progress stop.

