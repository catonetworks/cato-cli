
## CATO-CLI - mutation.policy.clientConnectivity.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.clientConnectivity.moveRule) for documentation on this operation.

### Usage for mutation.policy.clientConnectivity.moveRule:

```bash
catocli mutation policy clientConnectivity moveRule -h

catocli mutation policy clientConnectivity moveRule <json>

catocli mutation policy clientConnectivity moveRule --json-file mutation.policy.clientConnectivity.moveRule.json

catocli mutation policy clientConnectivity moveRule '{"clientConnectivityPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}}}'

catocli mutation policy clientConnectivity moveRule '{
    "clientConnectivityPolicyMutationInput": {
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
}'
```

#### Operation Arguments for mutation.policy.clientConnectivity.moveRule ####

`accountId` [ID] - (required) N/A    
`clientConnectivityPolicyMutationInput` [ClientConnectivityPolicyMutationInput] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
