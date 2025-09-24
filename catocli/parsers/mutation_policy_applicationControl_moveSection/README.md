
## CATO-CLI - mutation.policy.applicationControl.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.applicationControl.moveSection) for documentation on this operation.

### Usage for mutation.policy.applicationControl.moveSection:

`catocli mutation policy applicationControl moveSection -h`

`catocli mutation policy applicationControl moveSection <json>`

`catocli mutation policy applicationControl moveSection "$(cat < mutation.policy.applicationControl.moveSection.json)"`

`catocli mutation policy applicationControl moveSection '{"applicationControlPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyMoveSectionInput":{"id":"id","policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}}}'`

`catocli mutation policy applicationControl moveSection -p '{
    "applicationControlPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyMoveSectionInput": {
        "id": "id",
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.applicationControl.moveSection ####

`accountId` [ID] - (required) N/A    
`applicationControlPolicyMutationInput` [ApplicationControlPolicyMutationInput] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
