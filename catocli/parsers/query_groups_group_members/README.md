
## CATO-CLI - query.groups.group.members:
[Click here](https://api.catonetworks.com/documentation/#query-members) for documentation on this operation.

### Usage for query.groups.group.members:

`catocli query groups group members -h`

`catocli query groups group members <json>`

`catocli query groups group members "$(cat < members.json)"`

`catocli query groups group members '{"groupMembersListInput": {"groupMembersListFilterInput": {"name": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}, "regex": {"regex": "String"}}, "type": {"eq": {"eq": "enum(GroupMemberRefType)"}, "in": {"in": "enum(GroupMemberRefType)"}, "neq": {"neq": "enum(GroupMemberRefType)"}, "nin": {"nin": "enum(GroupMemberRefType)"}}}, "groupMembersListSortInput": {"name": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "type": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}}, "pagingInput": {"from": {"from": "Int"}, "limit": {"limit": "Int"}}}, "groupRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}'`

#### Operation Arguments for query.groups.group.members ####
`accountId` [ID] - (required) N/A 
`groupMembersListInput` [GroupMembersListInput] - (required) N/A 
`groupRefInput` [GroupRefInput] - (required) N/A 
