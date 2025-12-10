
## CATO-CLI - mutation.policy.clientConnectivity.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.clientConnectivity.removeSection) for documentation on this operation.

### Usage for mutation.policy.clientConnectivity.removeSection:

```bash
catocli mutation policy clientConnectivity removeSection -h

catocli mutation policy clientConnectivity removeSection <json>

catocli mutation policy clientConnectivity removeSection --json-file mutation.policy.clientConnectivity.removeSection.json

catocli mutation policy clientConnectivity removeSection '{"clientConnectivityPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyRemoveSectionInput":{"id":"id"}}'

catocli mutation policy clientConnectivity removeSection '{
    "clientConnectivityPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyRemoveSectionInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.policy.clientConnectivity.removeSection ####

`accountId` [ID] - (required) N/A    
`clientConnectivityPolicyMutationInput` [ClientConnectivityPolicyMutationInput] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
