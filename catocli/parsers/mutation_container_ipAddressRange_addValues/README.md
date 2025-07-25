
## CATO-CLI - mutation.container.ipAddressRange.addValues:
[Click here](https://api.catonetworks.com/documentation/#mutation-addValues) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.addValues:

`catocli mutation container ipAddressRange addValues -h`

`catocli mutation container ipAddressRange addValues <json>`

`catocli mutation container ipAddressRange addValues "$(cat < addValues.json)"`

`catocli mutation container ipAddressRange addValues '{"ipAddressRangeContainerAddValuesInput": {"containerRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "ipAddressRangeInput": {"from": {"from": "IPAddress"}, "to": {"to": "IPAddress"}}}}'`

#### Operation Arguments for mutation.container.ipAddressRange.addValues ####
`accountId` [ID] - (required) N/A 
`ipAddressRangeContainerAddValuesInput` [IpAddressRangeContainerAddValuesInput] - (required) N/A 
