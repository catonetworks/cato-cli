
## CATO-CLI - mutation.policy.wanNetwork.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanNetwork.moveRule) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.moveRule:

`catocli mutation policy wanNetwork moveRule -h`

`catocli mutation policy wanNetwork moveRule <json>`

`catocli mutation policy wanNetwork moveRule "$(cat < mutation.policy.wanNetwork.moveRule.json)"`

`catocli mutation policy wanNetwork moveRule '{"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}},"wanNetworkPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanNetwork moveRule -p '{
    "policyMoveRuleInput": {
        "id": "id",
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    },
    "wanNetworkPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanNetwork.moveRule ####

`accountId` [ID] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (required) N/A    
