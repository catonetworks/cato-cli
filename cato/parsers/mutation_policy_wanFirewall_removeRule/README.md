
## CATO-CLI - mutation.policy.wanFirewall.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-removeRule) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.removeRule:

`cato mutation policy wanFirewall removeRule -h`

`cato mutation policy wanFirewall removeRule <accountID> <json>`

`cato mutation policy wanFirewall removeRule 12345 "$(cat < removeRule.json)"`

`cato mutation policy wanFirewall removeRule 12345 '{"WanFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}, "WanFirewallRemoveRuleInput": {"id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.removeRule ####
`WanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
`WanFirewallRemoveRuleInput` [WanFirewallRemoveRuleInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
