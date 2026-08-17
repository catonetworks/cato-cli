
## CATO-CLI - mutation.user.deleteUser:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.user.deleteUser) for documentation on this operation.

### Usage for mutation.user.deleteUser:

```bash
catocli mutation user deleteUser -h

catocli mutation user deleteUser <json>

catocli mutation user deleteUser --json-file mutation.user.deleteUser.json

catocli mutation user deleteUser '{"deleteUserInput":{"userId":[1,2]}}'

catocli mutation user deleteUser '{
    "deleteUserInput": {
        "userId": [
            1,
            2
        ]
    }
}'
```

#### Operation Arguments for mutation.user.deleteUser ####

`accountId` [ID] - (required) Unique identifier of the Cato account.    
`deleteUserInput` [DeleteUserInput] - (required) N/A    
