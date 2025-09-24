
## CATO-CLI - query.accountRoles:
[Click here](https://api.catonetworks.com/documentation/#query-query.accountRoles) for documentation on this operation.

### Usage for query.accountRoles:

`catocli query accountRoles -h`

`catocli query accountRoles <json>`

`catocli query accountRoles "$(cat < query.accountRoles.json)"`

`catocli query accountRoles '{"accountType":"SYSTEM"}'`

`catocli query accountRoles -p '{
    "accountType": "SYSTEM"
}'`


#### Operation Arguments for query.accountRoles ####

`accountID` [ID] - (required) N/A    
`accountType` [AccountType] - (required) N/A Default Value: ['SYSTEM', 'REGULAR', 'RESELLER', 'ALL']   
