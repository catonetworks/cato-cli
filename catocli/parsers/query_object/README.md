
## CATO-CLI - query.object:
[Click here](https://api.catonetworks.com/documentation/#query-query.object) for documentation on this operation.

### Usage for query.object:

```bash
catocli query object -h

catocli query object <json>

catocli query object --json-file query.object.json

catocli query object '{"globalIpRangeListInput":{"globalIpRangeListFilterInput":{"description":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"ipRange":{"containedIn":"example_value"},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}}},"globalIpRangeRefInput":{"by":"ID","input":"string"}}'

catocli query object '{
    "globalIpRangeListInput": {
        "globalIpRangeListFilterInput": {
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
                "containedIn": "example_value"
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
    "globalIpRangeRefInput": {
        "by": "ID",
        "input": "string"
    }
}'
```

#### Operation Arguments for query.object ####

`accountId` [ID] - (required) N/A    
`globalIpRangeListInput` [GlobalIpRangeListInput] - (required) N/A    
`globalIpRangeRefInput` [GlobalIpRangeRefInput] - (required) N/A    
