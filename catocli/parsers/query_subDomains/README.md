
## CATO-CLI - query.subDomains:
[Click here](https://api.catonetworks.com/documentation/#query-query.subDomains) for documentation on this operation.

### Usage for query.subDomains:

`catocli query subDomains -h`

`catocli query subDomains <json>`

`catocli query subDomains "$(cat < query.subDomains.json)"`

`catocli query subDomains '{"managedAccount":true}'`

`catocli query subDomains -p '{
    "managedAccount": true
}'`


#### Operation Arguments for query.subDomains ####

`accountID` [ID] - (required) Unique Identifier of Account    
`managedAccount` [Boolean] - (required) When the boolean argument managedAccount is set to true (default), then the query returns all subdomains related to the account    
