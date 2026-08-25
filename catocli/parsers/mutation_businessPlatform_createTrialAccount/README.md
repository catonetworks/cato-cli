
## CATO-CLI - mutation.businessPlatform.createTrialAccount:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.businessPlatform.createTrialAccount) for documentation on this operation.

### Usage for mutation.businessPlatform.createTrialAccount:

```bash
catocli mutation businessPlatform createTrialAccount -h

catocli mutation businessPlatform createTrialAccount <json>

catocli mutation businessPlatform createTrialAccount --json-file mutation.businessPlatform.createTrialAccount.json

catocli mutation businessPlatform createTrialAccount '{"businessPlatformCreateTrialAccountInput":{"addAccountInput":{"description":"string","name":"string","tenancy":"SINGLE_TENANT","timezone":"example_value","type":"CUSTOMER"},"businessPlatformAdminData":{"email":"example_value","firstName":"string","lastName":"string"},"canManageSubAccounts":true,"id":"id"}}'

catocli mutation businessPlatform createTrialAccount '{
    "businessPlatformCreateTrialAccountInput": {
        "addAccountInput": {
            "description": "string",
            "name": "string",
            "tenancy": "SINGLE_TENANT",
            "timezone": "example_value",
            "type": "CUSTOMER"
        },
        "businessPlatformAdminData": {
            "email": "example_value",
            "firstName": "string",
            "lastName": "string"
        },
        "canManageSubAccounts": true,
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.businessPlatform.createTrialAccount ####

`accountId` [ID] - (required) N/A    
`businessPlatformCreateTrialAccountInput` [BusinessPlatformCreateTrialAccountInput] - (required) N/A    
