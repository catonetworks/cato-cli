
## CATO-CLI - mutation.policy.clientConnectivity.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.clientConnectivity.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.clientConnectivity.discardPolicyRevision:

```bash
catocli mutation policy clientConnectivity discardPolicyRevision -h

catocli mutation policy clientConnectivity discardPolicyRevision <json>

catocli mutation policy clientConnectivity discardPolicyRevision --json-file mutation.policy.clientConnectivity.discardPolicyRevision.json

catocli mutation policy clientConnectivity discardPolicyRevision '{"clientConnectivityPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyDiscardRevisionInput":{"id":"id"}}'

catocli mutation policy clientConnectivity discardPolicyRevision '{
    "clientConnectivityPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyDiscardRevisionInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.policy.clientConnectivity.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`clientConnectivityPolicyMutationInput` [ClientConnectivityPolicyMutationInput] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
