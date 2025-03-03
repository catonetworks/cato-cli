
## CATO-CLI - mutation.xdr.analystFeedback:
[Click here](https://api.catonetworks.com/documentation/#mutation-analystFeedback) for documentation on this operation.

### Usage for mutation.xdr.analystFeedback:

`catocli mutation xdr analystFeedback -h`

`catocli mutation xdr analystFeedback <json>`

`catocli mutation xdr analystFeedback "$(cat < analystFeedback.json)"`

`catocli mutation xdr analystFeedback '{"analystFeedbackInput": {"additionalInfo": {"additionalInfo": "String"}, "severity": {"severity": "enum(SeverityEnum)"}, "status": {"status": "enum(StoryStatusEnum)"}, "storyId": {"storyId": "ID"}, "storyThreatType": {"details": {"details": "String"}, "name": {"name": "String"}, "recommendedAction": {"recommendedAction": "String"}}, "threatClassification": {"threatClassification": "String"}, "verdict": {"verdict": "enum(StoryVerdictEnum)"}}, "perSecond": "Boolean"}'`

#### Operation Arguments for mutation.xdr.analystFeedback ####
`accountId` [ID] - (required) N/A 
`analystFeedbackInput` [AnalystFeedbackInput] - (required) N/A 
`perSecond` [Boolean] - (optional) whether to normalize the data into per second (i.e. divide by granularity) 
