
## CATO-CLI - mutation.policy.splitTunnel.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.splitTunnel.removeSection) for documentation on this operation.

### Usage for mutation.policy.splitTunnel.removeSection:

```bash
catocli mutation policy splitTunnel removeSection -h

catocli mutation policy splitTunnel removeSection <json>

catocli mutation policy splitTunnel removeSection --json-file mutation.policy.splitTunnel.removeSection.json

catocli mutation policy splitTunnel removeSection '{"policyRemoveSectionInput":{"id":"id"},"splitTunnelPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy splitTunnel removeSection '{
    "policyRemoveSectionInput": {
        "id": "id"
    },
    "splitTunnelPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.splitTunnel.removeSection ####

`accountId` [ID] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
`splitTunnelPolicyMutationInput` [SplitTunnelPolicyMutationInput] - (required) N/A    
