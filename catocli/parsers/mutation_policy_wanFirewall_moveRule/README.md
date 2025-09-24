
## CATO-CLI - mutation.policy.wanFirewall.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanFirewall.moveRule) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.moveRule:

`catocli mutation policy wanFirewall moveRule -h`

`catocli mutation policy wanFirewall moveRule <json>`

`catocli mutation policy wanFirewall moveRule "$(cat < mutation.policy.wanFirewall.moveRule.json)"`

`catocli mutation policy wanFirewall moveRule '{"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}},"wanFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanFirewall moveRule -p '{
    "policyMoveRuleInput": {
        "id": "id",
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    },
    "wanFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanFirewall.moveRule ####

`accountId` [ID] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (required) N/A    
