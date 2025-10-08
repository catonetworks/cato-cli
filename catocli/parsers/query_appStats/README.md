
## CATO-CLI - query.appStats:
[Click here](https://api.catonetworks.com/documentation/#query-query.appStats) for documentation on this operation.

### Usage for query.appStats:

```bash
catocli query appStats -h

catocli query appStats <json>

catocli query appStats "$(cat < query.appStats.json)"

catocli query appStats '{"appStatsFilter":{"fieldName":"ad_name","operator":"is","values":["string1","string2"]},"appStatsSort":{"fieldName":"ad_name","order":"asc"},"dimension":{"fieldName":"ad_name"},"measure":{"aggType":"sum","fieldName":"ad_name","trend":true},"timeFrame":"example_value"}'

catocli query appStats -p '{
    "appStatsFilter": {
        "fieldName": "ad_name",
        "operator": "is",
        "values": [
            "string1",
            "string2"
        ]
    },
    "appStatsSort": {
        "fieldName": "ad_name",
        "order": "asc"
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
# Query to export user activity as in flows_created, for distinct users (user_name) for the last day

`catocli query appStats '{"appStatsFilter":[],"appStatsSort":[],"dimension":[{"fieldName":"user_name"}],"measure":[{"aggType":"sum","fieldName":"flows_created"},{"aggType":"count_distinct","fieldName":"user_name"}],"timeFrame":"last.P1M"}'`

# Query to export application_name, user_name and risk_score with traffic sum(upstream, downstream, trafffic) for last day

catocli query appStats '{"appStatsFilter":[],"appStatsSort":[],"dimension":[{"fieldName":"application_name"},{"fieldName":"user_name"},{"fieldName":"risk_score"}],"measure":[{"aggType":"sum","fieldName":"downstream"},{"aggType":"sum","fieldName":"upstream"},{"aggType":"sum","fieldName":"traffic"}],"timeFrame":"last.P1D"}' -f csv




#### Operation Arguments for query.appStats ####

`accountID` [ID] - (required) Account ID    
`appStatsFilter` [AppStatsFilter[]] - (required) N/A    
`appStatsSort` [AppStatsSort[]] - (required) N/A    
`dimension` [Dimension[]] - (required) N/A    
`measure` [Measure[]] - (required) N/A    
`timeFrame` [TimeFrame] - (required) N/A    
