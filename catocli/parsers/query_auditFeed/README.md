
## CATO-CLI - query.auditFeed:
[Click here](https://api.catonetworks.com/documentation/#query-auditFeed) for documentation on this operation.

### Usage for query.auditFeed:

`catocli query auditFeed -h`

`catocli query auditFeed <json>`

`catocli query auditFeed "$(cat < auditFeed.json)"`

`catocli query auditFeed '{"AuditFieldFilterInput": {"FieldNameInput": {"AuditFieldName": {"AuditFieldName": "enum(AuditFieldName)"}, "EventFieldName": {"EventFieldName": "enum(EventFieldName)"}}, "operator": {"operator": "enum(ElasticOperator)"}, "values": {"values": ["String"]}}, "accountIDs": ["ID"], "fieldNames": "enum(AuditFieldName)", "marker": "String", "timeFrame": "TimeFrame"}'`

#### Operation Arguments for query.auditFeed ####
`AuditFieldFilterInput` [AuditFieldFilterInput[]] - (optional) N/A 
`accountIDs` [ID[]] - (optional) List of Unique Account Identifiers. 
`fieldNames` [AuditFieldName[]] - (optional) N/A Default Value: ['admin', 'apiKey', 'model_name', 'admin_id', 'module', 'audit_creation_type', 'insertion_date', 'change_type', 'creation_date', 'model_type', 'account', 'account_id']
`marker` [String] - (optional) Marker to use to get results from 
`timeFrame` [TimeFrame] - (required) N/A 
