
## CATO-CLI - query.user.usersGroup.members:
[Click here](https://api.catonetworks.com/documentation/#query-query.user.usersGroup.members) for documentation on this operation.

### Usage for query.user.usersGroup.members:

```bash
catocli query user usersGroup members -h

catocli query user usersGroup members <json>

catocli query user usersGroup members --json-file query.user.usersGroup.members.json

catocli query user usersGroup members '{"usersGroupInput":{"group":{"by":"ID","input":"string"}},"usersGroupMembersInput":{"filter":{"searchTerm":{"search":"string"}},"paging":{"from":1,"limit":1},"sort":{"email":{"direction":"ASC","priority":1},"importType":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}}}}'

catocli query user usersGroup members '{
    "usersGroupInput": {
        "group": {
            "by": "ID",
            "input": "string"
        }
    },
    "usersGroupMembersInput": {
        "filter": {
            "searchTerm": {
                "search": "string"
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "email": {
                "direction": "ASC",
                "priority": 1
            },
            "importType": {
                "direction": "ASC",
                "priority": 1
            },
            "name": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.user.usersGroup.members ####

`accountId` [ID] - (required) Unique identifier of the Cato account.
`usersGroupInput` [UsersGroupInput] - (required) N/A
`usersGroupMembersInput` [UsersGroupMembersInput] - (required) N/A
