
## CATO-CLI - query.accountSnapshot:
[Click here](https://api.catonetworks.com/documentation/#query-query.accountSnapshot) for documentation on this operation.

### Usage for query.accountSnapshot:

`catocli query accountSnapshot -h`

`catocli query accountSnapshot <json>`

`catocli query accountSnapshot "$(cat < query.accountSnapshot.json)"`

`catocli query accountSnapshot '{"siteIDs":["id1","id2"],"userIDs":["id1","id2"]}'`

`catocli query accountSnapshot -p '{
    "siteIDs": [
        "id1",
        "id2"
    ],
    "userIDs": [
        "id1",
        "id2"
    ]
}'`


#### Operation Arguments for query.accountSnapshot ####

`accountID` [ID] - (required) Unique Identifier of Account.    
`siteIDs` [ID[]] - (required) List of Unique Site Identifiers. If specified, only sites in list will be returned    
`userIDs` [ID[]] - (required) request specific IDs, regardless of if connected or not    
