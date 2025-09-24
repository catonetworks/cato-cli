
## CATO-CLI - mutation.policy.appTenantRestriction.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.moveRule) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.moveRule:

`catocli mutation policy appTenantRestriction moveRule -h`

`catocli mutation policy appTenantRestriction moveRule <json>`

`catocli mutation policy appTenantRestriction moveRule "$(cat < mutation.policy.appTenantRestriction.moveRule.json)"`

`catocli mutation policy appTenantRestriction moveRule '{"appTenantRestrictionPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}}}'`

`catocli mutation policy appTenantRestriction moveRule -p '{
    "appTenantRestrictionPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyMoveRuleInput": {
        "id": "id",
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.appTenantRestriction.moveRule ####

`accountId` [ID] - (required) N/A    
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
