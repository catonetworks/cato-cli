
## CATO-CLI - mutation.policy.wanNetwork.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-updatePolicy) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.updatePolicy:

`catocli mutation policy wanNetwork updatePolicy -h`

`catocli mutation policy wanNetwork updatePolicy <json>`

`catocli mutation policy wanNetwork updatePolicy "$(cat < updatePolicy.json)"`

`catocli mutation policy wanNetwork updatePolicy '{"wanNetworkPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "wanNetworkPolicyUpdateInput": {"state": {"state": "enum(PolicyToggleState)"}}}'`

#### Operation Arguments for mutation.policy.wanNetwork.updatePolicy ####
`accountId` [ID] - (required) N/A 
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (optional) N/A 
`wanNetworkPolicyUpdateInput` [WanNetworkPolicyUpdateInput] - (required) N/A 
