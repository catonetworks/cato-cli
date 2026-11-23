
## CATO-CLI - mutation.groups.createGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.groups.createGroup) for documentation on this operation.

### Usage for mutation.groups.createGroup:

```bash
catocli mutation groups createGroup -h

catocli mutation groups createGroup <json>

catocli mutation groups createGroup --json-file mutation.groups.createGroup.json

catocli mutation groups createGroup '{"createGroupInput":{"description":"string","members":[{"by":"ID","input":"string","type":"SITE"}],"name":"string"},"groupMembersListInput":{"filter":[{"name":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}],"type":[{"eq":"SITE","in":["SITE"],"neq":"SITE","nin":["SITE"]}]}],"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}}}}'

catocli mutation groups createGroup '{
    "createGroupInput": {
        "description": "string",
        "members": [
            {
                "by": "ID",
                "input": "string",
                "type": "SITE"
            }
        ],
        "name": "string"
    },
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
    }
}'
```

#### Operation Arguments for mutation.groups.createGroup ####

`accountId` [ID] - (required) ID of the account in which to create, update, or delete groups.
`createGroupInput` [CreateGroupInput] - (required) Name, description, and initial members of the group to create.
`groupMembersListInput` [GroupMembersListInput] - (optional) Filters, sorting, and pagination for the group members to retrieve.
