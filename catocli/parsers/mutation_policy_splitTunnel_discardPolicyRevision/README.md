
## CATO-CLI - mutation.policy.splitTunnel.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.splitTunnel.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.splitTunnel.discardPolicyRevision:

```bash
catocli mutation policy splitTunnel discardPolicyRevision -h

catocli mutation policy splitTunnel discardPolicyRevision <json>

catocli mutation policy splitTunnel discardPolicyRevision --json-file mutation.policy.splitTunnel.discardPolicyRevision.json

catocli mutation policy splitTunnel discardPolicyRevision '{"policyDiscardRevisionInput":{"id":"id"},"splitTunnelPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy splitTunnel discardPolicyRevision '{
    "policyDiscardRevisionInput": {
        "id": "id"
    },
    "splitTunnelPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.splitTunnel.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
`splitTunnelPolicyMutationInput` [SplitTunnelPolicyMutationInput] - (required) N/A    
