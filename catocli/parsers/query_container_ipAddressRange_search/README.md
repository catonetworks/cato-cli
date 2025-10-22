
## CATO-CLI - query.container.ipAddressRange.search:
[Click here](https://api.catonetworks.com/documentation/#query-query.container.ipAddressRange.search) for documentation on this operation.

### Usage for query.container.ipAddressRange.search:

```bash
catocli query container ipAddressRange search -h

catocli query container ipAddressRange search <json>

catocli query container ipAddressRange search "$(cat < query.container.ipAddressRange.search.json)"

catocli query container ipAddressRange search '{"ipAddressRangeContainerSearchInput":{"containerRefInput":{"by":"ID","input":"string"}}}'

catocli query container ipAddressRange search '{
    "ipAddressRangeContainerSearchInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for query.container.ipAddressRange.search ####

`accountId` [ID] - (required) N/A    
`ipAddressRangeContainerSearchInput` [IpAddressRangeContainerSearchInput] - (required) N/A    
