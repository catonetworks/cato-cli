
## CATO-CLI - mutation.container.ipAddressRange.removeValues:
[Click here](https://api.catonetworks.com/documentation/#mutation-removeValues) for documentation on this operation.

### Usage for mutation.container.ipAddressRange.removeValues:

`catocli mutation container ipAddressRange removeValues -h`

`catocli mutation container ipAddressRange removeValues <json>`

`catocli mutation container ipAddressRange removeValues "$(cat < removeValues.json)"`

`catocli mutation container ipAddressRange removeValues '{"ipAddressRangeContainerRemoveValuesInput": {"containerRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "ipAddressRangeInput": {"from": {"from": "IPAddress"}, "to": {"to": "IPAddress"}}}}'`

#### Operation Arguments for mutation.container.ipAddressRange.removeValues ####
`accountId` [ID] - (required) N/A 
`ipAddressRangeContainerRemoveValuesInput` [IpAddressRangeContainerRemoveValuesInput] - (required) N/A 
