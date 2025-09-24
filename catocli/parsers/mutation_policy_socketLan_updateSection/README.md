
## CATO-CLI - mutation.policy.socketLan.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.updateSection) for documentation on this operation.

### Usage for mutation.policy.socketLan.updateSection:

`catocli mutation policy socketLan updateSection -h`

`catocli mutation policy socketLan updateSection <json>`

`catocli mutation policy socketLan updateSection "$(cat < mutation.policy.socketLan.updateSection.json)"`

`catocli mutation policy socketLan updateSection '{"policyUpdateSectionInput":{"id":"id","policyUpdateSectionInfoInput":{"name":"string"}},"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy socketLan updateSection -p '{
    "policyUpdateSectionInput": {
        "id": "id",
        "policyUpdateSectionInfoInput": {
            "name": "string"
        }
    },
    "socketLanPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.socketLan.updateSection ####

`accountId` [ID] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
