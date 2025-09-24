
## CATO-CLI - query.accountBySubdomain:
[Click here](https://api.catonetworks.com/documentation/#query-query.accountBySubdomain) for documentation on this operation.

### Usage for query.accountBySubdomain:

`catocli query accountBySubdomain -h`

`catocli query accountBySubdomain <json>`

`catocli query accountBySubdomain "$(cat < query.accountBySubdomain.json)"`

`catocli query accountBySubdomain '{"subdomains":["string1","string2"]}'`

`catocli query accountBySubdomain -p '{
    "subdomains": [
        "string1",
        "string2"
    ]
}'`


#### Operation Arguments for query.accountBySubdomain ####

`accountID` [ID] - (required) N/A    
`subdomains` [String[]] - (required) a list of required subdomains    
