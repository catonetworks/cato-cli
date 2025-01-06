
## CATO-CLI - mutation.policy.appTenantRestriction.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.publishPolicyRevision:

`catocli mutation policy appTenantRestriction publishPolicyRevision -h`

`catocli mutation policy appTenantRestriction publishPolicyRevision <json>`

`catocli mutation policy appTenantRestriction publishPolicyRevision "$(cat < publishPolicyRevision.json)"`

`catocli mutation policy appTenantRestriction publishPolicyRevision '{"appTenantRestrictionPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyPublishRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}}'`

#### Operation Arguments for mutation.policy.appTenantRestriction.publishPolicyRevision ####
`accountId` [ID] - (required) N/A 
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (optional) N/A 
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (optional) N/A 
