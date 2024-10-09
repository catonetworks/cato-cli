
## CATO-CLI - query.accountRoles:
[Click here](https://api.catonetworks.com/documentation/#query-accountRoles) for documentation on this operation.

### Usage for query.accountRoles:

`catocli query accountRoles -h`

`catocli query accountRoles <accountID> <json>`

`catocli query accountRoles 12345 "$(cat < accountRoles.json)"`

`catocli query accountRoles 12345 '{"accountType": "enum(AccountType)"}'`

#### Operation Arguments for query.accountRoles ####
`accountID` [ID] - (required) N/A 
`accountType` [AccountType] - (optional) N/A Default Value: ['SYSTEM', 'REGULAR', 'RESELLER', 'ALL']
