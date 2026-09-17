
## CATO-CLI - mutation.policy.privateAccess.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.privateAccess.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.privateAccess.discardPolicyRevision:

```bash
catocli mutation policy privateAccess discardPolicyRevision -h

catocli mutation policy privateAccess discardPolicyRevision <json>

catocli mutation policy privateAccess discardPolicyRevision --json-file mutation.policy.privateAccess.discardPolicyRevision.json

catocli mutation policy privateAccess discardPolicyRevision '{"policyDiscardRevisionInput":{"id":"id"},"privateAccessPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy privateAccess discardPolicyRevision '{
    "policyDiscardRevisionInput": {
        "id": "id"
    },
    "privateAccessPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.privateAccess.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
`privateAccessPolicyMutationInput` [PrivateAccessPolicyMutationInput] - (required) N/A    
