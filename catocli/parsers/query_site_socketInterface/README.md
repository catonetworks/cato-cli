
## CATO-CLI - query.site.socketInterface:
[Click here](https://api.catonetworks.com/documentation/#query-query.site.socketInterface) for documentation on this operation.

### Usage for query.site.socketInterface:

```bash
catocli query site socketInterface -h

catocli query site socketInterface <json>

catocli query site socketInterface --json-file query.site.socketInterface.json

catocli query site socketInterface '{"siteSocketInterfaceInput":{"site":{"by":"ID","input":"string"},"socketInterfaceId":"LAN1"}}'

catocli query site socketInterface '{
    "siteSocketInterfaceInput": {
        "site": {
            "by": "ID",
            "input": "string"
        },
        "socketInterfaceId": "LAN1"
    }
}'
```

#### Operation Arguments for query.site.socketInterface ####

`accountId` [ID] - (required) N/A
`siteSocketInterfaceInput` [SiteSocketInterfaceInput] - (required) N/A
