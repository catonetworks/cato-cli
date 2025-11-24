
## CATO-CLI - mutation.container.ipAddressRange.createFromList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.ipAddressRange.createFromList) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.createFromList:

```bash
catocli mutation container ipAddressRange createFromList -h

catocli mutation container ipAddressRange createFromList <json>

catocli mutation container ipAddressRange createFromList --json-file mutation.container.ipAddressRange.createFromList.json

catocli mutation container ipAddressRange createFromList '{"createIpAddressRangeContainerFromListInput":{"description":"string","ipAddressRangeInput":{"from":"example_value","to":"example_value"},"name":"string"}}'

catocli mutation container ipAddressRange createFromList '{
    "createIpAddressRangeContainerFromListInput": {
        "description": "string",
        "ipAddressRangeInput": {
            "from": "example_value",
            "to": "example_value"
        },
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.container.ipAddressRange.createFromList ####

`accountId` [ID] - (required) N/A    
`createIpAddressRangeContainerFromListInput` [CreateIpAddressRangeContainerFromListInput] - (required) N/A    
