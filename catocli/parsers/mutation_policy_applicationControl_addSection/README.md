
## CATO-CLI - mutation.policy.applicationControl.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.applicationControl.addSection) for documentation on this operation.

### Usage for mutation.policy.applicationControl.addSection:

`catocli mutation policy applicationControl addSection -h`

`catocli mutation policy applicationControl addSection <json>`

`catocli mutation policy applicationControl addSection "$(cat < mutation.policy.applicationControl.addSection.json)"`

`catocli mutation policy applicationControl addSection '{"applicationControlPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyAddSectionInput":{"policyAddSectionInfoInput":{"name":"string"},"policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}}}'`

`catocli mutation policy applicationControl addSection -p '{
    "applicationControlPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyAddSectionInput": {
        "policyAddSectionInfoInput": {
            "name": "string"
        },
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.applicationControl.addSection ####

`accountId` [ID] - (required) N/A    
`applicationControlPolicyMutationInput` [ApplicationControlPolicyMutationInput] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
