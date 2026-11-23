
## CATO-CLI - mutation.container.ipAddressRange.updateFromURL:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.ipAddressRange.updateFromURL) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.updateFromURL:

```bash
catocli mutation container ipAddressRange updateFromURL -h

catocli mutation container ipAddressRange updateFromURL <json>

catocli mutation container ipAddressRange updateFromURL --json-file mutation.container.ipAddressRange.updateFromURL.json

catocli mutation container ipAddressRange updateFromURL '{"updateIpAddressRangeContainerFromUrlInput":{"description":"string","fileType":"STIX","ref":{"by":"ID","input":"string"},"syncData":{"notifications":{"mailingList":[{"by":"ID","input":"string"}],"subscriptionGroup":[{"by":"ID","input":"string"}],"webhook":[{"by":"ID","input":"string"}]},"timeInterval":1,"timeUnit":"HOUR","url":"https://example.com/"}}}'

catocli mutation container ipAddressRange updateFromURL '{
    "updateIpAddressRangeContainerFromUrlInput": {
        "description": "string",
        "fileType": "STIX",
        "ref": {
            "by": "ID",
            "input": "string"
        },
        "syncData": {
            "notifications": {
                "mailingList": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "subscriptionGroup": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ],
                "webhook": [
                    {
                        "by": "ID",
                        "input": "string"
                    }
                ]
            },
            "timeInterval": 1,
            "timeUnit": "HOUR",
            "url": "https://example.com/"
        }
    }
}'
```

#### Operation Arguments for mutation.container.ipAddressRange.updateFromURL ####

`accountId` [ID] - (required) ID of the account whose containers are accessed.
`updateIpAddressRangeContainerFromUrlInput` [UpdateIpAddressRangeContainerFromUrlInput] - (required) Container reference and URL synchronization settings to update.
