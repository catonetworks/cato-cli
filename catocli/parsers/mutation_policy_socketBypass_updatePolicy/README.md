
## CATO-CLI - mutation.policy.socketBypass.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.socketBypass.updatePolicy:

```bash
catocli mutation policy socketBypass updatePolicy -h

catocli mutation policy socketBypass updatePolicy <json>

catocli mutation policy socketBypass updatePolicy --json-file mutation.policy.socketBypass.updatePolicy.json

catocli mutation policy socketBypass updatePolicy '{"socketBypassPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"socketBypassPolicyUpdateInput":{"state":"ENABLED"}}'

catocli mutation policy socketBypass updatePolicy '{
    "socketBypassPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "socketBypassPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'
```

#### Operation Arguments for mutation.policy.socketBypass.updatePolicy ####

`accountId` [ID] - (required) N/A    
`socketBypassPolicyMutationInput` [SocketBypassPolicyMutationInput] - (required) N/A    
`socketBypassPolicyUpdateInput` [SocketBypassPolicyUpdateInput] - (required) N/A    
