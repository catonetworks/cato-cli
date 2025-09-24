
## CATO-CLI - mutation.policy.tlsInspect.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.tlsInspect.moveRule) for documentation on this operation.

### Usage for mutation.policy.tlsInspect.moveRule:

`catocli mutation policy tlsInspect moveRule -h`

`catocli mutation policy tlsInspect moveRule <json>`

`catocli mutation policy tlsInspect moveRule "$(cat < mutation.policy.tlsInspect.moveRule.json)"`

`catocli mutation policy tlsInspect moveRule '{"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}},"tlsInspectPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy tlsInspect moveRule -p '{
    "policyMoveRuleInput": {
        "id": "id",
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    },
    "tlsInspectPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.tlsInspect.moveRule ####

`accountId` [ID] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
`tlsInspectPolicyMutationInput` [TlsInspectPolicyMutationInput] - (required) N/A    
