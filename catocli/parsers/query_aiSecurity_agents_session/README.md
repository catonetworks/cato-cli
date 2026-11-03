
## CATO-CLI - query.aiSecurity.agents.session:
[Click here](https://api.catonetworks.com/documentation/#query-query.aiSecurity.agents.session) for documentation on this operation.

### Usage for query.aiSecurity.agents.session:

```bash
catocli query aiSecurity agents session -h

catocli query aiSecurity agents session <json>

catocli query aiSecurity agents session --json-file query.aiSecurity.agents.session.json

catocli query aiSecurity agents session '{"aiSecurityAgentsSessionInput":{"paging":{"from":1,"limit":1},"sessionId":"id"}}'

catocli query aiSecurity agents session '{
    "aiSecurityAgentsSessionInput": {
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sessionId": "id"
    }
}'
```

#### Operation Arguments for query.aiSecurity.agents.session ####

`accountId` [ID] - (required) N/A
`aiSecurityAgentsSessionInput` [AiSecurityAgentsSessionInput] - (required) N/A
