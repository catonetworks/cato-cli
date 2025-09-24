
## CATO-CLI - mutation.container.ipAddressRange.removeValues:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.ipAddressRange.removeValues) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.removeValues:

`catocli mutation container ipAddressRange removeValues -h`

`catocli mutation container ipAddressRange removeValues <json>`

`catocli mutation container ipAddressRange removeValues "$(cat < mutation.container.ipAddressRange.removeValues.json)"`

`catocli mutation container ipAddressRange removeValues '{"ipAddressRangeContainerRemoveValuesInput":{"containerRefInput":{"by":"ID","input":"string"},"ipAddressRangeInput":{"from":"example_value","to":"example_value"}}}'`

`catocli mutation container ipAddressRange removeValues -p '{
    "ipAddressRangeContainerRemoveValuesInput": {
        "containerRefInput": {
            "by": "ID",
            "input": "string"
        },
        "ipAddressRangeInput": {
            "from": "example_value",
            "to": "example_value"
        }
    }
}'`


#### Operation Arguments for mutation.container.ipAddressRange.removeValues ####

`accountId` [ID] - (required) N/A    
`ipAddressRangeContainerRemoveValuesInput` [IpAddressRangeContainerRemoveValuesInput] - (required) N/A    
