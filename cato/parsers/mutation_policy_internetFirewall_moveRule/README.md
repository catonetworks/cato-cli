
## CATO-CLI - mutation.policy.internetFirewall.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveRule) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.moveRule:

`cato mutation policy internetFirewall moveRule -h`

`cato mutation policy internetFirewall moveRule <accountID> <json>`

`cato mutation policy internetFirewall moveRule 12345 "$(cat < moveRule.json)"`

`cato mutation policy internetFirewall moveRule 12345 '{"InternetFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}, "PolicyMoveRuleInput": {"PolicyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}, "id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.moveRule ####
`InternetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`PolicyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
