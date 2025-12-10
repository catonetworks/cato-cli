
## CATO-CLI - mutation.policy.clientConnectivity.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.clientConnectivity.updateSection) for documentation on this operation.

### Usage for mutation.policy.clientConnectivity.updateSection:

```bash
catocli mutation policy clientConnectivity updateSection -h

catocli mutation policy clientConnectivity updateSection <json>

catocli mutation policy clientConnectivity updateSection --json-file mutation.policy.clientConnectivity.updateSection.json

catocli mutation policy clientConnectivity updateSection '{"clientConnectivityPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyUpdateSectionInput":{"id":"id","policyUpdateSectionInfoInput":{"name":"string"}}}'

catocli mutation policy clientConnectivity updateSection '{
    "clientConnectivityPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyUpdateSectionInput": {
        "id": "id",
        "policyUpdateSectionInfoInput": {
            "name": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.clientConnectivity.updateSection ####

`accountId` [ID] - (required) N/A    
`clientConnectivityPolicyMutationInput` [ClientConnectivityPolicyMutationInput] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
