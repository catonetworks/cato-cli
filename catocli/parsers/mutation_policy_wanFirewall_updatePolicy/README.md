
## CATO-CLI - mutation.policy.wanFirewall.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-updatePolicy) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.updatePolicy:

`catocli mutation policy wanFirewall updatePolicy -h`

`catocli mutation policy wanFirewall updatePolicy <accountID> <json>`

`catocli mutation policy wanFirewall updatePolicy 12345 "$(cat < updatePolicy.json)"`

`catocli mutation policy wanFirewall updatePolicy 12345 '{"WanFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}, "WanFirewallPolicyUpdateInput": {"state": {"state": "enum(PolicyToggleState)"}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.updatePolicy ####
`WanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
`WanFirewallPolicyUpdateInput` [WanFirewallPolicyUpdateInput] - (required) N/A 
`accountId` [ID] - (required) N/A 