
## CATO-CLI - mutation.policy.socketBypass.reorderPolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketBypass.reorderPolicy) for documentation on this operation.

### Usage for mutation.policy.socketBypass.reorderPolicy:

```bash
catocli mutation policy socketBypass reorderPolicy -h

catocli mutation policy socketBypass reorderPolicy <json>

catocli mutation policy socketBypass reorderPolicy --json-file mutation.policy.socketBypass.reorderPolicy.json

catocli mutation policy socketBypass reorderPolicy '{"policyReorderInput":{"policyReorderSectionInput":{"ref":{"by":"ID","input":"string"},"rules":{"ref":{"by":"ID","input":"string"},"subRules":{"ref":{"by":"ID","input":"string"}}}},"subPolicyId":"id"},"socketBypassPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'

catocli mutation policy socketBypass reorderPolicy '{
    "policyReorderInput": {
        "policyReorderSectionInput": {
            "ref": {
                "by": "ID",
                "input": "string"
            },
            "rules": {
                "ref": {
                    "by": "ID",
                    "input": "string"
                },
                "subRules": {
                    "ref": {
                        "by": "ID",
                        "input": "string"
                    }
                }
            }
        },
        "subPolicyId": "id"
    },
    "socketBypassPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketBypass.reorderPolicy ####

`accountId` [ID] - (required) N/A    
`policyReorderInput` [PolicyReorderInput] - (required) N/A    
`socketBypassPolicyMutationInput` [SocketBypassPolicyMutationInput] - (required) N/A    
