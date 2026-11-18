
## CATO-CLI - query.aiSecurity.apps.invocation:
[Click here](https://api.catonetworks.com/documentation/#query-query.aiSecurity.apps.invocation) for documentation on this operation.

### Usage for query.aiSecurity.apps.invocation:

```bash
catocli query aiSecurity apps invocation -h

catocli query aiSecurity apps invocation <json>

catocli query aiSecurity apps invocation --json-file query.aiSecurity.apps.invocation.json

catocli query aiSecurity apps invocation '{"aiSecurityAppsInvocationInput":{"id":"id"}}'

catocli query aiSecurity apps invocation '{
    "aiSecurityAppsInvocationInput": {
        "id": "id"
    }
}'
```

## Advanced Usage
### Additional Examples
- AI Security — App Invocation

# AI Security — App Invocation

Returns the structured, role-tagged messages and guardrail verdict for a single GenAI **app
invocation**, looked up by its `id`.

## Get candidate GenAI app IDs (appStats)

GenAI applications are identified by the `category` field. Pull the application IDs that are active
in your account, then use one as the invocation `id`:

```bash
catocli query appStats '{
    "timeFrame": "last.P30D",
    "dimension": [
        {"fieldName": "application_name"},
        {"fieldName": "application_id"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"}
    ],
    "appStatsFilter": [
        {"fieldName": "category", "operator": "in", "values": ["Generative AI Tools", "Conversational AI"]}
    ],
    "from": 0,
    "limit": 1000
}'
```

## Retrieve the app invocation

```bash
catocli query aiSecurity apps invocation '{
    "aiSecurityAppsInvocationInput": {
        "id": "<invocation_id>"
    }
}'
```

Returns `data.aiSecurity.apps.invocation`:

- `id`, `sessionId`, `timestamp`, `tokenCount`
- `guard` `{id, name}` — the guardrail that evaluated the invocation
- `action` — the policy verdict (e.g. allow/block/anonymize)
- `data.message[]` `{role, content.text}` — the role-tagged prompt/response messages



#### Operation Arguments for query.aiSecurity.apps.invocation ####

`accountId` [ID] - (required) N/A
`aiSecurityAppsInvocationInput` [AiSecurityAppsInvocationInput] - (required) N/A
