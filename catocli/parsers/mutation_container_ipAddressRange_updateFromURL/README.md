
## CATO-CLI - mutation.container.ipAddressRange.updateFromURL:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.ipAddressRange.updateFromURL) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.updateFromURL:

```bash
catocli mutation container ipAddressRange updateFromURL -h

catocli mutation container ipAddressRange updateFromURL <json>

catocli mutation container ipAddressRange updateFromURL --json-file mutation.container.ipAddressRange.updateFromURL.json

catocli mutation container ipAddressRange updateFromURL '{"updateIpAddressRangeContainerFromUrlInput":{"containerRefInput":{"by":"ID","input":"string"},"description":"string","fileType":"STIX","updateContainerSyncDataInput":{"notifications":{"mailingList":{"by":"ID","input":"string"},"subscriptionGroup":{"by":"ID","input":"string"},"webhook":{"by":"ID","input":"string"}},"timeInterval":1,"timeUnit":"HOUR","url":"example_value"}}}'

catocli mutation container ipAddressRange updateFromURL '{
    "updateIpAddressRangeContainerFromUrlInput": {
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

#### Operation Arguments for mutation.container.ipAddressRange.updateFromURL ####

`accountId` [ID] - (required) N/A    
`updateIpAddressRangeContainerFromUrlInput` [UpdateIpAddressRangeContainerFromUrlInput] - (required) N/A    
