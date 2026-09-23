
## CATO-CLI - mutation.user.updateUser:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.user.updateUser) for documentation on this operation.

### Usage for mutation.user.updateUser:

```bash
catocli mutation user updateUser -h

catocli mutation user updateUser <json>

catocli mutation user updateUser --json-file mutation.user.updateUser.json

catocli mutation user updateUser '{"updateUserInput":{"department":"string","email":"example_value","firstName":"string","id":"id","jobTitle":"string","lastName":"string","phoneNumber":"example_value"}}'

catocli mutation user updateUser '{
    "updateUserInput": {
        "department": "string",
        "email": "example_value",
        "firstName": "string",
        "id": "id",
        "jobTitle": "string",
        "lastName": "string",
        "phoneNumber": "example_value"
    }
}'
```

#### Operation Arguments for mutation.user.updateUser ####

`accountId` [ID] - (required) Unique identifier of the Cato account.    
`updateUserInput` [UpdateUserInput] - (required) N/A    
