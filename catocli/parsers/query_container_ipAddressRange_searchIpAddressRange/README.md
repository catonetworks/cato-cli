
## CATO-CLI - query.container.ipAddressRange.searchIpAddressRange:
[Click here](https://api.catonetworks.com/documentation/#query-query.container.ipAddressRange.searchIpAddressRange) for documentation on this operation.

### Usage for query.container.ipAddressRange.searchIpAddressRange:

```bash
catocli query container ipAddressRange searchIpAddressRange -h

catocli query container ipAddressRange searchIpAddressRange <json>

catocli query container ipAddressRange searchIpAddressRange --json-file query.container.ipAddressRange.searchIpAddressRange.json

catocli query container ipAddressRange searchIpAddressRange '{"ipAddressRangeContainerSearchIpAddressRangeInput":{"ipAddressRange":{"from":"192.0.2.1","to":"192.0.2.1"}}}'

catocli query container ipAddressRange searchIpAddressRange '{
    "ipAddressRangeContainerSearchIpAddressRangeInput": {
        "ipAddressRange": {
            "from": "192.0.2.1",
            "to": "192.0.2.1"
        }
    }
}'
```

#### Operation Arguments for query.container.ipAddressRange.searchIpAddressRange ####

`accountId` [ID] - (required) N/A
`ipAddressRangeContainerSearchIpAddressRangeInput` [IpAddressRangeContainerSearchIpAddressRangeInput] - (required) N/A
