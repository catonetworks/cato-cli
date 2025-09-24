
## CATO-CLI - mutation.policy.socketLan.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.socketLan.publishPolicyRevision:

`catocli mutation policy socketLan publishPolicyRevision -h`

`catocli mutation policy socketLan publishPolicyRevision <json>`

`catocli mutation policy socketLan publishPolicyRevision "$(cat < mutation.policy.socketLan.publishPolicyRevision.json)"`

`catocli mutation policy socketLan publishPolicyRevision '{"policyPublishRevisionInput":{"description":"string","name":"string"},"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy socketLan publishPolicyRevision -p '{
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "socketLanPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.socketLan.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
