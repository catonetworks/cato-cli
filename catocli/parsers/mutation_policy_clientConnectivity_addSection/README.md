
## CATO-CLI - mutation.policy.clientConnectivity.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.clientConnectivity.addSection) for documentation on this operation.

### Usage for mutation.policy.clientConnectivity.addSection:

```bash
catocli mutation policy clientConnectivity addSection -h

catocli mutation policy clientConnectivity addSection <json>

catocli mutation policy clientConnectivity addSection --json-file mutation.policy.clientConnectivity.addSection.json

catocli mutation policy clientConnectivity addSection '{"clientConnectivityPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyAddSectionInput":{"policyAddSectionInfoInput":{"name":"string"},"policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}}}'

catocli mutation policy clientConnectivity addSection '{
    "clientConnectivityPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyAddSectionInput": {
        "policyAddSectionInfoInput": {
            "name": "string"
        },
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.clientConnectivity.addSection ####

`accountId` [ID] - (required) N/A    
`clientConnectivityPolicyMutationInput` [ClientConnectivityPolicyMutationInput] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
