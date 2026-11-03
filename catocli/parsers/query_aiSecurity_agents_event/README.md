
## CATO-CLI - query.aiSecurity.agents.event:
[Click here](https://api.catonetworks.com/documentation/#query-query.aiSecurity.agents.event) for documentation on this operation.

### Usage for query.aiSecurity.agents.event:

```bash
catocli query aiSecurity agents event -h

catocli query aiSecurity agents event <json>

catocli query aiSecurity agents event --json-file query.aiSecurity.agents.event.json

catocli query aiSecurity agents event '{"aiSecurityAgentsEventInput":{"interactionId":"id","sessionId":"id"}}'

catocli query aiSecurity agents event '{
    "aiSecurityAgentsEventInput": {
        "interactionId": "id",
        "sessionId": "id"
    }
}'
```

## Advanced Usage
### Additional Examples
- AI Security — Agent Event

# AI Security — Agent Event

Returns a single AI agent interaction by `sessionId` + `interactionId`. Use
`aiSecurity agents session` first to list the interactions in a session, then drill into one with
this operation.

## Step 1 — List interactions in a session

```bash
catocli query aiSecurity agents session '{
    "aiSecurityAgentsSessionInput": {"sessionId": "<session_id>", "paging": {"from": 1, "limit": 50}}
}'
```

Take an `interactionId` from `items[]`.

## Step 2 — Retrieve the single agent event

```bash
catocli query aiSecurity agents event '{
    "aiSecurityAgentsEventInput": {
        "sessionId": "<session_id>",
        "interactionId": "<interaction_id>"
    }
}'
```

Returns `data.aiSecurity.agents.event`:

- `interactionId`
- `appActivityType` — e.g. `LLM Response`, `Tool Call`
- `time`
- `content` — the interaction content

> Tip: session IDs come from the `events` query filtered to
> `event_sub_type in ["Agent Interaction"]` — see `query.aiSecurity.agents.session.md`.



#### Operation Arguments for query.aiSecurity.agents.event ####

`accountId` [ID] - (required) N/A
`aiSecurityAgentsEventInput` [AiSecurityAgentsEventInput] - (required) N/A
