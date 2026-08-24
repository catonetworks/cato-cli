
## CATO-CLI - mutation.site.deleteNetworkRangeBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.deleteNetworkRangeBulk) for documentation on this operation.

### Usage for mutation.site.deleteNetworkRangeBulk:

```bash
catocli mutation site deleteNetworkRangeBulk -h

catocli mutation site deleteNetworkRangeBulk <json>

catocli mutation site deleteNetworkRangeBulk --json-file mutation.site.deleteNetworkRangeBulk.json

catocli mutation site deleteNetworkRangeBulk '{"deleteNetworkRangeBulkInput":{"networkRangeRefInput":{"networkRangeId":"id"},"siteRefInput":{"by":"ID","input":"string"}}}'

catocli mutation site deleteNetworkRangeBulk '{
    "deleteNetworkRangeBulkInput": {
        "networkRangeRefInput": {
            "networkRangeId": "id"
        },
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.deleteNetworkRangeBulk ####

`accountId` [ID] - (required) N/A    
`deleteNetworkRangeBulkInput` [DeleteNetworkRangeBulkInput] - (required) N/A    
