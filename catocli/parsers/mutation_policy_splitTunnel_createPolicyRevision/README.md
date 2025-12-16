
## CATO-CLI - mutation.policy.splitTunnel.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.splitTunnel.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.splitTunnel.createPolicyRevision:

```bash
catocli mutation policy splitTunnel createPolicyRevision -h

catocli mutation policy splitTunnel createPolicyRevision <json>

catocli mutation policy splitTunnel createPolicyRevision --json-file mutation.policy.splitTunnel.createPolicyRevision.json

catocli mutation policy splitTunnel createPolicyRevision '{"policyCreateRevisionInput":{"description":"string","name":"string"},"splitTunnelPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy splitTunnel createPolicyRevision '{
    "policyCreateRevisionInput": {
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

#### Operation Arguments for mutation.policy.splitTunnel.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
`splitTunnelPolicyMutationInput` [SplitTunnelPolicyMutationInput] - (required) N/A    
