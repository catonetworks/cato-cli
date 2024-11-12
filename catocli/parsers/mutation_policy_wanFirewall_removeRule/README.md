
## CATO-CLI - mutation.policy.wanFirewall.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-removeRule) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.removeRule:

`catocli mutation policy wanFirewall removeRule -h`

`catocli mutation policy wanFirewall removeRule <json>`

`catocli mutation policy wanFirewall removeRule "$(cat < removeRule.json)"`

`catocli mutation policy wanFirewall removeRule '{"wanFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "wanFirewallRemoveRuleInput": {"id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.removeRule ####
`accountId` [ID] - (required) N/A 
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
`wanFirewallRemoveRuleInput` [WanFirewallRemoveRuleInput] - (required) N/A 
