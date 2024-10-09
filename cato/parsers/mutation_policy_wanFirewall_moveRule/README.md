
## CATO-CLI - mutation.policy.wanFirewall.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveRule) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.moveRule:

`cato mutation policy wanFirewall moveRule -h`

`cato mutation policy wanFirewall moveRule <accountID> <json>`

`cato mutation policy wanFirewall moveRule 12345 "$(cat < moveRule.json)"`

`cato mutation policy wanFirewall moveRule 12345 '{"PolicyMoveRuleInput": {"PolicyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}, "id": {"id": "ID"}}, "WanFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.moveRule ####
`PolicyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A 
`WanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
