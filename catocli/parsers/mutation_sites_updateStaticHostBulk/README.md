
## CATO-CLI - mutation.sites.updateStaticHostBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateStaticHostBulk) for documentation on this operation.

### Usage for mutation.sites.updateStaticHostBulk:

```bash
catocli mutation sites updateStaticHostBulk -h

catocli mutation sites updateStaticHostBulk <json>

catocli mutation sites updateStaticHostBulk --json-file mutation.sites.updateStaticHostBulk.json

catocli mutation sites updateStaticHostBulk '{"updateStaticHostBulkInput":{"host":{"hostId":"id","ip":"example_value","macAddress":"string","name":"string"},"site":{"by":"ID","input":"string"}}}'

catocli mutation sites updateStaticHostBulk '{
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

#### Operation Arguments for mutation.sites.updateStaticHostBulk ####

`accountId` [ID] - (required) N/A    
`updateStaticHostBulkInput` [UpdateStaticHostBulkInput] - (required) N/A    
