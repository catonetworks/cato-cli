
## CATO-CLI - mutation.policy.appTenantRestriction.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.removeSection) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.removeSection:

`catocli mutation policy appTenantRestriction removeSection -h`

`catocli mutation policy appTenantRestriction removeSection <json>`

`catocli mutation policy appTenantRestriction removeSection "$(cat < mutation.policy.appTenantRestriction.removeSection.json)"`

`catocli mutation policy appTenantRestriction removeSection '{"appTenantRestrictionPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyRemoveSectionInput":{"id":"id"}}'`

`catocli mutation policy appTenantRestriction removeSection -p '{
    "appTenantRestrictionPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyRemoveSectionInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.appTenantRestriction.removeSection ####

`accountId` [ID] - (required) N/A    
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
