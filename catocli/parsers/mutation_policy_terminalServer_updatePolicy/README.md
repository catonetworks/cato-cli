
## CATO-CLI - mutation.policy.terminalServer.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-updatePolicy) for documentation on this operation.

### Usage for mutation.policy.terminalServer.updatePolicy:

`catocli mutation policy terminalServer updatePolicy -h`

`catocli mutation policy terminalServer updatePolicy <json>`

`catocli mutation policy terminalServer updatePolicy "$(cat < updatePolicy.json)"`

`catocli mutation policy terminalServer updatePolicy '{"terminalServerPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "terminalServerPolicyUpdateInput": {"state": {"state": "enum(PolicyToggleState)"}}}'`

#### Operation Arguments for mutation.policy.terminalServer.updatePolicy ####
`accountId` [ID] - (required) N/A 
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (optional) N/A 
`terminalServerPolicyUpdateInput` [TerminalServerPolicyUpdateInput] - (required) N/A 
