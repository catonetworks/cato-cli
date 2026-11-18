# AI Security Session Data Guide

## Overview

Cato's AI Security surface lets you retrieve **what users actually did with GenAI applications** —
the prompts users sent, the responses the LLM returned, and AI agent interaction content — not just
aggregate counts. Getting this data is a **two-step workflow**:

1. **Find the sessions** with the `events` query. AI activity shows up as events whose
   `event_sub_type` is `AI User Interaction` (end-user GenAI prompts) or `Agent Interaction`
   (AI agent activity). The `events` query returns the `session_id` (and, for prompts, the
   `message_id` and `application_id`) you need for step 2.
2. **Retrieve the prompt / conversation content** with the split `aiSecurity` sub-operations,
   keyed by the IDs from step 1.

| What you want | event_sub_type (step 1) | aiSecurity op (step 2) | Returns |
|---|---|---|---|
| A user's GenAI prompts & LLM answers | `AI User Interaction` | `aiSecurity endUsers sessionConversation` | `userPrompt`, `llmResponse` |
| AI agent session activity | `Agent Interaction` | `aiSecurity agents session` | `items[].{content, appActivityType, time}` |
| A single agent interaction | `Agent Interaction` | `aiSecurity agents event` | one `{content, appActivityType, time}` |
| A GenAI app invocation (guardrail verdict + messages) | — | `aiSecurity apps invocation` | `data.message[]`, `guard`, `action`, `tokenCount` |

## Basic Usage

```bash
# Step 1: get session IDs for a user's GenAI prompts (last 30 days)
catocli query events '{
    "timeFrame": "last.P30D",
    "eventsDimension": [
        {"fieldName": "session_id"},
        {"fieldName": "user_name"},
        {"fieldName": "time"},
        {"fieldName": "message_id"},
        {"fieldName": "application_id"}
    ],
    "eventsFilter": [
        {"fieldName": "event_sub_type", "operator": "in", "values": ["AI User Interaction"]},
        {"fieldName": "user_name", "operator": "is", "values": ["Jane Doe"]}
    ],
    "limit": 500
}'

# Step 2: retrieve the prompt + LLM response for one message
catocli query aiSecurity endUsers sessionConversation '{
    "aiSecurityEndUsersSessionConversationInput": {
        "sessionId": "<session_id>",
        "messageId": "<message_id>",
        "appId": "<application_id>"
    }
}'
```

## Query Structure

### Step 1 — the `events` query

- `eventsDimension`: the fields returned per record. For AI session lookups always include
  `session_id`. For end-user prompts also include `message_id` and `application_id` (required by the
  conversation lookup). `user_name` and `time` make the results readable.
- `eventsFilter`: at minimum `{"fieldName": "event_sub_type", "operator": "in", "values": [...]}`.
  Add `{"fieldName": "user_name", "operator": "is", "values": ["<name>"]}` to scope to one person.
- Read results from `data.events.records[].fieldsMap`.

### Step 2 — the `aiSecurity` sub-operations

Each is a split sub-operation under `aiSecurity`:

```bash
# End-user prompt + response (AI User Interaction)
catocli query aiSecurity endUsers sessionConversation '{"aiSecurityEndUsersSessionConversationInput":{"sessionId":"...","messageId":"...","appId":"..."}}'

# Agent session interactions (Agent Interaction)
catocli query aiSecurity agents session '{"aiSecurityAgentsSessionInput":{"sessionId":"...","paging":{"from":1,"limit":50}}}'

# A single agent interaction
catocli query aiSecurity agents event '{"aiSecurityAgentsEventInput":{"sessionId":"...","interactionId":"..."}}'

# A GenAI app invocation (guardrail verdict + messages)
catocli query aiSecurity apps invocation '{"aiSecurityAppsInvocationInput":{"id":"..."}}'
```

> **`endUsers sessionConversation` requires `messageId` and `appId`** in addition to `sessionId`,
> even though the schema marks them optional — the service rejects the call without them. Source all
> three from the same step-1 events record.

## AI Event Sub-Types

Filter `event_sub_type` to these values to find AI activity:

- `AI User Interaction` — a user sent a prompt to a GenAI app (→ `endUsers sessionConversation`).
- `Agent Interaction` — AI agent activity (→ `agents session` / `agents event`).
- `Application Runtime Protection`, `New AI App Discovered` — additional AI Security sub-types for
  overview/event reporting.

## Common Use Cases

### 1. What did a specific user ask GenAI apps?

```bash
# 1a. list the user's prompt messages
catocli query events '{"timeFrame":"last.P30D","eventsDimension":[{"fieldName":"session_id"},{"fieldName":"message_id"},{"fieldName":"application_id"},{"fieldName":"user_name"}],"eventsFilter":[{"fieldName":"event_sub_type","operator":"in","values":["AI User Interaction"]},{"fieldName":"user_name","operator":"is","values":["Jane Doe"]}],"limit":500}'

# 1b. for each (session_id, message_id, application_id), fetch the conversation
catocli query aiSecurity endUsers sessionConversation '{"aiSecurityEndUsersSessionConversationInput":{"sessionId":"<session_id>","messageId":"<message_id>","appId":"<application_id>"}}'
```

### 2. AI agent activity for the account

```bash
catocli query events '{"timeFrame":"last.P7D","eventsDimension":[{"fieldName":"session_id"},{"fieldName":"user_name"}],"eventsFilter":[{"fieldName":"event_sub_type","operator":"in","values":["Agent Interaction"]}],"limit":500}'

catocli query aiSecurity agents session '{"aiSecurityAgentsSessionInput":{"sessionId":"<session_id>","paging":{"from":1,"limit":50}}}'
```

### 3. All GenAI prompts across all users (audit)

Omit the `user_name` filter in step 1 to pull sessions for every user, then iterate step 2.

## Time Frame Options

AI session queries use the same relative time frames as other operations:

- `last.P1D` — last 24 hours
- `last.P7D` — last 7 days
- `last.P14D` — last 14 days
- `last.P30D` — last 30 days (common for AI session audits)

## Output Options

```bash
# Default JSON
catocli query aiSecurity endUsers sessionConversation '{...}'

# Raw API response (no post-processing)
catocli query aiSecurity endUsers sessionConversation '{...}' -raw
```

## Notes

- The `session_id` returned by `events` is the same identifier the `aiSecurity` session queries
  expect.
- A small number of sessions can return a transient downstream service error; retry or skip them
  when iterating.
- For aggregate AI reporting (bandwidth, policy triggers, app usage by user) see
  [app-stats.md](app-stats.md) and the `events` / `eventsTimeSeries` guides.

## See also

- Per-operation payload examples: `schema/examples/query.aiSecurity.*.md`
- Events query guide: [events-timeseries.md](events-timeseries.md)
