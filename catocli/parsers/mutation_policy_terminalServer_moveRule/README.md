
## CATO-CLI - mutation.policy.terminalServer.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveRule) for documentation on this operation.

### Usage for mutation.policy.terminalServer.moveRule:

`catocli mutation policy terminalServer moveRule -h`

`catocli mutation policy terminalServer moveRule <json>`

`catocli mutation policy terminalServer moveRule "$(cat < moveRule.json)"`

`catocli mutation policy terminalServer moveRule '{"policyMoveRuleInput": {"id": {"id": "ID"}, "policyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}}, "terminalServerPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.terminalServer.moveRule ####
`accountId` [ID] - (required) N/A 
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A 
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (optional) N/A 
