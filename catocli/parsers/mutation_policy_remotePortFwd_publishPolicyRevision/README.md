
## CATO-CLI - mutation.policy.remotePortFwd.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.publishPolicyRevision:

`catocli mutation policy remotePortFwd publishPolicyRevision -h`

`catocli mutation policy remotePortFwd publishPolicyRevision <json>`

`catocli mutation policy remotePortFwd publishPolicyRevision "$(cat < publishPolicyRevision.json)"`

`catocli mutation policy remotePortFwd publishPolicyRevision '{"policyPublishRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}, "remotePortFwdPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.remotePortFwd.publishPolicyRevision ####
`accountId` [ID] - (required) N/A 
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (optional) N/A 
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (optional) N/A 
