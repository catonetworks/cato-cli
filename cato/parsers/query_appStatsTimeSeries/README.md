
## CATO-CLI - query.appStatsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-appStatsTimeSeries) for documentation on this operation.

### Usage for query.appStatsTimeSeries:

`cato query appStatsTimeSeries -h`

`cato query appStatsTimeSeries <accountID> <json>`

`cato query appStatsTimeSeries 12345 "$(cat < appStatsTimeSeries.json)"`

`cato query appStatsTimeSeries 12345 '{"AppStatsFilter": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}, "operator": {"operator": "enum(FilterOperator)"}, "values": {"values": ["String"]}}, "Dimension": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}}, "Measure": {"aggType": {"aggType": "enum(AggregationType)"}, "fieldName": {"fieldName": "enum(AppStatsFieldName)"}, "trend": {"trend": "Boolean"}}, "buckets": "Int", "perSecond": "Boolean", "timeFrame": "TimeFrame", "withMissingData": "Boolean"}'`

#### Operation Arguments for query.appStatsTimeSeries ####
`AppStatsFilter` [AppStatsFilter[]] - (optional) N/A 
`Dimension` [Dimension[]] - (optional) N/A 
`Measure` [Measure[]] - (optional) N/A 
`accountID` [ID] - (required) Account ID 
`buckets` [Int] - (required) N/A 
`perSecond` [Boolean] - (optional) whether to normalize the data into per second (i.e. divide by granularity) 
`timeFrame` [TimeFrame] - (required) N/A 
`withMissingData` [Boolean] - (optional) If false, the data field will be set to '0' for buckets with no reported data. Otherwise it will be set to -1 
