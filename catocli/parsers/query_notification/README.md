
## CATO-CLI - query.notification:
[Click here](https://api.catonetworks.com/documentation/#query-query.notification) for documentation on this operation.

### Usage for query.notification:

```bash
catocli query notification -h

catocli query notification <json>

catocli query notification --json-file query.notification.json

catocli query notification '{"mailingListRefInput":{"by":"ID","input":"string"},"subscriptionGroupRefInput":{"by":"ID","input":"string"},"webhookIntegrationRefInput":{"by":"ID","input":"string"},"webhookTemplateRefInput":{"by":"ID","input":"string"}}'

catocli query notification '{
    "mailingListRefInput": {
        "by": "ID",
        "input": "string"
    },
    "subscriptionGroupRefInput": {
        "by": "ID",
        "input": "string"
    },
    "webhookIntegrationRefInput": {
        "by": "ID",
        "input": "string"
    },
    "webhookTemplateRefInput": {
        "by": "ID",
        "input": "string"
    }
}'
```

#### Operation Arguments for query.notification ####

`accountId` [ID] - (required) N/A    
`mailingListRefInput` [MailingListRefInput] - (required) N/A    
`subscriptionGroupRefInput` [SubscriptionGroupRefInput] - (required) N/A    
`webhookIntegrationRefInput` [WebhookIntegrationRefInput] - (required) N/A    
`webhookTemplateRefInput` [WebhookTemplateRefInput] - (required) N/A    
