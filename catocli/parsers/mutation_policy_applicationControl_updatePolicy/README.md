
## CATO-CLI - mutation.policy.applicationControl.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.applicationControl.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.applicationControl.updatePolicy:

`catocli mutation policy applicationControl updatePolicy -h`

`catocli mutation policy applicationControl updatePolicy <json>`

`catocli mutation policy applicationControl updatePolicy "$(cat < mutation.policy.applicationControl.updatePolicy.json)"`

`catocli mutation policy applicationControl updatePolicy '{"applicationControlPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"applicationControlPolicyUpdateInput":{"applicationControlConfigInput":{"dataControlEnabled":"ENABLED"},"state":"ENABLED"}}'`

`catocli mutation policy applicationControl updatePolicy -p '{
    "applicationControlPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "applicationControlPolicyUpdateInput": {
        "applicationControlConfigInput": {
            "dataControlEnabled": "ENABLED"
        },
        "state": "ENABLED"
    }
}'`


#### Operation Arguments for mutation.policy.applicationControl.updatePolicy ####

`accountId` [ID] - (required) N/A    
`applicationControlPolicyMutationInput` [ApplicationControlPolicyMutationInput] - (required) N/A    
`applicationControlPolicyUpdateInput` [ApplicationControlPolicyUpdateInput] - (required) N/A    
