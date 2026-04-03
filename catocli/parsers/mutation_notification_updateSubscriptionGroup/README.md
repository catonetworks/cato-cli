
## CATO-CLI - mutation.notification.updateSubscriptionGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.notification.updateSubscriptionGroup) for documentation on this operation.

### Usage for mutation.notification.updateSubscriptionGroup:

```bash
catocli mutation notification updateSubscriptionGroup -h

catocli mutation notification updateSubscriptionGroup <json>

catocli mutation notification updateSubscriptionGroup --json-file mutation.notification.updateSubscriptionGroup.json

catocli mutation notification updateSubscriptionGroup '{"updateSubscriptionGroupInput":{"integrationRefInput":{"by":"ID","input":"string"},"mailingListRefInput":{"by":"ID","input":"string"},"name":"string","subscriptionGroupRefInput":{"by":"ID","input":"string"}}}'

catocli mutation notification updateSubscriptionGroup '{
    "updateSubscriptionGroupInput": {
        "integrationRefInput": {
            "by": "ID",
            "input": "string"
        },
        "mailingListRefInput": {
            "by": "ID",
            "input": "string"
        },
        "name": "string",
        "subscriptionGroupRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.notification.updateSubscriptionGroup ####

`accountId` [ID] - (required) N/A    
`updateSubscriptionGroupInput` [UpdateSubscriptionGroupInput] - (required) N/A    
