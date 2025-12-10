
## CATO-CLI - mutation.policy.ztnaAlwaysOn.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.ztnaAlwaysOn.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.ztnaAlwaysOn.updatePolicy:

```bash
catocli mutation policy ztnaAlwaysOn updatePolicy -h

catocli mutation policy ztnaAlwaysOn updatePolicy <json>

catocli mutation policy ztnaAlwaysOn updatePolicy --json-file mutation.policy.ztnaAlwaysOn.updatePolicy.json

catocli mutation policy ztnaAlwaysOn updatePolicy '{"ztnaAlwaysOnPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"ztnaAlwaysOnPolicyUpdateInput":{"state":"ENABLED"}}'

catocli mutation policy ztnaAlwaysOn updatePolicy '{
    "ztnaAlwaysOnPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "ztnaAlwaysOnPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'
```

#### Operation Arguments for mutation.policy.ztnaAlwaysOn.updatePolicy ####

`accountId` [ID] - (required) N/A    
`ztnaAlwaysOnPolicyMutationInput` [ZtnaAlwaysOnPolicyMutationInput] - (required) N/A    
`ztnaAlwaysOnPolicyUpdateInput` [ZtnaAlwaysOnPolicyUpdateInput] - (required) N/A    
