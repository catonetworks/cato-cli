
## CATO-CLI - mutation.site.updateStaticHostBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateStaticHostBulk) for documentation on this operation.

### Usage for mutation.site.updateStaticHostBulk:

```bash
catocli mutation site updateStaticHostBulk -h

catocli mutation site updateStaticHostBulk <json>

catocli mutation site updateStaticHostBulk --json-file mutation.site.updateStaticHostBulk.json

catocli mutation site updateStaticHostBulk '{"updateStaticHostBulkInput":{"host":{"hostId":"id","ip":"example_value","macAddress":"string","name":"string"},"site":{"by":"ID","input":"string"}}}'

catocli mutation site updateStaticHostBulk '{
    "updateStaticHostBulkInput": {
        "host": {
            "hostId": "id",
            "ip": "example_value",
            "macAddress": "string",
            "name": "string"
        },
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.updateStaticHostBulk ####

`accountId` [ID] - (required) N/A    
`updateStaticHostBulkInput` [UpdateStaticHostBulkInput] - (required) N/A    
