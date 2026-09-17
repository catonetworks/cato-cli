
## CATO-CLI - mutation.site.deleteStaticHostBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.deleteStaticHostBulk) for documentation on this operation.

### Usage for mutation.site.deleteStaticHostBulk:

```bash
catocli mutation site deleteStaticHostBulk -h

catocli mutation site deleteStaticHostBulk <json>

catocli mutation site deleteStaticHostBulk --json-file mutation.site.deleteStaticHostBulk.json

catocli mutation site deleteStaticHostBulk '{"deleteStaticHostBulkInput":{"host":{"hostId":"id"},"site":{"by":"ID","input":"string"}}}'

catocli mutation site deleteStaticHostBulk '{
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

#### Operation Arguments for mutation.site.deleteStaticHostBulk ####

`accountId` [ID] - (required) N/A    
`deleteStaticHostBulkInput` [DeleteStaticHostBulkInput] - (required) N/A    
