
## CATO-CLI - mutation.container.ipAddressRange.createFromList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.ipAddressRange.createFromList) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.createFromList:

```bash
catocli mutation container ipAddressRange createFromList -h

catocli mutation container ipAddressRange createFromList <json>

catocli mutation container ipAddressRange createFromList --json-file mutation.container.ipAddressRange.createFromList.json

catocli mutation container ipAddressRange createFromList '{"createIpAddressRangeContainerFromListInput":{"description":"string","name":"string","values":[{"from":"192.0.2.1","to":"192.0.2.1"}]}}'

catocli mutation container ipAddressRange createFromList '{
    "createIpAddressRangeContainerFromListInput": {
        "description": "string",
        "name": "string",
        "values": [
            {
                "from": "192.0.2.1",
                "to": "192.0.2.1"
            }
        ]
    }
}'
```

#### Operation Arguments for mutation.container.ipAddressRange.createFromList ####

`accountId` [ID] - (required) N/A
`createIpAddressRangeContainerFromListInput` [CreateIpAddressRangeContainerFromListInput] - (required) N/A
