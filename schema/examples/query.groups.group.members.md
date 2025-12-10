# Get group members by group ID reference

```bash
# Get group members by group ID reference
catocli query groups group members '{
    "groupMembersListInput": {
        "filter": [],
        "paging": {
            "from": 0,
            "limit": 100
        }
    },
    "groupRefInput": {
        "by": "ID",
        "input": "abcde-12345"
    }
}'
```

# Get group members by group name reference

```bash
# Get group members by group ID reference
catocli query groups group members '{
    "groupMembersListInput": {
        "filter": [],
        "paging": {
            "from": 0,
            "limit": 100
        }
    },
    "groupRefInput": {
        "by": "NAME",
        "input": "My Advanced Group"
    }
}'
```
