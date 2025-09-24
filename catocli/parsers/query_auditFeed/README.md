
## CATO-CLI - query.auditFeed:
[Click here](https://api.catonetworks.com/documentation/#query-query.auditFeed) for documentation on this operation.

### Usage for query.auditFeed:

`catocli query auditFeed -h`

`catocli query auditFeed <json>`

`catocli query auditFeed "$(cat < query.auditFeed.json)"`

`catocli query auditFeed '{"accountIDs":["id1","id2"],"auditFieldFilterInput":{"fieldNameInput":{"AuditFieldName":"admin"},"operator":"is","values":["string1","string2"]},"fieldNames":"admin","marker":"string","timeFrame":"example_value"}'`

`catocli query auditFeed -p '{
    "accountIDs": [
        "id1",
        "id2"
    ],
    "auditFieldFilterInput": {
        "fieldNameInput": {
            "AuditFieldName": "admin"
        },
        "operator": "is",
        "values": [
            "string1",
            "string2"
        ]
    },
    "fieldNames": "admin",
    "marker": "string",
    "timeFrame": "example_value"
}'`


#### Operation Arguments for query.auditFeed ####

`accountIDs` [ID[]] - (required) List of Unique Account Identifiers.    
`auditFieldFilterInput` [AuditFieldFilterInput[]] - (required) N/A    
`fieldNames` [AuditFieldName[]] - (required) N/A Default Value: ['admin', 'apiKey', 'model_name', 'admin_id', 'module', 'audit_creation_type', 'insertion_date', 'change_type', 'creation_date', 'model_type', 'account', 'account_id']   
`marker` [String] - (required) Marker to use to get results from    
`timeFrame` [TimeFrame] - (required) N/A    
