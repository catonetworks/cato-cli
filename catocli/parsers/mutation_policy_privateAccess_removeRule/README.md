
## CATO-CLI - mutation.policy.privateAccess.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.privateAccess.removeRule) for documentation on this operation.

### Usage for mutation.policy.privateAccess.removeRule:

```bash
catocli mutation policy privateAccess removeRule -h

catocli mutation policy privateAccess removeRule <json>

catocli mutation policy privateAccess removeRule --json-file mutation.policy.privateAccess.removeRule.json

catocli mutation policy privateAccess removeRule '{"privateAccessPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"privateAccessRemoveRuleInput":{"id":"id"}}'

catocli mutation policy privateAccess removeRule '{
    "privateAccessPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "privateAccessRemoveRuleInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.policy.privateAccess.removeRule ####

`accountId` [ID] - (required) N/A    
`privateAccessPolicyMutationInput` [PrivateAccessPolicyMutationInput] - (required) N/A    
`privateAccessRemoveRuleInput` [PrivateAccessRemoveRuleInput] - (required) N/A    
