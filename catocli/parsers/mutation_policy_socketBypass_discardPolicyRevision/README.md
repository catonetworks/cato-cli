
## CATO-CLI - mutation.policy.socketBypass.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.socketBypass.discardPolicyRevision:

```bash
catocli mutation policy socketBypass discardPolicyRevision -h

catocli mutation policy socketBypass discardPolicyRevision <json>

catocli mutation policy socketBypass discardPolicyRevision --json-file mutation.policy.socketBypass.discardPolicyRevision.json

catocli mutation policy socketBypass discardPolicyRevision '{"policyDiscardRevisionInput":{"id":"id"},"socketBypassPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy socketBypass discardPolicyRevision '{
    "policyDiscardRevisionInput": {
        "id": "id"
    },
    "socketBypassPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketBypass.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
`socketBypassPolicyMutationInput` [SocketBypassPolicyMutationInput] - (required) N/A    
