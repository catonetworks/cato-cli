
## CATO-CLI - mutation.notification.updateMailingList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.notification.updateMailingList) for documentation on this operation.

### Usage for mutation.notification.updateMailingList:

```bash
catocli mutation notification updateMailingList -h

catocli mutation notification updateMailingList <json>

catocli mutation notification updateMailingList --json-file mutation.notification.updateMailingList.json

catocli mutation notification updateMailingList '{"updateMailingListInput":{"address":["example1","example2"],"addressToAdd":["example1","example2"],"addressToRemove":["example1","example2"],"adminRefInput":{"by":"ID","input":"string"},"mailingListRefInput":{"by":"ID","input":"string"},"name":"string"}}'

catocli mutation notification updateMailingList '{
    "updateMailingListInput": {
        "address": [
            "example1",
            "example2"
        ],
        "addressToAdd": [
            "example1",
            "example2"
        ],
        "addressToRemove": [
            "example1",
            "example2"
        ],
        "adminRefInput": {
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

#### Operation Arguments for mutation.notification.updateMailingList ####

`accountId` [ID] - (required) N/A    
`updateMailingListInput` [UpdateMailingListInput] - (required) N/A    
