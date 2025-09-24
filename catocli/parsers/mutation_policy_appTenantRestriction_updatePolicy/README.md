
## CATO-CLI - mutation.policy.appTenantRestriction.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.updatePolicy:

`catocli mutation policy appTenantRestriction updatePolicy -h`

`catocli mutation policy appTenantRestriction updatePolicy <json>`

`catocli mutation policy appTenantRestriction updatePolicy "$(cat < mutation.policy.appTenantRestriction.updatePolicy.json)"`

`catocli mutation policy appTenantRestriction updatePolicy '{"appTenantRestrictionPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"appTenantRestrictionPolicyUpdateInput":{"state":"ENABLED"}}'`

`catocli mutation policy appTenantRestriction updatePolicy -p '{
    "appTenantRestrictionPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "appTenantRestrictionPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'`


#### Operation Arguments for mutation.policy.appTenantRestriction.updatePolicy ####

`accountId` [ID] - (required) N/A    
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) N/A    
`appTenantRestrictionPolicyUpdateInput` [AppTenantRestrictionPolicyUpdateInput] - (required) N/A    
