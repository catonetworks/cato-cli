
## CATO-CLI - mutation.policy.clientConnectivity.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.clientConnectivity.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.clientConnectivity.updatePolicy:

```bash
catocli mutation policy clientConnectivity updatePolicy -h

catocli mutation policy clientConnectivity updatePolicy <json>

catocli mutation policy clientConnectivity updatePolicy --json-file mutation.policy.clientConnectivity.updatePolicy.json

catocli mutation policy clientConnectivity updatePolicy '{"clientConnectivityPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"clientConnectivityPolicyUpdateInput":{"state":"ENABLED"}}'

catocli mutation policy clientConnectivity updatePolicy '{
    "clientConnectivityPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "clientConnectivityPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'
```

#### Operation Arguments for mutation.policy.clientConnectivity.updatePolicy ####

`accountId` [ID] - (required) N/A    
`clientConnectivityPolicyMutationInput` [ClientConnectivityPolicyMutationInput] - (required) N/A    
`clientConnectivityPolicyUpdateInput` [ClientConnectivityPolicyUpdateInput] - (required) N/A    
