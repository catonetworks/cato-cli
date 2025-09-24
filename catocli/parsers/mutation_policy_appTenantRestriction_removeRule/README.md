
## CATO-CLI - mutation.policy.appTenantRestriction.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.removeRule) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.removeRule:

`catocli mutation policy appTenantRestriction removeRule -h`

`catocli mutation policy appTenantRestriction removeRule <json>`

`catocli mutation policy appTenantRestriction removeRule "$(cat < mutation.policy.appTenantRestriction.removeRule.json)"`

`catocli mutation policy appTenantRestriction removeRule '{"appTenantRestrictionPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"appTenantRestrictionRemoveRuleInput":{"id":"id"}}'`

`catocli mutation policy appTenantRestriction removeRule -p '{
    "appTenantRestrictionPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "appTenantRestrictionRemoveRuleInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.appTenantRestriction.removeRule ####

`accountId` [ID] - (required) N/A    
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) N/A    
`appTenantRestrictionRemoveRuleInput` [AppTenantRestrictionRemoveRuleInput] - (required) N/A    
