
## CATO-CLI - mutation.policy.appTenantRestriction.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.updateSection) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.updateSection:

`catocli mutation policy appTenantRestriction updateSection -h`

`catocli mutation policy appTenantRestriction updateSection <json>`

`catocli mutation policy appTenantRestriction updateSection "$(cat < mutation.policy.appTenantRestriction.updateSection.json)"`

`catocli mutation policy appTenantRestriction updateSection '{"appTenantRestrictionPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyUpdateSectionInput":{"id":"id","policyUpdateSectionInfoInput":{"name":"string"}}}'`

`catocli mutation policy appTenantRestriction updateSection -p '{
    "appTenantRestrictionPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyUpdateSectionInput": {
        "id": "id",
        "policyUpdateSectionInfoInput": {
            "name": "string"
        }
    }
}'`


#### Operation Arguments for mutation.policy.appTenantRestriction.updateSection ####

`accountId` [ID] - (required) N/A    
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
