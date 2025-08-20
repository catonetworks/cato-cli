
## CATO-CLI - query.socketPortMetricsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-socketPortMetricsTimeSeries) for documentation on this operation.

### Usage for query.socketPortMetricsTimeSeries:

`catocli query socketPortMetricsTimeSeries -h`

`catocli query socketPortMetricsTimeSeries <json>`

`catocli query socketPortMetricsTimeSeries "$(cat < socketPortMetricsTimeSeries.json)"`

`catocli query socketPortMetricsTimeSeries '{"buckets": "Int", "perSecond": "Boolean", "socketPortMetricsDimension": {"fieldName": {"fieldName": "enum(SocketPortMetricsFieldName)"}}, "socketPortMetricsFilter": {"fieldName": {"fieldName": "enum(SocketPortMetricsFieldName)"}, "operator": {"operator": "enum(FilterOperator)"}, "values": {"values": ["String"]}}, "socketPortMetricsMeasure": {"aggType": {"aggType": "enum(AggregationType)"}, "fieldName": {"fieldName": "enum(SocketPortMetricsFieldName)"}, "trend": {"trend": "Boolean"}}, "timeFrame": "TimeFrame", "useDefaultSizeBucket": "Boolean", "withMissingData": "Boolean"}'`

#### Operation Arguments for query.socketPortMetricsTimeSeries ####
`accountID` [ID] - (required) Account ID 
`buckets` [Int] - (required) N/A 
`perSecond` [Boolean] - (optional) whether to normalize the data into per second (i.e. divide by granularity) 
`socketPortMetricsDimension` [SocketPortMetricsDimension[]] - (optional) N/A 
`socketPortMetricsFilter` [SocketPortMetricsFilter[]] - (optional) N/A 
`socketPortMetricsMeasure` [SocketPortMetricsMeasure[]] - (optional) N/A 
`timeFrame` [TimeFrame] - (required) N/A 
`useDefaultSizeBucket` [Boolean] - (optional) In case we want to have the default size bucket (from properties) 
`withMissingData` [Boolean] - (optional) If false, the data field will be set to '0' for buckets with no reported data. Otherwise it will be set to -1 
