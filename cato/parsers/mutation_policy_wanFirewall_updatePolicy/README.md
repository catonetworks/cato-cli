
## CATO-CLI - mutation.policy.wanFirewall.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-updatePolicy) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.updatePolicy:

`cato mutation policy wanFirewall updatePolicy -h`

`cato mutation policy wanFirewall updatePolicy <accountID> <json>`

`cato mutation policy wanFirewall updatePolicy 12345 "$(cat < updatePolicy.json)"`

`cato mutation policy wanFirewall updatePolicy 12345 '{"WanFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}, "WanFirewallPolicyUpdateInput": {"state": {"state": "enum(PolicyToggleState)"}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.updatePolicy ####
`WanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
`WanFirewallPolicyUpdateInput` [WanFirewallPolicyUpdateInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
