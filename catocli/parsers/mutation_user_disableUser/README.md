
## CATO-CLI - mutation.user.disableUser:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.user.disableUser) for documentation on this operation.

### Usage for mutation.user.disableUser:

```bash
catocli mutation user disableUser -h

catocli mutation user disableUser <json>

catocli mutation user disableUser --json-file mutation.user.disableUser.json

catocli mutation user disableUser '{"disableUserInput":{"userId":[1,2]}}'

catocli mutation user disableUser '{
    "disableUserInput": {
        "userId": [
            1,
            2
        ]
    }
}'
```

#### Operation Arguments for mutation.user.disableUser ####

`accountId` [ID] - (required) Unique identifier of the Cato account.    
`disableUserInput` [DisableUserInput] - (required) N/A    
