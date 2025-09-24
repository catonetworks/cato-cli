
## CATO-CLI - mutation.policy.applicationControl.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.applicationControl.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.applicationControl.discardPolicyRevision:

`catocli mutation policy applicationControl discardPolicyRevision -h`

`catocli mutation policy applicationControl discardPolicyRevision <json>`

`catocli mutation policy applicationControl discardPolicyRevision "$(cat < mutation.policy.applicationControl.discardPolicyRevision.json)"`

`catocli mutation policy applicationControl discardPolicyRevision '{"applicationControlPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyDiscardRevisionInput":{"id":"id"}}'`

`catocli mutation policy applicationControl discardPolicyRevision -p '{
    "applicationControlPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyDiscardRevisionInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.applicationControl.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`applicationControlPolicyMutationInput` [ApplicationControlPolicyMutationInput] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
