
## CATO-CLI - mutation.policy.appTenantRestriction.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.moveSection) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.moveSection:

`catocli mutation policy appTenantRestriction moveSection -h`

`catocli mutation policy appTenantRestriction moveSection <json>`

`catocli mutation policy appTenantRestriction moveSection "$(cat < mutation.policy.appTenantRestriction.moveSection.json)"`

`catocli mutation policy appTenantRestriction moveSection '{"appTenantRestrictionPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyMoveSectionInput":{"id":"id","policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}}}'`

`catocli mutation policy appTenantRestriction moveSection -p '{
    "appTenantRestrictionPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyMoveSectionInput": {
        "id": "id",
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.appTenantRestriction.moveSection ####

`accountId` [ID] - (required) N/A    
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
