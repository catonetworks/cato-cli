
## CATO-CLI - query.appStats:
[Click here](https://api.catonetworks.com/documentation/#query-appStats) for documentation on this operation.

### Usage for query.appStats:

`catocli query appStats -h`

`catocli query appStats <json>`

`catocli query appStats "$(cat < appStats.json)"`

`catocli query appStats '{"AppStatsFilter": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}, "operator": {"operator": "enum(FilterOperator)"}, "values": {"values": ["String"]}}, "AppStatsSort": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}, "order": {"order": "enum(DirectionEnum)"}}, "Dimension": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}}, "Measure": {"aggType": {"aggType": "enum(AggregationType)"}, "fieldName": {"fieldName": "enum(AppStatsFieldName)"}, "trend": {"trend": "Boolean"}}, "from": "Int", "limit": "Int", "timeFrame": "TimeFrame"}'`

#### Operation Arguments for query.appStats ####
`AppStatsFilter` [AppStatsFilter[]] - (optional) N/A 
`AppStatsSort` [AppStatsSort[]] - (optional) N/A 
`Dimension` [Dimension[]] - (optional) N/A 
`Measure` [Measure[]] - (optional) N/A 
`accountID` [ID] - (required) Account ID 
`from` [Int] - (optional) N/A 
`limit` [Int] - (optional) N/A 
`timeFrame` [TimeFrame] - (required) N/A 
