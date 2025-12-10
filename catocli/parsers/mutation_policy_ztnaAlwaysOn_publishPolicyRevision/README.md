
## CATO-CLI - mutation.policy.ztnaAlwaysOn.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.ztnaAlwaysOn.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.ztnaAlwaysOn.publishPolicyRevision:

```bash
catocli mutation policy ztnaAlwaysOn publishPolicyRevision -h

catocli mutation policy ztnaAlwaysOn publishPolicyRevision <json>

catocli mutation policy ztnaAlwaysOn publishPolicyRevision --json-file mutation.policy.ztnaAlwaysOn.publishPolicyRevision.json

catocli mutation policy ztnaAlwaysOn publishPolicyRevision '{"policyPublishRevisionInput":{"description":"string","name":"string"},"ztnaAlwaysOnPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy ztnaAlwaysOn publishPolicyRevision '{
    "policyPublishRevisionInput": {
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

#### Operation Arguments for mutation.policy.ztnaAlwaysOn.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
`ztnaAlwaysOnPolicyMutationInput` [ZtnaAlwaysOnPolicyMutationInput] - (required) N/A    
