
## CATO-CLI - mutation.policy.socketBypass.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.updateSection) for documentation on this operation.

### Usage for mutation.policy.socketBypass.updateSection:

```bash
catocli mutation policy socketBypass updateSection -h

catocli mutation policy socketBypass updateSection <json>

catocli mutation policy socketBypass updateSection --json-file mutation.policy.socketBypass.updateSection.json

catocli mutation policy socketBypass updateSection '{"policyUpdateSectionInput":{"id":"id","policyUpdateSectionInfoInput":{"name":"string"}},"socketBypassPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy socketBypass updateSection '{
    "policyUpdateSectionInput": {
        "id": "id",
        "policyUpdateSectionInfoInput": {
            "name": "string"
        }
    },
    "socketBypassPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketBypass.updateSection ####

`accountId` [ID] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
`socketBypassPolicyMutationInput` [SocketBypassPolicyMutationInput] - (required) N/A    
