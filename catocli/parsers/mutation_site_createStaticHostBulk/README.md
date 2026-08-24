
## CATO-CLI - mutation.site.createStaticHostBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.createStaticHostBulk) for documentation on this operation.

### Usage for mutation.site.createStaticHostBulk:

```bash
catocli mutation site createStaticHostBulk -h

catocli mutation site createStaticHostBulk <json>

catocli mutation site createStaticHostBulk --json-file mutation.site.createStaticHostBulk.json

catocli mutation site createStaticHostBulk '{"createStaticHostBulkInput":{"siteAddStaticHostInput":{"ip":"example_value","macAddress":"example_value","name":"string"},"siteRefInput":{"by":"ID","input":"string"}}}'

catocli mutation site createStaticHostBulk '{
    "createStaticHostBulkInput": {
        "siteAddStaticHostInput": {
            "ip": "example_value",
            "macAddress": "example_value",
            "name": "string"
        },
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.createStaticHostBulk ####

`accountId` [ID] - (required) N/A    
`createStaticHostBulkInput` [CreateStaticHostBulkInput] - (required) N/A    
