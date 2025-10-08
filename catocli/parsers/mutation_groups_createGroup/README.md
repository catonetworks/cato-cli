
## CATO-CLI - mutation.groups.createGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.groups.createGroup) for documentation on this operation.

### Usage for mutation.groups.createGroup:

```bash
catocli mutation groups createGroup -h

catocli mutation groups createGroup <json>

catocli mutation groups createGroup "$(cat < mutation.groups.createGroup.json)"

catocli mutation groups createGroup '{"createGroupInput":{"description":"string","groupMemberRefTypedInput":{"by":"ID","input":"string","type":"SITE"},"name":"string"}}'

catocli mutation groups createGroup '{
    "createGroupInput": {
        "description": "string",
        "groupMemberRefTypedInput": {
            "by": "ID",
            "input": "string",
            "type": "SITE"
        },
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.groups.createGroup ####

`accountId` [ID] - (required) N/A    
`createGroupInput` [CreateGroupInput] - (required) N/A    
