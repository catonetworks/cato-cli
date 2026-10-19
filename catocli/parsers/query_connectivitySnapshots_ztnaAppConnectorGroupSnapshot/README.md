
## CATO-CLI - query.connectivitySnapshots.ztnaAppConnectorGroupSnapshot:
[Click here](https://api.catonetworks.com/documentation/#query-query.connectivitySnapshots.ztnaAppConnectorGroupSnapshot) for documentation on this operation.

### Usage for query.connectivitySnapshots.ztnaAppConnectorGroupSnapshot:

```bash
catocli query connectivitySnapshots ztnaAppConnectorGroupSnapshot -h

catocli query connectivitySnapshots ztnaAppConnectorGroupSnapshot <json>

catocli query connectivitySnapshots ztnaAppConnectorGroupSnapshot --json-file query.connectivitySnapshots.ztnaAppConnectorGroupSnapshot.json

catocli query connectivitySnapshots ztnaAppConnectorGroupSnapshot '{"ztnaAppConnectorGroupSnapshotInput":{"filter":{"connectedPop":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"connectivityStatus":[{"eq":"CONNECTED","in":["CONNECTED"],"neq":"CONNECTED","nin":["CONNECTED"]}],"connectorName":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"country":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"countryName":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"deviceVersion":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"dnsServer":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"freeText":[{"search":"string"}],"groupName":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"id":[{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]}],"lanIp":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"model":[{"eq":"X1500","in":["X1500"],"neq":"X1500","nin":["X1500"]}],"privateApp":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"serialNumber":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}]},"paging":{"from":1,"limit":1}}}'

catocli query connectivitySnapshots ztnaAppConnectorGroupSnapshot '{
    "ztnaAppConnectorGroupSnapshotInput": {
        "filter": {
            "connectedPop": [
                {
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
            ],
            "connectivityStatus": [
                {
                    "eq": "CONNECTED",
                    "in": [
                        "CONNECTED"
                    ],
                    "neq": "CONNECTED",
                    "nin": [
                        "CONNECTED"
                    ]
                }
            ],
            "connectorName": [
                {
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
            ],
            "country": [
                {
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
            ],
            "countryName": [
                {
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
            ],
            "deviceVersion": [
                {
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
            ],
            "dnsServer": [
                {
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
            ],
            "freeText": [
                {
                    "search": "string"
                }
            ],
            "groupName": [
                {
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
            ],
            "id": [
                {
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
            ],
            "lanIp": [
                {
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
            ],
            "model": [
                {
                    "eq": "X1500",
                    "in": [
                        "X1500"
                    ],
                    "neq": "X1500",
                    "nin": [
                        "X1500"
                    ]
                }
            ],
            "privateApp": [
                {
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
            ],
            "serialNumber": [
                {
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
            ]
        },
        "paging": {
            "from": 1,
            "limit": 1
        }
    }
}'
```

#### Operation Arguments for query.connectivitySnapshots.ztnaAppConnectorGroupSnapshot ####

`accountId` [ID] - (required) N/A
`ztnaAppConnectorGroupSnapshotInput` [ZtnaAppConnectorGroupSnapshotInput] - (required) N/A
