
## CATO-CLI - query.eventsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-query.eventsTimeSeries) for documentation on this operation.

### Usage for query.eventsTimeSeries:

`catocli query eventsTimeSeries -h`

`catocli query eventsTimeSeries <json>`

`catocli query eventsTimeSeries "$(cat < query.eventsTimeSeries.json)"`

`catocli query eventsTimeSeries '{"buckets":1,"eventsDimension":{"fieldName":"access_method"},"eventsFilter":{"fieldName":"access_method","operator":"is","values":["string1","string2"]},"eventsMeasure":{"aggType":"sum","fieldName":"access_method","trend":true},"perSecond":true,"timeFrame":"example_value","useDefaultSizeBucket":true,"withMissingData":true}'`

`catocli query eventsTimeSeries -p '{
    "buckets": 1,
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
    "perSecond": true,
    "timeFrame": "example_value",
    "useDefaultSizeBucket": true,
    "withMissingData": true
}'`


#### Operation Arguments for query.eventsTimeSeries ####

`accountID` [ID] - (required) Account ID    
`buckets` [Int] - (required) N/A    
`eventsDimension` [EventsDimension[]] - (required) N/A    
`eventsFilter` [EventsFilter[]] - (required) N/A    
`eventsMeasure` [EventsMeasure[]] - (required) N/A    
`perSecond` [Boolean] - (required) whether to normalize the data into per second (i.e. divide by granularity)    
`timeFrame` [TimeFrame] - (required) N/A    
`useDefaultSizeBucket` [Boolean] - (required) In case we want to have the default size bucket (from properties)    
`withMissingData` [Boolean] - (required) If false, the data field will be set to '0' for buckets with no reported data. Otherwise it will be set to -1    
