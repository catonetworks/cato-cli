
## CATO-CLI - query.hardware:
[Click here](https://api.catonetworks.com/documentation/#query-query.hardware) for documentation on this operation.

### Usage for query.hardware:

```bash
catocli query hardware -h

catocli query hardware <json>

catocli query hardware --json-file query.hardware.json

catocli query hardware '{"hardwareSearchInput":{"filter":{"account":{"accountInclusion":"ALL_ACCOUNTS","in":["id1","id2"]},"countryCode":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"countryName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"freeText":{"search":"string"},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"licenseStartDate":{"between":["example1","example2"],"eq":"example_value","gt":"example_value","gte":"example_value","in":["example1","example2"],"lt":"example_value","lte":"example_value","neq":"example_value","nin":["example1","example2"]},"orderType":{"eq":"PURCHASE","in":"PURCHASE"},"product":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"serialNumber":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"shippingStatus":{"eq":"PENDING_INFO","in":"PENDING_INFO","neq":"PENDING_INFO","nin":"PENDING_INFO"},"validAddress":{"eq":true,"neq":true}},"paging":{"from":1,"limit":1},"sort":{"country":{"direction":"ASC","priority":1},"incoterms":{"direction":"ASC","priority":1},"licenseId":{"direction":"ASC","priority":1},"licenseStartDate":{"direction":"ASC","priority":1},"productType":{"direction":"ASC","priority":1},"quoteId":{"direction":"ASC","priority":1},"serialNumber":{"direction":"ASC","priority":1},"shippingDate":{"direction":"ASC","priority":1},"shippingStatus":{"direction":"ASC","priority":1},"siteName":{"direction":"ASC","priority":1}}}}'

catocli query hardware '{
    "hardwareSearchInput": {
        "filter": {
            "account": {
                "accountInclusion": "ALL_ACCOUNTS",
                "in": [
                    "id1",
                    "id2"
                ]
            },
            "countryCode": {
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
            "freeText": {
                "search": "string"
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
            "licenseStartDate": {
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
            "orderType": {
                "eq": "PURCHASE",
                "in": "PURCHASE"
            },
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
            },
            "shippingStatus": {
                "eq": "PENDING_INFO",
                "in": "PENDING_INFO",
                "neq": "PENDING_INFO",
                "nin": "PENDING_INFO"
            },
            "validAddress": {
                "eq": true,
                "neq": true
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "country": {
                "direction": "ASC",
                "priority": 1
            },
            "incoterms": {
                "direction": "ASC",
                "priority": 1
            },
            "licenseId": {
                "direction": "ASC",
                "priority": 1
            },
            "licenseStartDate": {
                "direction": "ASC",
                "priority": 1
            },
            "productType": {
                "direction": "ASC",
                "priority": 1
            },
            "quoteId": {
                "direction": "ASC",
                "priority": 1
            },
            "serialNumber": {
                "direction": "ASC",
                "priority": 1
            },
            "shippingDate": {
                "direction": "ASC",
                "priority": 1
            },
            "shippingStatus": {
                "direction": "ASC",
                "priority": 1
            },
            "siteName": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.hardware ####

`accountId` [ID] - (required) N/A    
`hardwareSearchInput` [HardwareSearchInput] - (required) N/A    
