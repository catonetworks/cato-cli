
## CATO-CLI - mutation.groups.deleteGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-deleteGroup) for documentation on this operation.

### Usage for mutation.groups.deleteGroup:

`catocli mutation groups deleteGroup -h`

`catocli mutation groups deleteGroup <json>`

`catocli mutation groups deleteGroup "$(cat < deleteGroup.json)"`

`catocli mutation groups deleteGroup '{"groupMembersListInput": {"groupMembersListFilterInput": {"name": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}, "regex": {"regex": "String"}}, "type": {"eq": {"eq": "enum(GroupMemberRefType)"}, "in": {"in": "enum(GroupMemberRefType)"}, "neq": {"neq": "enum(GroupMemberRefType)"}, "nin": {"nin": "enum(GroupMemberRefType)"}}}, "groupMembersListSortInput": {"name": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "type": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}}, "pagingInput": {"from": {"from": "Int"}, "limit": {"limit": "Int"}}}, "groupRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}'`

#### Operation Arguments for mutation.groups.deleteGroup ####
`accountId` [ID] - (required) N/A 
`groupMembersListInput` [GroupMembersListInput] - (required) N/A 
`groupRefInput` [GroupRefInput] - (required) N/A 
