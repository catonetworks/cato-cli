
## CATO-CLI - mutation.hardware.moveSocketsToAccount:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.hardware.moveSocketsToAccount) for documentation on this operation.

### Usage for mutation.hardware.moveSocketsToAccount:

```bash
catocli mutation hardware moveSocketsToAccount -h

catocli mutation hardware moveSocketsToAccount <json>

catocli mutation hardware moveSocketsToAccount --json-file mutation.hardware.moveSocketsToAccount.json

catocli mutation hardware moveSocketsToAccount '{"moveSocketsToAccountInput":{"socketIds":["id1","id2"],"targetAccountId":"id"}}'

catocli mutation hardware moveSocketsToAccount '{
    "moveSocketsToAccountInput": {
        "socketIds": [
            "id1",
            "id2"
        ],
        "targetAccountId": "id"
    }
}'
```

#### Operation Arguments for mutation.hardware.moveSocketsToAccount ####

`accountId` [ID] - (required) N/A
`moveSocketsToAccountInput` [MoveSocketsToAccountInput] - (required) N/A
