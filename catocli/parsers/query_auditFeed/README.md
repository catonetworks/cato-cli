
## CATO-CLI - query.auditFeed:
[Click here](https://api.catonetworks.com/documentation/#query-query.auditFeed) for documentation on this operation.

### Usage for query.auditFeed:

```bash
catocli query auditFeed -h

catocli query auditFeed <json>

catocli query auditFeed "$(cat < query.auditFeed.json)"

catocli query auditFeed '{"accountIDs":["id1","id2"],"auditFieldFilterInput":{"fieldNameInput":{"AuditFieldName":"admin"},"operator":"is","values":["string1","string2"]},"fieldNames":"admin","marker":"string","timeFrame":"example_value"}'

catocli query auditFeed '{
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
}'
```


#### TimeFrame Parameter Examples

The `timeFrame` parameter supports both relative time ranges and absolute date ranges:

**Relative Time Ranges:**
- "last.PT5M" = Previous 5 minutes
- "last.PT1H" = Previous 1 hour  
- "last.P1D" = Previous 1 day
- "last.P14D" = Previous 14 days
- "last.P1M" = Previous 1 month

**Absolute Date Ranges:**
Format: `"utc.YYYY-MM-{DD/HH:MM:SS--DD/HH:MM:SS}"`

- Single day: "utc.2023-02-{28/00:00:00--28/23:59:59}"  
- Multiple days: "utc.2023-02-{25/00:00:00--28/23:59:59}"  
- Specific hours: "utc.2023-02-{28/09:00:00--28/17:00:00}"
- Across months: "utc.2023-{01-28/00:00:00--02-03/23:59:59}"


#### Operation Arguments for query.auditFeed ####

`accountIDs` [ID[]] - (required) List of Unique Account Identifiers.    
`auditFieldFilterInput` [AuditFieldFilterInput[]] - (required) N/A    
`fieldNames` [AuditFieldName[]] - (required) N/A Default Value: ['admin', 'apiKey', 'model_name', 'admin_id', 'module', 'audit_creation_type', 'insertion_date', 'change_type', 'creation_date', 'model_type', 'account', 'account_id']   
`marker` [String] - (required) Marker to use to get results from    
`timeFrame` [TimeFrame] - (required) N/A    
