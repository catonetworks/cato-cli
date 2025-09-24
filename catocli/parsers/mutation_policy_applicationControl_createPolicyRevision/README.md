
## CATO-CLI - mutation.policy.applicationControl.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.applicationControl.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.applicationControl.createPolicyRevision:

`catocli mutation policy applicationControl createPolicyRevision -h`

`catocli mutation policy applicationControl createPolicyRevision <json>`

`catocli mutation policy applicationControl createPolicyRevision "$(cat < mutation.policy.applicationControl.createPolicyRevision.json)"`

`catocli mutation policy applicationControl createPolicyRevision '{"applicationControlPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyCreateRevisionInput":{"description":"string","name":"string"}}'`

`catocli mutation policy applicationControl createPolicyRevision -p '{
    "applicationControlPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    }
}'`


#### Operation Arguments for mutation.policy.applicationControl.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`applicationControlPolicyMutationInput` [ApplicationControlPolicyMutationInput] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
