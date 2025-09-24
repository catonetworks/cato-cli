
## CATO-CLI - mutation.policy.appTenantRestriction.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.appTenantRestriction.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.publishPolicyRevision:

`catocli mutation policy appTenantRestriction publishPolicyRevision -h`

`catocli mutation policy appTenantRestriction publishPolicyRevision <json>`

`catocli mutation policy appTenantRestriction publishPolicyRevision "$(cat < mutation.policy.appTenantRestriction.publishPolicyRevision.json)"`

`catocli mutation policy appTenantRestriction publishPolicyRevision '{"appTenantRestrictionPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyPublishRevisionInput":{"description":"string","name":"string"}}'`

`catocli mutation policy appTenantRestriction publishPolicyRevision -p '{
    "appTenantRestrictionPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    }
}'`


#### Operation Arguments for mutation.policy.appTenantRestriction.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
