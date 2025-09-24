
## CATO-CLI - query.devices:
[Click here](https://api.catonetworks.com/documentation/#query-query.devices) for documentation on this operation.

### Usage for query.devices:

`catocli query devices -h`

`catocli query devices <json>`

`catocli query devices "$(cat < query.devices.json)"`

`catocli query devices '{"deviceAttributeCatalogInput":{"pagingInput":{"from":1,"limit":1},"sortOrderInput":{"direction":"ASC","priority":1},"stringFilterInput":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"deviceCsvExportInput":{"deviceV2FilterInput":{"category":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"confidence":{"eq":"LOW","in":"LOW","neq":"LOW","nin":"LOW"},"firstSeen":{"between":["example1","example2"],"eq":"example_value","gt":"example_value","gte":"example_value","in":["example1","example2"],"lt":"example_value","lte":"example_value","neq":"example_value","nin":["example1","example2"]},"hw":{"manufacturer":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"model":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"type":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"ipAddress":{"between":["example1","example2"],"eq":"example_value","in":["example1","example2"],"neq":"example_value","nin":["example1","example2"],"nwithin":"example_value","within":"example_value"},"isManaged":{"eq":true,"neq":true},"lastSeen":{"between":["example1","example2"],"eq":"example_value","gt":"example_value","gte":"example_value","in":["example1","example2"],"lt":"example_value","lte":"example_value","neq":"example_value","nin":["example1","example2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"network":{"networkName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"subnet":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"nic":{"macAddress":{"eq":"example_value","in":["example1","example2"],"neq":"example_value","nin":["example1","example2"]},"vendor":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"os":{"product":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"vendor":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"version":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"riskScore":{"between":[1,2],"eq":1,"gt":1,"gte":1,"in":[1,2],"lt":1,"lte":1,"neq":1,"nin":[1,2]},"site":{"eq":{"by":"ID","input":"string"},"in":{"by":"ID","input":"string"},"neq":{"by":"ID","input":"string"},"nin":{"by":"ID","input":"string"}},"user":{"eq":{"by":"ID","input":"string"},"in":{"by":"ID","input":"string"},"neq":{"by":"ID","input":"string"},"nin":{"by":"ID","input":"string"}}}},"deviceV2Input":{"deviceSortInput":{"category":{"direction":"ASC","priority":1},"confidence":{"direction":"ASC","priority":1},"firstSeen":{"direction":"ASC","priority":1},"hw":{"manufacturer":{"direction":"ASC","priority":1},"model":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}},"id":{"direction":"ASC","priority":1},"ip":{"direction":"ASC","priority":1},"lastSeen":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1},"network":{"networkName":{"direction":"ASC","priority":1},"subnet":{"direction":"ASC","priority":1}},"nic":{"macAddress":{"direction":"ASC","priority":1},"vendor":{"direction":"ASC","priority":1}},"os":{"product":{"direction":"ASC","priority":1},"vendor":{"direction":"ASC","priority":1},"version":{"direction":"ASC","priority":1}},"riskScore":{"direction":"ASC","priority":1},"site":{"id":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}},"user":{"id":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}}},"deviceV2FilterInput":{"category":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"confidence":{"eq":"LOW","in":"LOW","neq":"LOW","nin":"LOW"},"firstSeen":{"between":["example1","example2"],"eq":"example_value","gt":"example_value","gte":"example_value","in":["example1","example2"],"lt":"example_value","lte":"example_value","neq":"example_value","nin":["example1","example2"]},"hw":{"manufacturer":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"model":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"type":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"ipAddress":{"between":["example1","example2"],"eq":"example_value","in":["example1","example2"],"neq":"example_value","nin":["example1","example2"],"nwithin":"example_value","within":"example_value"},"isManaged":{"eq":true,"neq":true},"lastSeen":{"between":["example1","example2"],"eq":"example_value","gt":"example_value","gte":"example_value","in":["example1","example2"],"lt":"example_value","lte":"example_value","neq":"example_value","nin":["example1","example2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"network":{"networkName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"subnet":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"nic":{"macAddress":{"eq":"example_value","in":["example1","example2"],"neq":"example_value","nin":["example1","example2"]},"vendor":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"os":{"product":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"vendor":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"version":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"riskScore":{"between":[1,2],"eq":1,"gt":1,"gte":1,"in":[1,2],"lt":1,"lte":1,"neq":1,"nin":[1,2]},"site":{"eq":{"by":"ID","input":"string"},"in":{"by":"ID","input":"string"},"neq":{"by":"ID","input":"string"},"nin":{"by":"ID","input":"string"}},"user":{"eq":{"by":"ID","input":"string"},"in":{"by":"ID","input":"string"},"neq":{"by":"ID","input":"string"},"nin":{"by":"ID","input":"string"}}},"pagingInput":{"from":1,"limit":1}},"jobId":"id","sortOrderInput":{"direction":"ASC","priority":1}}'`

`catocli query devices -p '{
    "deviceAttributeCatalogInput": {
        "pagingInput": {
            "from": 1,
            "limit": 1
        },
        "sortOrderInput": {
            "direction": "ASC",
            "priority": 1
        },
        "stringFilterInput": {
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
    "deviceCsvExportInput": {
        "deviceV2FilterInput": {
            "category": {
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
            "confidence": {
                "eq": "LOW",
                "in": "LOW",
                "neq": "LOW",
                "nin": "LOW"
            },
            "firstSeen": {
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
            "hw": {
                "manufacturer": {
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
                "type": {
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
            "ipAddress": {
                "between": [
                    "example1",
                    "example2"
                ],
                "eq": "example_value",
                "in": [
                    "example1",
                    "example2"
                ],
                "neq": "example_value",
                "nin": [
                    "example1",
                    "example2"
                ],
                "nwithin": "example_value",
                "within": "example_value"
            },
            "isManaged": {
                "eq": true,
                "neq": true
            },
            "lastSeen": {
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
            "network": {
                "networkName": {
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
            },
            "nic": {
                "macAddress": {
                    "eq": "example_value",
                    "in": [
                        "example1",
                        "example2"
                    ],
                    "neq": "example_value",
                    "nin": [
                        "example1",
                        "example2"
                    ]
                },
                "vendor": {
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
            "os": {
                "product": {
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
                "vendor": {
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
                "version": {
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
            "riskScore": {
                "between": [
                    1,
                    2
                ],
                "eq": 1,
                "gt": 1,
                "gte": 1,
                "in": [
                    1,
                    2
                ],
                "lt": 1,
                "lte": 1,
                "neq": 1,
                "nin": [
                    1,
                    2
                ]
            },
            "site": {
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
            "user": {
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
            }
        }
    },
    "deviceV2Input": {
        "deviceSortInput": {
            "category": {
                "direction": "ASC",
                "priority": 1
            },
            "confidence": {
                "direction": "ASC",
                "priority": 1
            },
            "firstSeen": {
                "direction": "ASC",
                "priority": 1
            },
            "hw": {
                "manufacturer": {
                    "direction": "ASC",
                    "priority": 1
                },
                "model": {
                    "direction": "ASC",
                    "priority": 1
                },
                "type": {
                    "direction": "ASC",
                    "priority": 1
                }
            },
            "id": {
                "direction": "ASC",
                "priority": 1
            },
            "ip": {
                "direction": "ASC",
                "priority": 1
            },
            "lastSeen": {
                "direction": "ASC",
                "priority": 1
            },
            "name": {
                "direction": "ASC",
                "priority": 1
            },
            "network": {
                "networkName": {
                    "direction": "ASC",
                    "priority": 1
                },
                "subnet": {
                    "direction": "ASC",
                    "priority": 1
                }
            },
            "nic": {
                "macAddress": {
                    "direction": "ASC",
                    "priority": 1
                },
                "vendor": {
                    "direction": "ASC",
                    "priority": 1
                }
            },
            "os": {
                "product": {
                    "direction": "ASC",
                    "priority": 1
                },
                "vendor": {
                    "direction": "ASC",
                    "priority": 1
                },
                "version": {
                    "direction": "ASC",
                    "priority": 1
                }
            },
            "riskScore": {
                "direction": "ASC",
                "priority": 1
            },
            "site": {
                "id": {
                    "direction": "ASC",
                    "priority": 1
                },
                "name": {
                    "direction": "ASC",
                    "priority": 1
                }
            },
            "user": {
                "id": {
                    "direction": "ASC",
                    "priority": 1
                },
                "name": {
                    "direction": "ASC",
                    "priority": 1
                }
            }
        },
        "deviceV2FilterInput": {
            "category": {
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
            "confidence": {
                "eq": "LOW",
                "in": "LOW",
                "neq": "LOW",
                "nin": "LOW"
            },
            "firstSeen": {
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
            "hw": {
                "manufacturer": {
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
                "type": {
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
            "ipAddress": {
                "between": [
                    "example1",
                    "example2"
                ],
                "eq": "example_value",
                "in": [
                    "example1",
                    "example2"
                ],
                "neq": "example_value",
                "nin": [
                    "example1",
                    "example2"
                ],
                "nwithin": "example_value",
                "within": "example_value"
            },
            "isManaged": {
                "eq": true,
                "neq": true
            },
            "lastSeen": {
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
            "network": {
                "networkName": {
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
            },
            "nic": {
                "macAddress": {
                    "eq": "example_value",
                    "in": [
                        "example1",
                        "example2"
                    ],
                    "neq": "example_value",
                    "nin": [
                        "example1",
                        "example2"
                    ]
                },
                "vendor": {
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
            "os": {
                "product": {
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
                "vendor": {
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
                "version": {
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
            "riskScore": {
                "between": [
                    1,
                    2
                ],
                "eq": 1,
                "gt": 1,
                "gte": 1,
                "in": [
                    1,
                    2
                ],
                "lt": 1,
                "lte": 1,
                "neq": 1,
                "nin": [
                    1,
                    2
                ]
            },
            "site": {
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
            "user": {
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
            }
        },
        "pagingInput": {
            "from": 1,
            "limit": 1
        }
    },
    "jobId": "id",
    "sortOrderInput": {
        "direction": "ASC",
        "priority": 1
    }
}'`


#### Operation Arguments for query.devices ####

`accountId` [ID] - (required) N/A    
`deviceAttributeCatalogInput` [DeviceAttributeCatalogInput] - (required) N/A    
`deviceCsvExportInput` [DeviceCsvExportInput] - (required) N/A    
`deviceV2Input` [DeviceV2Input] - (required) N/A    
`jobId` [ID] - (required) N/A    
`sortOrderInput` [SortOrderInput] - (required) N/A    
