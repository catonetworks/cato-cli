
## CATO-CLI - mutation.policy.socketLan.firewall.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.firewall.moveRule) for documentation on this operation.

### Usage for mutation.policy.socketLan.firewall.moveRule:

```bash
catocli mutation policy socketLan firewall moveRule -h

catocli mutation policy socketLan firewall moveRule <json>

catocli mutation policy socketLan firewall moveRule --json-file mutation.policy.socketLan.firewall.moveRule.json

catocli mutation policy socketLan firewall moveRule '{"policyMoveSubRuleInput":{"id":"id","policySubRulePositionInput":{"position":"AFTER_SUB_RULE","ref":"id"}},"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy socketLan firewall moveRule '{
    "policyMoveSubRuleInput": {
        "id": "id",
        "policySubRulePositionInput": {
            "position": "AFTER_SUB_RULE",
            "ref": "id"
        }
    },
    "socketLanPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketLan.firewall.moveRule ####

`accountId` [ID] - (required) N/A    
`policyMoveSubRuleInput` [PolicyMoveSubRuleInput] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
