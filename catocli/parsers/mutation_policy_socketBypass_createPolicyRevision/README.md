
## CATO-CLI - mutation.policy.socketBypass.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.socketBypass.createPolicyRevision:

```bash
catocli mutation policy socketBypass createPolicyRevision -h

catocli mutation policy socketBypass createPolicyRevision <json>

catocli mutation policy socketBypass createPolicyRevision --json-file mutation.policy.socketBypass.createPolicyRevision.json

catocli mutation policy socketBypass createPolicyRevision '{"policyCreateRevisionInput":{"description":"string","name":"string"},"socketBypassPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy socketBypass createPolicyRevision '{
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "socketBypassPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketBypass.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
`socketBypassPolicyMutationInput` [SocketBypassPolicyMutationInput] - (required) N/A    
