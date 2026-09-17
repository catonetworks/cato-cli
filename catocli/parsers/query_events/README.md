
## CATO-CLI - query.events:
[Click here](https://api.catonetworks.com/documentation/#query-query.events) for documentation on this operation.

### Usage for query.events:

```bash
catocli query events -h

catocli query events <json>

catocli query events --json-file query.events.json

catocli query events '{"eventsDimension":{"fieldName":"access_method"},"eventsFilter":{"fieldName":"access_method","operator":"is","values":["string1","string2"]},"eventsMeasure":{"aggType":"sum","alias":"string","fieldName":"access_method","trend":true},"eventsPostAggFilter":{"aggType":"sum","filter":{"fieldName":"access_method","operator":"is","values":["string1","string2"]}},"eventsSort":{"alias":"string","fieldName":"access_method","order":"asc"},"from":1,"includeEmptyDimension":true,"limit":1,"timeFrame":"example_value"}'

catocli query events '{
    "eventsDimension": {
        "fieldName": "access_method"
    },
    "eventsFilter": {
        "fieldName": "access_method",
        "operator": "is",
        "values": [
            "string1",
            "string2"
        ]
    },
    "eventsMeasure": {
        "aggType": "sum",
        "alias": "string",
        "fieldName": "access_method",
        "trend": true
    },
    "eventsPostAggFilter": {
        "aggType": "sum",
        "filter": {
            "fieldName": "access_method",
            "operator": "is",
            "values": [
                "string1",
                "string2"
            ]
        }
    },
    "eventsSort": {
        "alias": "string",
        "fieldName": "access_method",
        "order": "asc"
    },
    "from": 1,
    "includeEmptyDimension": true,
    "limit": 1,
    "timeFrame": "example_value"
}'
```

#### Operation Arguments for query.events ####

