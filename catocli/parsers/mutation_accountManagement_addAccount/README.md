
## CATO-CLI - mutation.accountManagement.addAccount:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.accountManagement.addAccount) for documentation on this operation.

### Usage for mutation.accountManagement.addAccount:

`catocli mutation accountManagement addAccount -h`

`catocli mutation accountManagement addAccount <json>`

`catocli mutation accountManagement addAccount "$(cat < mutation.accountManagement.addAccount.json)"`

`catocli mutation accountManagement addAccount '{"addAccountInput":{"description":"string","name":"string","tenancy":"SINGLE_TENANT","timezone":"example_value","type":"CUSTOMER"}}'`

`catocli mutation accountManagement addAccount -p '{
    "addAccountInput": {
        "description": "string",
        "name": "string",
        "tenancy": "SINGLE_TENANT",
        "timezone": "example_value",
        "type": "CUSTOMER"
    }
}'`


#### Operation Arguments for mutation.accountManagement.addAccount ####

`accountId` [ID] - (required) N/A    
`addAccountInput` [AddAccountInput] - (required) N/A    
