
## CATO-CLI - mutation.policy.socketLan.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.addSection) for documentation on this operation.

### Usage for mutation.policy.socketLan.addSection:

`catocli mutation policy socketLan addSection -h`

`catocli mutation policy socketLan addSection <json>`

`catocli mutation policy socketLan addSection "$(cat < mutation.policy.socketLan.addSection.json)"`

`catocli mutation policy socketLan addSection '{"policyAddSectionInput":{"policyAddSectionInfoInput":{"name":"string"},"policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy socketLan addSection -p '{
    "policyAddSectionInput": {
        "policyAddSectionInfoInput": {
            "name": "string"
        },
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


#### Operation Arguments for mutation.policy.socketLan.addSection ####

`accountId` [ID] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
