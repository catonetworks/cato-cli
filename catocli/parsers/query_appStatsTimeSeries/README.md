
## CATO-CLI - query.appStatsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-query.appStatsTimeSeries) for documentation on this operation.

### Usage for query.appStatsTimeSeries:

`catocli query appStatsTimeSeries -h`

`catocli query appStatsTimeSeries <json>`

`catocli query appStatsTimeSeries "$(cat < query.appStatsTimeSeries.json)"`

`catocli query appStatsTimeSeries '{"appStatsFilter":{"fieldName":"ad_name","operator":"is","values":["string1","string2"]},"buckets":1,"dimension":{"fieldName":"ad_name"},"measure":{"aggType":"sum","fieldName":"ad_name","trend":true},"perSecond":true,"timeFrame":"example_value","useDefaultSizeBucket":true,"withMissingData":true}'`

`catocli query appStatsTimeSeries -p '{
    "appStatsFilter": {
        "fieldName": "ad_name",
        "operator": "is",
        "values": [
            "string1",
            "string2"
        ]
    },
    "buckets": 1,
    "dimension": {
        "fieldName": "ad_name"
    },
    "measure": {
        "aggType": "sum",
        "fieldName": "ad_name",
        "trend": true
    },
    "perSecond": true,
    "timeFrame": "example_value",
    "useDefaultSizeBucket": true,
    "withMissingData": true
}'`


## Advanced Usage
# Query to export upstream, downstream and traffic for user_name and application_name for last day broken into 1 hour buckets

`catocli query appStatsTimeSeries '{"appStatsFilter":[],"buckets":24,"dimension":[{"fieldName":"user_name"},{"fieldName":"application_name"}],"measure":[{"aggType":"sum","fieldName":"upstream"},{"aggType":"sum","fieldName":"downstream"},{"aggType":"sum","fieldName":"traffic"}],"timeFrame":"last.PT5M"}'`

# Query to export WANBOUND traffic including upstream, downstream and traffic for user_name and application_name for last day broken into 1 hour buckets

`catocli query appStatsTimeSeries '{"appStatsFilter":[{"fieldName":"traffic_direction","operator":"is","values":["WANBOUND"]}],"buckets":4,"dimension":[{"fieldName":"application_name"},{"fieldName":"user_name"}],"measure":[{"aggType":"sum","fieldName":"traffic"},{"aggType":"sum","fieldName":"upstream"},{"aggType":"sum","fieldName":"downstream"}],"timeFrame":"last.PT1H"}'`


#### Operation Arguments for query.appStatsTimeSeries ####

`accountID` [ID] - (required) Account ID    
`appStatsFilter` [AppStatsFilter[]] - (required) N/A    
`buckets` [Int] - (required) N/A    
`dimension` [Dimension[]] - (required) N/A    
`measure` [Measure[]] - (required) N/A    
`perSecond` [Boolean] - (required) whether to normalize the data into per second (i.e. divide by granularity)    
`timeFrame` [TimeFrame] - (required) N/A    
`useDefaultSizeBucket` [Boolean] - (required) In case we want to have the default size bucket (from properties)    
`withMissingData` [Boolean] - (required) If false, the data field will be set to '0' for buckets with no reported data. Otherwise it will be set to -1    
