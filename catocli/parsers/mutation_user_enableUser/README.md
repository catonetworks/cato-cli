
## CATO-CLI - mutation.user.enableUser:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.user.enableUser) for documentation on this operation.

### Usage for mutation.user.enableUser:

```bash
catocli mutation user enableUser -h

catocli mutation user enableUser <json>

catocli mutation user enableUser --json-file mutation.user.enableUser.json

catocli mutation user enableUser '{"enableUserInput":{"userId":["example1","example2"]}}'

catocli mutation user enableUser '{
    "enableUserInput": {
        "userId": [
            "example1",
            "example2"
        ]
    }
}'
```

#### Operation Arguments for mutation.user.enableUser ####

`accountId` [ID] - (required) Unique identifier of the Cato account.    
`enableUserInput` [EnableUserInput] - (required) N/A    
