
## CATO-CLI - mutation.policy.socketLan.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.removeSection) for documentation on this operation.

### Usage for mutation.policy.socketLan.removeSection:

`catocli mutation policy socketLan removeSection -h`

`catocli mutation policy socketLan removeSection <json>`

`catocli mutation policy socketLan removeSection "$(cat < mutation.policy.socketLan.removeSection.json)"`

`catocli mutation policy socketLan removeSection '{"policyRemoveSectionInput":{"id":"id"},"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy socketLan removeSection -p '{
    "policyRemoveSectionInput": {
        "id": "id"
    },
    "socketLanPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.socketLan.removeSection ####

`accountId` [ID] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
