
## CATO-CLI - mutation.policy.wanNetwork.reorderPolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanNetwork.reorderPolicy) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.reorderPolicy:

```bash
catocli mutation policy wanNetwork reorderPolicy -h

catocli mutation policy wanNetwork reorderPolicy <json>

catocli mutation policy wanNetwork reorderPolicy --json-file mutation.policy.wanNetwork.reorderPolicy.json

catocli mutation policy wanNetwork reorderPolicy '{"policyReorderInput":{"sections":{"ref":{"by":"ID","input":"string"},"rules":{"ref":{"by":"ID","input":"string"},"subRules":{"ref":{"by":"ID","input":"string"}}}},"subPolicyId":"id"},"wanNetworkPolicyMutationInput":{"revision":{"id":"id"}}}'

catocli mutation policy wanNetwork reorderPolicy '{
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
    "wanNetworkPolicyMutationInput": {
        "revision": {
            "id": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.wanNetwork.reorderPolicy ####

`accountId` [ID] - (required) N/A    
`policyReorderInput` [PolicyReorderInput] - (required) N/A    
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (required) N/A    
