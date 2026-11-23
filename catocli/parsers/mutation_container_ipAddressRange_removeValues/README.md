
## CATO-CLI - mutation.container.ipAddressRange.removeValues:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.ipAddressRange.removeValues) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.removeValues:

```bash
catocli mutation container ipAddressRange removeValues -h

catocli mutation container ipAddressRange removeValues <json>

catocli mutation container ipAddressRange removeValues --json-file mutation.container.ipAddressRange.removeValues.json

catocli mutation container ipAddressRange removeValues '{"ipAddressRangeContainerRemoveValuesInput":{"ref":{"by":"ID","input":"string"},"values":[{"from":"192.0.2.1","to":"192.0.2.1"}]}}'

catocli mutation container ipAddressRange removeValues '{
    "ipAddressRangeContainerRemoveValuesInput": {
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

#### Operation Arguments for mutation.container.ipAddressRange.removeValues ####

`accountId` [ID] - (required) ID of the account whose containers are accessed.
`ipAddressRangeContainerRemoveValuesInput` [IpAddressRangeContainerRemoveValuesInput] - (required) Container reference and values to remove.
