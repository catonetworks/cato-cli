
## CATO-CLI - query.groups.groupList:
[Click here](https://api.catonetworks.com/documentation/#query-groupList) for documentation on this operation.

### Usage for query.groups.groupList:

`catocli query groups groupList -h`

`catocli query groups groupList <json>`

`catocli query groups groupList "$(cat < groupList.json)"`

`catocli query groups groupList '{"groupListInput": {"groupListFilterInput": {"audit": {"updatedBy": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "updatedTime": {"between": {"between": ["DateTime"]}, "eq": {"eq": "DateTime"}, "gt": {"gt": "DateTime"}, "gte": {"gte": "DateTime"}, "in": {"in": ["DateTime"]}, "lt": {"lt": "DateTime"}, "lte": {"lte": "DateTime"}, "neq": {"neq": "DateTime"}, "nin": {"nin": ["DateTime"]}}}, "freeText": {"search": {"search": "String"}}, "id": {"eq": {"eq": "ID"}, "in": {"in": ["ID"]}, "neq": {"neq": "ID"}, "nin": {"nin": ["ID"]}}, "member": {"ref": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}, "type": {"type": "enum(GroupMemberRefType)"}}}, "name": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}, "regex": {"regex": "String"}}}, "groupListSortInput": {"audit": {"updatedBy": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "updatedTime": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}}, "name": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}}, "pagingInput": {"from": {"from": "Int"}, "limit": {"limit": "Int"}}}, "groupMembersListInput": {"groupMembersListFilterInput": {"name": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}, "regex": {"regex": "String"}}, "type": {"eq": {"eq": "enum(GroupMemberRefType)"}, "in": {"in": "enum(GroupMemberRefType)"}, "neq": {"neq": "enum(GroupMemberRefType)"}, "nin": {"nin": "enum(GroupMemberRefType)"}}}, "groupMembersListSortInput": {"name": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "type": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}}, "pagingInput": {"from": {"from": "Int"}, "limit": {"limit": "Int"}}}}'`

#### Operation Arguments for query.groups.groupList ####
`accountId` [ID] - (required) N/A 
`groupListInput` [GroupListInput] - (optional) N/A 
`groupMembersListInput` [GroupMembersListInput] - (required) N/A 
