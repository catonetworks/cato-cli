
## CATO-CLI - mutation.policy.privateAccess.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.privateAccess.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.privateAccess.createPolicyRevision:

```bash
catocli mutation policy privateAccess createPolicyRevision -h

catocli mutation policy privateAccess createPolicyRevision <json>

catocli mutation policy privateAccess createPolicyRevision --json-file mutation.policy.privateAccess.createPolicyRevision.json

catocli mutation policy privateAccess createPolicyRevision '{"policyCreateRevisionInput":{"description":"string","name":"string"},"privateAccessPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy privateAccess createPolicyRevision '{
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "privateAccessPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.privateAccess.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
`privateAccessPolicyMutationInput` [PrivateAccessPolicyMutationInput] - (required) N/A    
