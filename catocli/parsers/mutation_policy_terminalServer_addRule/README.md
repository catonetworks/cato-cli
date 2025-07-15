
## CATO-CLI - mutation.policy.terminalServer.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-addRule) for documentation on this operation.

### Usage for mutation.policy.terminalServer.addRule:

`catocli mutation policy terminalServer addRule -h`

`catocli mutation policy terminalServer addRule <json>`

`catocli mutation policy terminalServer addRule "$(cat < addRule.json)"`

`catocli mutation policy terminalServer addRule '{"terminalServerAddRuleInput": {"policyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}, "terminalServerAddRuleDataInput": {"allowedHostIP": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "description": {"description": "String"}, "enabled": {"enabled": "Boolean"}, "excludeTraffic": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "name": {"name": "String"}}}, "terminalServerPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.terminalServer.addRule ####
`accountId` [ID] - (required) N/A 
`terminalServerAddRuleInput` [TerminalServerAddRuleInput] - (required) N/A 
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (optional) N/A 
