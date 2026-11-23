
## CATO-CLI - query.reporting:
[Click here](https://api.catonetworks.com/documentation/#query-query.reporting) for documentation on this operation.

### Usage for query.reporting:

```bash
catocli query reporting -h

catocli query reporting <json>

catocli query reporting --json-file query.reporting.json

catocli query reporting '{"id":"id","reportingReportConfigurationListInput":{"filter":{"enabled":{"eq":true,"neq":true},"frequency":{"eq":"DAILY","in":["DAILY"],"neq":"DAILY","nin":["DAILY"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"templateId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]}},"paging":{"from":1,"limit":1},"sort":{"lastModified":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}}},"reportingReportRunListInput":{"filter":{"reportConfigurationId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"runAt":{"between":["2026-01-02T15:04:05Z"],"eq":"2026-01-02T15:04:05Z","gt":"2026-01-02T15:04:05Z","gte":"2026-01-02T15:04:05Z","in":["2026-01-02T15:04:05Z"],"lt":"2026-01-02T15:04:05Z","lte":"2026-01-02T15:04:05Z","neq":"2026-01-02T15:04:05Z","nin":["2026-01-02T15:04:05Z"]},"status":{"eq":"PENDING","in":["PENDING"],"neq":"PENDING","nin":["PENDING"]}},"paging":{"from":1,"limit":1},"sort":{"reportName":{"direction":"ASC","priority":1},"runAt":{"direction":"ASC","priority":1},"status":{"direction":"ASC","priority":1}}},"reportingReportTemplateListInput":{"filter":{"alias":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"predefined":{"eq":true,"neq":true}},"paging":{"from":1,"limit":1},"sort":{"lastModified":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}}}}'

catocli query reporting '{
    "id": "id",
    "reportingReportConfigurationListInput": {
        "filter": {
            "enabled": {
                "eq": true,
                "neq": true
            },
            "frequency": {
                "eq": "DAILY",
                "in": [
                    "DAILY"
                ],
                "neq": "DAILY",
                "nin": [
                    "DAILY"
                ]
            },
            "name": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ]
            },
            "templateId": {
                "eq": "id",
                "in": [
                    "id1",
                    "id2"
                ],
                "neq": "id",
                "nin": [
                    "id1",
                    "id2"
                ]
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "lastModified": {
                "direction": "ASC",
                "priority": 1
            },
            "name": {
                "direction": "ASC",
                "priority": 1
            }
        }
    },
    "reportingReportRunListInput": {
        "filter": {
            "reportConfigurationId": {
                "eq": "id",
                "in": [
                    "id1",
                    "id2"
                ],
                "neq": "id",
                "nin": [
                    "id1",
                    "id2"
                ]
            },
            "runAt": {
                "between": [
                    "2026-01-02T15:04:05Z"
                ],
                "eq": "2026-01-02T15:04:05Z",
                "gt": "2026-01-02T15:04:05Z",
                "gte": "2026-01-02T15:04:05Z",
                "in": [
                    "2026-01-02T15:04:05Z"
                ],
                "lt": "2026-01-02T15:04:05Z",
                "lte": "2026-01-02T15:04:05Z",
                "neq": "2026-01-02T15:04:05Z",
                "nin": [
                    "2026-01-02T15:04:05Z"
                ]
            },
            "status": {
                "eq": "PENDING",
                "in": [
                    "PENDING"
                ],
                "neq": "PENDING",
                "nin": [
                    "PENDING"
                ]
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "reportName": {
                "direction": "ASC",
                "priority": 1
            },
            "runAt": {
                "direction": "ASC",
                "priority": 1
            },
            "status": {
                "direction": "ASC",
                "priority": 1
            }
        }
    },
    "reportingReportTemplateListInput": {
        "filter": {
            "alias": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ]
            },
            "name": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ]
            },
            "predefined": {
                "eq": true,
                "neq": true
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "lastModified": {
                "direction": "ASC",
                "priority": 1
            },
            "name": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.reporting ####

`accountId` [ID] - (required) ID of the account whose reports are queried.
`id` [ID] - (required) ID of the report template to retrieve.
`reportingReportConfigurationListInput` [ReportingReportConfigurationListInput] - (required) Filter, sort, and paging settings for the report configurations.
`reportingReportRunListInput` [ReportingReportRunListInput] - (required) Filter, sort, and paging settings for the report runs.
`reportingReportTemplateListInput` [ReportingReportTemplateListInput] - (required) Filter, sort, and paging settings for the report templates.
