
## CATO-CLI - mutation.policy.privateAccess.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.privateAccess.updateSection) for documentation on this operation.

### Usage for mutation.policy.privateAccess.updateSection:

```bash
catocli mutation policy privateAccess updateSection -h

catocli mutation policy privateAccess updateSection <json>

catocli mutation policy privateAccess updateSection --json-file mutation.policy.privateAccess.updateSection.json

catocli mutation policy privateAccess updateSection '{"policyUpdateSectionInput":{"id":"id","section":{"name":"string"}},"privateAccessPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy privateAccess updateSection '{
    "policyUpdateSectionInput": {
        "id": "id",
        "section": {
            "name": "string"
        }
    },
    "privateAccessPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.privateAccess.updateSection ####

`accountId` [ID] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
`privateAccessPolicyMutationInput` [PrivateAccessPolicyMutationInput] - (required) N/A    
