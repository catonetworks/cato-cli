
## CATO-CLI - mutation.policy.applicationControl.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.applicationControl.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.applicationControl.publishPolicyRevision:

`catocli mutation policy applicationControl publishPolicyRevision -h`

`catocli mutation policy applicationControl publishPolicyRevision <json>`

`catocli mutation policy applicationControl publishPolicyRevision "$(cat < mutation.policy.applicationControl.publishPolicyRevision.json)"`

`catocli mutation policy applicationControl publishPolicyRevision '{"applicationControlPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyPublishRevisionInput":{"description":"string","name":"string"}}'`

`catocli mutation policy applicationControl publishPolicyRevision -p '{
    "applicationControlPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    }
}'`


#### Operation Arguments for mutation.policy.applicationControl.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`applicationControlPolicyMutationInput` [ApplicationControlPolicyMutationInput] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
