
## CATO-CLI - mutation.policy.terminalServer.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSection) for documentation on this operation.

### Usage for mutation.policy.terminalServer.addSection:

`catocli mutation policy terminalServer addSection -h`

`catocli mutation policy terminalServer addSection <json>`

`catocli mutation policy terminalServer addSection "$(cat < addSection.json)"`

`catocli mutation policy terminalServer addSection '{"policyAddSectionInput": {"policyAddSectionInfoInput": {"name": {"name": "String"}}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}, "terminalServerPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.terminalServer.addSection ####
`accountId` [ID] - (required) N/A 
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A 
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (optional) N/A 
