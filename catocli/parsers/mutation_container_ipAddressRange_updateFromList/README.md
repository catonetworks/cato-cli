
## CATO-CLI - mutation.container.ipAddressRange.updateFromList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.ipAddressRange.updateFromList) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.updateFromList:

```bash
catocli mutation container ipAddressRange updateFromList -h

catocli mutation container ipAddressRange updateFromList <json>

catocli mutation container ipAddressRange updateFromList --json-file mutation.container.ipAddressRange.updateFromList.json

catocli mutation container ipAddressRange updateFromList '{"updateIpAddressRangeContainerFromListInput":{"description":"string","ref":{"by":"ID","input":"string"},"values":[{"from":"192.0.2.1","to":"192.0.2.1"}]}}'

catocli mutation container ipAddressRange updateFromList '{
    "updateIpAddressRangeContainerFromListInput": {
        "description": "string",
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

#### Operation Arguments for mutation.container.ipAddressRange.updateFromList ####

`accountId` [ID] - (required) N/A
`updateIpAddressRangeContainerFromListInput` [UpdateIpAddressRangeContainerFromListInput] - (required) N/A
