
## CATO-CLI - mutation.policy.remotePortFwd.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-updatePolicy) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.updatePolicy:

`catocli mutation policy remotePortFwd updatePolicy -h`

`catocli mutation policy remotePortFwd updatePolicy <json>`

`catocli mutation policy remotePortFwd updatePolicy "$(cat < updatePolicy.json)"`

`catocli mutation policy remotePortFwd updatePolicy '{"remotePortFwdPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "remotePortFwdPolicyUpdateInput": {"state": {"state": "enum(PolicyToggleState)"}}}'`

#### Operation Arguments for mutation.policy.remotePortFwd.updatePolicy ####
`accountId` [ID] - (required) N/A 
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (optional) N/A 
`remotePortFwdPolicyUpdateInput` [RemotePortFwdPolicyUpdateInput] - (required) N/A 
