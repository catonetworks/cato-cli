
## CATO-CLI - query.container.ipAddressRange.downloadFile:
[Click here](https://api.catonetworks.com/documentation/#query-query.container.ipAddressRange.downloadFile) for documentation on this operation.

### Usage for query.container.ipAddressRange.downloadFile:

```bash
catocli query container ipAddressRange downloadFile -h

catocli query container ipAddressRange downloadFile <json>

catocli query container ipAddressRange downloadFile "$(cat < query.container.ipAddressRange.downloadFile.json)"

catocli query container ipAddressRange downloadFile '{"downloadIpAddressRangeContainerFileInput":{"by":"ID","input":"string"}}'

catocli query container ipAddressRange downloadFile '{
    "downloadIpAddressRangeContainerFileInput": {
        "by": "ID",
        "input": "string"
    }
}'
```

#### Operation Arguments for query.container.ipAddressRange.downloadFile ####

`accountId` [ID] - (required) N/A    
`downloadIpAddressRangeContainerFileInput` [DownloadIpAddressRangeContainerFileInput] - (required) N/A    
