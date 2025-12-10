
## CATO-CLI - mutation.policy.ztnaAlwaysOn.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.ztnaAlwaysOn.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.ztnaAlwaysOn.discardPolicyRevision:

```bash
catocli mutation policy ztnaAlwaysOn discardPolicyRevision -h

catocli mutation policy ztnaAlwaysOn discardPolicyRevision <json>

catocli mutation policy ztnaAlwaysOn discardPolicyRevision --json-file mutation.policy.ztnaAlwaysOn.discardPolicyRevision.json

catocli mutation policy ztnaAlwaysOn discardPolicyRevision '{"policyDiscardRevisionInput":{"id":"id"},"ztnaAlwaysOnPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy ztnaAlwaysOn discardPolicyRevision '{
    "policyDiscardRevisionInput": {
        "id": "id"
    },
    "ztnaAlwaysOnPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.ztnaAlwaysOn.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
`ztnaAlwaysOnPolicyMutationInput` [ZtnaAlwaysOnPolicyMutationInput] - (required) N/A    
