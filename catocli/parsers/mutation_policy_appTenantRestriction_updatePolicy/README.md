
## CATO-CLI - mutation.policy.appTenantRestriction.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-updatePolicy) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.updatePolicy:

`catocli mutation policy appTenantRestriction updatePolicy -h`

`catocli mutation policy appTenantRestriction updatePolicy <json>`

`catocli mutation policy appTenantRestriction updatePolicy "$(cat < updatePolicy.json)"`

`catocli mutation policy appTenantRestriction updatePolicy '{"appTenantRestrictionPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "appTenantRestrictionPolicyUpdateInput": {"state": {"state": "enum(PolicyToggleState)"}}}'`

#### Operation Arguments for mutation.policy.appTenantRestriction.updatePolicy ####
`accountId` [ID] - (required) N/A 
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (optional) N/A 
`appTenantRestrictionPolicyUpdateInput` [AppTenantRestrictionPolicyUpdateInput] - (required) N/A 
