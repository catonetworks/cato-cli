
## CATO-CLI - mutation.policy.ztnaAlwaysOn.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.ztnaAlwaysOn.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.ztnaAlwaysOn.createPolicyRevision:

```bash
catocli mutation policy ztnaAlwaysOn createPolicyRevision -h

catocli mutation policy ztnaAlwaysOn createPolicyRevision <json>

catocli mutation policy ztnaAlwaysOn createPolicyRevision --json-file mutation.policy.ztnaAlwaysOn.createPolicyRevision.json

catocli mutation policy ztnaAlwaysOn createPolicyRevision '{"policyCreateRevisionInput":{"description":"string","name":"string"},"ztnaAlwaysOnPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy ztnaAlwaysOn createPolicyRevision '{
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "ztnaAlwaysOnPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.ztnaAlwaysOn.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
`ztnaAlwaysOnPolicyMutationInput` [ZtnaAlwaysOnPolicyMutationInput] - (required) N/A    
