
## CATO-CLI - query.appStats:
[Click here](https://api.catonetworks.com/documentation/#query-appStats) for documentation on this operation.

### Usage for query.appStats:

`catocli query appStats -h`

`catocli query appStats <json>`

`catocli query appStats "$(cat < appStats.json)"`

`catocli query appStats '{"appStatsFilter": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}, "operator": {"operator": "enum(FilterOperator)"}, "values": {"values": ["String"]}}, "appStatsSort": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}, "order": {"order": "enum(DirectionEnum)"}}, "dimension": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}}, "from": "Int", "limit": "Int", "measure": {"aggType": {"aggType": "enum(AggregationType)"}, "fieldName": {"fieldName": "enum(AppStatsFieldName)"}, "trend": {"trend": "Boolean"}}, "timeFrame": "TimeFrame"}'`

#### Operation Arguments for query.appStats ####
`accountID` [ID] - (required) Account ID 
`appStatsFilter` [AppStatsFilter[]] - (optional) N/A 
`appStatsSort` [AppStatsSort[]] - (optional) N/A 
`dimension` [Dimension[]] - (optional) N/A 
`from` [Int] - (optional) N/A 
`limit` [Int] - (optional) N/A 
`measure` [Measure[]] - (optional) N/A 
`timeFrame` [TimeFrame] - (required) N/A 
