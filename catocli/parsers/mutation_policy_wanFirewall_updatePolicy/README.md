
## CATO-CLI - mutation.policy.wanFirewall.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-updatePolicy) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.updatePolicy:

`catocli mutation policy wanFirewall updatePolicy -h`

`catocli mutation policy wanFirewall updatePolicy <json>`

`catocli mutation policy wanFirewall updatePolicy "$(cat < updatePolicy.json)"`

`catocli mutation policy wanFirewall updatePolicy '{"wanFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "wanFirewallPolicyUpdateInput": {"state": {"state": "enum(PolicyToggleState)"}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.updatePolicy ####
`accountId` [ID] - (required) N/A 
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
`wanFirewallPolicyUpdateInput` [WanFirewallPolicyUpdateInput] - (required) N/A 
