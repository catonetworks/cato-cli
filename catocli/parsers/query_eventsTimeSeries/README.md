
## CATO-CLI - query.eventsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-eventsTimeSeries) for documentation on this operation.

### Usage for query.eventsTimeSeries:

`catocli query eventsTimeSeries -h`

`catocli query eventsTimeSeries <json>`

`catocli query eventsTimeSeries "$(cat < eventsTimeSeries.json)"`

`catocli query eventsTimeSeries '{"buckets": "Int", "eventsDimension": {"fieldName": {"fieldName": "enum(EventFieldName)"}}, "eventsFilter": {"fieldName": {"fieldName": "enum(EventFieldName)"}, "operator": {"operator": "enum(FilterOperator)"}, "values": {"values": ["String"]}}, "eventsMeasure": {"aggType": {"aggType": "enum(AggregationType)"}, "fieldName": {"fieldName": "enum(EventFieldName)"}, "trend": {"trend": "Boolean"}}, "perSecond": "Boolean", "timeFrame": "TimeFrame", "withMissingData": "Boolean"}'`

#### Operation Arguments for query.eventsTimeSeries ####
`accountID` [ID] - (required) Account ID 
`buckets` [Int] - (required) N/A 
`eventsDimension` [EventsDimension[]] - (optional) N/A 
`eventsFilter` [EventsFilter[]] - (optional) N/A 
`eventsMeasure` [EventsMeasure[]] - (optional) N/A 
`perSecond` [Boolean] - (optional) whether to normalize the data into per second (i.e. divide by granularity) 
`timeFrame` [TimeFrame] - (required) N/A 
`withMissingData` [Boolean] - (optional) If false, the data field will be set to '0' for buckets with no reported data. Otherwise it will be set to -1 
