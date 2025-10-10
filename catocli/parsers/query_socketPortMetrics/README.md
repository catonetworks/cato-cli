
## CATO-CLI - query.socketPortMetrics:
[Click here](https://api.catonetworks.com/documentation/#query-query.socketPortMetrics) for documentation on this operation.

### Usage for query.socketPortMetrics:

```bash
catocli query socketPortMetrics -h

catocli query socketPortMetrics <json>

catocli query socketPortMetrics "$(cat < query.socketPortMetrics.json)"

catocli query socketPortMetrics '{"from":1,"limit":1,"socketPortMetricsDimension":{"fieldName":"account_id"},"socketPortMetricsFilter":{"fieldName":"account_id","operator":"is","values":["string1","string2"]},"socketPortMetricsMeasure":{"aggType":"sum","fieldName":"account_id","trend":true},"socketPortMetricsSort":{"fieldName":"account_id","order":"asc"},"timeFrame":"example_value"}'

catocli query socketPortMetrics '{
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
}'
```


#### TimeFrame Parameter Examples

The `timeFrame` parameter supports both relative time ranges and absolute date ranges:

**Relative Time Ranges:**
- "last.PT5M" = Previous 5 minutes
- "last.PT1H" = Previous 1 hour  
- "last.P1D" = Previous 1 day
- "last.P14D" = Previous 14 days
- "last.P1M" = Previous 1 month

**Absolute Date Ranges:**
Format: `"utc.YYYY-MM-{DD/HH:MM:SS--DD/HH:MM:SS}"`

- Single day: "utc.2023-02-{28/00:00:00--28/23:59:59}"  
- Multiple days: "utc.2023-02-{25/00:00:00--28/23:59:59}"  
- Specific hours: "utc.2023-02-{28/09:00:00--28/17:00:00}"
- Across months: "utc.2023-{01-28/00:00:00--02-03/23:59:59}"


#### Operation Arguments for query.socketPortMetrics ####

`accountID` [ID] - (required) Account ID    
`from` [Int] - (required) N/A    
`limit` [Int] - (required) N/A    
`socketPortMetricsDimension` [SocketPortMetricsDimension[]] - (required) N/A    
`socketPortMetricsFilter` [SocketPortMetricsFilter[]] - (required) N/A    
`socketPortMetricsMeasure` [SocketPortMetricsMeasure[]] - (required) N/A    
`socketPortMetricsSort` [SocketPortMetricsSort[]] - (required) N/A    
`timeFrame` [TimeFrame] - (required) N/A    
