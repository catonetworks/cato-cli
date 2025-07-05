
## CATO-CLI - mutation.policy.wanNetwork.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.createPolicyRevision:

`catocli mutation policy wanNetwork createPolicyRevision -h`

`catocli mutation policy wanNetwork createPolicyRevision <json>`

`catocli mutation policy wanNetwork createPolicyRevision "$(cat < createPolicyRevision.json)"`

`catocli mutation policy wanNetwork createPolicyRevision '{"policyCreateRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}, "wanNetworkPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanNetwork.createPolicyRevision ####
`accountId` [ID] - (required) N/A 
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A 
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (optional) N/A 
