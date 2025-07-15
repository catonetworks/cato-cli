
## CATO-CLI - mutation.policy.terminalServer.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.terminalServer.createPolicyRevision:

`catocli mutation policy terminalServer createPolicyRevision -h`

`catocli mutation policy terminalServer createPolicyRevision <json>`

`catocli mutation policy terminalServer createPolicyRevision "$(cat < createPolicyRevision.json)"`

`catocli mutation policy terminalServer createPolicyRevision '{"policyCreateRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}, "terminalServerPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.terminalServer.createPolicyRevision ####
`accountId` [ID] - (required) N/A 
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A 
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (optional) N/A 
