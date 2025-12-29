
## CATO-CLI - mutation.container.fqdn.updateFromURL:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.fqdn.updateFromURL) for documentation on this operation.

### Usage for mutation.container.fqdn.updateFromURL:

```bash
catocli mutation container fqdn updateFromURL -h

catocli mutation container fqdn updateFromURL <json>

catocli mutation container fqdn updateFromURL --json-file mutation.container.fqdn.updateFromURL.json

catocli mutation container fqdn updateFromURL '{"updateFqdnContainerFromUrlInput":{"containerRefInput":{"by":"ID","input":"string"},"description":"string","fileType":"STIX","updateContainerSyncDataInput":{"notifications":{"mailingList":{"by":"ID","input":"string"},"subscriptionGroup":{"by":"ID","input":"string"},"webhook":{"by":"ID","input":"string"}},"timeInterval":1,"timeUnit":"HOUR","url":"example_value"}}}'

catocli mutation container fqdn updateFromURL '{
    "updateFqdnContainerFromUrlInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        },
        "description": "string",
        "fileType": "STIX",
        "updateContainerSyncDataInput": {
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

#### Operation Arguments for mutation.container.fqdn.updateFromURL ####

`accountId` [ID] - (required) N/A    
`updateFqdnContainerFromUrlInput` [UpdateFqdnContainerFromUrlInput] - (required) N/A    
