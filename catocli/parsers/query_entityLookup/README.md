
## CATO-CLI - query.entityLookup:
[Click here](https://api.catonetworks.com/documentation/#query-query.entityLookup) for documentation on this operation.

### Usage for query.entityLookup:

```bash
catocli query entityLookup -h

catocli query entityLookup <json>

catocli query entityLookup --json-file query.entityLookup.json

catocli query entityLookup '{"entityIDs":["id1","id2"],"entityInput":{"id":"id","name":"string","type":"site"},"from":1,"helperFields":["string1","string2"],"limit":1,"lookupFilterInput":{"filter":"filterByConnectionTypeFamily","value":"string"},"search":"string","sortInput":{"field":"string","order":"asc"},"type":"site"}'

catocli query entityLookup '{
    "entityIDs": [
        "id1",
        "id2"
    ],
    "entityInput": {
        "id": "id",
        "name": "string",
        "type": "site"
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
    "type": "site"
}'
```

#### Operation Arguments for query.entityLookup ####

`accountID` [ID] - (required) N/A
`entityIDs` [ID[]] - (required) N/A
`entityInput` [EntityInput] - (required) N/A
`from` [Int] - (required) N/A
`helperFields` [String[]] - (required) N/A
`limit` [Int] - (required) N/A
`lookupFilterInput` [LookupFilterInput[]] - (required) N/A
`search` [String] - (required) N/A
`sortInput` [SortInput[]] - (required) N/A
`type` [EntityType] - (required) N/A Default Value: ['site', 'account', 'vpnUser', 'country', 'countryState', 'timezone', 'host', 'any', 'networkInterface', 'location', 'admin', 'localRouting', 'lanFirewall', 'allocatedIP', 'siteRange', 'simpleService', 'availableSiteUsage', 'availablePooledUsage', 'dhcpRelayGroup', 'portProtocol', 'city', 'groupSubscription', 'mailingListSubscription', 'webhookSubscription']
