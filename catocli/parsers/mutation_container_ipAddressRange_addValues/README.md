
## CATO-CLI - mutation.container.ipAddressRange.addValues:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.container.ipAddressRange.addValues) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.addValues:

`catocli mutation container ipAddressRange addValues -h`

`catocli mutation container ipAddressRange addValues <json>`

`catocli mutation container ipAddressRange addValues "$(cat < mutation.container.ipAddressRange.addValues.json)"`

`catocli mutation container ipAddressRange addValues '{"ipAddressRangeContainerAddValuesInput":{"containerRefInput":{"by":"ID","input":"string"},"ipAddressRangeInput":{"from":"example_value","to":"example_value"}}}'`

`catocli mutation container ipAddressRange addValues -p '{
    "ipAddressRangeContainerAddValuesInput": {
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


#### Operation Arguments for mutation.container.ipAddressRange.addValues ####

`accountId` [ID] - (required) N/A    
`ipAddressRangeContainerAddValuesInput` [IpAddressRangeContainerAddValuesInput] - (required) N/A    
