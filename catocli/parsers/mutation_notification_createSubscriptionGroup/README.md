
## CATO-CLI - mutation.notification.createSubscriptionGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.notification.createSubscriptionGroup) for documentation on this operation.

### Usage for mutation.notification.createSubscriptionGroup:

```bash
catocli mutation notification createSubscriptionGroup -h

catocli mutation notification createSubscriptionGroup <json>

catocli mutation notification createSubscriptionGroup --json-file mutation.notification.createSubscriptionGroup.json

catocli mutation notification createSubscriptionGroup '{"createSubscriptionGroupInput":{"integrationRefInput":{"by":"ID","input":"string"},"mailingListRefInput":{"by":"ID","input":"string"},"name":"string"}}'

catocli mutation notification createSubscriptionGroup '{
    "createSubscriptionGroupInput": {
        "integrationRefInput": {
            "by": "ID",
            "input": "string"
        },
        "mailingListRefInput": {
            "by": "ID",
            "input": "string"
        },
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.notification.createSubscriptionGroup ####

`accountId` [ID] - (required) N/A    
`createSubscriptionGroupInput` [CreateSubscriptionGroupInput] - (required) N/A    
