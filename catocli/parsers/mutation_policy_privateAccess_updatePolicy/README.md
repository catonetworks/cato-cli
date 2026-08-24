
## CATO-CLI - mutation.policy.privateAccess.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.privateAccess.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.privateAccess.updatePolicy:

```bash
catocli mutation policy privateAccess updatePolicy -h

catocli mutation policy privateAccess updatePolicy <json>

catocli mutation policy privateAccess updatePolicy --json-file mutation.policy.privateAccess.updatePolicy.json

catocli mutation policy privateAccess updatePolicy '{"privateAccessPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"privateAccessPolicyUpdateInput":{"state":"ENABLED"}}'

catocli mutation policy privateAccess updatePolicy '{
    "privateAccessPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "privateAccessPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'
```

#### Operation Arguments for mutation.policy.privateAccess.updatePolicy ####

`accountId` [ID] - (required) N/A    
`privateAccessPolicyMutationInput` [PrivateAccessPolicyMutationInput] - (required) N/A    
`privateAccessPolicyUpdateInput` [PrivateAccessPolicyUpdateInput] - (required) N/A    
