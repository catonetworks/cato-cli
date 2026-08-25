
## CATO-CLI - query.ztnaAppConnector.ztnaAppConnectorList:
[Click here](https://api.catonetworks.com/documentation/#query-query.ztnaAppConnector.ztnaAppConnectorList) for documentation on this operation.

### Usage for query.ztnaAppConnector.ztnaAppConnectorList:

```bash
catocli query ztnaAppConnector ztnaAppConnectorList -h

catocli query ztnaAppConnector ztnaAppConnectorList <json>

catocli query ztnaAppConnector ztnaAppConnectorList --json-file query.ztnaAppConnector.ztnaAppConnectorList.json

catocli query ztnaAppConnector ztnaAppConnectorList '{"ztnaAppConnectorListInput":{"pagingInput":{"from":1,"limit":1},"ztnaAppConnectorListFilterInput":{"countryCode":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"countryName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"freeText":{"search":"string"},"groupName":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"isAssigned":{"eq":true,"neq":true},"model":{"eq":"X1500","in":"X1500","neq":"X1500","nin":"X1500"},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"privateApp":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"searchGroupName":{"search":"string"},"searchName":{"search":"string"},"serialNumber":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"type":{"eq":"VIRTUAL","in":"VIRTUAL","neq":"VIRTUAL","nin":"VIRTUAL"}},"ztnaAppConnectorListSortInput":{"createdAt":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}}}}'

catocli query ztnaAppConnector ztnaAppConnectorList '{
    "ztnaAppConnectorListInput": {
        "pagingInput": {
            "from": 1,
            "limit": 1
        },
        "ztnaAppConnectorListFilterInput": {
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
            "isAssigned": {
                "eq": true,
                "neq": true
            },
            "model": {
                "eq": "X1500",
                "in": "X1500",
                "neq": "X1500",
                "nin": "X1500"
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
            "searchGroupName": {
                "search": "string"
            },
            "searchName": {
                "search": "string"
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
            "type": {
                "eq": "VIRTUAL",
                "in": "VIRTUAL",
                "neq": "VIRTUAL",
                "nin": "VIRTUAL"
            }
        },
        "ztnaAppConnectorListSortInput": {
            "createdAt": {
                "direction": "ASC",
                "priority": 1
            },
            "name": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.ztnaAppConnector.ztnaAppConnectorList ####

`accountId` [ID] - (required) N/A    
`ztnaAppConnectorListInput` [ZtnaAppConnectorListInput] - (required) N/A    
