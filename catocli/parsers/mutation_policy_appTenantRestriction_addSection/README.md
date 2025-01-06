
## CATO-CLI - mutation.policy.appTenantRestriction.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSection) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.addSection:

`catocli mutation policy appTenantRestriction addSection -h`

`catocli mutation policy appTenantRestriction addSection <json>`

`catocli mutation policy appTenantRestriction addSection "$(cat < addSection.json)"`

`catocli mutation policy appTenantRestriction addSection '{"appTenantRestrictionPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyAddSectionInput": {"policyAddSectionInfoInput": {"name": {"name": "String"}}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}}'`

#### Operation Arguments for mutation.policy.appTenantRestriction.addSection ####
`accountId` [ID] - (required) N/A 
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (optional) N/A 
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A 
