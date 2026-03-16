
## CATO-CLI - mutation.policy.socketBypass.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.removeSection) for documentation on this operation.

### Usage for mutation.policy.socketBypass.removeSection:

```bash
catocli mutation policy socketBypass removeSection -h

catocli mutation policy socketBypass removeSection <json>

catocli mutation policy socketBypass removeSection --json-file mutation.policy.socketBypass.removeSection.json

catocli mutation policy socketBypass removeSection '{"policyRemoveSectionInput":{"id":"id"},"socketBypassPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy socketBypass removeSection '{
    "policyRemoveSectionInput": {
        "id": "id"
    },
    "socketBypassPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketBypass.removeSection ####

`accountId` [ID] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
`socketBypassPolicyMutationInput` [SocketBypassPolicyMutationInput] - (required) N/A    
