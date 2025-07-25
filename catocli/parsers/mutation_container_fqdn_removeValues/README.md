
## CATO-CLI - mutation.container.fqdn.removeValues:
[Click here](https://api.catonetworks.com/documentation/#mutation-removeValues) for documentation on this operation.

### Usage for mutation.container.fqdn.removeValues:

`catocli mutation container fqdn removeValues -h`

`catocli mutation container fqdn removeValues <json>`

`catocli mutation container fqdn removeValues "$(cat < removeValues.json)"`

`catocli mutation container fqdn removeValues '{"fqdnContainerRemoveValuesInput": {"containerRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "values": {"values": ["Fqdn"]}}}'`

#### Operation Arguments for mutation.container.fqdn.removeValues ####
`accountId` [ID] - (required) N/A 
`fqdnContainerRemoveValuesInput` [FqdnContainerRemoveValuesInput] - (required) N/A 
