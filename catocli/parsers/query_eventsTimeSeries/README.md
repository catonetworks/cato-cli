
## CATO-CLI - query.eventsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-query.eventsTimeSeries) for documentation on this operation.

### Usage for query.eventsTimeSeries:

```bash
catocli query eventsTimeSeries -h

catocli query eventsTimeSeries <json>

catocli query eventsTimeSeries "$(cat < query.eventsTimeSeries.json)"

catocli query eventsTimeSeries '{"buckets":1,"eventsDimension":{"fieldName":"access_method"},"eventsFilter":{"fieldName":"access_method","operator":"is","values":["string1","string2"]},"eventsMeasure":{"aggType":"sum","fieldName":"access_method","trend":true},"perSecond":true,"timeFrame":"example_value","useDefaultSizeBucket":true,"withMissingData":true}'

catocli query eventsTimeSeries '{
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
}'
```


#### TimeFrame Parameter Examples

The `timeFrame` parameter supports both relative time ranges and absolute date ranges:

**Relative Time Ranges:**
- `"last.PT5M"` = Previous 5 minutes
- `"last.PT1H"` = Previous 1 hour  
- `"last.P1D"` = Previous 1 day
- `"last.P14D"` = Previous 14 days
- `"last.P1M"` = Previous 1 month

**Absolute Date Ranges:**
Format: `"utc.YYYY-MM-{DD/HH:MM:SS--DD/HH:MM:SS}"`

- Single day: `"utc.2023-02-{28/00:00:00--28/23:59:59}"`
- Multiple days: `"utc.2023-02-{25/00:00:00--28/23:59:59}"`  
- Specific hours: `"utc.2023-02-{28/09:00:00--28/17:00:00}"`
- Across months: `"utc.2023-{01-28/00:00:00--02-03/23:59:59}"`


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
