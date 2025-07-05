
## CATO-CLI - query.hardware:
[Click here](https://api.catonetworks.com/documentation/#query-hardware) for documentation on this operation.

### Usage for query.hardware:

`catocli query hardware -h`

`catocli query hardware <json>`

`catocli query hardware "$(cat < hardware.json)"`

`catocli query hardware '{"hardwareSearchInput": {"hardwareFilterInput": {"account": {"accountInclusion": {"accountInclusion": "enum(AccountInclusion)"}, "in": {"in": ["ID"]}}, "countryName": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}}, "freeText": {"search": {"search": "String"}}, "id": {"eq": {"eq": "ID"}, "in": {"in": ["ID"]}, "neq": {"neq": "ID"}, "nin": {"nin": ["ID"]}}, "licenseStartDate": {"between": {"between": ["DateTime"]}, "eq": {"eq": "DateTime"}, "gt": {"gt": "DateTime"}, "gte": {"gte": "DateTime"}, "in": {"in": ["DateTime"]}, "lt": {"lt": "DateTime"}, "lte": {"lte": "DateTime"}, "neq": {"neq": "DateTime"}, "nin": {"nin": ["DateTime"]}}, "product": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}}, "serialNumber": {"eq": {"eq": "String"}, "in": {"in": ["String"]}, "neq": {"neq": "String"}, "nin": {"nin": ["String"]}}, "shippingStatus": {"eq": {"eq": "enum(ShippingStatus)"}, "in": {"in": "enum(ShippingStatus)"}, "neq": {"neq": "enum(ShippingStatus)"}, "nin": {"nin": "enum(ShippingStatus)"}}, "validAddress": {"eq": {"eq": "Boolean"}, "neq": {"neq": "Boolean"}}}, "hardwareSortInput": {"accountName": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "country": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "incoterms": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "licenseId": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "licenseStartDate": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "productType": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "quoteId": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "shippingDate": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "shippingStatus": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}, "siteName": {"direction": {"direction": "enum(SortOrder)"}, "priority": {"priority": "Int"}}}, "pagingInput": {"from": {"from": "Int"}, "limit": {"limit": "Int"}}}}'`

#### Operation Arguments for query.hardware ####
`accountId` [ID] - (required) N/A 
`hardwareSearchInput` [HardwareSearchInput] - (optional) N/A 
