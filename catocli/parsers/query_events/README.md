
## CATO-CLI - query.events:
[Click here](https://api.catonetworks.com/documentation/#query-events) for documentation on this operation.

### Usage for query.events:

`catocli query events -h`

`catocli query events <accountID> <json>`

`catocli query events 12345 "$(cat < events.json)"`

`catocli query events 12345 '{"EventsDimension": {"fieldName": {"fieldName": "enum(EventFieldName)"}}, "EventsFilter": {"fieldName": {"fieldName": "enum(EventFieldName)"}, "operator": {"operator": "enum(FilterOperator)"}, "values": {"values": ["String"]}}, "EventsMeasure": {"aggType": {"aggType": "enum(AggregationType)"}, "fieldName": {"fieldName": "enum(EventFieldName)"}, "trend": {"trend": "Boolean"}}, "EventsSort": {"fieldName": {"fieldName": "enum(EventFieldName)"}, "order": {"order": "enum(DirectionEnum)"}}, "from": "Int", "limit": "Int", "timeFrame": "TimeFrame"}'`

#### Operation Arguments for query.events ####
`EventsDimension` [EventsDimension[]] - (optional) N/A 
`EventsFilter` [EventsFilter[]] - (optional) N/A 
`EventsMeasure` [EventsMeasure[]] - (optional) N/A 
`EventsSort` [EventsSort[]] - (optional) N/A 
`accountID` [ID] - (required) Account ID 
`from` [Int] - (optional) N/A 
`limit` [Int] - (optional) N/A 
`timeFrame` [TimeFrame] - (required) N/A 