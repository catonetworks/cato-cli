
## CATO-CLI - mutation.policy.socketLan.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-updatePolicy) for documentation on this operation.

### Usage for mutation.policy.socketLan.updatePolicy:

`catocli mutation policy socketLan updatePolicy -h`

`catocli mutation policy socketLan updatePolicy <json>`

`catocli mutation policy socketLan updatePolicy "$(cat < updatePolicy.json)"`

`catocli mutation policy socketLan updatePolicy '{"socketLanPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "socketLanPolicyUpdateInput": {"state": {"state": "enum(PolicyToggleState)"}}}'`

#### Operation Arguments for mutation.policy.socketLan.updatePolicy ####
`accountId` [ID] - (required) N/A 
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (optional) N/A 
`socketLanPolicyUpdateInput` [SocketLanPolicyUpdateInput] - (required) N/A 
