
## CATO-CLI - mutation.policy.socketLan.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.moveSection) for documentation on this operation.

### Usage for mutation.policy.socketLan.moveSection:

`catocli mutation policy socketLan moveSection -h`

`catocli mutation policy socketLan moveSection <json>`

`catocli mutation policy socketLan moveSection "$(cat < mutation.policy.socketLan.moveSection.json)"`

`catocli mutation policy socketLan moveSection '{"policyMoveSectionInput":{"id":"id","policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy socketLan moveSection -p '{
    "policyMoveSectionInput": {
        "id": "id",
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    },
    "socketLanPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.socketLan.moveSection ####

`accountId` [ID] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
