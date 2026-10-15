
## CATO-CLI - query.popLocations.allocatedIpList:
[Click here](https://api.catonetworks.com/documentation/#query-query.popLocations.allocatedIpList) for documentation on this operation.

### Usage for query.popLocations.allocatedIpList:

```bash
catocli query popLocations allocatedIpList -h

catocli query popLocations allocatedIpList <json>

catocli query popLocations allocatedIpList --json-file query.popLocations.allocatedIpList.json

catocli query popLocations allocatedIpList '{"popLocationAllocatedIpInput":{"filter":{"account":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"allocatedIp":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"allocationType":{"eq":"SYSTEM","in":["SYSTEM"],"neq":"SYSTEM","nin":["SYSTEM"]},"description":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"global":{"search":"string"},"id":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"popLocation":{"eq":{"by":"ID","input":"string"},"in":[{"by":"ID","input":"string"}],"neq":{"by":"ID","input":"string"},"nin":[{"by":"ID","input":"string"}]},"subnet":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}}}}'

catocli query popLocations allocatedIpList '{
    "popLocationAllocatedIpInput": {
        "filter": {
            "account": {
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
            "allocatedIp": {
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
            "allocationType": {
                "eq": "SYSTEM",
                "in": [
                    "SYSTEM"
                ],
                "neq": "SYSTEM",
                "nin": [
                    "SYSTEM"
                ]
            },
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
            "global": {
                "search": "string"
            },
            "id": {
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
            "popLocation": {
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
        }
    }
}'
```

#### Operation Arguments for query.popLocations.allocatedIpList ####

`accountId` [ID] - (required) N/A
`popLocationAllocatedIpInput` [PopLocationAllocatedIpInput] - (required) N/A
