
## CATO-CLI - mutation.policy.tlsInspect.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.addSection) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.addSection:

`catocli mutation policy tlsInspect addSection -h`

`catocli mutation policy tlsInspect addSection <json>`

`catocli mutation policy tlsInspect addSection "$(cat < mutation.policy.tlsInspect.addSection.json)"`

`catocli mutation policy tlsInspect addSection '{"policyAddSectionInput":{"policyAddSectionInfoInput":{"name":"string"},"policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"tlsInspectPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy tlsInspect addSection -p '{
    "policyAddSectionInput": {
        "policyAddSectionInfoInput": {
            "name": "string"
        },
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    },
    "tlsInspectPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.tlsInspect.addSection ####

`accountId` [ID] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A    
