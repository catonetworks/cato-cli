
## CATO-CLI - query.popLocations.popLocationList:
[Click here](https://api.catonetworks.com/documentation/#query-query.popLocations.popLocationList) for documentation on this operation.

### Usage for query.popLocations.popLocationList:

```bash
catocli query popLocations popLocationList -h

catocli query popLocations popLocationList <json>

catocli query popLocations popLocationList --json-file query.popLocations.popLocationList.json

catocli query popLocations popLocationList '{"popLocationFilterInput":{"country":{"eq":{"by":"ID","input":"string"},"in":[{"by":"ID","input":"string"}],"neq":{"by":"ID","input":"string"},"nin":[{"by":"ID","input":"string"}]},"id":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"interconnectTagging":{"taggingMethod":{"eq":"DOT1Q","in":["DOT1Q"],"neq":"DOT1Q","nin":["DOT1Q"]}},"isPrivate":{"eq":true,"neq":true},"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]},"primary":{"eq":true,"neq":true},"siteLicenseRegion":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}}}'

catocli query popLocations popLocationList '{
    "popLocationFilterInput": {
        "country": {
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
        "interconnectTagging": {
            "taggingMethod": {
                "eq": "DOT1Q",
                "in": [
                    "DOT1Q"
                ],
                "neq": "DOT1Q",
                "nin": [
                    "DOT1Q"
                ]
            }
        },
        "isPrivate": {
            "eq": true,
            "neq": true
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
        "primary": {
            "eq": true,
            "neq": true
        },
        "siteLicenseRegion": {
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
}'
```

#### Operation Arguments for query.popLocations.popLocationList ####

`accountId` [ID] - (required) N/A
`popLocationFilterInput` [PopLocationFilterInput] - (required) N/A
