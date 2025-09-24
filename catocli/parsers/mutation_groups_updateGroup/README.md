
## CATO-CLI - mutation.groups.updateGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.groups.updateGroup) for documentation on this operation.

### Usage for mutation.groups.updateGroup:

`catocli mutation groups updateGroup -h`

`catocli mutation groups updateGroup <json>`

`catocli mutation groups updateGroup "$(cat < mutation.groups.updateGroup.json)"`

`catocli mutation groups updateGroup '{"groupMembersListInput":{"groupMembersListFilterInput":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"type":{"eq":"SITE","in":"SITE","neq":"SITE","nin":"SITE"}},"groupMembersListSortInput":{"name":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}},"updateGroupInput":{"description":"string","groupMemberRefTypedInput":{"by":"ID","input":"string","type":"SITE"},"groupRefInput":{"by":"ID","input":"string"},"name":"string"}}'`

`catocli mutation groups updateGroup -p '{
    "groupMembersListInput": {
        "groupMembersListFilterInput": {
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
        "groupMembersListSortInput": {
            "name": {
                "direction": "ASC",
                "priority": 1
            },
            "type": {
                "direction": "ASC",
                "priority": 1
            }
        },
        "pagingInput": {
            "from": 1,
            "limit": 1
        }
    },
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
}'`


#### Operation Arguments for mutation.groups.updateGroup ####

`accountId` [ID] - (required) N/A    
`groupMembersListInput` [GroupMembersListInput] - (required) N/A    
`updateGroupInput` [UpdateGroupInput] - (required) N/A    
