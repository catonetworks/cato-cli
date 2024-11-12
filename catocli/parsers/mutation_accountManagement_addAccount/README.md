
## CATO-CLI - mutation.accountManagement.addAccount:
[Click here](https://api.catonetworks.com/documentation/#mutation-addAccount) for documentation on this operation.

### Usage for mutation.accountManagement.addAccount:

`catocli mutation accountManagement addAccount -h`

`catocli mutation accountManagement addAccount <json>`

`catocli mutation accountManagement addAccount "$(cat < addAccount.json)"`

`catocli mutation accountManagement addAccount '{"addAccountInput": {"description": {"description": "String"}, "name": {"name": "String"}, "tenancy": {"tenancy": "enum(AccountTenancy)"}, "timezone": {"timezone": "TimeZone"}, "type": {"type": "enum(AccountProfileType)"}}}'`

#### Operation Arguments for mutation.accountManagement.addAccount ####
`accountId` [ID] - (required) N/A 
`addAccountInput` [AddAccountInput] - (required) N/A 
