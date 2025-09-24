
## CATO-CLI - query.events:
[Click here](https://api.catonetworks.com/documentation/#query-query.events) for documentation on this operation.

### Usage for query.events:

`catocli query events -h`

`catocli query events <json>`

`catocli query events "$(cat < query.events.json)"`

`catocli query events '{"eventsDimension":{"fieldName":"access_method"},"eventsFilter":{"fieldName":"access_method","operator":"is","values":["string1","string2"]},"eventsMeasure":{"aggType":"sum","fieldName":"access_method","trend":true},"eventsSort":{"fieldName":"access_method","order":"asc"},"from":1,"limit":1,"timeFrame":"example_value"}'`

`catocli query events -p '{
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
    "eventsSort": {
        "fieldName": "access_method",
        "order": "asc"
    },
    "from": 1,
    "limit": 1,
    "timeFrame": "example_value"
}'`


#### Operation Arguments for query.events ####

`accountID` [ID] - (required) Account ID    
`eventsDimension` [EventsDimension[]] - (required) N/A    
`eventsFilter` [EventsFilter[]] - (required) N/A    
`eventsMeasure` [EventsMeasure[]] - (required) N/A    
`eventsSort` [EventsSort[]] - (required) N/A    
`from` [Int] - (required) N/A    
`limit` [Int] - (required) N/A    
`timeFrame` [TimeFrame] - (required) N/A    
