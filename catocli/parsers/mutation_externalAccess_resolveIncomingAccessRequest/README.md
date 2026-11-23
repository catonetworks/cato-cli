
## CATO-CLI - mutation.externalAccess.resolveIncomingAccessRequest:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.externalAccess.resolveIncomingAccessRequest) for documentation on this operation.

### Usage for mutation.externalAccess.resolveIncomingAccessRequest:

```bash
catocli mutation externalAccess resolveIncomingAccessRequest -h

catocli mutation externalAccess resolveIncomingAccessRequest <json>

catocli mutation externalAccess resolveIncomingAccessRequest --json-file mutation.externalAccess.resolveIncomingAccessRequest.json

catocli mutation externalAccess resolveIncomingAccessRequest '{"resolveIncomingAccessRequestInput":{"approval":"APPROVE","note":"string","requestId":"id"}}'

catocli mutation externalAccess resolveIncomingAccessRequest '{
    "resolveIncomingAccessRequestInput": {
        "approval": "APPROVE",
        "note": "string",
        "requestId": "id"
    }
}'
```

#### Operation Arguments for mutation.externalAccess.resolveIncomingAccessRequest ####

`accountId` [ID] - (required) ID of the account in which to manage external access requests.
`resolveIncomingAccessRequestInput` [ResolveIncomingAccessRequestInput] - (required) Access request to approve or reject, with the decision and an optional note.
