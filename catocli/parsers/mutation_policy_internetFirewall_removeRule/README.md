
## CATO-CLI - mutation.policy.internetFirewall.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-removeRule) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.removeRule:

`catocli mutation policy internetFirewall removeRule -h`

`catocli mutation policy internetFirewall removeRule <json>`

`catocli mutation policy internetFirewall removeRule "$(cat < removeRule.json)"`

`catocli mutation policy internetFirewall removeRule '{"internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "internetFirewallRemoveRuleInput": {"id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.removeRule ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`internetFirewallRemoveRuleInput` [InternetFirewallRemoveRuleInput] - (required) N/A 
