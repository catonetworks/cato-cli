
## CATO-CLI - query.popLocations:
[Click here](https://api.catonetworks.com/documentation/#query-query.popLocations) for documentation on this operation.

### Usage for query.popLocations:

```bash
catocli query popLocations -h

catocli query popLocations <json>

catocli query popLocations --json-file query.popLocations.json

catocli query popLocations '{"id":"id","popLocationAllocatedIpInput":{"filter":{"account":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"allocatedIp":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"allocationType":{"eq":"SYSTEM","in":"SYSTEM","neq":"SYSTEM","nin":"SYSTEM"},"description":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"global":{"search":"string"},"id":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"popLocation":{"eq":{"by":"ID","input":"string"},"in":{"by":"ID","input":"string"},"neq":{"by":"ID","input":"string"},"nin":{"by":"ID","input":"string"}},"subnet":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}}},"popLocationFilterInput":{"country":{"eq":{"by":"ID","input":"string"},"in":{"by":"ID","input":"string"},"neq":{"by":"ID","input":"string"},"nin":{"by":"ID","input":"string"}},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"interconnectTagging":{"taggingMethod":{"eq":"DOT1Q","in":"DOT1Q","neq":"DOT1Q","nin":"DOT1Q"}},"isPrivate":{"eq":true,"neq":true},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"primary":{"eq":true,"neq":true},"siteLicenseRegion":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}}}'

catocli query popLocations '{
    "id": "id",
    "popLocationAllocatedIpInput": {
        "filter": {
            "account": {
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
            "allocatedIp": {
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
            "allocationType": {
                "eq": "SYSTEM",
                "in": "SYSTEM",
                "neq": "SYSTEM",
                "nin": "SYSTEM"
            },
            "description": {
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
            "global": {
                "search": "string"
            },
            "id": {
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
            "popLocation": {
                "eq": {
                    "by": "ID",
                    "input": "string"
                },
                "in": {
                    "by": "ID",
                    "input": "string"
                },
                "neq": {
                    "by": "ID",
                    "input": "string"
                },
                "nin": {
                    "by": "ID",
                    "input": "string"
                }
            },
            "subnet": {
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
            }
        }
    },
    "popLocationFilterInput": {
        "country": {
            "eq": {
                "by": "ID",
                "input": "string"
            },
            "in": {
                "by": "ID",
                "input": "string"
            },
            "neq": {
                "by": "ID",
                "input": "string"
            },
            "nin": {
                "by": "ID",
                "input": "string"
            }
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
        "interconnectTagging": {
            "taggingMethod": {
                "eq": "DOT1Q",
                "in": "DOT1Q",
                "neq": "DOT1Q",
                "nin": "DOT1Q"
            }
        },
        "isPrivate": {
            "eq": true,
            "neq": true
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
        "primary": {
            "eq": true,
            "neq": true
        },
        "siteLicenseRegion": {
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
        }
    }
}'
```

#### Operation Arguments for query.popLocations ####

`accountId` [ID] - (required) N/A    
`id` [ID] - (required) N/A    
`popLocationAllocatedIpInput` [PopLocationAllocatedIpInput] - (required) N/A    
`popLocationFilterInput` [PopLocationFilterInput] - (required) N/A    
