
## CATO-CLI - mutation.policy.socketLan.removeSubPolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.socketLan.removeSubPolicy) for documentation on this operation.

### Usage for mutation.policy.socketLan.removeSubPolicy:

```bash
catocli mutation policy socketLan removeSubPolicy -h

catocli mutation policy socketLan removeSubPolicy <json>

catocli mutation policy socketLan removeSubPolicy --json-file mutation.policy.socketLan.removeSubPolicy.json

catocli mutation policy socketLan removeSubPolicy '{"socketLanPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"socketLanRemoveSubPolicyInput":{"socketLanPolicyRefInput":{"by":"ID","input":"string"}}}'

catocli mutation policy socketLan removeSubPolicy '{
    "socketLanPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "socketLanRemoveSubPolicyInput": {
        "socketLanPolicyRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.policy.socketLan.removeSubPolicy ####

`accountId` [ID] - (required) N/A    
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (required) N/A    
`socketLanRemoveSubPolicyInput` [SocketLanRemoveSubPolicyInput] - (required) N/A    
