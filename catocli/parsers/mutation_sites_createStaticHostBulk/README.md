
## CATO-CLI - mutation.sites.createStaticHostBulk:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.createStaticHostBulk) for documentation on this operation.

### Usage for mutation.sites.createStaticHostBulk:

```bash
catocli mutation sites createStaticHostBulk -h

catocli mutation sites createStaticHostBulk <json>

catocli mutation sites createStaticHostBulk --json-file mutation.sites.createStaticHostBulk.json

catocli mutation sites createStaticHostBulk '{"createStaticHostBulkInput":{"siteAddStaticHostInput":{"ip":"example_value","macAddress":"example_value","name":"string"},"siteRefInput":{"by":"ID","input":"string"}}}'

catocli mutation sites createStaticHostBulk '{
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

#### Operation Arguments for mutation.sites.createStaticHostBulk ####

`accountId` [ID] - (required) N/A    
`createStaticHostBulkInput` [CreateStaticHostBulkInput] - (required) N/A    
