
## CATO-CLI - mutation.user.createUser:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.user.createUser) for documentation on this operation.

### Usage for mutation.user.createUser:

```bash
catocli mutation user createUser -h

catocli mutation user createUser <json>

catocli mutation user createUser --json-file mutation.user.createUser.json

catocli mutation user createUser '{"createUserInput":{"department":"string","email":"user@example.com","firstName":"string","jobTitle":"string","lastName":"string","phoneNumber":"+15053334070"}}'

catocli mutation user createUser '{
    "createUserInput": {
        "department": "string",
        "email": "user@example.com",
        "firstName": "string",
        "jobTitle": "string",
        "lastName": "string",
        "phoneNumber": "+15053334070"
    }
}'
```

#### Operation Arguments for mutation.user.createUser ####

`accountId` [ID] - (required) Unique identifier of the Cato account.
`createUserInput` [CreateUserInput] - (required) N/A
