
## CATO-CLI - mutation.policy.tlsInspect.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.updateSection) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.updateSection:

`catocli mutation policy tlsInspect updateSection -h`

`catocli mutation policy tlsInspect updateSection <json>`

`catocli mutation policy tlsInspect updateSection "$(cat < mutation.policy.tlsInspect.updateSection.json)"`

`catocli mutation policy tlsInspect updateSection '{"policyUpdateSectionInput":{"id":"id","policyUpdateSectionInfoInput":{"name":"string"}},"tlsInspectPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy tlsInspect updateSection -p '{
    "policyUpdateSectionInput": {
        "id": "id",
        "policyUpdateSectionInfoInput": {
            "name": "string"
        }
    },
    "tlsInspectPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.tlsInspect.updateSection ####

`accountId` [ID] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A    
