
## CATO-CLI - query.devices:
[Click here](https://api.catonetworks.com/documentation/#query-query.devices) for documentation on this operation.

### Usage for query.devices:

```bash
catocli query devices -h

catocli query devices <json>

catocli query devices --json-file query.devices.json

catocli query devices '{"deviceAttributeCatalogInput":{"filter":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"paging":{"from":1,"limit":1},"sort":{"direction":"ASC","priority":1}},"deviceComplianceCatalogInput":{"filter":{"applicationConnector":{"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"state":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}},"paging":{"from":1,"limit":1},"sort":{"applicationConnector":{"id":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}},"state":{"direction":"ASC","priority":1}}},"deviceCsvExportInput":{"filter":[{"category":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"complianceState":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"confidence":[{"eq":"LOW","in":["LOW"],"neq":"LOW","nin":["LOW"]}],"firstSeen":[{"between":["2026-01-02T15:04:05Z"],"eq":"2026-01-02T15:04:05Z","gt":"2026-01-02T15:04:05Z","gte":"2026-01-02T15:04:05Z","in":["2026-01-02T15:04:05Z"],"lt":"2026-01-02T15:04:05Z","lte":"2026-01-02T15:04:05Z","neq":"2026-01-02T15:04:05Z","nin":["2026-01-02T15:04:05Z"]}],"freeText":{"search":"string"},"hw":{"manufacturer":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"model":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"type":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}]},"id":[{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]}],"ipAddress":[{"between":["192.0.2.1"],"eq":"192.0.2.1","in":["192.0.2.1"],"neq":"192.0.2.1","nin":["192.0.2.1"],"nwithin":"192.0.2.0/24","within":"192.0.2.0/24"}],"isCrownJewel":[{"eq":true,"neq":true}],"isManaged":[{"eq":true,"neq":true}],"lastSeen":[{"between":["2026-01-02T15:04:05Z"],"eq":"2026-01-02T15:04:05Z","gt":"2026-01-02T15:04:05Z","gte":"2026-01-02T15:04:05Z","in":["2026-01-02T15:04:05Z"],"lt":"2026-01-02T15:04:05Z","lte":"2026-01-02T15:04:05Z","neq":"2026-01-02T15:04:05Z","nin":["2026-01-02T15:04:05Z"]}],"name":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"network":{"networkName":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"subnet":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}]},"nic":{"macAddress":[{"eq":"02:00:00:00:00:01","in":["02:00:00:00:00:01"],"neq":"02:00:00:00:00:01","nin":["02:00:00:00:00:01"]}],"vendor":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}]},"originTypes":[{"hasAll":["Unknown"],"in":["Unknown"],"nin":["Unknown"]}],"os":{"product":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"vendor":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"version":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}]},"riskScore":[{"between":[1,2],"eq":1,"gt":1,"gte":1,"in":[1,2],"lt":1,"lte":1,"neq":1,"nin":[1,2]}],"site":[{"eq":{"by":"ID","input":"string"},"in":[{"by":"ID","input":"string"}],"neq":{"by":"ID","input":"string"},"nin":[{"by":"ID","input":"string"}]}],"user":[{"eq":{"by":"ID","input":"string"},"in":[{"by":"ID","input":"string"}],"neq":{"by":"ID","input":"string"},"nin":[{"by":"ID","input":"string"}]}]}],"timeFrame":{"from":"2026-01-02T15:04:05Z","to":"2026-01-02T15:04:05Z"}},"deviceRiskCatalogInput":{"filter":{"applicationConnector":{"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}}},"paging":{"from":1,"limit":1},"sort":{"applicationConnector":{"id":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}}}},"deviceV2Input":{"filter":[{"category":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"complianceState":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"confidence":[{"eq":"LOW","in":["LOW"],"neq":"LOW","nin":["LOW"]}],"firstSeen":[{"between":["2026-01-02T15:04:05Z"],"eq":"2026-01-02T15:04:05Z","gt":"2026-01-02T15:04:05Z","gte":"2026-01-02T15:04:05Z","in":["2026-01-02T15:04:05Z"],"lt":"2026-01-02T15:04:05Z","lte":"2026-01-02T15:04:05Z","neq":"2026-01-02T15:04:05Z","nin":["2026-01-02T15:04:05Z"]}],"freeText":{"search":"string"},"hw":{"manufacturer":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"model":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"type":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}]},"id":[{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]}],"ipAddress":[{"between":["192.0.2.1"],"eq":"192.0.2.1","in":["192.0.2.1"],"neq":"192.0.2.1","nin":["192.0.2.1"],"nwithin":"192.0.2.0/24","within":"192.0.2.0/24"}],"isCrownJewel":[{"eq":true,"neq":true}],"isManaged":[{"eq":true,"neq":true}],"lastSeen":[{"between":["2026-01-02T15:04:05Z"],"eq":"2026-01-02T15:04:05Z","gt":"2026-01-02T15:04:05Z","gte":"2026-01-02T15:04:05Z","in":["2026-01-02T15:04:05Z"],"lt":"2026-01-02T15:04:05Z","lte":"2026-01-02T15:04:05Z","neq":"2026-01-02T15:04:05Z","nin":["2026-01-02T15:04:05Z"]}],"name":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"network":{"networkName":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"subnet":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}]},"nic":{"macAddress":[{"eq":"02:00:00:00:00:01","in":["02:00:00:00:00:01"],"neq":"02:00:00:00:00:01","nin":["02:00:00:00:00:01"]}],"vendor":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}]},"originTypes":[{"hasAll":["Unknown"],"in":["Unknown"],"nin":["Unknown"]}],"os":{"product":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"vendor":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}],"version":[{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}]},"riskScore":[{"between":[1,2],"eq":1,"gt":1,"gte":1,"in":[1,2],"lt":1,"lte":1,"neq":1,"nin":[1,2]}],"site":[{"eq":{"by":"ID","input":"string"},"in":[{"by":"ID","input":"string"}],"neq":{"by":"ID","input":"string"},"nin":[{"by":"ID","input":"string"}]}],"user":[{"eq":{"by":"ID","input":"string"},"in":[{"by":"ID","input":"string"}],"neq":{"by":"ID","input":"string"},"nin":[{"by":"ID","input":"string"}]}]}],"paging":{"from":1,"limit":1},"sort":{"category":{"direction":"ASC","priority":1},"confidence":{"direction":"ASC","priority":1},"firstSeen":{"direction":"ASC","priority":1},"hw":{"manufacturer":{"direction":"ASC","priority":1},"model":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}},"id":{"direction":"ASC","priority":1},"ip":{"direction":"ASC","priority":1},"lastSeen":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1},"network":{"networkName":{"direction":"ASC","priority":1},"subnet":{"direction":"ASC","priority":1}},"nic":{"macAddress":{"direction":"ASC","priority":1},"vendor":{"direction":"ASC","priority":1}},"os":{"product":{"direction":"ASC","priority":1},"vendor":{"direction":"ASC","priority":1},"version":{"direction":"ASC","priority":1}},"riskScore":{"direction":"ASC","priority":1},"site":{"id":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}},"user":{"id":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}}}},"jobId":"id","sortOrderInput":{"direction":"ASC","priority":1}}'

catocli query devices '{
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
    "deviceCsvExportInput": {
        "filter": [
            {
                "category": [
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
                "complianceState": [
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
                "confidence": [
                    {
                        "eq": "LOW",
                        "in": [
                            "LOW"
                        ],
                        "neq": "LOW",
                        "nin": [
                            "LOW"
                        ]
                    }
                ],
                "firstSeen": [
                    {
                        "between": [
                            "2026-01-02T15:04:05Z"
                        ],
                        "eq": "2026-01-02T15:04:05Z",
                        "gt": "2026-01-02T15:04:05Z",
                        "gte": "2026-01-02T15:04:05Z",
                        "in": [
                            "2026-01-02T15:04:05Z"
                        ],
                        "lt": "2026-01-02T15:04:05Z",
                        "lte": "2026-01-02T15:04:05Z",
                        "neq": "2026-01-02T15:04:05Z",
                        "nin": [
                            "2026-01-02T15:04:05Z"
                        ]
                    }
                ],
                "freeText": {
                    "search": "string"
                },
                "hw": {
                    "manufacturer": [
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
                    "type": [
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
                "ipAddress": [
                    {
                        "between": [
                            "192.0.2.1"
                        ],
                        "eq": "192.0.2.1",
                        "in": [
                            "192.0.2.1"
                        ],
                        "neq": "192.0.2.1",
                        "nin": [
                            "192.0.2.1"
                        ],
                        "nwithin": "192.0.2.0/24",
                        "within": "192.0.2.0/24"
                    }
                ],
                "isCrownJewel": [
                    {
                        "eq": true,
                        "neq": true
                    }
                ],
                "isManaged": [
                    {
                        "eq": true,
                        "neq": true
                    }
                ],
                "lastSeen": [
                    {
                        "between": [
                            "2026-01-02T15:04:05Z"
                        ],
                        "eq": "2026-01-02T15:04:05Z",
                        "gt": "2026-01-02T15:04:05Z",
                        "gte": "2026-01-02T15:04:05Z",
                        "in": [
                            "2026-01-02T15:04:05Z"
                        ],
                        "lt": "2026-01-02T15:04:05Z",
                        "lte": "2026-01-02T15:04:05Z",
                        "neq": "2026-01-02T15:04:05Z",
                        "nin": [
                            "2026-01-02T15:04:05Z"
                        ]
                    }
                ],
                "name": [
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
                "network": {
                    "networkName": [
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
                    "subnet": [
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
                "nic": {
                    "macAddress": [
                        {
                            "eq": "02:00:00:00:00:01",
                            "in": [
                                "02:00:00:00:00:01"
                            ],
                            "neq": "02:00:00:00:00:01",
                            "nin": [
                                "02:00:00:00:00:01"
                            ]
                        }
                    ],
                    "vendor": [
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
                "originTypes": [
                    {
                        "hasAll": [
                            "Unknown"
                        ],
                        "in": [
                            "Unknown"
                        ],
                        "nin": [
                            "Unknown"
                        ]
                    }
                ],
                "os": {
                    "product": [
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
                    "vendor": [
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
                    "version": [
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
                "riskScore": [
                    {
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
                    }
                ],
                "site": [
                    {
                        "eq": {
                            "by": "ID",
                            "input": "string"
                        },
                        "in": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "neq": {
                            "by": "ID",
                            "input": "string"
                        },
                        "nin": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ]
                    }
                ],
                "user": [
                    {
                        "eq": {
                            "by": "ID",
                            "input": "string"
                        },
                        "in": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "neq": {
                            "by": "ID",
                            "input": "string"
                        },
                        "nin": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ]
                    }
                ]
            }
        ],
        "timeFrame": {
            "from": "2026-01-02T15:04:05Z",
            "to": "2026-01-02T15:04:05Z"
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
    "deviceV2Input": {
        "filter": [
            {
                "category": [
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
                "complianceState": [
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
                "confidence": [
                    {
                        "eq": "LOW",
                        "in": [
                            "LOW"
                        ],
                        "neq": "LOW",
                        "nin": [
                            "LOW"
                        ]
                    }
                ],
                "firstSeen": [
                    {
                        "between": [
                            "2026-01-02T15:04:05Z"
                        ],
                        "eq": "2026-01-02T15:04:05Z",
                        "gt": "2026-01-02T15:04:05Z",
                        "gte": "2026-01-02T15:04:05Z",
                        "in": [
                            "2026-01-02T15:04:05Z"
                        ],
                        "lt": "2026-01-02T15:04:05Z",
                        "lte": "2026-01-02T15:04:05Z",
                        "neq": "2026-01-02T15:04:05Z",
                        "nin": [
                            "2026-01-02T15:04:05Z"
                        ]
                    }
                ],
                "freeText": {
                    "search": "string"
                },
                "hw": {
                    "manufacturer": [
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
                    "type": [
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
                "ipAddress": [
                    {
                        "between": [
                            "192.0.2.1"
                        ],
                        "eq": "192.0.2.1",
                        "in": [
                            "192.0.2.1"
                        ],
                        "neq": "192.0.2.1",
                        "nin": [
                            "192.0.2.1"
                        ],
                        "nwithin": "192.0.2.0/24",
                        "within": "192.0.2.0/24"
                    }
                ],
                "isCrownJewel": [
                    {
                        "eq": true,
                        "neq": true
                    }
                ],
                "isManaged": [
                    {
                        "eq": true,
                        "neq": true
                    }
                ],
                "lastSeen": [
                    {
                        "between": [
                            "2026-01-02T15:04:05Z"
                        ],
                        "eq": "2026-01-02T15:04:05Z",
                        "gt": "2026-01-02T15:04:05Z",
                        "gte": "2026-01-02T15:04:05Z",
                        "in": [
                            "2026-01-02T15:04:05Z"
                        ],
                        "lt": "2026-01-02T15:04:05Z",
                        "lte": "2026-01-02T15:04:05Z",
                        "neq": "2026-01-02T15:04:05Z",
                        "nin": [
                            "2026-01-02T15:04:05Z"
                        ]
                    }
                ],
                "name": [
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
                "network": {
                    "networkName": [
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
                    "subnet": [
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
                "nic": {
                    "macAddress": [
                        {
                            "eq": "02:00:00:00:00:01",
                            "in": [
                                "02:00:00:00:00:01"
                            ],
                            "neq": "02:00:00:00:00:01",
                            "nin": [
                                "02:00:00:00:00:01"
                            ]
                        }
                    ],
                    "vendor": [
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
                "originTypes": [
                    {
                        "hasAll": [
                            "Unknown"
                        ],
                        "in": [
                            "Unknown"
                        ],
                        "nin": [
                            "Unknown"
                        ]
                    }
                ],
                "os": {
                    "product": [
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
                    "vendor": [
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
                    "version": [
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
                "riskScore": [
                    {
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
                    }
                ],
                "site": [
                    {
                        "eq": {
                            "by": "ID",
                            "input": "string"
                        },
                        "in": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "neq": {
                            "by": "ID",
                            "input": "string"
                        },
                        "nin": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ]
                    }
                ],
                "user": [
                    {
                        "eq": {
                            "by": "ID",
                            "input": "string"
                        },
                        "in": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ],
                        "neq": {
                            "by": "ID",
                            "input": "string"
                        },
                        "nin": [
                            {
                                "by": "ID",
                                "input": "string"
                            }
                        ]
                    }
                ]
            }
        ],
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
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
        }
    },
    "jobId": "id",
    "sortOrderInput": {
        "direction": "ASC",
        "priority": 1
    }
}'
```

#### Operation Arguments for query.devices ####

`accountId` [ID] - (required) N/A
`deviceAttributeCatalogInput` [DeviceAttributeCatalogInput] - (required) N/A
`deviceComplianceCatalogInput` [DeviceComplianceCatalogInput] - (required) N/A
`deviceCsvExportInput` [DeviceCsvExportInput] - (required) N/A
`deviceRiskCatalogInput` [DeviceRiskCatalogInput] - (required) N/A
`deviceV2Input` [DeviceV2Input] - (required) N/A
`jobId` [ID] - (required) N/A
`sortOrderInput` [SortOrderInput] - (required) N/A
