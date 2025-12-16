
## CATO-CLI - mutation.policy.splitTunnel.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.splitTunnel.removeRule) for documentation on this operation.

### Usage for mutation.policy.splitTunnel.removeRule:

```bash
catocli mutation policy splitTunnel removeRule -h

catocli mutation policy splitTunnel removeRule <json>

catocli mutation policy splitTunnel removeRule --json-file mutation.policy.splitTunnel.removeRule.json

catocli mutation policy splitTunnel removeRule '{"splitTunnelPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"splitTunnelRemoveRuleInput":{"id":"id"}}'

catocli mutation policy splitTunnel removeRule '{
    "splitTunnelPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "splitTunnelRemoveRuleInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.policy.splitTunnel.removeRule ####

`accountId` [ID] - (required) N/A    
`splitTunnelPolicyMutationInput` [SplitTunnelPolicyMutationInput] - (required) N/A    
`splitTunnelRemoveRuleInput` [SplitTunnelRemoveRuleInput] - (required) N/A    
