
## CATO-CLI - query.socketPortMetricsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-query.socketPortMetricsTimeSeries) for documentation on this operation.

### Usage for query.socketPortMetricsTimeSeries:

`catocli query socketPortMetricsTimeSeries -h`

`catocli query socketPortMetricsTimeSeries <json>`

`catocli query socketPortMetricsTimeSeries "$(cat < query.socketPortMetricsTimeSeries.json)"`

`catocli query socketPortMetricsTimeSeries '{"buckets":1,"perSecond":true,"socketPortMetricsDimension":{"fieldName":"account_id"},"socketPortMetricsFilter":{"fieldName":"account_id","operator":"is","values":["string1","string2"]},"socketPortMetricsMeasure":{"aggType":"sum","fieldName":"account_id","trend":true},"timeFrame":"example_value","useDefaultSizeBucket":true,"withMissingData":true}'`

`catocli query socketPortMetricsTimeSeries -p '{
    "buckets": 1,
    "perSecond": true,
    "socketPortMetricsDimension": {
        "fieldName": "account_id"
    },
    "socketPortMetricsFilter": {
        "fieldName": "account_id",
        "operator": "is",
        "values": [
            "string1",
            "string2"
        ]
    },
    "socketPortMetricsMeasure": {
        "aggType": "sum",
        "fieldName": "account_id",
        "trend": true
    },
    "timeFrame": "example_value",
    "useDefaultSizeBucket": true,
    "withMissingData": true
}'`


#### Operation Arguments for query.socketPortMetricsTimeSeries ####

`accountID` [ID] - (required) Account ID    
`buckets` [Int] - (required) N/A    
`perSecond` [Boolean] - (required) whether to normalize the data into per second (i.e. divide by granularity)    
`socketPortMetricsDimension` [SocketPortMetricsDimension[]] - (required) N/A    
`socketPortMetricsFilter` [SocketPortMetricsFilter[]] - (required) N/A    
`socketPortMetricsMeasure` [SocketPortMetricsMeasure[]] - (required) N/A    
`timeFrame` [TimeFrame] - (required) N/A    
`useDefaultSizeBucket` [Boolean] - (required) In case we want to have the default size bucket (from properties)    
`withMissingData` [Boolean] - (required) If false, the data field will be set to '0' for buckets with no reported data. Otherwise it will be set to -1    
