
## CATO-CLI - mutation.policy.socketBypass.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.moveSection) for documentation on this operation.

### Usage for mutation.policy.socketBypass.moveSection:

```bash
catocli mutation policy socketBypass moveSection -h

catocli mutation policy socketBypass moveSection <json>

catocli mutation policy socketBypass moveSection --json-file mutation.policy.socketBypass.moveSection.json

catocli mutation policy socketBypass moveSection '{"policyMoveSectionInput":{"id":"id","policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"socketBypassPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy socketBypass moveSection '{
    "policyMoveSectionInput": {
        "id": "id",
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

#### Operation Arguments for mutation.policy.socketBypass.moveSection ####

`accountId` [ID] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
`socketBypassPolicyMutationInput` [SocketBypassPolicyMutationInput] - (required) N/A    
