
## CATO-CLI - mutation.groups.updateGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.groups.updateGroup) for documentation on this operation.

### Usage for mutation.groups.updateGroup:

```bash
catocli mutation groups updateGroup -h

catocli mutation groups updateGroup <json>

catocli mutation groups updateGroup "$(cat < mutation.groups.updateGroup.json)"

catocli mutation groups updateGroup '{"updateGroupInput":{"description":"string","groupMemberRefTypedInput":{"by":"ID","input":"string","type":"SITE"},"groupRefInput":{"by":"ID","input":"string"},"name":"string"}}'

catocli mutation groups updateGroup -p '{
    "updateGroupInput": {
        "description": "string",
        "groupMemberRefTypedInput": {
            "by": "ID",
            "input": "string",
            "type": "SITE"
        },
        "groupRefInput": {
            "by": "ID",
            "input": "string"
        },
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.groups.updateGroup ####

`accountId` [ID] - (required) N/A    
`updateGroupInput` [UpdateGroupInput] - (required) N/A    
