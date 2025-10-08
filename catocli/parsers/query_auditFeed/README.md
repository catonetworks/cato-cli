
## CATO-CLI - query.auditFeed:
[Click here](https://api.catonetworks.com/documentation/#query-query.auditFeed) for documentation on this operation.

### Usage for query.auditFeed:

```bash
catocli query auditFeed -h

catocli query auditFeed <json>

catocli query auditFeed "$(cat < query.auditFeed.json)"

catocli query auditFeed '{"accountIDs":["id1","id2"],"auditFieldFilterInput":{"fieldNameInput":{"AuditFieldName":"admin"},"operator":"is","values":["string1","string2"]},"marker":"string","timeFrame":"example_value"}'

catocli query auditFeed -p '{
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
    "marker": "string",
    "timeFrame": "example_value"
}'
```

#### Operation Arguments for query.auditFeed ####

`accountIDs` [ID[]] - (required) List of Unique Account Identifiers.    
`auditFieldFilterInput` [AuditFieldFilterInput[]] - (required) N/A    
`marker` [String] - (required) Marker to use to get results from    
`timeFrame` [TimeFrame] - (required) N/A    
