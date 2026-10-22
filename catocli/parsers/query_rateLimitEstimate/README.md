
## CATO-CLI - query.rateLimitEstimate:
[Click here](https://api.catonetworks.com/documentation/#query-query.rateLimitEstimate) for documentation on this operation.

### Usage for query.rateLimitEstimate:

```bash
catocli query rateLimitEstimate -h

catocli query rateLimitEstimate <json>

catocli query rateLimitEstimate --json-file query.rateLimitEstimate.json

catocli query rateLimitEstimate '{"operationName":"string","query":"string","variables":{"key":"value"}}'

catocli query rateLimitEstimate '{
    "operationName": "string",
    "query": "string",
    "variables": {
        "key": "value"
    }
}'
```

#### Operation Arguments for query.rateLimitEstimate ####

`operationName` [String] - (required) The operation to estimate when `query` contains more than one.
`query` [String] - (required) The GraphQL document to estimate.
`variables` [Map] - (required) Variables for the operation in `query`.
