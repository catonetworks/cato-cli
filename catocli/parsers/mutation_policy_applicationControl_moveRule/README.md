
## CATO-CLI - mutation.policy.applicationControl.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.applicationControl.moveRule) for documentation on this operation.

### Usage for mutation.policy.applicationControl.moveRule:

`catocli mutation policy applicationControl moveRule -h`

`catocli mutation policy applicationControl moveRule <json>`

`catocli mutation policy applicationControl moveRule "$(cat < mutation.policy.applicationControl.moveRule.json)"`

`catocli mutation policy applicationControl moveRule '{"applicationControlPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}}}'`

`catocli mutation policy applicationControl moveRule -p '{
    "applicationControlPolicyMutationInput": {
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


#### Operation Arguments for mutation.policy.applicationControl.moveRule ####

`accountId` [ID] - (required) N/A    
`applicationControlPolicyMutationInput` [ApplicationControlPolicyMutationInput] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
