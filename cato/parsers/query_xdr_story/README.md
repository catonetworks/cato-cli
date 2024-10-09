
## CATO-CLI - query.xdr.story:
[Click here](https://api.catonetworks.com/documentation/#query-story) for documentation on this operation.

### Usage for query.xdr.story:

`cato query xdr story -h`

`cato query xdr story <accountID> <json>`

`cato query xdr story 12345 "$(cat < story.json)"`

`cato query xdr story 12345 '{"incidentId": "ID", "perSecond": "Boolean", "producer": "enum(StoryProducerEnum)", "storyId": "ID"}'`

#### Operation Arguments for query.xdr.story ####
`accountID` [ID] - (required) N/A 
`incidentId` [ID] - (optional) N/A 
`perSecond` [Boolean] - (optional) whether to normalize the data into per second (i.e. divide by granularity) 
`producer` [StoryProducerEnum] - (optional) N/A Default Value: ['AnomalyStats', 'AnomalyEvents', 'ThreatHunt', 'ThreatPrevention', 'NetworkMonitor', 'NetworkXDR', 'MicrosoftEndpointDefender', 'CatoEndpointAlert', 'EntraIdAlert']
`storyId` [ID] - (optional) N/A 
