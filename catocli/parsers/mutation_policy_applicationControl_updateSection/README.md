
## CATO-CLI - mutation.policy.applicationControl.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.applicationControl.updateSection) for documentation on this operation.

### Usage for mutation.policy.applicationControl.updateSection:

`catocli mutation policy applicationControl updateSection -h`

`catocli mutation policy applicationControl updateSection <json>`

`catocli mutation policy applicationControl updateSection "$(cat < mutation.policy.applicationControl.updateSection.json)"`

`catocli mutation policy applicationControl updateSection '{"applicationControlPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyUpdateSectionInput":{"id":"id","policyUpdateSectionInfoInput":{"name":"string"}}}'`

`catocli mutation policy applicationControl updateSection -p '{
    "applicationControlPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyUpdateSectionInput": {
        "id": "id",
        "policyUpdateSectionInfoInput": {
            "name": "string"
        }
    }
}'`


#### Operation Arguments for mutation.policy.applicationControl.updateSection ####

`accountId` [ID] - (required) N/A    
`applicationControlPolicyMutationInput` [ApplicationControlPolicyMutationInput] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
