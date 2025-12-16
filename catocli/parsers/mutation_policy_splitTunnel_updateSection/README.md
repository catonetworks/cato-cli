
## CATO-CLI - mutation.policy.splitTunnel.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.splitTunnel.updateSection) for documentation on this operation.

### Usage for mutation.policy.splitTunnel.updateSection:

```bash
catocli mutation policy splitTunnel updateSection -h

catocli mutation policy splitTunnel updateSection <json>

catocli mutation policy splitTunnel updateSection --json-file mutation.policy.splitTunnel.updateSection.json

catocli mutation policy splitTunnel updateSection '{"policyUpdateSectionInput":{"id":"id","policyUpdateSectionInfoInput":{"name":"string"}},"splitTunnelPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy splitTunnel updateSection '{
    "policyUpdateSectionInput": {
        "id": "id",
        "policyUpdateSectionInfoInput": {
            "name": "string"
        }
    },
    "splitTunnelPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.splitTunnel.updateSection ####

`accountId` [ID] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
`splitTunnelPolicyMutationInput` [SplitTunnelPolicyMutationInput] - (required) N/A    
