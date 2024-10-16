
## CATO-CLI - query.entityLookup:
[Click here](https://api.catonetworks.com/documentation/#query-entityLookup) for documentation on this operation.

### Usage for query.entityLookup:

`catocli query entityLookup -h`

`catocli query entityLookup <json>`

`catocli query entityLookup "$(cat < entityLookup.json)"`

`catocli query entityLookup '{"EntityInput": {"id": {"id": "ID"}, "name": {"name": "String"}, "type": {"type": "enum(EntityType)"}}, "LookupFilterInput": {"filter": {"filter": "enum(LookupFilterType)"}, "value": {"value": "String"}}, "SortInput": {"field": {"field": "String"}, "order": {"order": "enum(DirectionInput)"}}, "entityIDs": ["ID"], "from": "Int", "helperFields": ["String"], "limit": "Int", "search": "String", "type": "enum(EntityType)"}'`

#### Operation Arguments for query.entityLookup ####
`EntityInput` [EntityInput] - (optional) Return items under a parent entity (can be site, vpn user, etc),
used to filter for networks that belong to a specific site for example 
`LookupFilterInput` [LookupFilterInput[]] - (optional) Custom filters for entityLookup 
`SortInput` [SortInput[]] - (optional) Adds additional sort criteria(s) for the lookup.
This option is not universally available, and may not be applicable specific Entity types. 
`accountID` [ID] - (required) The account ID (or 0 for non-authenticated requests) 
`entityIDs` [ID[]] - (optional) Adds additional search criteria to fetch by the selected list of entity IDs. This option is not
universally available, and may not be applicable specific Entity types. If used on non applicable entity
type, an error will be generated. 
`from` [Int] - (optional) Sets the offset number of items (for paging) 
`helperFields` [String[]] - (optional) Additional helper fields 
`limit` [Int] - (optional) Sets the maximum number of items to retrieve 
`search` [String] - (optional) Adds additional search parameters for the lookup. Available options:
country lookup: "removeExcluded" to return only allowed countries
countryState lookup: country code ("US", "CN", etc) to get country's states 
`type` [EntityType] - (required) Type of entity to lookup for Default Value: ['account', 'site', 'vpnUser', 'country', 'countryState', 'timezone', 'host', 'any', 'networkInterface', 'location', 'admin', 'localRouting', 'lanFirewall', 'allocatedIP', 'siteRange', 'simpleService', 'availableSiteUsage', 'availablePooledUsage', 'dhcpRelayGroup', 'portProtocol', 'city', 'groupSubscription', 'mailingListSubscription', 'webhookSubscription']
