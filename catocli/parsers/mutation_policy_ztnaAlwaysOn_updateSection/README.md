
## CATO-CLI - mutation.policy.ztnaAlwaysOn.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.ztnaAlwaysOn.updateSection) for documentation on this operation.

### Usage for mutation.policy.ztnaAlwaysOn.updateSection:

```bash
catocli mutation policy ztnaAlwaysOn updateSection -h

catocli mutation policy ztnaAlwaysOn updateSection <json>

catocli mutation policy ztnaAlwaysOn updateSection --json-file mutation.policy.ztnaAlwaysOn.updateSection.json

catocli mutation policy ztnaAlwaysOn updateSection '{"policyUpdateSectionInput":{"id":"id","policyUpdateSectionInfoInput":{"name":"string"}},"ztnaAlwaysOnPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy ztnaAlwaysOn updateSection '{
    "policyUpdateSectionInput": {
        "id": "id",
        "policyUpdateSectionInfoInput": {
            "name": "string"
        }
    },
    "ztnaAlwaysOnPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.ztnaAlwaysOn.updateSection ####

`accountId` [ID] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
`ztnaAlwaysOnPolicyMutationInput` [ZtnaAlwaysOnPolicyMutationInput] - (required) N/A    
