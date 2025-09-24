
## CATO-CLI - mutation.policy.appTenantRestriction.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.createPolicyRevision:

`catocli mutation policy appTenantRestriction createPolicyRevision -h`

`catocli mutation policy appTenantRestriction createPolicyRevision <json>`

`catocli mutation policy appTenantRestriction createPolicyRevision "$(cat < mutation.policy.appTenantRestriction.createPolicyRevision.json)"`

`catocli mutation policy appTenantRestriction createPolicyRevision '{"appTenantRestrictionPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyCreateRevisionInput":{"description":"string","name":"string"}}'`

`catocli mutation policy appTenantRestriction createPolicyRevision -p '{
    "appTenantRestrictionPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    }
}'`


#### Operation Arguments for mutation.policy.appTenantRestriction.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
