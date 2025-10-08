
## CATO-CLI - query.socketPortMetricsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-query.socketPortMetricsTimeSeries) for documentation on this operation.

### Usage for query.socketPortMetricsTimeSeries:

```bash
catocli query socketPortMetricsTimeSeries -h

catocli query socketPortMetricsTimeSeries <json>

catocli query socketPortMetricsTimeSeries "$(cat < query.socketPortMetricsTimeSeries.json)"

catocli query socketPortMetricsTimeSeries '{"socketPortMetricsDimension":{"fieldName":"account_id"},"socketPortMetricsFilter":{"fieldName":"account_id","operator":"is","values":["string1","string2"]},"socketPortMetricsMeasure":{"aggType":"sum","fieldName":"account_id","trend":true},"timeFrame":"example_value"}'

catocli query socketPortMetricsTimeSeries -p '{
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
    "timeFrame": "example_value"
}'
```

#### Operation Arguments for query.socketPortMetricsTimeSeries ####

`accountID` [ID] - (required) Account ID    
`socketPortMetricsDimension` [SocketPortMetricsDimension[]] - (required) N/A    
`socketPortMetricsFilter` [SocketPortMetricsFilter[]] - (required) N/A    
`socketPortMetricsMeasure` [SocketPortMetricsMeasure[]] - (required) N/A    
`timeFrame` [TimeFrame] - (required) N/A    
