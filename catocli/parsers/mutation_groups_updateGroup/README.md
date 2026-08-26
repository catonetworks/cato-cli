
## CATO-CLI - mutation.groups.updateGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.groups.updateGroup) for documentation on this operation.

### Usage for mutation.groups.updateGroup:

```bash
catocli mutation groups updateGroup -h

catocli mutation groups updateGroup <json>

catocli mutation groups updateGroup --json-file mutation.groups.updateGroup.json

catocli mutation groups updateGroup '{"groupMembersListInput":{"filter":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"type":{"eq":"SITE","in":"SITE","neq":"SITE","nin":"SITE"}},"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}}},"updateGroupInput":{"description":"string","group":{"by":"ID","input":"string"},"members":{"by":"ID","input":"string","type":"SITE"},"membersToAdd":{"by":"ID","input":"string","type":"SITE"},"membersToRemove":{"by":"ID","input":"string","type":"SITE"},"name":"string"}}'

catocli mutation groups updateGroup '{
    "groupMembersListInput": {
        "filter": {
            "name": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ],
                "regex": "string"
            },
            "type": {
                "eq": "SITE",
                "in": "SITE",
                "neq": "SITE",
                "nin": "SITE"
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "name": {
                "direction": "ASC",
                "priority": 1
            },
            "type": {
                "direction": "ASC",
                "priority": 1
            }
        }
    },
    "updateGroupInput": {
        "description": "string",
        "group": {
            "by": "ID",
            "input": "string"
        },
        "members": {
            "by": "ID",
            "input": "string",
            "type": "SITE"
        },
        "membersToAdd": {
            "by": "ID",
            "input": "string",
            "type": "SITE"
        },
        "membersToRemove": {
            "by": "ID",
            "input": "string",
            "type": "SITE"
        },
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.groups.updateGroup ####

`accountId` [ID] - (required) N/A    
`groupMembersListInput` [GroupMembersListInput] - (required) N/A    
`updateGroupInput` [UpdateGroupInput] - (required) N/A    
