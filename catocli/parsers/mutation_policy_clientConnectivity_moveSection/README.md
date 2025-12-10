
## CATO-CLI - mutation.policy.clientConnectivity.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.clientConnectivity.moveSection) for documentation on this operation.

### Usage for mutation.policy.clientConnectivity.moveSection:

```bash
catocli mutation policy clientConnectivity moveSection -h

catocli mutation policy clientConnectivity moveSection <json>

catocli mutation policy clientConnectivity moveSection --json-file mutation.policy.clientConnectivity.moveSection.json

catocli mutation policy clientConnectivity moveSection '{"clientConnectivityPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyMoveSectionInput":{"id":"id","policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}}}'

catocli mutation policy clientConnectivity moveSection '{
    "clientConnectivityPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyMoveSectionInput": {
        "id": "id",
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.clientConnectivity.moveSection ####

`accountId` [ID] - (required) N/A    
`clientConnectivityPolicyMutationInput` [ClientConnectivityPolicyMutationInput] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
