
## CATO-CLI - mutation.policy.appTenantRestriction.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.createPolicyRevision:

`catocli mutation policy appTenantRestriction createPolicyRevision -h`

`catocli mutation policy appTenantRestriction createPolicyRevision <json>`

`catocli mutation policy appTenantRestriction createPolicyRevision "$(cat < createPolicyRevision.json)"`

`catocli mutation policy appTenantRestriction createPolicyRevision '{"appTenantRestrictionPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyCreateRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}}'`

#### Operation Arguments for mutation.policy.appTenantRestriction.createPolicyRevision ####
`accountId` [ID] - (required) N/A 
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (optional) N/A 
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A 
