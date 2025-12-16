
## CATO-CLI - mutation.policy.splitTunnel.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.splitTunnel.addSection) for documentation on this operation.

### Usage for mutation.policy.splitTunnel.addSection:

```bash
catocli mutation policy splitTunnel addSection -h

catocli mutation policy splitTunnel addSection <json>

catocli mutation policy splitTunnel addSection --json-file mutation.policy.splitTunnel.addSection.json

catocli mutation policy splitTunnel addSection '{"policyAddSectionInput":{"policyAddSectionInfoInput":{"name":"string"},"policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"splitTunnelPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy splitTunnel addSection '{
    "policyAddSectionInput": {
        "policyAddSectionInfoInput": {
            "name": "string"
        },
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

#### Operation Arguments for mutation.policy.splitTunnel.addSection ####

`accountId` [ID] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
`splitTunnelPolicyMutationInput` [SplitTunnelPolicyMutationInput] - (required) N/A    
