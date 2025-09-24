
## CATO-CLI - mutation.policy.socketLan.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.socketLan.createPolicyRevision:

`catocli mutation policy socketLan createPolicyRevision -h`

`catocli mutation policy socketLan createPolicyRevision <json>`

`catocli mutation policy socketLan createPolicyRevision "$(cat < mutation.policy.socketLan.createPolicyRevision.json)"`

`catocli mutation policy socketLan createPolicyRevision '{"policyCreateRevisionInput":{"description":"string","name":"string"},"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy socketLan createPolicyRevision -p '{
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "socketLanPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.socketLan.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
