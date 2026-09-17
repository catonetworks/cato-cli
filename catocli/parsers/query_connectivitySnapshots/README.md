
## CATO-CLI - query.connectivitySnapshots:
[Click here](https://api.catonetworks.com/documentation/#query-query.connectivitySnapshots) for documentation on this operation.

### Usage for query.connectivitySnapshots:

```bash
catocli query connectivitySnapshots -h

catocli query connectivitySnapshots <json>

catocli query connectivitySnapshots --json-file query.connectivitySnapshots.json

catocli query connectivitySnapshots '{"ztnaAppConnectorGroupSnapshotInput":{"filter":{"connectedPop":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"connectivityStatus":{"eq":"CONNECTED","in":"CONNECTED","neq":"CONNECTED","nin":"CONNECTED"},"connectorName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"country":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"countryName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"deviceVersion":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"dnsServer":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"freeText":{"search":"string"},"groupName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"lanIp":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"model":{"eq":"X1500","in":"X1500","neq":"X1500","nin":"X1500"},"privateApp":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"serialNumber":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"paging":{"from":1,"limit":1}},"ztnaAppConnectorSnapshotInput":{"filter":{"connectedPop":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"connectivityStatus":{"eq":"CONNECTED","in":"CONNECTED","neq":"CONNECTED","nin":"CONNECTED"},"connectorName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"country":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"countryName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"deviceVersion":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"dnsServer":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"freeText":{"search":"string"},"groupName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"lanIp":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"model":{"eq":"X1500","in":"X1500","neq":"X1500","nin":"X1500"},"privateApp":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"serialNumber":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"paging":{"from":1,"limit":1},"sort":{"connectivity":{"direction":"ASC","priority":1},"createdAt":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}}},"ztnaAppConnectorSnapshotSummaryInput":{"filter":{"connectivityStatus":{"eq":"CONNECTED","in":"CONNECTED","neq":"CONNECTED","nin":"CONNECTED"}}}}'

catocli query connectivitySnapshots '{
    "ztnaAppConnectorGroupSnapshotInput": {
        "filter": {
            "connectedPop": {
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
            "connectivityStatus": {
                "eq": "CONNECTED",
                "in": "CONNECTED",
                "neq": "CONNECTED",
                "nin": "CONNECTED"
            },
            "connectorName": {
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
            "country": {
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
            "countryName": {
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
            "deviceVersion": {
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
            "dnsServer": {
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
            "freeText": {
                "search": "string"
            },
            "groupName": {
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
            "lanIp": {
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
            "model": {
                "eq": "X1500",
                "in": "X1500",
                "neq": "X1500",
                "nin": "X1500"
            },
            "privateApp": {
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
            "serialNumber": {
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
        },
        "paging": {
            "from": 1,
            "limit": 1
        }
    },
    "ztnaAppConnectorSnapshotInput": {
        "filter": {
            "connectedPop": {
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
            "connectivityStatus": {
                "eq": "CONNECTED",
                "in": "CONNECTED",
                "neq": "CONNECTED",
                "nin": "CONNECTED"
            },
            "connectorName": {
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
            "country": {
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
            "countryName": {
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
            "deviceVersion": {
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
            "dnsServer": {
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
            "freeText": {
                "search": "string"
            },
            "groupName": {
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
            "lanIp": {
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
            "model": {
                "eq": "X1500",
                "in": "X1500",
                "neq": "X1500",
                "nin": "X1500"
            },
            "privateApp": {
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
            "serialNumber": {
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
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "connectivity": {
                "direction": "ASC",
                "priority": 1
            },
            "createdAt": {
                "direction": "ASC",
                "priority": 1
            },
            "name": {
                "direction": "ASC",
                "priority": 1
            }
        }
    },
    "ztnaAppConnectorSnapshotSummaryInput": {
        "filter": {
            "connectivityStatus": {
                "eq": "CONNECTED",
                "in": "CONNECTED",
                "neq": "CONNECTED",
                "nin": "CONNECTED"
            }
        }
    }
}'
```

#### Operation Arguments for query.connectivitySnapshots ####

`accountId` [ID] - (required) N/A    
`ztnaAppConnectorGroupSnapshotInput` [ZtnaAppConnectorGroupSnapshotInput] - (required) N/A    
`ztnaAppConnectorSnapshotInput` [ZtnaAppConnectorSnapshotInput] - (required) N/A    
`ztnaAppConnectorSnapshotSummaryInput` [ZtnaAppConnectorSnapshotSummaryInput] - (required) N/A    
