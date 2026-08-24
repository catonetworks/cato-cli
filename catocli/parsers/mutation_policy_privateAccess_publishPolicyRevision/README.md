
## CATO-CLI - mutation.policy.privateAccess.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.privateAccess.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.privateAccess.publishPolicyRevision:

```bash
catocli mutation policy privateAccess publishPolicyRevision -h

catocli mutation policy privateAccess publishPolicyRevision <json>

catocli mutation policy privateAccess publishPolicyRevision --json-file mutation.policy.privateAccess.publishPolicyRevision.json

catocli mutation policy privateAccess publishPolicyRevision '{"policyPublishRevisionInput":{"description":"string","name":"string"},"privateAccessPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy privateAccess publishPolicyRevision '{
    "policyPublishRevisionInput": {
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

#### Operation Arguments for mutation.policy.privateAccess.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
`privateAccessPolicyMutationInput` [PrivateAccessPolicyMutationInput] - (required) N/A    
