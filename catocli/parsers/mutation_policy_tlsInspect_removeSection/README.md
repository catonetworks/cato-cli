
## CATO-CLI - mutation.policy.tlsInspect.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.removeSection) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.removeSection:

`catocli mutation policy tlsInspect removeSection -h`

`catocli mutation policy tlsInspect removeSection <json>`

`catocli mutation policy tlsInspect removeSection "$(cat < mutation.policy.tlsInspect.removeSection.json)"`

`catocli mutation policy tlsInspect removeSection '{"policyRemoveSectionInput":{"id":"id"},"tlsInspectPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy tlsInspect removeSection -p '{
    "policyRemoveSectionInput": {
        "id": "id"
    },
    "tlsInspectPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.tlsInspect.removeSection ####

`accountId` [ID] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A    
