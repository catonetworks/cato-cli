
## CATO-CLI - mutation.popLocationMutations.allocateIp:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.popLocationMutations.allocateIp) for documentation on this operation.

### Usage for mutation.popLocationMutations.allocateIp:

```bash
catocli mutation popLocationMutations allocateIp -h

catocli mutation popLocationMutations allocateIp <json>

catocli mutation popLocationMutations allocateIp --json-file mutation.popLocationMutations.allocateIp.json

catocli mutation popLocationMutations allocateIp '{"popLocationAllocateIpInput":{"description":"string","popLocationRefInput":{"by":"ID","input":"string"},"type":"SYSTEM"}}'

catocli mutation popLocationMutations allocateIp '{
    "popLocationAllocateIpInput": {
        "description": "string",
        "popLocationRefInput": {
            "by": "ID",
            "input": "string"
        },
        "type": "SYSTEM"
    }
}'
```

#### Operation Arguments for mutation.popLocationMutations.allocateIp ####

`accountId` [ID] - (required) N/A    
`popLocationAllocateIpInput` [PopLocationAllocateIpInput] - (required) N/A    
