
## CATO-CLI - mutation.policy.clientConnectivity.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.clientConnectivity.removeRule) for documentation on this operation.

### Usage for mutation.policy.clientConnectivity.removeRule:

```bash
catocli mutation policy clientConnectivity removeRule -h

catocli mutation policy clientConnectivity removeRule <json>

catocli mutation policy clientConnectivity removeRule --json-file mutation.policy.clientConnectivity.removeRule.json

catocli mutation policy clientConnectivity removeRule '{"clientConnectivityPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"clientConnectivityRemoveRuleInput":{"id":"id"}}'

catocli mutation policy clientConnectivity removeRule '{
    "clientConnectivityPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "clientConnectivityRemoveRuleInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.policy.clientConnectivity.removeRule ####

`accountId` [ID] - (required) N/A    
`clientConnectivityPolicyMutationInput` [ClientConnectivityPolicyMutationInput] - (required) N/A    
`clientConnectivityRemoveRuleInput` [ClientConnectivityRemoveRuleInput] - (required) N/A    
