
## CATO-CLI - mutation.groups.deleteGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.groups.deleteGroup) for documentation on this operation.

### Usage for mutation.groups.deleteGroup:

```bash
catocli mutation groups deleteGroup -h

catocli mutation groups deleteGroup <json>

catocli mutation groups deleteGroup "$(cat < mutation.groups.deleteGroup.json)"

catocli mutation groups deleteGroup '{"groupRefInput":{"by":"ID","input":"string"}}'

catocli mutation groups deleteGroup -p '{
    "groupRefInput": {
        "by": "ID",
        "input": "string"
    }
}'
```

#### Operation Arguments for mutation.groups.deleteGroup ####

`accountId` [ID] - (required) N/A    
`groupRefInput` [GroupRefInput] - (required) N/A    
