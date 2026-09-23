
## CATO-CLI - mutation.policy.privateAccess.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.privateAccess.moveSection) for documentation on this operation.

### Usage for mutation.policy.privateAccess.moveSection:

```bash
catocli mutation policy privateAccess moveSection -h

catocli mutation policy privateAccess moveSection <json>

catocli mutation policy privateAccess moveSection --json-file mutation.policy.privateAccess.moveSection.json

catocli mutation policy privateAccess moveSection '{"policyMoveSectionInput":{"id":"id","to":{"position":"AFTER_SECTION","ref":"id"}},"privateAccessPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy privateAccess moveSection '{
    "policyMoveSectionInput": {
        "id": "id",
        "to": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    },
    "privateAccessPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.privateAccess.moveSection ####

`accountId` [ID] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
`privateAccessPolicyMutationInput` [PrivateAccessPolicyMutationInput] - (required) N/A    
