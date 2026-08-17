
## CATO-CLI - mutation.sites.deleteBgpPeerBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.deleteBgpPeerBulk) for documentation on this operation.

### Usage for mutation.sites.deleteBgpPeerBulk:

```bash
catocli mutation sites deleteBgpPeerBulk -h

catocli mutation sites deleteBgpPeerBulk <json>

catocli mutation sites deleteBgpPeerBulk --json-file mutation.sites.deleteBgpPeerBulk.json

catocli mutation sites deleteBgpPeerBulk '{"deleteBgpPeerBulkInput":{"bgpPeerRefInput":{"by":"ID","input":"string"},"siteRefInput":{"by":"ID","input":"string"}}}'

catocli mutation sites deleteBgpPeerBulk '{
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

#### Operation Arguments for mutation.sites.deleteBgpPeerBulk ####

`accountId` [ID] - (required) N/A    
`deleteBgpPeerBulkInput` [DeleteBgpPeerBulkInput] - (required) N/A    
