
## CATO-CLI - query.accountSnapshot:
[Click here](https://api.catonetworks.com/documentation/#query-accountSnapshot) for documentation on this operation.

### Usage for query.accountSnapshot:

`catocli query accountSnapshot -h`

`catocli query accountSnapshot <accountID> <json>`

`catocli query accountSnapshot 12345 "$(cat < accountSnapshot.json)"`

`catocli query accountSnapshot 12345 '{"siteIDs": ["ID"], "userIDs": ["ID"]}'`

#### Operation Arguments for query.accountSnapshot ####
`accountID` [ID] - (optional) Unique Identifier of Account. 
`siteIDs` [ID[]] - (optional) List of Unique Site Identifiers. If specified, only sites in list will be returned 
`userIDs` [ID[]] - (optional) request specific IDs, regardless of if connected or not 