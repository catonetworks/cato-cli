
## CATO-CLI - query.socketPortMetrics:
[Click here](https://api.catonetworks.com/documentation/#query-query.socketPortMetrics) for documentation on this operation.

### Usage for query.socketPortMetrics:

`catocli query socketPortMetrics -h`

`catocli query socketPortMetrics <json>`

`catocli query socketPortMetrics "$(cat < query.socketPortMetrics.json)"`

`catocli query socketPortMetrics '{"from":1,"limit":1,"socketPortMetricsDimension":{"fieldName":"account_id"},"socketPortMetricsFilter":{"fieldName":"account_id","operator":"is","values":["string1","string2"]},"socketPortMetricsMeasure":{"aggType":"sum","fieldName":"account_id","trend":true},"socketPortMetricsSort":{"fieldName":"account_id","order":"asc"},"timeFrame":"example_value"}'`

`catocli query socketPortMetrics -p '{
    "from": 1,
    "limit": 1,
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
    "socketPortMetricsSort": {
        "fieldName": "account_id",
        "order": "asc"
    },
    "timeFrame": "example_value"
}'`


#### Operation Arguments for query.socketPortMetrics ####

`accountID` [ID] - (required) Account ID    
`from` [Int] - (required) N/A    
`limit` [Int] - (required) N/A    
`socketPortMetricsDimension` [SocketPortMetricsDimension[]] - (required) N/A    
`socketPortMetricsFilter` [SocketPortMetricsFilter[]] - (required) N/A    
`socketPortMetricsMeasure` [SocketPortMetricsMeasure[]] - (required) N/A    
`socketPortMetricsSort` [SocketPortMetricsSort[]] - (required) N/A    
`timeFrame` [TimeFrame] - (required) N/A    
