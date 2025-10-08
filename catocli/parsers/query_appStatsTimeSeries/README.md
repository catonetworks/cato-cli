
## CATO-CLI - query.appStatsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-query.appStatsTimeSeries) for documentation on this operation.

### Usage for query.appStatsTimeSeries:

```bash
catocli query appStatsTimeSeries -h

catocli query appStatsTimeSeries <json>

catocli query appStatsTimeSeries "$(cat < query.appStatsTimeSeries.json)"

catocli query appStatsTimeSeries '{"appStatsFilter":{"fieldName":"ad_name","operator":"is","values":["string1","string2"]},"dimension":{"fieldName":"ad_name"},"measure":{"aggType":"sum","fieldName":"ad_name","trend":true},"timeFrame":"example_value"}'

catocli query appStatsTimeSeries -p '{
    "appStatsFilter": {
        "fieldName": "ad_name",
        "operator": "is",
        "values": [
            "string1",
            "string2"
        ]
    },
    "dimension": {
        "fieldName": "ad_name"
    },
    "measure": {
        "aggType": "sum",
        "fieldName": "ad_name",
        "trend": true
    },
    "timeFrame": "example_value"
}'
```

## Advanced Usage
# Query to export upstream, downstream and traffic for user_name and application_name for last day broken into 1 hour buckets

`catocli query appStatsTimeSeries '{"appStatsFilter":[],"buckets":24,"dimension":[{"fieldName":"user_name"},{"fieldName":"application_name"}],"measure":[{"aggType":"sum","fieldName":"upstream"},{"aggType":"sum","fieldName":"downstream"},{"aggType":"sum","fieldName":"traffic"}],"timeFrame":"last.PT5M"}'`

# Query to export WANBOUND traffic including upstream, downstream and traffic for user_name and application_name for last day broken into 1 hour buckets

`catocli query appStatsTimeSeries '{"appStatsFilter":[{"fieldName":"traffic_direction","operator":"is","values":["WANBOUND"]}],"buckets":4,"dimension":[{"fieldName":"application_name"},{"fieldName":"user_name"}],"measure":[{"aggType":"sum","fieldName":"traffic"},{"aggType":"sum","fieldName":"upstream"},{"aggType":"sum","fieldName":"downstream"}],"timeFrame":"last.PT1H"}'`


#### Operation Arguments for query.appStatsTimeSeries ####

`accountID` [ID] - (required) Account ID    
`appStatsFilter` [AppStatsFilter[]] - (required) N/A    
`dimension` [Dimension[]] - (required) N/A    
`measure` [Measure[]] - (required) N/A    
`timeFrame` [TimeFrame] - (required) N/A    
