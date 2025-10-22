
## CATO-CLI - query.container.list:
[Click here](https://api.catonetworks.com/documentation/#query-query.container.list) for documentation on this operation.

### Usage for query.container.list:

```bash
catocli query container list -h

catocli query container list <json>

catocli query container list "$(cat < query.container.list.json)"

catocli query container list '{"containerSearchInput":{"containerRefInput":{"by":"ID","input":"string"},"types":"IP_RANGE"}}'

catocli query container list '{
    "containerSearchInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        },
        "types": "IP_RANGE"
    }
}'
```

#### Operation Arguments for query.container.list ####

`accountId` [ID] - (required) N/A    
`containerSearchInput` [ContainerSearchInput] - (required) N/A    
