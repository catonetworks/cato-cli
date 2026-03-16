
## CATO-CLI - mutation.policy.socketBypass.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.removeRule) for documentation on this operation.

### Usage for mutation.policy.socketBypass.removeRule:

```bash
catocli mutation policy socketBypass removeRule -h

catocli mutation policy socketBypass removeRule <json>

catocli mutation policy socketBypass removeRule --json-file mutation.policy.socketBypass.removeRule.json

catocli mutation policy socketBypass removeRule '{"socketBypassPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"socketBypassRemoveRuleInput":{"id":"id"}}'

catocli mutation policy socketBypass removeRule '{
    "socketBypassPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "socketBypassRemoveRuleInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.policy.socketBypass.removeRule ####

`accountId` [ID] - (required) N/A    
`socketBypassPolicyMutationInput` [SocketBypassPolicyMutationInput] - (required) N/A    
`socketBypassRemoveRuleInput` [SocketBypassRemoveRuleInput] - (required) N/A    
