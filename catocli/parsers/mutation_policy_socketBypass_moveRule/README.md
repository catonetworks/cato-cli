
## CATO-CLI - mutation.policy.socketBypass.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.moveRule) for documentation on this operation.

### Usage for mutation.policy.socketBypass.moveRule:

```bash
catocli mutation policy socketBypass moveRule -h

catocli mutation policy socketBypass moveRule <json>

catocli mutation policy socketBypass moveRule --json-file mutation.policy.socketBypass.moveRule.json

catocli mutation policy socketBypass moveRule '{"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}},"socketBypassPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy socketBypass moveRule '{
    "policyMoveRuleInput": {
        "id": "id",
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    },
    "socketBypassPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketBypass.moveRule ####

`accountId` [ID] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
`socketBypassPolicyMutationInput` [SocketBypassPolicyMutationInput] - (required) N/A    
