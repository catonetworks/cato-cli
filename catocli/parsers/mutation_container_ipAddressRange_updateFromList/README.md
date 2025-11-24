
## CATO-CLI - mutation.container.ipAddressRange.updateFromList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.ipAddressRange.updateFromList) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.updateFromList:

```bash
catocli mutation container ipAddressRange updateFromList -h

catocli mutation container ipAddressRange updateFromList <json>

catocli mutation container ipAddressRange updateFromList --json-file mutation.container.ipAddressRange.updateFromList.json

catocli mutation container ipAddressRange updateFromList '{"updateIpAddressRangeContainerFromListInput":{"containerRefInput":{"by":"ID","input":"string"},"description":"string","ipAddressRangeInput":{"from":"example_value","to":"example_value"}}}'

catocli mutation container ipAddressRange updateFromList '{
    "updateIpAddressRangeContainerFromListInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        },
        "description": "string",
        "ipAddressRangeInput": {
            "from": "example_value",
            "to": "example_value"
        }
    }
}'
```

#### Operation Arguments for mutation.container.ipAddressRange.updateFromList ####

`accountId` [ID] - (required) N/A    
`updateIpAddressRangeContainerFromListInput` [UpdateIpAddressRangeContainerFromListInput] - (required) N/A    
