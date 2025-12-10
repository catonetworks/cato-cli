
## CATO-CLI - mutation.policy.clientConnectivity.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.clientConnectivity.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.clientConnectivity.createPolicyRevision:

```bash
catocli mutation policy clientConnectivity createPolicyRevision -h

catocli mutation policy clientConnectivity createPolicyRevision <json>

catocli mutation policy clientConnectivity createPolicyRevision --json-file mutation.policy.clientConnectivity.createPolicyRevision.json

catocli mutation policy clientConnectivity createPolicyRevision '{"clientConnectivityPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyCreateRevisionInput":{"description":"string","name":"string"}}'

catocli mutation policy clientConnectivity createPolicyRevision '{
    "clientConnectivityPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.policy.clientConnectivity.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`clientConnectivityPolicyMutationInput` [ClientConnectivityPolicyMutationInput] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
