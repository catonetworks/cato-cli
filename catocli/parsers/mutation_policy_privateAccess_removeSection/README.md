
## CATO-CLI - mutation.policy.privateAccess.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.privateAccess.removeSection) for documentation on this operation.

### Usage for mutation.policy.privateAccess.removeSection:

```bash
catocli mutation policy privateAccess removeSection -h

catocli mutation policy privateAccess removeSection <json>

catocli mutation policy privateAccess removeSection --json-file mutation.policy.privateAccess.removeSection.json

catocli mutation policy privateAccess removeSection '{"policyRemoveSectionInput":{"id":"id"},"privateAccessPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy privateAccess removeSection '{
    "policyRemoveSectionInput": {
        "id": "id"
    },
    "privateAccessPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.privateAccess.removeSection ####

`accountId` [ID] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
`privateAccessPolicyMutationInput` [PrivateAccessPolicyMutationInput] - (required) N/A    
