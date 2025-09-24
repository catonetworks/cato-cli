
## CATO-CLI - query.groups.group.members:
[Click here](https://api.catonetworks.com/documentation/#query-query.groups.group.members) for documentation on this operation.

### Usage for query.groups.group.members:

`catocli query groups group members -h`

`catocli query groups group members <json>`

`catocli query groups group members "$(cat < query.groups.group.members.json)"`

`catocli query groups group members '{"groupMembersListInput":{"groupMembersListFilterInput":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"type":{"eq":"SITE","in":"SITE","neq":"SITE","nin":"SITE"}},"groupMembersListSortInput":{"name":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}},"groupRefInput":{"by":"ID","input":"string"}}'`

`catocli query groups group members -p '{
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


#### Operation Arguments for query.groups.group.members ####

`accountId` [ID] - (required) N/A    
`groupMembersListInput` [GroupMembersListInput] - (required) N/A    
`groupRefInput` [GroupRefInput] - (required) N/A    
