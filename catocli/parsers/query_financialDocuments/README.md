
## CATO-CLI - query.financialDocuments:
[Click here](https://api.catonetworks.com/documentation/#query-query.financialDocuments) for documentation on this operation.

### Usage for query.financialDocuments:

```bash
catocli query financialDocuments -h

catocli query financialDocuments <json>

catocli query financialDocuments --json-file query.financialDocuments.json

catocli query financialDocuments '{"invoiceAccountListInput":{"filter":{"account":[{"accountInclusion":"ALL_ACCOUNTS","in":["id1","id2"]}],"chargeItem":[{"search":"string"}],"endDate":[{"between":["2026-01-02"],"eq":"2026-01-02","gt":"2026-01-02","gte":"2026-01-02","in":["2026-01-02"],"lt":"2026-01-02","lte":"2026-01-02","neq":"2026-01-02","nin":["2026-01-02"]}],"startDate":[{"between":["2026-01-02"],"eq":"2026-01-02","gt":"2026-01-02","gte":"2026-01-02","in":["2026-01-02"],"lt":"2026-01-02","lte":"2026-01-02","neq":"2026-01-02","nin":["2026-01-02"]}]},"invoice":{"by":"ID","input":"string"},"paging":{"from":1,"limit":1},"sort":{"account":{"direction":"ASC","priority":1},"amount":{"direction":"ASC","priority":1},"endDate":{"direction":"ASC","priority":1},"startDate":{"direction":"ASC","priority":1}}},"invoiceChargeItemListInput":{"filter":{"account":[{"accountInclusion":"ALL_ACCOUNTS","in":["id1","id2"]}],"endDate":[{"between":["2026-01-02"],"eq":"2026-01-02","gt":"2026-01-02","gte":"2026-01-02","in":["2026-01-02"],"lt":"2026-01-02","lte":"2026-01-02","neq":"2026-01-02","nin":["2026-01-02"]}],"freeText":[{"search":"string"}],"startDate":[{"between":["2026-01-02"],"eq":"2026-01-02","gt":"2026-01-02","gte":"2026-01-02","in":["2026-01-02"],"lt":"2026-01-02","lte":"2026-01-02","neq":"2026-01-02","nin":["2026-01-02"]}]},"invoice":{"by":"ID","input":"string"},"paging":{"from":1,"limit":1},"sort":{"account":{"direction":"ASC","priority":1},"amount":{"direction":"ASC","priority":1},"description":{"direction":"ASC","priority":1},"endDate":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1},"quantity":{"direction":"ASC","priority":1},"startDate":{"direction":"ASC","priority":1}}},"invoiceSummaryListInput":{"filter":{"account":[{"accountInclusion":"ALL_ACCOUNTS","in":["id1","id2"]}],"dueDate":[{"between":["2026-01-02"],"eq":"2026-01-02","gt":"2026-01-02","gte":"2026-01-02","in":["2026-01-02"],"lt":"2026-01-02","lte":"2026-01-02","neq":"2026-01-02","nin":["2026-01-02"]}],"freeText":[{"search":"string"}],"id":[{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]}],"issuedDate":[{"between":["2026-01-02"],"eq":"2026-01-02","gt":"2026-01-02","gte":"2026-01-02","in":["2026-01-02"],"lt":"2026-01-02","lte":"2026-01-02","neq":"2026-01-02","nin":["2026-01-02"]}],"total":[{"between":[1,2],"eq":1,"gt":1,"gte":1,"in":[1,2],"lt":1,"lte":1,"neq":1,"nin":[1,2]}]},"paging":{"from":1,"limit":1},"sort":{"dueDate":{"direction":"ASC","priority":1},"issuedDate":{"direction":"ASC","priority":1},"total":{"direction":"ASC","priority":1}}}}'

catocli query financialDocuments '{
    "invoiceAccountListInput": {
        "filter": {
            "account": [
                {
                    "accountInclusion": "ALL_ACCOUNTS",
                    "in": [
                        "id1",
                        "id2"
                    ]
                }
            ],
            "chargeItem": [
                {
                    "search": "string"
                }
            ],
            "endDate": [
                {
                    "between": [
                        "2026-01-02"
                    ],
                    "eq": "2026-01-02",
                    "gt": "2026-01-02",
                    "gte": "2026-01-02",
                    "in": [
                        "2026-01-02"
                    ],
                    "lt": "2026-01-02",
                    "lte": "2026-01-02",
                    "neq": "2026-01-02",
                    "nin": [
                        "2026-01-02"
                    ]
                }
            ],
            "startDate": [
                {
                    "between": [
                        "2026-01-02"
                    ],
                    "eq": "2026-01-02",
                    "gt": "2026-01-02",
                    "gte": "2026-01-02",
                    "in": [
                        "2026-01-02"
                    ],
                    "lt": "2026-01-02",
                    "lte": "2026-01-02",
                    "neq": "2026-01-02",
                    "nin": [
                        "2026-01-02"
                    ]
                }
            ]
        },
        "invoice": {
            "by": "ID",
            "input": "string"
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "account": {
                "direction": "ASC",
                "priority": 1
            },
            "amount": {
                "direction": "ASC",
                "priority": 1
            },
            "endDate": {
                "direction": "ASC",
                "priority": 1
            },
            "startDate": {
                "direction": "ASC",
                "priority": 1
            }
        }
    },
    "invoiceChargeItemListInput": {
        "filter": {
            "account": [
                {
                    "accountInclusion": "ALL_ACCOUNTS",
                    "in": [
                        "id1",
                        "id2"
                    ]
                }
            ],
            "endDate": [
                {
                    "between": [
                        "2026-01-02"
                    ],
                    "eq": "2026-01-02",
                    "gt": "2026-01-02",
                    "gte": "2026-01-02",
                    "in": [
                        "2026-01-02"
                    ],
                    "lt": "2026-01-02",
                    "lte": "2026-01-02",
                    "neq": "2026-01-02",
                    "nin": [
                        "2026-01-02"
                    ]
                }
            ],
            "freeText": [
                {
                    "search": "string"
                }
            ],
            "startDate": [
                {
                    "between": [
                        "2026-01-02"
                    ],
                    "eq": "2026-01-02",
                    "gt": "2026-01-02",
                    "gte": "2026-01-02",
                    "in": [
                        "2026-01-02"
                    ],
                    "lt": "2026-01-02",
                    "lte": "2026-01-02",
                    "neq": "2026-01-02",
                    "nin": [
                        "2026-01-02"
                    ]
                }
            ]
        },
        "invoice": {
            "by": "ID",
            "input": "string"
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "account": {
                "direction": "ASC",
                "priority": 1
            },
            "amount": {
                "direction": "ASC",
                "priority": 1
            },
            "description": {
                "direction": "ASC",
                "priority": 1
            },
            "endDate": {
                "direction": "ASC",
                "priority": 1
            },
            "name": {
                "direction": "ASC",
                "priority": 1
            },
            "quantity": {
                "direction": "ASC",
                "priority": 1
            },
            "startDate": {
                "direction": "ASC",
                "priority": 1
            }
        }
    },
    "invoiceSummaryListInput": {
        "filter": {
            "account": [
                {
                    "accountInclusion": "ALL_ACCOUNTS",
                    "in": [
                        "id1",
                        "id2"
                    ]
                }
            ],
            "dueDate": [
                {
                    "between": [
                        "2026-01-02"
                    ],
                    "eq": "2026-01-02",
                    "gt": "2026-01-02",
                    "gte": "2026-01-02",
                    "in": [
                        "2026-01-02"
                    ],
                    "lt": "2026-01-02",
                    "lte": "2026-01-02",
                    "neq": "2026-01-02",
                    "nin": [
                        "2026-01-02"
                    ]
                }
            ],
            "freeText": [
                {
                    "search": "string"
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
            "issuedDate": [
                {
                    "between": [
                        "2026-01-02"
                    ],
                    "eq": "2026-01-02",
                    "gt": "2026-01-02",
                    "gte": "2026-01-02",
                    "in": [
                        "2026-01-02"
                    ],
                    "lt": "2026-01-02",
                    "lte": "2026-01-02",
                    "neq": "2026-01-02",
                    "nin": [
                        "2026-01-02"
                    ]
                }
            ],
            "total": [
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
            ]
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "dueDate": {
                "direction": "ASC",
                "priority": 1
            },
            "issuedDate": {
                "direction": "ASC",
                "priority": 1
            },
            "total": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.financialDocuments ####

`accountId` [ID] - (required) N/A
`invoiceAccountListInput` [InvoiceAccountListInput] - (required) N/A
`invoiceChargeItemListInput` [InvoiceChargeItemListInput] - (required) N/A
`invoiceSummaryListInput` [InvoiceSummaryListInput] - (required) N/A
