
## CATO-CLI - mutation.policy.remotePortFwd.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSection) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.addSection:

`catocli mutation policy remotePortFwd addSection -h`

`catocli mutation policy remotePortFwd addSection <json>`

`catocli mutation policy remotePortFwd addSection "$(cat < addSection.json)"`

`catocli mutation policy remotePortFwd addSection '{"policyAddSectionInput": {"policyAddSectionInfoInput": {"name": {"name": "String"}}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}, "remotePortFwdPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.remotePortFwd.addSection ####
`accountId` [ID] - (required) N/A 
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A 
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (optional) N/A 
