
## CATO-CLI - mutation.user.revokeUserSession:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.user.revokeUserSession) for documentation on this operation.

### Usage for mutation.user.revokeUserSession:

```bash
catocli mutation user revokeUserSession -h

catocli mutation user revokeUserSession <json>

catocli mutation user revokeUserSession --json-file mutation.user.revokeUserSession.json

catocli mutation user revokeUserSession '{"revokeUserSessionInput":{"userId":["example1","example2"]}}'

catocli mutation user revokeUserSession '{
    "revokeUserSessionInput": {
        "userId": [
            "example1",
            "example2"
        ]
    }
}'
```

#### Operation Arguments for mutation.user.revokeUserSession ####

`accountId` [ID] - (required) Unique identifier of the Cato account.    
`revokeUserSessionInput` [RevokeUserSessionInput] - (required) N/A    
