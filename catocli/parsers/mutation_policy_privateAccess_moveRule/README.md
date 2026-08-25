
## CATO-CLI - mutation.policy.privateAccess.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.privateAccess.moveRule) for documentation on this operation.

### Usage for mutation.policy.privateAccess.moveRule:

```bash
catocli mutation policy privateAccess moveRule -h

catocli mutation policy privateAccess moveRule <json>

catocli mutation policy privateAccess moveRule --json-file mutation.policy.privateAccess.moveRule.json

catocli mutation policy privateAccess moveRule '{"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}},"privateAccessPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy privateAccess moveRule '{
    "policyMoveRuleInput": {
        "id": "id",
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    },
    "privateAccessPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.privateAccess.moveRule ####

`accountId` [ID] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
`privateAccessPolicyMutationInput` [PrivateAccessPolicyMutationInput] - (required) N/A    
