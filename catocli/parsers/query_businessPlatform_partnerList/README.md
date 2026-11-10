
## CATO-CLI - query.businessPlatform.partnerList:
[Click here](https://api.catonetworks.com/documentation/#query-query.businessPlatform.partnerList) for documentation on this operation.

### Usage for query.businessPlatform.partnerList:

```bash
catocli query businessPlatform partnerList -h

catocli query businessPlatform partnerList <json>

catocli query businessPlatform partnerList --json-file query.businessPlatform.partnerList.json

catocli query businessPlatform partnerList '{"businessPlatformPartnerListInput":{"filter":{"account":{"accountInclusion":"ALL_ACCOUNTS","in":["id1","id2"]},"freeText":{"search":"string"}},"paging":{"from":1,"limit":1},"sort":{"account":{"direction":"ASC","priority":1},"createdAt":{"direction":"ASC","priority":1},"createdBy":{"direction":"ASC","priority":1},"name":{"direction":"ASC","priority":1}}}}'

catocli query businessPlatform partnerList '{
    "businessPlatformPartnerListInput": {
        "filter": {
            "account": {
                "accountInclusion": "ALL_ACCOUNTS",
                "in": [
                    "id1",
                    "id2"
                ]
            },
            "freeText": {
                "search": "string"
            }
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
            "createdAt": {
                "direction": "ASC",
                "priority": 1
            },
            "createdBy": {
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

#### Operation Arguments for query.businessPlatform.partnerList ####

`accountId` [ID] - (required) N/A
`businessPlatformPartnerListInput` [BusinessPlatformPartnerListInput] - (required) N/A
