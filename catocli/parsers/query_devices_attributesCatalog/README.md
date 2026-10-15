
## CATO-CLI - query.devices.attributesCatalog:
[Click here](https://api.catonetworks.com/documentation/#query-query.devices.attributesCatalog) for documentation on this operation.

### Usage for query.devices.attributesCatalog:

```bash
catocli query devices attributesCatalog -h

catocli query devices attributesCatalog <json>

catocli query devices attributesCatalog --json-file query.devices.attributesCatalog.json

catocli query devices attributesCatalog '{"deviceAttributeCatalogInput":{"filter":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"paging":{"from":1,"limit":1},"sort":{"direction":"ASC","priority":1}},"deviceComplianceCatalogInput":{"filter":{"applicationConnector":{"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"state":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"paging":{"from":1,"limit":1},"sort":{"applicationConnector":{"id":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}},"state":{"direction":"ASC","priority":1}}},"deviceRiskCatalogInput":{"filter":{"applicationConnector":{"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}}},"paging":{"from":1,"limit":1},"sort":{"applicationConnector":{"id":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}}}},"sortOrderInput":{"direction":"ASC","priority":1}}'

catocli query devices attributesCatalog '{
    "deviceAttributeCatalogInput": {
        "filter": {
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
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "direction": "ASC",
            "priority": 1
        }
    },
    "deviceComplianceCatalogInput": {
        "filter": {
            "applicationConnector": {
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
                }
            },
            "state": {
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
            "applicationConnector": {
                "id": {
                    "direction": "ASC",
                    "priority": 1
                },
                "name": {
                    "direction": "ASC",
                    "priority": 1
                }
            },
            "state": {
                "direction": "ASC",
                "priority": 1
            }
        }
    },
    "deviceRiskCatalogInput": {
        "filter": {
            "applicationConnector": {
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
                }
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "applicationConnector": {
                "id": {
                    "direction": "ASC",
                    "priority": 1
                },
                "name": {
                    "direction": "ASC",
                    "priority": 1
                }
            }
        }
    },
    "sortOrderInput": {
        "direction": "ASC",
        "priority": 1
    }
}'
```

#### Operation Arguments for query.devices.attributesCatalog ####

`accountId` [ID] - (required) N/A
`deviceAttributeCatalogInput` [DeviceAttributeCatalogInput] - (required) N/A
`deviceComplianceCatalogInput` [DeviceComplianceCatalogInput] - (required) N/A
`deviceRiskCatalogInput` [DeviceRiskCatalogInput] - (required) N/A
`sortOrderInput` [SortOrderInput] - (required) N/A
