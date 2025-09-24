
## CATO-CLI - query.appStats:
[Click here](https://api.catonetworks.com/documentation/#query-query.appStats) for documentation on this operation.

### Usage for query.appStats:

`catocli query appStats -h`

`catocli query appStats <json>`

`catocli query appStats "$(cat < query.appStats.json)"`

`catocli query appStats '{"appStatsFilter":{"fieldName":"ad_name","operator":"is","values":["string1","string2"]},"appStatsSort":{"fieldName":"ad_name","order":"asc"},"dimension":{"fieldName":"ad_name"},"from":1,"limit":1,"measure":{"aggType":"sum","fieldName":"ad_name","trend":true},"timeFrame":"example_value"}'`

`catocli query appStats -p '{
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
    "from": 1,
    "limit": 1,
    "measure": {
        "aggType": "sum",
        "fieldName": "ad_name",
        "trend": true
    },
    "timeFrame": "example_value"
}'`


## Advanced Usage
# Query to export flows_created, and distinct users (user_name) for user_names for last day

`catocli query appStats '{"appStatsFilter":[],"appStatsSort":[],"dimension":[{"fieldName":"user_name"}],"measure":[{"aggType":"sum","fieldName":"flows_created"},{"aggType":"count_distinct","fieldName":"user_name"}],"timeFrame":"last.P1M"}'`



#### Operation Arguments for query.appStats ####

`accountID` [ID] - (required) Account ID    
`appStatsFilter` [AppStatsFilter[]] - (required) N/A    
`appStatsSort` [AppStatsSort[]] - (required) N/A    
`dimension` [Dimension[]] - (required) N/A    
`from` [Int] - (required) N/A    
`limit` [Int] - (required) N/A    
`measure` [Measure[]] - (required) N/A    
`timeFrame` [TimeFrame] - (required) N/A    
