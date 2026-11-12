
## CATO-CLI - mutation.notification.integration.createWebhook:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.notification.integration.createWebhook) for documentation on this operation.

### Usage for mutation.notification.integration.createWebhook:

```bash
catocli mutation notification integration createWebhook -h

catocli mutation notification integration createWebhook <json>

catocli mutation notification integration createWebhook --json-file mutation.notification.integration.createWebhook.json

catocli mutation notification integration createWebhook '{"createWebhookInput":{"auth":{"basic":{"password":"replace-with-your-secret","username":"string"},"bearer":{"bearerToken":"replace-with-your-secret"},"custom":{"name":"string","value":"replace-with-your-secret"}},"body":"string","enabled":true,"header":[{"name":"X-Example","value":"example"}],"name":"string","relatedWebhookRef":{"by":"ID","input":"string"},"requestMethod":"POST","responseMapping":[{"key":"string","value":"string"}],"url":"https://example.com/"}}'

catocli mutation notification integration createWebhook '{
    "createWebhookInput": {
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
        "url": "https://example.com/"
    }
}'
```

#### Operation Arguments for mutation.notification.integration.createWebhook ####

`accountId` [ID] - (required) N/A
`createWebhookInput` [CreateWebhookInput] - (required) N/A
