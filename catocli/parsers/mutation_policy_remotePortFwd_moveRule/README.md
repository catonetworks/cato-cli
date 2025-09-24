
## CATO-CLI - mutation.policy.remotePortFwd.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.remotePortFwd.moveRule) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.moveRule:

`catocli mutation policy remotePortFwd moveRule -h`

`catocli mutation policy remotePortFwd moveRule <json>`

`catocli mutation policy remotePortFwd moveRule "$(cat < mutation.policy.remotePortFwd.moveRule.json)"`

`catocli mutation policy remotePortFwd moveRule '{"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}},"remotePortFwdPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy remotePortFwd moveRule -p '{
    "policyMoveRuleInput": {
        "id": "id",
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    },
    "remotePortFwdPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.remotePortFwd.moveRule ####

`accountId` [ID] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (required) N/A    
