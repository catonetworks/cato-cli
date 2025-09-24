
## CATO-CLI - mutation.policy.socketLan.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.socketLan.updatePolicy:

`catocli mutation policy socketLan updatePolicy -h`

`catocli mutation policy socketLan updatePolicy <json>`

`catocli mutation policy socketLan updatePolicy "$(cat < mutation.policy.socketLan.updatePolicy.json)"`

`catocli mutation policy socketLan updatePolicy '{"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"socketLanPolicyUpdateInput":{"state":"ENABLED"}}'`

`catocli mutation policy socketLan updatePolicy -p '{
    "socketLanPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "socketLanPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'`


#### Operation Arguments for mutation.policy.socketLan.updatePolicy ####

`accountId` [ID] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
`socketLanPolicyUpdateInput` [SocketLanPolicyUpdateInput] - (required) N/A    
