
## CATO-CLI - mutation.container.ipAddressRange.addValues:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.ipAddressRange.addValues) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.addValues:

```bash
catocli mutation container ipAddressRange addValues -h

catocli mutation container ipAddressRange addValues <json>

catocli mutation container ipAddressRange addValues --json-file mutation.container.ipAddressRange.addValues.json

catocli mutation container ipAddressRange addValues '{"ipAddressRangeContainerAddValuesInput":{"ref":{"by":"ID","input":"string"},"values":[{"from":"192.0.2.1","to":"192.0.2.1"}]}}'

catocli mutation container ipAddressRange addValues '{
    "ipAddressRangeContainerAddValuesInput": {
        "ref": {
            "by": "ID",
            "input": "string"
        },
        "values": [
            {
                "from": "192.0.2.1",
                "to": "192.0.2.1"
            }
        ]
    }
}'
```

#### Operation Arguments for mutation.container.ipAddressRange.addValues ####

`accountId` [ID] - (required) N/A
`ipAddressRangeContainerAddValuesInput` [IpAddressRangeContainerAddValuesInput] - (required) N/A
