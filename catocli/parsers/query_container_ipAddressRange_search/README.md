
## CATO-CLI - query.container.ipAddressRange.search:
[Click here](https://api.catonetworks.com/documentation/#query-query.container.ipAddressRange.search) for documentation on this operation.

### Usage for query.container.ipAddressRange.search:

```bash
catocli query container ipAddressRange search -h

catocli query container ipAddressRange search <json>

catocli query container ipAddressRange search --json-file query.container.ipAddressRange.search.json

catocli query container ipAddressRange search '{"ipAddressRangeContainerSearchInput":{"ref":{"by":"ID","input":"string"}}}'

catocli query container ipAddressRange search '{
    "ipAddressRangeContainerSearchInput": {
        "ref": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for query.container.ipAddressRange.search ####

`accountId` [ID] - (required) ID of the account whose containers are accessed.
`ipAddressRangeContainerSearchInput` [IpAddressRangeContainerSearchInput] - (required) Reference identifying the container to retrieve.
