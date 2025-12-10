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
