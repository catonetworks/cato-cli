
## CATO-CLI - query.eventsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-query.eventsTimeSeries) for documentation on this operation.

### Usage for query.eventsTimeSeries:

```bash
catocli query eventsTimeSeries -h

catocli query eventsTimeSeries <json>

catocli query eventsTimeSeries "$(cat < query.eventsTimeSeries.json)"

catocli query eventsTimeSeries '{"eventsDimension":{"fieldName":"access_method"},"eventsFilter":{"fieldName":"access_method","operator":"is","values":["string1","string2"]},"eventsMeasure":{"aggType":"sum","fieldName":"access_method","trend":true},"timeFrame":"example_value"}'

catocli query eventsTimeSeries -p '{
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
        "fieldName": "access_method",
        "trend": true
    },
    "timeFrame": "example_value"
}'
```

#### Operation Arguments for query.eventsTimeSeries ####

`accountID` [ID] - (required) Account ID    
`eventsDimension` [EventsDimension[]] - (required) N/A    
`eventsFilter` [EventsFilter[]] - (required) N/A    
`eventsMeasure` [EventsMeasure[]] - (required) N/A    
`timeFrame` [TimeFrame] - (required) N/A    
