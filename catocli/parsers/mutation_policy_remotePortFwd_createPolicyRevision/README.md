
## CATO-CLI - mutation.policy.remotePortFwd.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.createPolicyRevision:

`catocli mutation policy remotePortFwd createPolicyRevision -h`

`catocli mutation policy remotePortFwd createPolicyRevision <json>`

`catocli mutation policy remotePortFwd createPolicyRevision "$(cat < createPolicyRevision.json)"`

`catocli mutation policy remotePortFwd createPolicyRevision '{"policyCreateRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}, "remotePortFwdPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.remotePortFwd.createPolicyRevision ####
`accountId` [ID] - (required) N/A 
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A 
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (optional) N/A 
