
## CATO-CLI - mutation.sites.deleteStaticHostBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.deleteStaticHostBulk) for documentation on this operation.

### Usage for mutation.sites.deleteStaticHostBulk:

```bash
catocli mutation sites deleteStaticHostBulk -h

catocli mutation sites deleteStaticHostBulk <json>

catocli mutation sites deleteStaticHostBulk --json-file mutation.sites.deleteStaticHostBulk.json

catocli mutation sites deleteStaticHostBulk '{"deleteStaticHostBulkInput":{"host":{"hostId":"id"},"site":{"by":"ID","input":"string"}}}'

catocli mutation sites deleteStaticHostBulk '{
    "deleteStaticHostBulkInput": {
        "host": {
            "hostId": "id"
        },
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.deleteStaticHostBulk ####

`accountId` [ID] - (required) N/A    
`deleteStaticHostBulkInput` [DeleteStaticHostBulkInput] - (required) N/A    
