# List all groups

```bash
# List all groups (first page of 50)
catocli query groups groupList '{
    "groupListInput": {
        "paging": {
            "from": 0,
            "limit": 50
        }
    }
}'
```

# Search groups by name

```bash
# Search groups by name (free-text match)
catocli query groups groupList '{
    "groupListInput": {
        "filter": [
            {
                "freeText": {
                    "search": "my-group"
                }
            }
        ],
        "paging": {
            "from": 0,
            "limit": 50
        }
    }
}'
```

# Use raw query to get group list

```bash
# Use raw query to get group list
catocli raw '{
     "query": "query groupsGroupList ( $accountId:ID! ) { groups ( accountId:$accountId ) { groupList { items { audit { updatedBy { id name } updatedTime } description id membersCount membersCountPerType { membersCount type } name } paging { total } } } }",
     "variables": {
         "accountId": 15412
     },
     "operationName": "groupsGroupList"
}'
```

Note: the members of each group cannot be requested inside groupList; list a
specific group's members separately with `catocli query groups group members`.
