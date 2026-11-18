
## CATO-CLI - mutation.notification.integration.updateWebhook:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.notification.integration.updateWebhook) for documentation on this operation.

### Usage for mutation.notification.integration.updateWebhook:

```bash
catocli mutation notification integration updateWebhook -h

catocli mutation notification integration updateWebhook <json>

catocli mutation notification integration updateWebhook --json-file mutation.notification.integration.updateWebhook.json

catocli mutation notification integration updateWebhook '{"updateWebhookInput":{"auth":{"basic":{"password":"replace-with-your-secret","username":"string"},"bearer":{"bearerToken":"replace-with-your-secret"},"custom":{"name":"string","value":"replace-with-your-secret"}},"body":"string","enabled":true,"header":[{"name":"X-Example","value":"example"}],"headerToAdd":[{"name":"X-Example","value":"example"}],"headerToRemove":[{"name":"X-Example","value":"example"}],"name":"string","relatedWebhookRef":{"by":"ID","input":"string"},"requestMethod":"POST","responseMapping":[{"key":"string","value":"string"}],"responseMappingToAdd":[{"key":"string","value":"string"}],"responseMappingToRemove":[{"key":"string","value":"string"}],"url":"https://example.com/","webhook":{"by":"ID","input":"string"}}}'

catocli mutation notification integration updateWebhook '{
    "updateWebhookInput": {
        "auth": {
            "basic": {
                "password": "replace-with-your-secret",
                "username": "string"
            },
            "bearer": {
                "bearerToken": "replace-with-your-secret"
            },
            "custom": {
                "name": "string",
                "value": "replace-with-your-secret"
            }
        },
        "body": "string",
        "enabled": true,
        "header": [
            {
                "name": "X-Example",
                "value": "example"
            }
        ],
        "headerToAdd": [
            {
                "name": "X-Example",
                "value": "example"
            }
        ],
        "headerToRemove": [
            {
                "name": "X-Example",
                "value": "example"
            }
        ],
        "name": "string",
        "relatedWebhookRef": {
            "by": "ID",
            "input": "string"
        },
        "requestMethod": "POST",
        "responseMapping": [
            {
                "key": "string",
                "value": "string"
            }
        ],
        "responseMappingToAdd": [
            {
                "key": "string",
                "value": "string"
            }
        ],
        "responseMappingToRemove": [
            {
                "key": "string",
                "value": "string"
            }
        ],
        "url": "https://example.com/",
        "webhook": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.notification.integration.updateWebhook ####

`accountId` [ID] - (required) N/A
`updateWebhookInput` [UpdateWebhookInput] - (required) N/A
