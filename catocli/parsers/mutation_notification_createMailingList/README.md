
## CATO-CLI - mutation.notification.createMailingList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.notification.createMailingList) for documentation on this operation.

### Usage for mutation.notification.createMailingList:

```bash
catocli mutation notification createMailingList -h

catocli mutation notification createMailingList <json>

catocli mutation notification createMailingList --json-file mutation.notification.createMailingList.json

catocli mutation notification createMailingList '{"createMailingListInput":{"address":["example1","example2"],"adminRefInput":{"by":"ID","input":"string"},"name":"string"}}'

catocli mutation notification createMailingList '{
    "createMailingListInput": {
        "address": [
            "example1",
            "example2"
        ],
        "adminRefInput": {
            "by": "ID",
            "input": "string"
        },
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.notification.createMailingList ####

`accountId` [ID] - (required) N/A    
`createMailingListInput` [CreateMailingListInput] - (required) N/A    
