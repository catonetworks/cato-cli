
## CATO-CLI - query.aiSecurity:
[Click here](https://api.catonetworks.com/documentation/#query-query.aiSecurity) for documentation on this operation.

### Usage for query.aiSecurity:

```bash
catocli query aiSecurity -h

catocli query aiSecurity <json>

catocli query aiSecurity --json-file query.aiSecurity.json

catocli query aiSecurity '{"aiSecurityAppsInvocationInput":{"id":"id"},"aiSecurityEndUsersSessionConversationInput":{"appId":"id","messageId":"id","sessionId":"id","userId":"id"}}'

catocli query aiSecurity '{
    "aiSecurityAppsInvocationInput": {
        "id": "id"
    },
    "aiSecurityEndUsersSessionConversationInput": {
        "appId": "id",
        "messageId": "id",
        "sessionId": "id",
        "userId": "id"
    }
}'
```

#### Operation Arguments for query.aiSecurity ####

`accountId` [ID] - (required) N/A    
`aiSecurityAppsInvocationInput` [AiSecurityAppsInvocationInput] - (required) N/A    
`aiSecurityEndUsersSessionConversationInput` [AiSecurityEndUsersSessionConversationInput] - (required) N/A    
