
## CATO-CLI - mutation.posture.unmuteCheck:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.posture.unmuteCheck) for documentation on this operation.

### Usage for mutation.posture.unmuteCheck:

```bash
catocli mutation posture unmuteCheck -h

catocli mutation posture unmuteCheck <json>

catocli mutation posture unmuteCheck --json-file mutation.posture.unmuteCheck.json

catocli mutation posture unmuteCheck '{"postureUnmuteCheckInput":{"checkId":"id"}}'

catocli mutation posture unmuteCheck '{
    "postureUnmuteCheckInput": {
        "checkId": "id"
    }
}'
```

#### Operation Arguments for mutation.posture.unmuteCheck ####

`accountId` [ID] - (required) ID of the account whose Posture configuration or findings are modified. 
`postureUnmuteCheckInput` [PostureUnmuteCheckInput] - (required) Check result id to restore from a muted state. 
