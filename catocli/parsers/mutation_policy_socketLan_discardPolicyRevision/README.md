
## CATO-CLI - mutation.policy.socketLan.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.socketLan.discardPolicyRevision:

`catocli mutation policy socketLan discardPolicyRevision -h`

`catocli mutation policy socketLan discardPolicyRevision <json>`

`catocli mutation policy socketLan discardPolicyRevision "$(cat < mutation.policy.socketLan.discardPolicyRevision.json)"`

`catocli mutation policy socketLan discardPolicyRevision '{"policyDiscardRevisionInput":{"id":"id"},"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy socketLan discardPolicyRevision -p '{
    "policyDiscardRevisionInput": {
        "id": "id"
    },
    "socketLanPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.socketLan.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
