
## CATO-CLI - mutation.popLocationMutations.addAllocatedIp:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.popLocationMutations.addAllocatedIp) for documentation on this operation.

### Usage for mutation.popLocationMutations.addAllocatedIp:

```bash
catocli mutation popLocationMutations addAllocatedIp -h

catocli mutation popLocationMutations addAllocatedIp <json>

catocli mutation popLocationMutations addAllocatedIp --json-file mutation.popLocationMutations.addAllocatedIp.json

catocli mutation popLocationMutations addAllocatedIp '{"popLocationAddAllocatedIpInput":{"description":"string","popLocation":{"by":"ID","input":"string"},"type":"SYSTEM"}}'

catocli mutation popLocationMutations addAllocatedIp '{
    "popLocationAddAllocatedIpInput": {
        "description": "string",
        "popLocation": {
            "by": "ID",
            "input": "string"
        },
        "type": "SYSTEM"
    }
}'
```

#### Operation Arguments for mutation.popLocationMutations.addAllocatedIp ####

`accountId` [ID] - (required) N/A    
`popLocationAddAllocatedIpInput` [PopLocationAddAllocatedIpInput] - (required) N/A    
