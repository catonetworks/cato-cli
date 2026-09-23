
## CATO-CLI - mutation.container.fqdn.createFromURL:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.fqdn.createFromURL) for documentation on this operation.

### Usage for mutation.container.fqdn.createFromURL:

```bash
catocli mutation container fqdn createFromURL -h

catocli mutation container fqdn createFromURL <json>

catocli mutation container fqdn createFromURL --json-file mutation.container.fqdn.createFromURL.json

catocli mutation container fqdn createFromURL '{"createFqdnContainerFromUrlInput":{"description":"string","fileType":"STIX","name":"string","syncData":{"notifications":{"mailingList":{"by":"ID","input":"string"},"subscriptionGroup":{"by":"ID","input":"string"},"webhook":{"by":"ID","input":"string"}},"timeInterval":1,"timeUnit":"HOUR","url":"example_value"}}}'

catocli mutation container fqdn createFromURL '{
    "createFqdnContainerFromUrlInput": {
        "description": "string",
        "fileType": "STIX",
        "name": "string",
        "syncData": {
            "notifications": {
                "mailingList": {
                    "by": "ID",
                    "input": "string"
                },
                "subscriptionGroup": {
                    "by": "ID",
                    "input": "string"
                },
                "webhook": {
                    "by": "ID",
                    "input": "string"
                }
            },
            "timeInterval": 1,
            "timeUnit": "HOUR",
            "url": "example_value"
        }
    }
}'
```

#### Operation Arguments for mutation.container.fqdn.createFromURL ####

`accountId` [ID] - (required) N/A    
`createFqdnContainerFromUrlInput` [CreateFqdnContainerFromUrlInput] - (required) N/A    
