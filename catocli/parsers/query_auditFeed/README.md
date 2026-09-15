
## CATO-CLI - query.auditFeed:
[Click here](https://api.catonetworks.com/documentation/#query-query.auditFeed) for documentation on this operation.

### Usage for query.auditFeed:

```bash
catocli query auditFeed -h

catocli query auditFeed <json>

catocli query auditFeed --json-file query.auditFeed.json

catocli query auditFeed '{"accountIDs":["id1","id2"],"auditFieldFilterInput":{"fieldName":{"AuditFieldName":"admin"},"operator":"is","values":["string1","string2"]},"fieldNames":"admin","marker":"string","timeFrame":"example_value"}'

catocli query auditFeed '{
    "accountIDs": [
        "id1",
        "id2"
    ],
    "auditFieldFilterInput": {
        "fieldName": {
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

#### Operation Arguments for query.auditFeed ####

