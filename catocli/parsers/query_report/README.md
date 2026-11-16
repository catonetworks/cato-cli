
## CATO-CLI - query.report:
[Click here](https://api.catonetworks.com/documentation/#query-query.report) for documentation on this operation.

### Usage for query.report:

```bash
catocli query report -h

catocli query report <json>

catocli query report --json-file query.report.json

catocli query report '{"id":"id","reportConfigurationListInput":{"filter":{"enabled":{"eq":true,"neq":true},"frequency":{"eq":"DAILY","in":["DAILY"],"neq":"DAILY","nin":["DAILY"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"templateId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]}},"paging":{"from":1,"limit":1},"sort":{"lastModified":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}}},"reportRunListInput":{"filter":{"reportConfigurationId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"runAt":{"between":["2026-01-02T15:04:05Z"],"eq":"2026-01-02T15:04:05Z","gt":"2026-01-02T15:04:05Z","gte":"2026-01-02T15:04:05Z","in":["2026-01-02T15:04:05Z"],"lt":"2026-01-02T15:04:05Z","lte":"2026-01-02T15:04:05Z","neq":"2026-01-02T15:04:05Z","nin":["2026-01-02T15:04:05Z"]},"status":{"eq":"PENDING","in":["PENDING"],"neq":"PENDING","nin":["PENDING"]}},"paging":{"from":1,"limit":1},"sort":{"reportName":{"direction":"ASC","priority":1},"runAt":{"direction":"ASC","priority":1},"status":{"direction":"ASC","priority":1}}},"reportTemplateListInput":{"filter":{"alias":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"predefined":{"eq":true,"neq":true}},"paging":{"from":1,"limit":1},"sort":{"lastModified":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}}}}'

catocli query report '{
    "id": "id",
    "reportConfigurationListInput": {
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
    "reportRunListInput": {
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
    "reportTemplateListInput": {
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

#### Operation Arguments for query.report ####

`accountId` [ID] - (required) ID of the account whose reports are queried.
`id` [ID] - (required) ID of the report template to retrieve.
`reportConfigurationListInput` [ReportConfigurationListInput] - (required) Filter, sort, and paging settings for the report configurations.
`reportRunListInput` [ReportRunListInput] - (required) Filter, sort, and paging settings for the report runs.
`reportTemplateListInput` [ReportTemplateListInput] - (required) Filter, sort, and paging settings for the report templates.
