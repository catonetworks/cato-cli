
## CATO-CLI - mutation.posture.muteFinding:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.posture.muteFinding) for documentation on this operation.

### Usage for mutation.posture.muteFinding:

```bash
catocli mutation posture muteFinding -h

catocli mutation posture muteFinding <json>

catocli mutation posture muteFinding --json-file mutation.posture.muteFinding.json

catocli mutation posture muteFinding '{"accountId":"id","postureMuteFindingInput":{"durationInDays":1,"findingId":"id","reason":"string"}}'

catocli mutation posture muteFinding '{
    "accountId": "id",
    "postureMuteFindingInput": {
        "durationInDays": 1,
        "findingId": "id",
        "reason": "string"
    }
}'
```

#### Operation Arguments for mutation.posture.muteFinding ####

`accountId` [ID] - (required) N/A    
`postureMuteFindingInput` [PostureMuteFindingInput] - (required) N/A    
