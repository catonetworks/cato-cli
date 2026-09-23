
## CATO-CLI - mutation.posture.dismissFinding:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.posture.dismissFinding) for documentation on this operation.

### Usage for mutation.posture.dismissFinding:

```bash
catocli mutation posture dismissFinding -h

catocli mutation posture dismissFinding <json>

catocli mutation posture dismissFinding --json-file mutation.posture.dismissFinding.json

catocli mutation posture dismissFinding '{"postureDismissFindingInput":{"findingId":"id","reason":"string"}}'

catocli mutation posture dismissFinding '{
    "postureDismissFindingInput": {
        "findingId": "id",
        "reason": "string"
    }
}'
```

#### Operation Arguments for mutation.posture.dismissFinding ####

`accountId` [ID] - (required) N/A    
`postureDismissFindingInput` [PostureDismissFindingInput] - (required) N/A    
