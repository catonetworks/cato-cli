
## CATO-CLI - mutation.policy.ztnaAlwaysOn.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.ztnaAlwaysOn.moveRule) for documentation on this operation.

### Usage for mutation.policy.ztnaAlwaysOn.moveRule:

```bash
catocli mutation policy ztnaAlwaysOn moveRule -h

catocli mutation policy ztnaAlwaysOn moveRule <json>

catocli mutation policy ztnaAlwaysOn moveRule --json-file mutation.policy.ztnaAlwaysOn.moveRule.json

catocli mutation policy ztnaAlwaysOn moveRule '{"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}},"ztnaAlwaysOnPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy ztnaAlwaysOn moveRule '{
    "policyMoveRuleInput": {
        "id": "id",
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    },
    "ztnaAlwaysOnPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.ztnaAlwaysOn.moveRule ####

`accountId` [ID] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
`ztnaAlwaysOnPolicyMutationInput` [ZtnaAlwaysOnPolicyMutationInput] - (required) N/A    
