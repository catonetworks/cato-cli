
## CATO-CLI - query.events:
[Click here](https://api.catonetworks.com/documentation/#query-events) for documentation on this operation.

### Usage for query.events:

`catocli query events -h`

`catocli query events <json>`

`catocli query events "$(cat < events.json)"`

`catocli query events '{"eventsDimension": {"fieldName": {"fieldName": "enum(EventFieldName)"}}, "eventsFilter": {"fieldName": {"fieldName": "enum(EventFieldName)"}, "operator": {"operator": "enum(FilterOperator)"}, "values": {"values": ["String"]}}, "eventsMeasure": {"aggType": {"aggType": "enum(AggregationType)"}, "fieldName": {"fieldName": "enum(EventFieldName)"}, "trend": {"trend": "Boolean"}}, "eventsSort": {"fieldName": {"fieldName": "enum(EventFieldName)"}, "order": {"order": "enum(DirectionEnum)"}}, "from": "Int", "limit": "Int", "timeFrame": "TimeFrame"}'`

#### Operation Arguments for query.events ####
`accountID` [ID] - (required) Account ID 
`eventsDimension` [EventsDimension[]] - (optional) N/A 
`eventsFilter` [EventsFilter[]] - (optional) N/A 
`eventsMeasure` [EventsMeasure[]] - (optional) N/A 
`eventsSort` [EventsSort[]] - (optional) N/A 
`from` [Int] - (optional) N/A 
`limit` [Int] - (optional) N/A 
`timeFrame` [TimeFrame] - (required) N/A 
