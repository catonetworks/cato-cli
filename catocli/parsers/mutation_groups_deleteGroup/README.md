
## CATO-CLI - mutation.groups.deleteGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.groups.deleteGroup) for documentation on this operation.

### Usage for mutation.groups.deleteGroup:

```bash
catocli mutation groups deleteGroup -h

catocli mutation groups deleteGroup <json>

catocli mutation groups deleteGroup --json-file mutation.groups.deleteGroup.json

catocli mutation groups deleteGroup '{"groupMembersListInput":{"filter":[{"name":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}],"type":[{"eq":"SITE","in":["SITE"],"neq":"SITE","nin":["SITE"]}]}],"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}}},"groupRefInput":{"by":"ID","input":"string"}}'

catocli mutation groups deleteGroup '{
    "groupMembersListInput": {
        "filter": [
            {
                "name": [
                    {
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
                    }
                ],
                "type": [
                    {
                        "eq": "SITE",
                        "in": [
                            "SITE"
                        ],
                        "neq": "SITE",
                        "nin": [
                            "SITE"
                        ]
                    }
                ]
            }
        ],
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
    "groupRefInput": {
        "by": "ID",
        "input": "string"
    }
}'
```

#### Operation Arguments for mutation.groups.deleteGroup ####

`accountId` [ID] - (required) ID of the account in which to create, update, or delete groups.
`groupMembersListInput` [GroupMembersListInput] - (optional) Filters, sorting, and pagination for the group members to retrieve.
`groupRefInput` [GroupRefInput] - (required) Group to delete, identified by ID or name.
