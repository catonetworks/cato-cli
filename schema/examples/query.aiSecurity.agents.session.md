# AI Security — Agent Session

Returns the interaction content for an AI **agent** session (`event_sub_type = "Agent Interaction"`).
Only a `sessionId` is required — resolve it from the `events` query first.

## Step 1 — Get agent session IDs (events query)

```bash
catocli query events '{
    "timeFrame": "last.P30D",
    "eventsDimension": [
        {"fieldName": "session_id"},
        {"fieldName": "user_name"},
        {"fieldName": "time"}
    ],
    "eventsFilter": [
        {"fieldName": "event_sub_type", "operator": "in", "values": ["Agent Interaction"]}
    ],
    "limit": 500,
    "from": 0
}'
```

Read `session_id` from each `data.events.records[].fieldsMap`.

## Step 2 — Retrieve the agent session interactions

```bash
catocli query aiSecurity agents session '{
    "aiSecurityAgentsSessionInput": {
        "sessionId": "<session_id>",
        "paging": {"from": 1, "limit": 50}
    }
}'
```

Returns `data.aiSecurity.agents.session.items[]`, each with:

- `interactionId` — unique id of the interaction
- `appActivityType` — e.g. `LLM Response`, `Tool Call`
- `time` — interaction timestamp
- `content` — the interaction content (prompt/response/tool text)

plus `paging.total`.
