
## CATO-CLI - mutation.groups.updateGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateGroup) for documentation on this operation.

### Usage for mutation.groups.updateGroup:

`catocli mutation groups updateGroup -h`

`catocli mutation groups updateGroup <json>`

`catocli mutation groups updateGroup "$(cat < updateGroup.json)"`

`catocli mutation groups updateGroup '{"groupMembersListInput": {"groupMembersListFilterInput": {"name": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}, "regex": {"regex": "String"}}, "type": {"eq": {"eq": "enum(GroupMemberRefType)"}, "in": {"in": "enum(GroupMemberRefType)"}, "neq": {"neq": "enum(GroupMemberRefType)"}, "nin": {"nin": "enum(GroupMemberRefType)"}}}, "groupMembersListSortInput": {"name": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "type": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}}, "pagingInput": {"from": {"from": "Int"}, "limit": {"limit": "Int"}}}, "updateGroupInput": {"description": {"description": "String"}, "groupMemberRefTypedInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}, "type": {"type": "enum(GroupMemberRefType)"}}, "groupRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "name": {"name": "String"}}}'`

#### Operation Arguments for mutation.groups.updateGroup ####
`accountId` [ID] - (required) N/A 
`groupMembersListInput` [GroupMembersListInput] - (required) N/A 
`updateGroupInput` [UpdateGroupInput] - (required) N/A 
