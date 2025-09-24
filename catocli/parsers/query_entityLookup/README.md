
## CATO-CLI - query.entityLookup:
[Click here](https://api.catonetworks.com/documentation/#query-query.entityLookup) for documentation on this operation.

### Usage for query.entityLookup:

`catocli query entityLookup -h`

`catocli query entityLookup <json>`

`catocli query entityLookup "$(cat < query.entityLookup.json)"`

`catocli query entityLookup '{"entityIDs":["id1","id2"],"entityInput":{"id":"id","name":"string","type":"account"},"from":1,"helperFields":["string1","string2"],"limit":1,"lookupFilterInput":{"filter":"filterByConnectionTypeFamily","value":"string"},"search":"string","sortInput":{"field":"string","order":"asc"},"type":"account"}'`

`catocli query entityLookup -p '{
    "entityIDs": [
        "id1",
        "id2"
    ],
    "entityInput": {
        "id": "id",
        "name": "string",
        "type": "account"
    },
    "from": 1,
    "helperFields": [
        "string1",
        "string2"
    ],
    "limit": 1,
    "lookupFilterInput": {
        "filter": "filterByConnectionTypeFamily",
        "value": "string"
    },
    "search": "string",
    "sortInput": {
        "field": "string",
        "order": "asc"
    },
    "type": "account"
}'`


#### Operation Arguments for query.entityLookup ####

`accountID` [ID] - (required) The account ID (or 0 for non-authenticated requests)    
`entityIDs` [ID[]] - (required) Adds additional search criteria to fetch by the selected list of entity IDs. This option is not
universally available, and may not be applicable specific Entity types. If used on non applicable entity
type, an error will be generated.    
`entityInput` [EntityInput] - (required) Return items under a parent entity (can be site, vpn user, etc),
used to filter for networks that belong to a specific site for example    
`from` [Int] - (required) Sets the offset number of items (for paging)    
`helperFields` [String[]] - (required) Additional helper fields    
`limit` [Int] - (required) Sets the maximum number of items to retrieve    
`lookupFilterInput` [LookupFilterInput[]] - (required) Custom filters for entityLookup    
`search` [String] - (required) Adds additional search parameters for the lookup. Available options:
country lookup: "removeExcluded" to return only allowed countries
countryState lookup: country code ("US", "CN", etc) to get country's states    
`sortInput` [SortInput[]] - (required) Adds additional sort criteria(s) for the lookup.
This option is not universally available, and may not be applicable specific Entity types.    
`type` [EntityType] - (required) Type of entity to lookup for Default Value: ['account', 'site', 'vpnUser', 'country', 'countryState', 'timezone', 'host', 'any', 'networkInterface', 'location', 'admin', 'localRouting', 'lanFirewall', 'allocatedIP', 'siteRange', 'simpleService', 'availableSiteUsage', 'availablePooledUsage', 'dhcpRelayGroup', 'portProtocol', 'city', 'groupSubscription', 'mailingListSubscription', 'webhookSubscription']   
