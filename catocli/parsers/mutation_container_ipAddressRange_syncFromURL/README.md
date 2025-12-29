
## CATO-CLI - mutation.container.ipAddressRange.syncFromURL:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.ipAddressRange.syncFromURL) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.syncFromURL:

```bash
catocli mutation container ipAddressRange syncFromURL -h

catocli mutation container ipAddressRange syncFromURL <json>

catocli mutation container ipAddressRange syncFromURL --json-file mutation.container.ipAddressRange.syncFromURL.json

catocli mutation container ipAddressRange syncFromURL '{"syncIpAddressRangeContainerFromUrlInput":{"containerRefInput":{"by":"ID","input":"string"}}}'

catocli mutation container ipAddressRange syncFromURL '{
    "syncIpAddressRangeContainerFromUrlInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.container.ipAddressRange.syncFromURL ####

`accountId` [ID] - (required) N/A    
`syncIpAddressRangeContainerFromUrlInput` [SyncIpAddressRangeContainerFromUrlInput] - (required) N/A    
