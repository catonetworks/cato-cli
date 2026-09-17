
## CATO-CLI - query.posture.checkSummary:
[Click here](https://api.catonetworks.com/documentation/#query-query.posture.checkSummary) for documentation on this operation.

### Usage for query.posture.checkSummary:

```bash
catocli query posture checkSummary -h

catocli query posture checkSummary <json>

catocli query posture checkSummary --json-file query.posture.checkSummary.json

catocli query posture checkSummary '{"postureCheckSummaryInput":{"filter":{"application":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"areaId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"categoryId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"checkId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"checkType":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"complianceControl":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"complianceFramework":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"findingName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"label":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"muteStatus":{"eq":"MUTED","in":"MUTED","neq":"MUTED","nin":"MUTED"},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"securityDomain":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"severity":{"eq":"INFORMATIONAL","in":"INFORMATIONAL","neq":"INFORMATIONAL","nin":"INFORMATIONAL"},"status":{"eq":"PASSED","in":"PASSED","neq":"PASSED","nin":"PASSED"},"suppressedStatus":{"eq":"ENABLED","in":"ENABLED","neq":"ENABLED","nin":"ENABLED"}},"newCheckDaysThreshold":1}}'

catocli query posture checkSummary '{
    "postureCheckSummaryInput": {
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
        "newCheckDaysThreshold": 1
    }
}'
```

#### Operation Arguments for query.posture.checkSummary ####

