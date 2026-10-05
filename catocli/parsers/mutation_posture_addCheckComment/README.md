
## CATO-CLI - mutation.posture.addCheckComment:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.posture.addCheckComment) for documentation on this operation.

### Usage for mutation.posture.addCheckComment:

```bash
catocli mutation posture addCheckComment -h

catocli mutation posture addCheckComment <json>

catocli mutation posture addCheckComment --json-file mutation.posture.addCheckComment.json

catocli mutation posture addCheckComment '{"addCheckCommentInput":{"checkId":"id","text":"string"}}'

catocli mutation posture addCheckComment '{
    "addCheckCommentInput": {
        "checkId": "id",
        "text": "string"
    }
}'
```

#### Operation Arguments for mutation.posture.addCheckComment ####

`accountId` [ID] - (required) ID of the account whose Posture configuration or findings are modified.
`addCheckCommentInput` [AddCheckCommentInput] - (required) Check result id and comment text.
