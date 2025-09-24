
## CATO-CLI - mutation.policy.terminalServer.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.terminalServer.moveRule) for documentation on this operation.

### Usage for mutation.policy.terminalServer.moveRule:

`catocli mutation policy terminalServer moveRule -h`

`catocli mutation policy terminalServer moveRule <json>`

`catocli mutation policy terminalServer moveRule "$(cat < mutation.policy.terminalServer.moveRule.json)"`

`catocli mutation policy terminalServer moveRule '{"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}},"terminalServerPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy terminalServer moveRule -p '{
    "policyMoveRuleInput": {
        "id": "id",
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    },
    "terminalServerPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.terminalServer.moveRule ####

`accountId` [ID] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
`terminalServerPolicyMutationInput` [TerminalServerPolicyMutationInput] - (required) N/A    
