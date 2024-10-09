
## CATO-CLI - query.subDomains:
[Click here](https://api.catonetworks.com/documentation/#query-subDomains) for documentation on this operation.

### Usage for query.subDomains:

`cato query subDomains -h`

`cato query subDomains <accountID> <json>`

`cato query subDomains 12345 "$(cat < subDomains.json)"`

`cato query subDomains 12345 '{"managedAccount": "Boolean"}'`

#### Operation Arguments for query.subDomains ####
`accountID` [ID] - (required) Unique Identifier of Account 
`managedAccount` [Boolean] - (optional) When the boolean argument managedAccount is set to true (default), then the query returns all subdomains related to the account 
