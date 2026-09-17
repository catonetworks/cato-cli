
## CATO-CLI - mutation.policy.privateAccess.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.privateAccess.addSection) for documentation on this operation.

### Usage for mutation.policy.privateAccess.addSection:

```bash
catocli mutation policy privateAccess addSection -h

catocli mutation policy privateAccess addSection <json>

catocli mutation policy privateAccess addSection --json-file mutation.policy.privateAccess.addSection.json

catocli mutation policy privateAccess addSection '{"policyAddSectionInput":{"at":{"position":"AFTER_SECTION","ref":"id"},"section":{"name":"string"}},"privateAccessPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy privateAccess addSection '{
    "policyAddSectionInput": {
        "at": {
            "position": "AFTER_SECTION",
            "ref": "id"
        },
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

#### Operation Arguments for mutation.policy.privateAccess.addSection ####

`accountId` [ID] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
`privateAccessPolicyMutationInput` [PrivateAccessPolicyMutationInput] - (required) N/A    
