
## CATO-CLI - mutation.policy.internetFirewall.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-removeRule) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.removeRule:

`catocli mutation policy internetFirewall removeRule -h`

`catocli mutation policy internetFirewall removeRule <accountID> <json>`

`catocli mutation policy internetFirewall removeRule 12345 "$(cat < removeRule.json)"`

`catocli mutation policy internetFirewall removeRule 12345 '{"InternetFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}, "InternetFirewallRemoveRuleInput": {"id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.removeRule ####
`InternetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`InternetFirewallRemoveRuleInput` [InternetFirewallRemoveRuleInput] - (required) N/A 
`accountId` [ID] - (required) N/A 