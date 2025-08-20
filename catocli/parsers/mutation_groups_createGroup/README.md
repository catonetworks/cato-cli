
## CATO-CLI - mutation.groups.createGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-createGroup) for documentation on this operation.

### Usage for mutation.groups.createGroup:

`catocli mutation groups createGroup -h`

`catocli mutation groups createGroup <json>`

`catocli mutation groups createGroup "$(cat < createGroup.json)"`

`catocli mutation groups createGroup '{"createGroupInput": {"description": {"description": "String"}, "groupMemberRefTypedInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}, "type": {"type": "enum(GroupMemberRefType)"}}, "name": {"name": "String"}}, "groupMembersListInput": {"groupMembersListFilterInput": {"name": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}, "regex": {"regex": "String"}}, "type": {"eq": {"eq": "enum(GroupMemberRefType)"}, "in": {"in": "enum(GroupMemberRefType)"}, "neq": {"neq": "enum(GroupMemberRefType)"}, "nin": {"nin": "enum(GroupMemberRefType)"}}}, "groupMembersListSortInput": {"name": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "type": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}}, "pagingInput": {"from": {"from": "Int"}, "limit": {"limit": "Int"}}}}'`

#### Operation Arguments for mutation.groups.createGroup ####
`accountId` [ID] - (required) N/A 
`createGroupInput` [CreateGroupInput] - (required) N/A 
`groupMembersListInput` [GroupMembersListInput] - (required) N/A 
