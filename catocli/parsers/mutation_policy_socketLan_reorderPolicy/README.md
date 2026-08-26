
## CATO-CLI - mutation.policy.socketLan.reorderPolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.reorderPolicy) for documentation on this operation.

### Usage for mutation.policy.socketLan.reorderPolicy:

```bash
catocli mutation policy socketLan reorderPolicy -h

catocli mutation policy socketLan reorderPolicy <json>

catocli mutation policy socketLan reorderPolicy --json-file mutation.policy.socketLan.reorderPolicy.json

catocli mutation policy socketLan reorderPolicy '{"policyReorderInput":{"sections":{"ref":{"by":"ID","input":"string"},"rules":{"ref":{"by":"ID","input":"string"},"subRules":{"ref":{"by":"ID","input":"string"}}}},"subPolicyId":"id"},"socketLanPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy socketLan reorderPolicy '{
    "policyReorderInput": {
        "sections": {
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
    "socketLanPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketLan.reorderPolicy ####

`accountId` [ID] - (required) N/A    
`policyReorderInput` [PolicyReorderInput] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
