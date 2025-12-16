
## CATO-CLI - mutation.policy.splitTunnel.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.splitTunnel.moveSection) for documentation on this operation.

### Usage for mutation.policy.splitTunnel.moveSection:

```bash
catocli mutation policy splitTunnel moveSection -h

catocli mutation policy splitTunnel moveSection <json>

catocli mutation policy splitTunnel moveSection --json-file mutation.policy.splitTunnel.moveSection.json

catocli mutation policy splitTunnel moveSection '{"policyMoveSectionInput":{"id":"id","policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"splitTunnelPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy splitTunnel moveSection '{
    "policyMoveSectionInput": {
        "id": "id",
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
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

#### Operation Arguments for mutation.policy.splitTunnel.moveSection ####

`accountId` [ID] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
`splitTunnelPolicyMutationInput` [SplitTunnelPolicyMutationInput] - (required) N/A    
