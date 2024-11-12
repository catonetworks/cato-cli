
## CATO-CLI - query.xdr.stories:
[Click here](https://api.catonetworks.com/documentation/#query-stories) for documentation on this operation.

### Usage for query.xdr.stories:

`catocli query xdr stories -h`

`catocli query xdr stories <json>`

`catocli query xdr stories "$(cat < stories.json)"`

`catocli query xdr stories '{"perSecond": "Boolean", "storyInput": {"pagingInput": {"from": {"from": "Int"}, "limit": {"limit": "Int"}}, "storyFilterInput": {"accountId": {"in": {"in": ["ID"]}, "not_in": {"not_in": ["ID"]}}, "criticality": {"eq": {"eq": "Int"}, "gt": {"gt": "Int"}, "gte": {"gte": "Int"}, "in": {"in": ["Int"]}, "lt": {"lt": "Int"}, "lte": {"lte": "Int"}, "not_in": {"not_in": ["Int"]}}, "engineType": {"in": {"in": "enum(StoryEngineTypeEnum)"}, "not_in": {"not_in": "enum(StoryEngineTypeEnum)"}}, "incidentId": {"contains": {"contains": "String"}, "in": {"in": ["String"]}, "not_in": {"not_in": ["String"]}}, "ioa": {"contains": {"contains": "String"}, "in": {"in": ["String"]}, "not_in": {"not_in": ["String"]}}, "muted": {"is": {"is": "String"}}, "producer": {"in": {"in": "enum(StoryProducerEnum)"}, "not_in": {"not_in": "enum(StoryProducerEnum)"}}, "queryName": {"contains": {"contains": "String"}, "in": {"in": ["String"]}, "not_in": {"not_in": ["String"]}}, "severity": {"in": {"in": "enum(SeverityEnum)"}, "not_in": {"not_in": "enum(SeverityEnum)"}}, "source": {"contains": {"contains": "String"}, "in": {"in": ["String"]}, "not_in": {"not_in": ["String"]}}, "sourceIp": {"contains": {"contains": "String"}, "in": {"in": ["String"]}, "not_in": {"not_in": ["String"]}}, "status": {"in": {"in": "enum(StoryStatusEnum)"}, "not_in": {"not_in": "enum(StoryStatusEnum)"}}, "storyId": {"in": {"in": ["ID"]}, "not_in": {"not_in": ["ID"]}}, "timeFrame": {"time": {"time": "TimeFrame"}, "timeFrameModifier": {"timeFrameModifier": "enum(TimeFrameModifier)"}}, "vendor": {"in": {"in": "enum(VendorEnum)"}, "not_in": {"not_in": "enum(VendorEnum)"}}, "verdict": {"in": {"in": "enum(StoryVerdictEnum)"}, "not_in": {"not_in": "enum(StoryVerdictEnum)"}}}, "storySortInput": {"fieldName": {"fieldName": "enum(StorySortFieldName)"}, "order": {"order": "enum(SortDirectionEnum)"}}}}'`

#### Operation Arguments for query.xdr.stories ####
`accountID` [ID] - (required) N/A 
`perSecond` [Boolean] - (optional) whether to normalize the data into per second (i.e. divide by granularity) 
`storyInput` [StoryInput] - (required) N/A 
