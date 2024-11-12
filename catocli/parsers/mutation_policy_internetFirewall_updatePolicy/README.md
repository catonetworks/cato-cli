
## CATO-CLI - mutation.policy.internetFirewall.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-updatePolicy) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.updatePolicy:

`catocli mutation policy internetFirewall updatePolicy -h`

`catocli mutation policy internetFirewall updatePolicy <json>`

`catocli mutation policy internetFirewall updatePolicy "$(cat < updatePolicy.json)"`

`catocli mutation policy internetFirewall updatePolicy '{"internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "internetFirewallPolicyUpdateInput": {"state": {"state": "enum(PolicyToggleState)"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.updatePolicy ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`internetFirewallPolicyUpdateInput` [InternetFirewallPolicyUpdateInput] - (required) N/A 
