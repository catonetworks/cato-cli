
## CATO-CLI - mutation.posture.muteCheck:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.posture.muteCheck) for documentation on this operation.

### Usage for mutation.posture.muteCheck:

```bash
catocli mutation posture muteCheck -h

catocli mutation posture muteCheck <json>

catocli mutation posture muteCheck --json-file mutation.posture.muteCheck.json

catocli mutation posture muteCheck '{"postureMuteCheckInput":{"checkId":"id","durationInDays":1,"reason":"string"}}'

catocli mutation posture muteCheck '{
    "postureMuteCheckInput": {
        "checkId": "id",
        "durationInDays": 1,
        "reason": "string"
    }
}'
```

#### Operation Arguments for mutation.posture.muteCheck ####

`accountId` [ID] - (required) ID of the account whose Posture configuration or findings are modified. 
`postureMuteCheckInput` [PostureMuteCheckInput] - (required) Check result id, mute duration, and optional reason. 
