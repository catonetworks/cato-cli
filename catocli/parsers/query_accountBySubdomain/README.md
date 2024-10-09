
## CATO-CLI - query.accountBySubdomain:
[Click here](https://api.catonetworks.com/documentation/#query-accountBySubdomain) for documentation on this operation.

### Usage for query.accountBySubdomain:

`catocli query accountBySubdomain -h`

`catocli query accountBySubdomain <accountID> <json>`

`catocli query accountBySubdomain 12345 "$(cat < accountBySubdomain.json)"`

`catocli query accountBySubdomain 12345 '{"subdomains": ["String"]}'`

#### Operation Arguments for query.accountBySubdomain ####
`accountID` [ID] - (required) N/A 
`subdomains` [String[]] - (required) a list of required subdomains 
