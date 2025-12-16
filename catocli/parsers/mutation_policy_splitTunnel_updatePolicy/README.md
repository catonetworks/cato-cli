
## CATO-CLI - mutation.policy.splitTunnel.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.splitTunnel.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.splitTunnel.updatePolicy:

```bash
catocli mutation policy splitTunnel updatePolicy -h

catocli mutation policy splitTunnel updatePolicy <json>

catocli mutation policy splitTunnel updatePolicy --json-file mutation.policy.splitTunnel.updatePolicy.json

catocli mutation policy splitTunnel updatePolicy '{"splitTunnelPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"splitTunnelPolicyUpdateInput":{"state":"ENABLED"}}'

catocli mutation policy splitTunnel updatePolicy '{
    "splitTunnelPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "splitTunnelPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'
```

#### Operation Arguments for mutation.policy.splitTunnel.updatePolicy ####

`accountId` [ID] - (required) N/A    
`splitTunnelPolicyMutationInput` [SplitTunnelPolicyMutationInput] - (required) N/A    
`splitTunnelPolicyUpdateInput` [SplitTunnelPolicyUpdateInput] - (required) N/A    
