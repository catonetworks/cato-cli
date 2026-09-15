
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

