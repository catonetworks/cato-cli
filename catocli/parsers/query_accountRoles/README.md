
## CATO-CLI - query.accountRoles:
[Click here](https://api.catonetworks.com/documentation/#query-accountRoles) for documentation on this operation.

### Usage for query.accountRoles:

`catocli query accountRoles -h`

`catocli query accountRoles <json>`

`catocli query accountRoles "$(cat < accountRoles.json)"`

`catocli query accountRoles '{"accountType": "enum(AccountType)"}'`

#### Operation Arguments for query.accountRoles ####
`accountID` [ID] - (required) N/A 
`accountType` [AccountType] - (optional) N/A Default Value: ['SYSTEM', 'REGULAR', 'RESELLER', 'ALL']
