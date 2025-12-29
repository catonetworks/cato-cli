
## CATO-CLI - mutation.container.ipAddressRange.createFromURL:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.ipAddressRange.createFromURL) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.createFromURL:

```bash
catocli mutation container ipAddressRange createFromURL -h

catocli mutation container ipAddressRange createFromURL <json>

catocli mutation container ipAddressRange createFromURL --json-file mutation.container.ipAddressRange.createFromURL.json

catocli mutation container ipAddressRange createFromURL '{"createIpAddressRangeContainerFromUrlInput":{"createContainerSyncDataInput":{"notifications":{"mailingList":{"by":"ID","input":"string"},"subscriptionGroup":{"by":"ID","input":"string"},"webhook":{"by":"ID","input":"string"}},"timeInterval":1,"timeUnit":"HOUR","url":"example_value"},"description":"string","fileType":"STIX","name":"string"}}'

catocli mutation container ipAddressRange createFromURL '{
    "createIpAddressRangeContainerFromUrlInput": {
        "createContainerSyncDataInput": {
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
        },
        "description": "string",
        "fileType": "STIX",
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.container.ipAddressRange.createFromURL ####

`accountId` [ID] - (required) N/A    
`createIpAddressRangeContainerFromUrlInput` [CreateIpAddressRangeContainerFromUrlInput] - (required) N/A    
