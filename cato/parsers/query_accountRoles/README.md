
## CATO-CLI - query.accountRoles:
[Click here](https://api.catonetworks.com/documentation/#query-accountRoles) for documentation on this operation.

### Usage for query.accountRoles:

`cato query accountRoles -h`

`cato query accountRoles <accountID> <json>`

`cato query accountRoles 12345 "$(cat < accountRoles.json)"`

`cato query accountRoles 12345 '{"accountType": "enum(AccountType)"}'`

#### Operation Arguments for query.accountRoles ####
`accountID` [ID] - (required) N/A 
`accountType` [AccountType] - (optional) N/A Default Value: ['SYSTEM', 'REGULAR', 'RESELLER', 'ALL']
