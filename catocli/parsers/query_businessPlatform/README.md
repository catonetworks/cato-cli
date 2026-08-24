
## CATO-CLI - query.businessPlatform:
[Click here](https://api.catonetworks.com/documentation/#query-query.businessPlatform) for documentation on this operation.

### Usage for query.businessPlatform:

```bash
catocli query businessPlatform -h

catocli query businessPlatform <json>

catocli query businessPlatform --json-file query.businessPlatform.json

catocli query businessPlatform '{"businessPlatformAccountListInput":{"businessPlatformFilterInput":{"account":{"accountInclusion":"ALL_ACCOUNTS","in":["id1","id2"]},"expiresOn":{"between":["example1","example2"],"eq":"example_value","gt":"example_value","gte":"example_value","in":["example1","example2"],"lt":"example_value","lte":"example_value","neq":"example_value","nin":["example1","example2"]},"freeText":{"search":"string"},"plan":{"eq":"PENDING_APPROVAL","in":"PENDING_APPROVAL"}},"businessPlatformSortInput":{"account":{"direction":"ASC","priority":1},"cmaCreatedAt":{"direction":"ASC","priority":1},"cmaCreatedBy":{"direction":"ASC","priority":1},"partner":{"direction":"ASC","priority":1},"plan":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}}}'

catocli query businessPlatform '{
    "businessPlatformAccountListInput": {
        "businessPlatformFilterInput": {
            "account": {
                "accountInclusion": "ALL_ACCOUNTS",
                "in": [
                    "id1",
                    "id2"
                ]
            },
            "expiresOn": {
                "between": [
                    "example1",
                    "example2"
                ],
                "eq": "example_value",
                "gt": "example_value",
                "gte": "example_value",
                "in": [
                    "example1",
                    "example2"
                ],
                "lt": "example_value",
                "lte": "example_value",
                "neq": "example_value",
                "nin": [
                    "example1",
                    "example2"
                ]
            },
            "freeText": {
                "search": "string"
            },
            "plan": {
                "eq": "PENDING_APPROVAL",
                "in": "PENDING_APPROVAL"
            }
        },
        "businessPlatformSortInput": {
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
        },
        "pagingInput": {
            "from": 1,
            "limit": 1
        }
    }
}'
```

#### Operation Arguments for query.businessPlatform ####

`accountId` [ID] - (required) N/A    
`businessPlatformAccountListInput` [BusinessPlatformAccountListInput] - (required) N/A    
