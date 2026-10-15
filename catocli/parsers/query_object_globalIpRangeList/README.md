
## CATO-CLI - query.object.globalIpRangeList:
[Click here](https://api.catonetworks.com/documentation/#query-query.object.globalIpRangeList) for documentation on this operation.

### Usage for query.object.globalIpRangeList:

```bash
catocli query object globalIpRangeList -h

catocli query object globalIpRangeList <json>

catocli query object globalIpRangeList --json-file query.object.globalIpRangeList.json

catocli query object globalIpRangeList '{"globalIpRangeListInput":{"filter":{"description":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"ipRange":{"containedIn":"192.0.2.10-192.0.2.20"},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}}}}'

catocli query object globalIpRangeList '{
    "globalIpRangeListInput": {
        "filter": {
            "description": {
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
            "ipRange": {
                "containedIn": "192.0.2.10-192.0.2.20"
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
    }
}'
```

#### Operation Arguments for query.object.globalIpRangeList ####

`accountId` [ID] - (required) N/A
`globalIpRangeListInput` [GlobalIpRangeListInput] - (required) N/A
