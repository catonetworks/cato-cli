
## CATO-CLI - query.catalogs:
[Click here](https://api.catonetworks.com/documentation/#query-catalogs) for documentation on this operation.

### Usage for query.catalogs:

`catocli query catalogs -h`

`catocli query catalogs <json>`

`catocli query catalogs "$(cat < catalogs.json)"`

`catocli query catalogs '{"applicationRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "catalogApplicationContentTypeGroupListInput": {"catalogApplicationContentTypeGroupFilterInput": {"contentType": {"id": {"eq": {"eq": "ID"}, "in": {"in": ["ID"]}, "neq": {"neq": "ID"}, "nin": {"nin": ["ID"]}}, "name": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}}}, "id": {"eq": {"eq": "ID"}, "in": {"in": ["ID"]}, "neq": {"neq": "ID"}, "nin": {"nin": ["ID"]}}, "name": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}}}, "catalogApplicationContentTypeGroupSortInput": {"name": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}}, "pagingInput": {"from": {"from": "Int"}, "limit": {"limit": "Int"}}}, "catalogApplicationListInput": {"catalogApplicationFilterInput": {"activity": {"hasAny": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}, "capability": {"hasAny": {"hasAny": "enum(CatalogApplicationCapability)"}}, "category": {"hasAny": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}, "id": {"eq": {"eq": "ID"}, "in": {"in": ["ID"]}, "neq": {"neq": "ID"}, "nin": {"nin": ["ID"]}}, "name": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}}, "recentlyAdded": {"eq": {"eq": "Boolean"}, "neq": {"neq": "Boolean"}}, "risk": {"between": {"between": ["Int"]}, "eq": {"eq": "Int"}, "gt": {"gt": "Int"}, "gte": {"gte": "Int"}, "in": {"in": ["Int"]}, "lt": {"lt": "Int"}, "lte": {"lte": "Int"}, "neq": {"neq": "Int"}, "nin": {"nin": ["Int"]}}, "type": {"eq": {"eq": "enum(CatalogApplicationType)"}, "in": {"in": "enum(CatalogApplicationType)"}, "neq": {"neq": "enum(CatalogApplicationType)"}, "nin": {"nin": "enum(CatalogApplicationType)"}}}, "catalogApplicationSortInput": {"category": {"name": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}}, "description": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "name": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "risk": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "type": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}}, "pagingInput": {"from": {"from": "Int"}, "limit": {"limit": "Int"}}}}'`

#### Operation Arguments for query.catalogs ####
`accountId` [ID] - (required) N/A 
`applicationRefInput` [ApplicationRefInput] - (required) N/A 
`catalogApplicationContentTypeGroupListInput` [CatalogApplicationContentTypeGroupListInput] - (required) N/A 
`catalogApplicationListInput` [CatalogApplicationListInput] - (required) N/A 
