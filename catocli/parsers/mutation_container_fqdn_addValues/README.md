
## CATO-CLI - mutation.container.fqdn.addValues:
[Click here](https://api.catonetworks.com/documentation/#mutation-addValues) for documentation on this operation.

### Usage for mutation.container.fqdn.addValues:

`catocli mutation container fqdn addValues -h`

`catocli mutation container fqdn addValues <json>`

`catocli mutation container fqdn addValues "$(cat < addValues.json)"`

`catocli mutation container fqdn addValues '{"fqdnContainerAddValuesInput": {"containerRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "values": {"values": ["Fqdn"]}}}'`

#### Operation Arguments for mutation.container.fqdn.addValues ####
`accountId` [ID] - (required) N/A 
`fqdnContainerAddValuesInput` [FqdnContainerAddValuesInput] - (required) N/A 
