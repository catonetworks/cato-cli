
## CATO-CLI - mutation.sites.deleteStaticHostBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.deleteStaticHostBulk) for documentation on this operation.

### Usage for mutation.sites.deleteStaticHostBulk:

```bash
catocli mutation sites deleteStaticHostBulk -h

catocli mutation sites deleteStaticHostBulk <json>

catocli mutation sites deleteStaticHostBulk --json-file mutation.sites.deleteStaticHostBulk.json

catocli mutation sites deleteStaticHostBulk '{"deleteStaticHostBulkInput":{"siteRefInput":{"by":"ID","input":"string"},"siteStaticHostRefInput":{"hostId":"id"}}}'

catocli mutation sites deleteStaticHostBulk '{
    "deleteStaticHostBulkInput": {
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        },
        "siteStaticHostRefInput": {
            "hostId": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.deleteStaticHostBulk ####

`accountId` [ID] - (required) N/A    
`deleteStaticHostBulkInput` [DeleteStaticHostBulkInput] - (required) N/A    
