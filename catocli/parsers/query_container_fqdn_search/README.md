
## CATO-CLI - query.container.fqdn.search:
[Click here](https://api.catonetworks.com/documentation/#query-query.container.fqdn.search) for documentation on this operation.

### Usage for query.container.fqdn.search:

```bash
catocli query container fqdn search -h

catocli query container fqdn search <json>

catocli query container fqdn search "$(cat < query.container.fqdn.search.json)"

catocli query container fqdn search '{"fqdnContainerSearchInput":{"containerRefInput":{"by":"ID","input":"string"}}}'

catocli query container fqdn search '{
    "fqdnContainerSearchInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for query.container.fqdn.search ####

`accountId` [ID] - (required) N/A    
`fqdnContainerSearchInput` [FqdnContainerSearchInput] - (required) N/A    
