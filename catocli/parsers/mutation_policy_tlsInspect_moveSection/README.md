
## CATO-CLI - mutation.policy.tlsInspect.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.moveSection) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.moveSection:

`catocli mutation policy tlsInspect moveSection -h`

`catocli mutation policy tlsInspect moveSection <json>`

`catocli mutation policy tlsInspect moveSection "$(cat < mutation.policy.tlsInspect.moveSection.json)"`

`catocli mutation policy tlsInspect moveSection '{"policyMoveSectionInput":{"id":"id","policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"tlsInspectPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy tlsInspect moveSection -p '{
    "policyMoveSectionInput": {
        "id": "id",
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


#### Operation Arguments for mutation.policy.tlsInspect.moveSection ####

`accountId` [ID] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A    
