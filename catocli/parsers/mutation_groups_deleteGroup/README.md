
## CATO-CLI - mutation.groups.deleteGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.groups.deleteGroup) for documentation on this operation.

### Usage for mutation.groups.deleteGroup:

`catocli mutation groups deleteGroup -h`

`catocli mutation groups deleteGroup <json>`

`catocli mutation groups deleteGroup "$(cat < mutation.groups.deleteGroup.json)"`

`catocli mutation groups deleteGroup '{"groupMembersListInput":{"groupMembersListFilterInput":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"type":{"eq":"SITE","in":"SITE","neq":"SITE","nin":"SITE"}},"groupMembersListSortInput":{"name":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}},"groupRefInput":{"by":"ID","input":"string"}}'`

`catocli mutation groups deleteGroup -p '{
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
    "groupRefInput": {
        "by": "ID",
        "input": "string"
    }
}'`


#### Operation Arguments for mutation.groups.deleteGroup ####

`accountId` [ID] - (required) N/A    
`groupMembersListInput` [GroupMembersListInput] - (required) N/A    
`groupRefInput` [GroupRefInput] - (required) N/A    
