
## CATO-CLI - mutation.policy.socketLan.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.removeRule) for documentation on this operation.

### Usage for mutation.policy.socketLan.removeRule:

`catocli mutation policy socketLan removeRule -h`

`catocli mutation policy socketLan removeRule <json>`

`catocli mutation policy socketLan removeRule "$(cat < mutation.policy.socketLan.removeRule.json)"`

`catocli mutation policy socketLan removeRule '{"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"socketLanRemoveRuleInput":{"id":"id"}}'`

`catocli mutation policy socketLan removeRule -p '{
    "socketLanPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "socketLanRemoveRuleInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.socketLan.removeRule ####

`accountId` [ID] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
`socketLanRemoveRuleInput` [SocketLanRemoveRuleInput] - (required) N/A    
