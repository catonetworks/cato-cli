
## CATO-CLI - query.container.fqdn.downloadFile:
[Click here](https://api.catonetworks.com/documentation/#query-query.container.fqdn.downloadFile) for documentation on this operation.

### Usage for query.container.fqdn.downloadFile:

```bash
catocli query container fqdn downloadFile -h

catocli query container fqdn downloadFile <json>

catocli query container fqdn downloadFile "$(cat < query.container.fqdn.downloadFile.json)"

catocli query container fqdn downloadFile '{"downloadFqdnContainerFileInput":{"by":"ID","input":"string"}}'

catocli query container fqdn downloadFile '{
    "downloadFqdnContainerFileInput": {
        "by": "ID",
        "input": "string"
    }
}'
```

#### Operation Arguments for query.container.fqdn.downloadFile ####

`accountId` [ID] - (required) N/A    
`downloadFqdnContainerFileInput` [DownloadFqdnContainerFileInput] - (required) N/A    
