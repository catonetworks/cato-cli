
## CATO-CLI - query.posture.findingList:
[Click here](https://api.catonetworks.com/documentation/#query-query.posture.findingList) for documentation on this operation.

### Usage for query.posture.findingList:

```bash
catocli query posture findingList -h

catocli query posture findingList <json>

catocli query posture findingList --json-file query.posture.findingList.json

catocli query posture findingList '{"postureFindingListInput":{"filter":{"appInstance":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"application":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"areaId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"categoryId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"checkId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"checkName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"checkSeverity":{"eq":"INFORMATIONAL","in":"INFORMATIONAL","neq":"INFORMATIONAL","nin":"INFORMATIONAL"},"checkType":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"complianceControl":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"complianceFramework":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"label":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"muteStatus":{"eq":"MUTED","in":"MUTED","neq":"MUTED","nin":"MUTED"},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"resolutionStatus":{"eq":"OPEN","in":"OPEN","neq":"OPEN","nin":"OPEN"},"securityDomain":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"severity":{"eq":"INFORMATIONAL","in":"INFORMATIONAL","neq":"INFORMATIONAL","nin":"INFORMATIONAL"},"suppressedStatus":{"eq":"ENABLED","in":"ENABLED","neq":"ENABLED","nin":"ENABLED"}},"paging":{"from":1,"limit":1},"sort":{"appInstance":{"direction":"ASC","priority":1},"application":{"direction":"ASC","priority":1},"areaId":{"direction":"ASC","priority":1},"categoryId":{"direction":"ASC","priority":1},"checkId":{"direction":"ASC","priority":1},"checkName":{"direction":"ASC","priority":1},"checkSeverity":{"direction":"ASC","priority":1},"checkType":{"direction":"ASC","priority":1},"complianceControl":{"direction":"ASC","priority":1},"complianceFramework":{"direction":"ASC","priority":1},"id":{"direction":"ASC","priority":1},"label":{"direction":"ASC","priority":1},"muteStatus":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1},"resolutionStatus":{"direction":"ASC","priority":1},"securityDomain":{"direction":"ASC","priority":1},"severity":{"direction":"ASC","priority":1},"suppressedStatus":{"direction":"ASC","priority":1}}}}'

catocli query posture findingList '{
    "postureFindingListInput": {
        "filter": {
            "appInstance": {
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
            "checkName": {
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
            "checkSeverity": {
                "eq": "INFORMATIONAL",
                "in": "INFORMATIONAL",
                "neq": "INFORMATIONAL",
                "nin": "INFORMATIONAL"
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
            "id": {
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
            "resolutionStatus": {
                "eq": "OPEN",
                "in": "OPEN",
                "neq": "OPEN",
                "nin": "OPEN"
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
            "appInstance": {
                "direction": "ASC",
                "priority": 1
            },
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
            "checkName": {
                "direction": "ASC",
                "priority": 1
            },
            "checkSeverity": {
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
            "id": {
                "direction": "ASC",
                "priority": 1
            },
            "label": {
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
            "resolutionStatus": {
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
            "suppressedStatus": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.posture.findingList ####

`accountId` [ID] - (required) ID of the account whose Posture data is queried. 
`postureFindingListInput` [PostureFindingListInput] - (required) Filter, sort, and paging settings for the findings. 
