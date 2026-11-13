
## CATO-CLI - query.businessPlatform.accountList:
[Click here](https://api.catonetworks.com/documentation/#query-query.businessPlatform.accountList) for documentation on this operation.

### Usage for query.businessPlatform.accountList:

```bash
catocli query businessPlatform accountList -h

catocli query businessPlatform accountList <json>

catocli query businessPlatform accountList --json-file query.businessPlatform.accountList.json

catocli query businessPlatform accountList '{"businessPlatformAccountListInput":{"filter":{"account":{"accountInclusion":"ALL_ACCOUNTS","in":["id1","id2"]},"customerAccount":{"accountInclusion":"ALL_ACCOUNTS","in":["id1","id2"]},"expiresOn":[{"between":["2026-01-02"],"eq":"2026-01-02","gt":"2026-01-02","gte":"2026-01-02","in":["2026-01-02"],"lt":"2026-01-02","lte":"2026-01-02","neq":"2026-01-02","nin":["2026-01-02"]}],"freeText":{"search":"string"},"includeMSP":true,"plan":[{"eq":"PENDING_APPROVAL","in":["PENDING_APPROVAL"]}]},"paging":{"from":1,"limit":1},"sort":{"account":{"direction":"ASC","priority":1},"cmaCreatedAt":{"direction":"ASC","priority":1},"cmaCreatedBy":{"direction":"ASC","priority":1},"partner":{"direction":"ASC","priority":1},"plan":{"direction":"ASC","priority":1}}}}'

catocli query businessPlatform accountList '{
    "businessPlatformAccountListInput": {
        "filter": {
            "account": {
                "accountInclusion": "ALL_ACCOUNTS",
                "in": [
                    "id1",
                    "id2"
                ]
            },
            "customerAccount": {
                "accountInclusion": "ALL_ACCOUNTS",
                "in": [
                    "id1",
                    "id2"
                ]
            },
            "expiresOn": [
                {
                    "between": [
                        "2026-01-02"
                    ],
                    "eq": "2026-01-02",
                    "gt": "2026-01-02",
                    "gte": "2026-01-02",
                    "in": [
                        "2026-01-02"
                    ],
                    "lt": "2026-01-02",
                    "lte": "2026-01-02",
                    "neq": "2026-01-02",
                    "nin": [
                        "2026-01-02"
                    ]
                }
            ],
            "freeText": {
                "search": "string"
            },
            "includeMSP": true,
            "plan": [
                {
                    "eq": "PENDING_APPROVAL",
                    "in": [
                        "PENDING_APPROVAL"
                    ]
                }
            ]
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "account": {
                "direction": "ASC",
                "priority": 1
            },
            "cmaCreatedAt": {
                "direction": "ASC",
                "priority": 1
            },
            "cmaCreatedBy": {
                "direction": "ASC",
                "priority": 1
            },
            "partner": {
                "direction": "ASC",
                "priority": 1
            },
            "plan": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.businessPlatform.accountList ####

`accountId` [ID] - (required) N/A
`businessPlatformAccountListInput` [BusinessPlatformAccountListInput] - (required) N/A
