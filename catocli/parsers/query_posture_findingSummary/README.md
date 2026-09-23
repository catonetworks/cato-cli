
## CATO-CLI - query.posture.findingSummary:
[Click here](https://api.catonetworks.com/documentation/#query-query.posture.findingSummary) for documentation on this operation.

### Usage for query.posture.findingSummary:

```bash
catocli query posture findingSummary -h

catocli query posture findingSummary <json>

catocli query posture findingSummary --json-file query.posture.findingSummary.json

catocli query posture findingSummary '{"accountId":"id","postureFindingSummaryInput":{"filter":{"appInstance":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"application":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"areaId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"categoryId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"checkId":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"checkName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"checkSeverity":{"eq":"INFORMATIONAL","in":"INFORMATIONAL","neq":"INFORMATIONAL","nin":"INFORMATIONAL"},"checkType":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"complianceControl":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"complianceFramework":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"label":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"muteStatus":{"eq":"MUTED","in":"MUTED","neq":"MUTED","nin":"MUTED"},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"resolutionStatus":{"eq":"OPEN","in":"OPEN","neq":"OPEN","nin":"OPEN"},"securityDomain":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"},"severity":{"eq":"INFORMATIONAL","in":"INFORMATIONAL","neq":"INFORMATIONAL","nin":"INFORMATIONAL"},"suppressedStatus":{"eq":"ENABLED","in":"ENABLED","neq":"ENABLED","nin":"ENABLED"}},"valueBreakdownLimit":1}}'

catocli query posture findingSummary '{
    "accountId": "id",
    "postureFindingSummaryInput": {
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
        "valueBreakdownLimit": 1
    }
}'
```

#### Operation Arguments for query.posture.findingSummary ####

`accountId` [ID] - (required) N/A    
`postureFindingSummaryInput` [PostureFindingSummaryInput] - (required) N/A    
