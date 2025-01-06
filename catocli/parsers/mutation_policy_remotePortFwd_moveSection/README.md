
## CATO-CLI - mutation.policy.remotePortFwd.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveSection) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.moveSection:

`catocli mutation policy remotePortFwd moveSection -h`

`catocli mutation policy remotePortFwd moveSection <json>`

`catocli mutation policy remotePortFwd moveSection "$(cat < moveSection.json)"`

`catocli mutation policy remotePortFwd moveSection '{"policyMoveSectionInput": {"id": {"id": "ID"}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}, "remotePortFwdPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.remotePortFwd.moveSection ####
`accountId` [ID] - (required) N/A 
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A 
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (optional) N/A 
