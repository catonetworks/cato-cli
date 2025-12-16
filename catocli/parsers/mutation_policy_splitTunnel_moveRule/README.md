
## CATO-CLI - mutation.policy.splitTunnel.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.splitTunnel.moveRule) for documentation on this operation.

### Usage for mutation.policy.splitTunnel.moveRule:

```bash
catocli mutation policy splitTunnel moveRule -h

catocli mutation policy splitTunnel moveRule <json>

catocli mutation policy splitTunnel moveRule --json-file mutation.policy.splitTunnel.moveRule.json

catocli mutation policy splitTunnel moveRule '{"policyMoveRuleInput":{"id":"id","policyRulePositionInput":{"position":"AFTER_RULE","ref":"id"}},"splitTunnelPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy splitTunnel moveRule '{
    "policyMoveRuleInput": {
        "id": "id",
        "policyRulePositionInput": {
            "position": "AFTER_RULE",
            "ref": "id"
        }
    },
    "splitTunnelPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.splitTunnel.moveRule ####

`accountId` [ID] - (required) N/A    
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A    
`splitTunnelPolicyMutationInput` [SplitTunnelPolicyMutationInput] - (required) N/A    
