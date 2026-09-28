
## CATO-CLI - query.posture.checkResultList:
[Click here](https://api.catonetworks.com/documentation/#query-query.posture.checkResultList) for documentation on this operation.

### Usage for query.posture.checkResultList:

```bash
catocli query posture checkResultList -h

catocli query posture checkResultList <json>

catocli query posture checkResultList --json-file query.posture.checkResultList.json

catocli query posture checkResultList '{"postureCheckResultListInput":{"filter":{"application":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"areaId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"categoryId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"checkId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"checkType":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"complianceControl":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"complianceFramework":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"findingName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"label":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"muteStatus":{"eq":"MUTED","in":"MUTED","neq":"MUTED","nin":"MUTED"},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"securityDomain":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"severity":{"eq":"INFORMATIONAL","in":"INFORMATIONAL","neq":"INFORMATIONAL","nin":"INFORMATIONAL"},"status":{"eq":"PASSED","in":"PASSED","neq":"PASSED","nin":"PASSED"},"suppressedStatus":{"eq":"ENABLED","in":"ENABLED","neq":"ENABLED","nin":"ENABLED"}},"paging":{"from":1,"limit":1},"sort":{"application":{"direction":"ASC","priority":1},"areaId":{"direction":"ASC","priority":1},"categoryId":{"direction":"ASC","priority":1},"checkId":{"direction":"ASC","priority":1},"checkType":{"direction":"ASC","priority":1},"complianceControl":{"direction":"ASC","priority":1},"complianceFramework":{"direction":"ASC","priority":1},"findingName":{"direction":"ASC","priority":1},"label":{"direction":"ASC","priority":1},"lastChecked":{"direction":"ASC","priority":1},"muteStatus":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1},"securityDomain":{"direction":"ASC","priority":1},"severity":{"direction":"ASC","priority":1},"status":{"direction":"ASC","priority":1},"suppressedStatus":{"direction":"ASC","priority":1}}}}'

catocli query posture checkResultList '{
    "postureCheckResultListInput": {
        "filter": {
            "application": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ],
                "regex": "string"
            },
            "areaId": {
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
            "categoryId": {
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
            "checkId": {
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
            "checkType": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ],
                "regex": "string"
            },
            "complianceControl": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ],
                "regex": "string"
            },
            "complianceFramework": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ],
                "regex": "string"
            },
            "findingName": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ],
                "regex": "string"
            },
            "label": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ],
                "regex": "string"
            },
            "muteStatus": {
                "eq": "MUTED",
                "in": "MUTED",
                "neq": "MUTED",
                "nin": "MUTED"
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
                ],
                "regex": "string"
            },
            "securityDomain": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ],
                "regex": "string"
            },
            "severity": {
                "eq": "INFORMATIONAL",
                "in": "INFORMATIONAL",
                "neq": "INFORMATIONAL",
                "nin": "INFORMATIONAL"
            },
            "status": {
                "eq": "PASSED",
                "in": "PASSED",
                "neq": "PASSED",
                "nin": "PASSED"
            },
            "suppressedStatus": {
                "eq": "ENABLED",
                "in": "ENABLED",
                "neq": "ENABLED",
                "nin": "ENABLED"
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "application": {
                "direction": "ASC",
                "priority": 1
            },
            "areaId": {
                "direction": "ASC",
                "priority": 1
            },
            "categoryId": {
                "direction": "ASC",
                "priority": 1
            },
            "checkId": {
                "direction": "ASC",
                "priority": 1
            },
            "checkType": {
                "direction": "ASC",
                "priority": 1
            },
            "complianceControl": {
                "direction": "ASC",
                "priority": 1
            },
            "complianceFramework": {
                "direction": "ASC",
                "priority": 1
            },
            "findingName": {
                "direction": "ASC",
                "priority": 1
            },
            "label": {
                "direction": "ASC",
                "priority": 1
            },
            "lastChecked": {
                "direction": "ASC",
                "priority": 1
            },
            "muteStatus": {
                "direction": "ASC",
                "priority": 1
            },
            "name": {
                "direction": "ASC",
                "priority": 1
            },
            "securityDomain": {
                "direction": "ASC",
                "priority": 1
            },
            "severity": {
                "direction": "ASC",
                "priority": 1
            },
            "status": {
                "direction": "ASC",
                "priority": 1
            },
            "suppressedStatus": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.posture.checkResultList ####

`accountId` [ID] - (required) ID of the account whose Posture data is queried.    
`postureCheckResultListInput` [PostureCheckResultListInput] - (required) Filter, sort, and paging settings for the check results.    
