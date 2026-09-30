
## CATO-CLI - query.accountSnapshot:
[Click here](https://api.catonetworks.com/documentation/#query-query.accountSnapshot) for documentation on this operation.

### Usage for query.accountSnapshot:

```bash
catocli query accountSnapshot -h

catocli query accountSnapshot <json>

catocli query accountSnapshot --json-file query.accountSnapshot.json

catocli query accountSnapshot '{"siteIDs":["id1","id2"],"userIDs":["id1","id2"]}'

catocli query accountSnapshot '{
    "siteIDs": [
        "id1",
        "id2"
    ],
    "userIDs": [
        "id1",
        "id2"
    ]
}'
```

#### Operation Arguments for query.accountSnapshot ####

`accountID` [ID] - (required) N/A
`siteIDs` [ID[]] - (required) N/A
`userIDs` [ID[]] - (required) N/A
