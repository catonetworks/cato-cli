
## CATO-CLI - mutation.policy.appTenantRestriction.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.addSection) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.addSection:

`catocli mutation policy appTenantRestriction addSection -h`

`catocli mutation policy appTenantRestriction addSection <json>`

`catocli mutation policy appTenantRestriction addSection "$(cat < mutation.policy.appTenantRestriction.addSection.json)"`

`catocli mutation policy appTenantRestriction addSection '{"appTenantRestrictionPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyAddSectionInput":{"policyAddSectionInfoInput":{"name":"string"},"policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}}}'`

`catocli mutation policy appTenantRestriction addSection -p '{
    "appTenantRestrictionPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyAddSectionInput": {
        "policyAddSectionInfoInput": {
            "name": "string"
        },
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.appTenantRestriction.addSection ####

`accountId` [ID] - (required) N/A    
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
