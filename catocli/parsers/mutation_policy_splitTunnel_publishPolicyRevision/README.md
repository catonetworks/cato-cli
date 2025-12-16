
## CATO-CLI - mutation.policy.splitTunnel.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.splitTunnel.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.splitTunnel.publishPolicyRevision:

```bash
catocli mutation policy splitTunnel publishPolicyRevision -h

catocli mutation policy splitTunnel publishPolicyRevision <json>

catocli mutation policy splitTunnel publishPolicyRevision --json-file mutation.policy.splitTunnel.publishPolicyRevision.json

catocli mutation policy splitTunnel publishPolicyRevision '{"policyPublishRevisionInput":{"description":"string","name":"string"},"splitTunnelPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy splitTunnel publishPolicyRevision '{
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "splitTunnelPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.splitTunnel.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
`splitTunnelPolicyMutationInput` [SplitTunnelPolicyMutationInput] - (required) N/A    
