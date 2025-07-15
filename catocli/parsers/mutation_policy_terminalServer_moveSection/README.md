
## CATO-CLI - mutation.policy.terminalServer.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveSection) for documentation on this operation.

### Usage for mutation.policy.terminalServer.moveSection:

`catocli mutation policy terminalServer moveSection -h`

`catocli mutation policy terminalServer moveSection <json>`

`catocli mutation policy terminalServer moveSection "$(cat < moveSection.json)"`

`catocli mutation policy terminalServer moveSection '{"policyMoveSectionInput": {"id": {"id": "ID"}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}, "terminalServerPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.terminalServer.moveSection ####
`accountId` [ID] - (required) N/A 
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A 
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (optional) N/A 
