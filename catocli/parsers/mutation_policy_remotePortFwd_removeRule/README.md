
## CATO-CLI - mutation.policy.remotePortFwd.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-removeRule) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.removeRule:

`catocli mutation policy remotePortFwd removeRule -h`

`catocli mutation policy remotePortFwd removeRule <json>`

`catocli mutation policy remotePortFwd removeRule "$(cat < removeRule.json)"`

`catocli mutation policy remotePortFwd removeRule '{"remotePortFwdPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "remotePortFwdRemoveRuleInput": {"id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.remotePortFwd.removeRule ####
`accountId` [ID] - (required) N/A 
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (optional) N/A 
`remotePortFwdRemoveRuleInput` [RemotePortFwdRemoveRuleInput] - (required) N/A 
