
## CATO-CLI - query.aiSecurity.endUsers.sessionConversation:
[Click here](https://api.catonetworks.com/documentation/#query-query.aiSecurity.endUsers.sessionConversation) for documentation on this operation.

### Usage for query.aiSecurity.endUsers.sessionConversation:

```bash
catocli query aiSecurity endUsers sessionConversation -h

catocli query aiSecurity endUsers sessionConversation <json>

catocli query aiSecurity endUsers sessionConversation --json-file query.aiSecurity.endUsers.sessionConversation.json

catocli query aiSecurity endUsers sessionConversation '{"aiSecurityEndUsersSessionConversationInput":{"appId":"id","messageId":"id","sessionId":"id","userId":"id"}}'

catocli query aiSecurity endUsers sessionConversation '{
    "aiSecurityEndUsersSessionConversationInput": {
        "appId": "id",
        "messageId": "id",
        "sessionId": "id",
        "userId": "id"
    }
}'
```

## Advanced Usage
### Additional Examples
- AI Security — End-User Session Conversation

# AI Security — End-User Session Conversation

Retrieves the actual user prompt and LLM response for a single GenAI "AI User Interaction".
This requires `sessionId`, `messageId`, and `appId`, which you first resolve from the `events`
query.

## Step 1 — Get session IDs per user (events query)

`event_sub_type = "AI User Interaction"` marks end-user GenAI prompts. Request `session_id`,
`message_id` and `application_id` as dimensions so each record carries everything the conversation
lookup needs. Filter by `user_name` to scope to one person.

```bash
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
    "limit": 500,
    "from": 0
}'
```

Each `data.events.records[].fieldsMap` returns `{session_id, message_id, application_id, user_name, time}`.

## Step 2 — Retrieve the prompt + response

```bash
catocli query aiSecurity endUsers sessionConversation '{
    "aiSecurityEndUsersSessionConversationInput": {
        "sessionId": "<session_id>",
        "messageId": "<message_id>",
        "appId": "<application_id>"
    }
}'
```

Returns `data.aiSecurity.endUsers.sessionConversation`:

- `userPrompt` — the text the user sent to the AI app
- `llmResponse` — the AI app's response

> Note: `messageId` and `appId` are required by the service even though the schema marks them
> optional. Omitting them returns a validation error. A small number of sessions may return a
> transient downstream error — retry or skip those.



#### Operation Arguments for query.aiSecurity.endUsers.sessionConversation ####

`accountId` [ID] - (required) N/A
`aiSecurityEndUsersSessionConversationInput` [AiSecurityEndUsersSessionConversationInput] - (required) N/A
