
## CATO-CLI - query.xdr.stories:
[Click here](https://api.catonetworks.com/documentation/#query-query.xdr.stories) for documentation on this operation.

### Usage for query.xdr.stories:

```bash
catocli query xdr stories -h

catocli query xdr stories <json>

catocli query xdr stories "$(cat < query.xdr.stories.json)"

catocli query xdr stories '{"storyInput":{"filter":{"accountId":{"in":["id1","id2"],"not_in":["id1","id2"]},"criticality":{"eq":1,"gt":1,"gte":1,"in":[1,2],"lt":1,"lte":1,"not_in":[1,2]},"engineType":{"in":"ANOMALY","not_in":"ANOMALY"},"incidentId":{"contains":"string","in":["string1","string2"],"not_in":["string1","string2"]},"ioa":{"contains":"string","in":["string1","string2"],"not_in":["string1","string2"]},"muted":{"is":"string"},"producer":{"in":"AnomalyStats","not_in":"AnomalyStats"},"queryName":{"contains":"string","in":["string1","string2"],"not_in":["string1","string2"]},"severity":{"in":"High","not_in":"High"},"source":{"contains":"string","in":["string1","string2"],"not_in":["string1","string2"]},"sourceIp":{"contains":"string","in":["string1","string2"],"not_in":["string1","string2"]},"status":{"in":"Open","not_in":"Open"},"storyId":{"in":["id1","id2"],"not_in":["id1","id2"]},"timeFrame":{"time":"example_value","timeFrameModifier":"StoryUpdate"},"vendor":{"in":"CATO","not_in":"CATO"},"verdict":{"in":"Suspicious","not_in":"Suspicious"}},"paging":{"from":1,"limit":1},"storySortInput":{"fieldName":"firstSignal","order":"asc"}}}'

catocli query xdr stories '{
    "storyInput": {
        "filter": {
            "accountId": {
                "in": [
                    "id1",
                    "id2"
                ],
                "not_in": [
                    "id1",
                    "id2"
                ]
            },
            "criticality": {
                "eq": 1,
                "gt": 1,
                "gte": 1,
                "in": [
                    1,
                    2
                ],
                "lt": 1,
                "lte": 1,
                "not_in": [
                    1,
                    2
                ]
            },
            "engineType": {
                "in": "ANOMALY",
                "not_in": "ANOMALY"
            },
            "incidentId": {
                "contains": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "not_in": [
                    "string1",
                    "string2"
                ]
            },
            "ioa": {
                "contains": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "not_in": [
                    "string1",
                    "string2"
                ]
            },
            "muted": {
                "is": "string"
            },
            "producer": {
                "in": "AnomalyStats",
                "not_in": "AnomalyStats"
            },
            "queryName": {
                "contains": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "not_in": [
                    "string1",
                    "string2"
                ]
            },
            "severity": {
                "in": "High",
                "not_in": "High"
            },
            "source": {
                "contains": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "not_in": [
                    "string1",
                    "string2"
                ]
            },
            "sourceIp": {
                "contains": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "not_in": [
                    "string1",
                    "string2"
                ]
            },
            "status": {
                "in": "Open",
                "not_in": "Open"
            },
            "storyId": {
                "in": [
                    "id1",
                    "id2"
                ],
                "not_in": [
                    "id1",
                    "id2"
                ]
            },
            "timeFrame": {
                "time": "example_value",
                "timeFrameModifier": "StoryUpdate"
            },
            "vendor": {
                "in": "CATO",
                "not_in": "CATO"
            },
            "verdict": {
                "in": "Suspicious",
                "not_in": "Suspicious"
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "storySortInput": {
            "fieldName": "firstSignal",
            "order": "asc"
        }
    }
}'
```

## Advanced Usage
### Additional Examples
- XDR query with minimum fields
- Example with minimum required fields

# XDR query with minimum fields

```bash
# Example with minimum required fields
catocli query xdr stories '{
    "storyInput": {
        "filter": [
            {
                "timeFrame": {
                    "time": "last.P1M"
                }
            }
        ],
        "paging": {
            "from": 0,
            "limit": 100
        }
    }
}'
```


#### Operation Arguments for query.xdr.stories ####

`accountID` [ID] - (required) N/A    
`storyInput` [StoryInput] - (required) N/A    
