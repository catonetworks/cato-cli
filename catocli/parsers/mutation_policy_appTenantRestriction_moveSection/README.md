
## CATO-CLI - mutation.policy.appTenantRestriction.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveSection) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.moveSection:

`catocli mutation policy appTenantRestriction moveSection -h`

`catocli mutation policy appTenantRestriction moveSection <json>`

`catocli mutation policy appTenantRestriction moveSection "$(cat < moveSection.json)"`

`catocli mutation policy appTenantRestriction moveSection '{"appTenantRestrictionPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyMoveSectionInput": {"id": {"id": "ID"}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}}'`

#### Operation Arguments for mutation.policy.appTenantRestriction.moveSection ####
`accountId` [ID] - (required) N/A 
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (optional) N/A 
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A 
