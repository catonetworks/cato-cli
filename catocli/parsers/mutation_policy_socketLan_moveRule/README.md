
## CATO-CLI - mutation.policy.socketLan.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.moveRule) for documentation on this operation.

### Usage for mutation.policy.socketLan.moveRule:

`catocli mutation policy socketLan moveRule -h`

`catocli mutation policy socketLan moveRule <json>`

`catocli mutation policy socketLan moveRule "$(cat < mutation.policy.socketLan.moveRule.json)"`

`catocli mutation policy socketLan moveRule '{"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}},"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy socketLan moveRule -p '{
    "policyMoveRuleInput": {
        "id": "id",
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    },
    "socketLanPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.socketLan.moveRule ####

`accountId` [ID] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
