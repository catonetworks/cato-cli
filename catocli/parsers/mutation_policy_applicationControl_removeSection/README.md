
## CATO-CLI - mutation.policy.applicationControl.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.applicationControl.removeSection) for documentation on this operation.

### Usage for mutation.policy.applicationControl.removeSection:

`catocli mutation policy applicationControl removeSection -h`

`catocli mutation policy applicationControl removeSection <json>`

`catocli mutation policy applicationControl removeSection "$(cat < mutation.policy.applicationControl.removeSection.json)"`

`catocli mutation policy applicationControl removeSection '{"applicationControlPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyRemoveSectionInput":{"id":"id"}}'`

`catocli mutation policy applicationControl removeSection -p '{
    "applicationControlPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyRemoveSectionInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.applicationControl.removeSection ####

`accountId` [ID] - (required) N/A    
`applicationControlPolicyMutationInput` [ApplicationControlPolicyMutationInput] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
