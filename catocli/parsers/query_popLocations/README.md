
## CATO-CLI - query.popLocations:
[Click here](https://api.catonetworks.com/documentation/#query-query.popLocations) for documentation on this operation.

### Usage for query.popLocations:

`catocli query popLocations -h`

`catocli query popLocations <json>`

`catocli query popLocations "$(cat < query.popLocations.json)"`

`catocli query popLocations '{"popLocationFilterInput":{"booleanFilterInput":{"eq":true,"neq":true},"countryRefFilterInput":{"eq":{"by":"ID","input":"string"},"in":{"by":"ID","input":"string"},"neq":{"by":"ID","input":"string"},"nin":{"by":"ID","input":"string"}},"idFilterInput":{"eq":"id","in":["id1","id2"],"neq":"id","nin":["id1","id2"]},"popLocationCloudInterconnectFilterInput":{"taggingMethod":{"eq":"DOT1Q","in":"DOT1Q","neq":"DOT1Q","nin":"DOT1Q"}},"stringFilterInput":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"]}}}'`

`catocli query popLocations -p '{
    "popLocationFilterInput": {
        "booleanFilterInput": {
            "eq": true,
            "neq": true
        },
        "countryRefFilterInput": {
            "eq": {
                "by": "ID",
                "input": "string"
            },
            "in": {
                "by": "ID",
                "input": "string"
            },
            "neq": {
                "by": "ID",
                "input": "string"
            },
            "nin": {
                "by": "ID",
                "input": "string"
            }
        },
        "idFilterInput": {
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
        "popLocationCloudInterconnectFilterInput": {
            "taggingMethod": {
                "eq": "DOT1Q",
                "in": "DOT1Q",
                "neq": "DOT1Q",
                "nin": "DOT1Q"
            }
        },
        "stringFilterInput": {
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
}'`


#### Operation Arguments for query.popLocations ####

`accountId` [ID] - (required) N/A    
`popLocationFilterInput` [PopLocationFilterInput] - (required) N/A    
