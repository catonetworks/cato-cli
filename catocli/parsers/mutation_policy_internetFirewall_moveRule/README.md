
## CATO-CLI - mutation.policy.internetFirewall.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.internetFirewall.moveRule) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.moveRule:

`catocli mutation policy internetFirewall moveRule -h`

`catocli mutation policy internetFirewall moveRule <json>`

`catocli mutation policy internetFirewall moveRule "$(cat < mutation.policy.internetFirewall.moveRule.json)"`

`catocli mutation policy internetFirewall moveRule '{"internetFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}}}'`

`catocli mutation policy internetFirewall moveRule -p '{
    "internetFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyMoveRuleInput": {
        "id": "id",
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.internetFirewall.moveRule ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
