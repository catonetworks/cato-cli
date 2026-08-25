
## CATO-CLI - mutation.site.deleteBgpPeerBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.deleteBgpPeerBulk) for documentation on this operation.

### Usage for mutation.site.deleteBgpPeerBulk:

```bash
catocli mutation site deleteBgpPeerBulk -h

catocli mutation site deleteBgpPeerBulk <json>

catocli mutation site deleteBgpPeerBulk --json-file mutation.site.deleteBgpPeerBulk.json

catocli mutation site deleteBgpPeerBulk '{"deleteBgpPeerBulkInput":{"bgpPeerRefInput":{"by":"ID","input":"string"},"siteRefInput":{"by":"ID","input":"string"}}}'

catocli mutation site deleteBgpPeerBulk '{
    "deleteBgpPeerBulkInput": {
        "bgpPeerRefInput": {
            "by": "ID",
            "input": "string"
        },
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.deleteBgpPeerBulk ####

`accountId` [ID] - (required) N/A    
`deleteBgpPeerBulkInput` [DeleteBgpPeerBulkInput] - (required) N/A    
