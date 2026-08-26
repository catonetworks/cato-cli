
## CATO-CLI - mutation.sites.deleteNetworkRangeBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.deleteNetworkRangeBulk) for documentation on this operation.

### Usage for mutation.sites.deleteNetworkRangeBulk:

```bash
catocli mutation sites deleteNetworkRangeBulk -h

catocli mutation sites deleteNetworkRangeBulk <json>

catocli mutation sites deleteNetworkRangeBulk --json-file mutation.sites.deleteNetworkRangeBulk.json

catocli mutation sites deleteNetworkRangeBulk '{"deleteNetworkRangeBulkInput":{"networkRange":{"networkRangeId":"id"},"site":{"by":"ID","input":"string"}}}'

catocli mutation sites deleteNetworkRangeBulk '{
    "deleteNetworkRangeBulkInput": {
        "networkRange": {
            "networkRangeId": "id"
        },
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.deleteNetworkRangeBulk ####

`accountId` [ID] - (required) N/A    
`deleteNetworkRangeBulkInput` [DeleteNetworkRangeBulkInput] - (required) N/A    
