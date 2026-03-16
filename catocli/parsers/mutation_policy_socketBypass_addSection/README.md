
## CATO-CLI - mutation.policy.socketBypass.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.addSection) for documentation on this operation.

### Usage for mutation.policy.socketBypass.addSection:

```bash
catocli mutation policy socketBypass addSection -h

catocli mutation policy socketBypass addSection <json>

catocli mutation policy socketBypass addSection --json-file mutation.policy.socketBypass.addSection.json

catocli mutation policy socketBypass addSection '{"policyAddSectionInput":{"policyAddSectionInfoInput":{"name":"string"},"policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"socketBypassPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy socketBypass addSection '{
    "policyAddSectionInput": {
        "policyAddSectionInfoInput": {
            "name": "string"
        },
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    },
    "socketBypassPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketBypass.addSection ####

`accountId` [ID] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
`socketBypassPolicyMutationInput` [SocketBypassPolicyMutationInput] - (required) N/A    
