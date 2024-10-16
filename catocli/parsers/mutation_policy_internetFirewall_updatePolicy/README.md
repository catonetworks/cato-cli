
## CATO-CLI - mutation.policy.internetFirewall.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-updatePolicy) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.updatePolicy:

`catocli mutation policy internetFirewall updatePolicy -h`

`catocli mutation policy internetFirewall updatePolicy <json>`

`catocli mutation policy internetFirewall updatePolicy "$(cat < updatePolicy.json)"`

`catocli mutation policy internetFirewall updatePolicy '{"InternetFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}, "InternetFirewallPolicyUpdateInput": {"state": {"state": "enum(PolicyToggleState)"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.updatePolicy ####
`InternetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`InternetFirewallPolicyUpdateInput` [InternetFirewallPolicyUpdateInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
