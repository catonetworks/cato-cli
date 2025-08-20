
## CATO-CLI - query.socketPortMetrics:
[Click here](https://api.catonetworks.com/documentation/#query-socketPortMetrics) for documentation on this operation.

### Usage for query.socketPortMetrics:

`catocli query socketPortMetrics -h`

`catocli query socketPortMetrics <json>`

`catocli query socketPortMetrics "$(cat < socketPortMetrics.json)"`

`catocli query socketPortMetrics '{"from": "Int", "limit": "Int", "socketPortMetricsDimension": {"fieldName": {"fieldName": "enum(SocketPortMetricsFieldName)"}}, "socketPortMetricsFilter": {"fieldName": {"fieldName": "enum(SocketPortMetricsFieldName)"}, "operator": {"operator": "enum(FilterOperator)"}, "values": {"values": ["String"]}}, "socketPortMetricsMeasure": {"aggType": {"aggType": "enum(AggregationType)"}, "fieldName": {"fieldName": "enum(SocketPortMetricsFieldName)"}, "trend": {"trend": "Boolean"}}, "socketPortMetricsSort": {"fieldName": {"fieldName": "enum(SocketPortMetricsFieldName)"}, "order": {"order": "enum(DirectionEnum)"}}, "timeFrame": "TimeFrame"}'`

#### Operation Arguments for query.socketPortMetrics ####
`accountID` [ID] - (required) Account ID 
`from` [Int] - (optional) N/A 
`limit` [Int] - (optional) N/A 
`socketPortMetricsDimension` [SocketPortMetricsDimension[]] - (optional) N/A 
`socketPortMetricsFilter` [SocketPortMetricsFilter[]] - (optional) N/A 
`socketPortMetricsMeasure` [SocketPortMetricsMeasure[]] - (optional) N/A 
`socketPortMetricsSort` [SocketPortMetricsSort[]] - (optional) N/A 
`timeFrame` [TimeFrame] - (required) N/A 
