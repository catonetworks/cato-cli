
## CATO-CLI - mutation.groups.createGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.groups.createGroup) for documentation on this operation.

### Usage for mutation.groups.createGroup:

`catocli mutation groups createGroup -h`

`catocli mutation groups createGroup <json>`

`catocli mutation groups createGroup "$(cat < mutation.groups.createGroup.json)"`

`catocli mutation groups createGroup '{"createGroupInput":{"description":"string","groupMemberRefTypedInput":{"by":"ID","input":"string","type":"SITE"},"name":"string"},"groupMembersListInput":{"groupMembersListFilterInput":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"type":{"eq":"SITE","in":"SITE","neq":"SITE","nin":"SITE"}},"groupMembersListSortInput":{"name":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}}}'`

`catocli mutation groups createGroup -p '{
    "createGroupInput": {
        "description": "string",
        "groupMemberRefTypedInput": {
            "by": "ID",
            "input": "string",
            "type": "SITE"
        },
        "name": "string"
    },
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
    }
}'`


#### Operation Arguments for mutation.groups.createGroup ####

`accountId` [ID] - (required) N/A    
`createGroupInput` [CreateGroupInput] - (required) N/A    
`groupMembersListInput` [GroupMembersListInput] - (required) N/A    
