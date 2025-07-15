
## CATO-CLI - mutation.policy.terminalServer.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateRule) for documentation on this operation.

### Usage for mutation.policy.terminalServer.updateRule:

`catocli mutation policy terminalServer updateRule -h`

`catocli mutation policy terminalServer updateRule <json>`

`catocli mutation policy terminalServer updateRule "$(cat < updateRule.json)"`

`catocli mutation policy terminalServer updateRule '{"terminalServerPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "terminalServerUpdateRuleInput": {"id": {"id": "ID"}, "terminalServerUpdateRuleDataInput": {"allowedHostIP": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "description": {"description": "String"}, "enabled": {"enabled": "Boolean"}, "excludeTraffic": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "name": {"name": "String"}}}}'`

#### Operation Arguments for mutation.policy.terminalServer.updateRule ####
`accountId` [ID] - (required) N/A 
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (optional) N/A 
`terminalServerUpdateRuleInput` [TerminalServerUpdateRuleInput] - (required) N/A 
