
## CATO-CLI - query.enterpriseDirectory:
[Click here](https://api.catonetworks.com/documentation/#query-query.enterpriseDirectory) for documentation on this operation.

### Usage for query.enterpriseDirectory:

`catocli query enterpriseDirectory -h`

`catocli query enterpriseDirectory <json>`

`catocli query enterpriseDirectory "$(cat < query.enterpriseDirectory.json)"`

`catocli query enterpriseDirectory '{"enterpriseDirectoryLocationListInput":{"locationFilterInput":{"account":{"accountInclusion":"ALL_ACCOUNTS","in":["id1","id2"]},"countryCode":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"freeText":{"search":"string"},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"includeArchived":true,"isShippingLocation":true,"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"type":{"eq":"BRANCH","in":"BRANCH","neq":"BRANCH","nin":"BRANCH"}},"locationSortInput":{"country":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1},"type":{"direction":"ASC","priority":1}},"pagingInput":{"from":1,"limit":1}}}'`

`catocli query enterpriseDirectory -p '{
    "enterpriseDirectoryLocationListInput": {
        "locationFilterInput": {
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
            "includeArchived": true,
            "isShippingLocation": true,
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
            "type": {
                "eq": "BRANCH",
                "in": "BRANCH",
                "neq": "BRANCH",
                "nin": "BRANCH"
            }
        },
        "locationSortInput": {
            "country": {
                "direction": "ASC",
                "priority": 1
            },
            "name": {
                "direction": "ASC",
                "priority": 1
            },
            "type": {
                "direction": "ASC",
                "priority": 1
            }
        },
        "pagingInput": {
            "from": 1,
            "limit": 1
        }
    }
}'`


#### Operation Arguments for query.enterpriseDirectory ####

`accountId` [ID] - (required) N/A    
`enterpriseDirectoryLocationListInput` [EnterpriseDirectoryLocationListInput] - (required) N/A    
