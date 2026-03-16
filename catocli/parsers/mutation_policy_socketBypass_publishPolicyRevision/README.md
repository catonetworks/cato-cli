
## CATO-CLI - mutation.policy.socketBypass.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.socketBypass.publishPolicyRevision:

```bash
catocli mutation policy socketBypass publishPolicyRevision -h

catocli mutation policy socketBypass publishPolicyRevision <json>

catocli mutation policy socketBypass publishPolicyRevision --json-file mutation.policy.socketBypass.publishPolicyRevision.json

catocli mutation policy socketBypass publishPolicyRevision '{"policyPublishRevisionInput":{"description":"string","name":"string"},"socketBypassPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy socketBypass publishPolicyRevision '{
    "policyPublishRevisionInput": {
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

#### Operation Arguments for mutation.policy.socketBypass.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
`socketBypassPolicyMutationInput` [SocketBypassPolicyMutationInput] - (required) N/A    
