
## CATO-CLI - query.xdr.story:
[Click here](https://api.catonetworks.com/documentation/#query-query.xdr.story) for documentation on this operation.

### Usage for query.xdr.story:

`catocli query xdr story -h`

`catocli query xdr story <json>`

`catocli query xdr story "$(cat < query.xdr.story.json)"`

`catocli query xdr story '{"incidentId":"id","producer":"AnomalyStats","storyId":"id"}'`

`catocli query xdr story -p '{
    "incidentId": "id",
    "producer": "AnomalyStats",
    "storyId": "id"
}'`


#### Operation Arguments for query.xdr.story ####

`accountID` [ID] - (required) N/A    
`incidentId` [ID] - (required) N/A    
`producer` [StoryProducerEnum] - (required) N/A Default Value: ['AnomalyStats', 'AnomalyEvents', 'AnomalyExperience', 'ThreatHunt', 'ThreatPrevention', 'NetworkMonitor', 'NetworkXDR', 'MicrosoftEndpointDefender', 'CatoEndpointAlert', 'EntraIdAlert']   
`storyId` [ID] - (required) N/A    
