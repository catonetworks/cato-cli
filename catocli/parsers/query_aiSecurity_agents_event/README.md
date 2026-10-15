
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

#### Operation Arguments for query.aiSecurity.agents.event ####

`accountId` [ID] - (required) N/A
`aiSecurityAgentsEventInput` [AiSecurityAgentsEventInput] - (required) N/A
