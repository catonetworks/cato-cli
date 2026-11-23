
## CATO-CLI - mutation.externalAccess.revokePartnerAccess:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.externalAccess.revokePartnerAccess) for documentation on this operation.

### Usage for mutation.externalAccess.revokePartnerAccess:

```bash
catocli mutation externalAccess revokePartnerAccess -h

catocli mutation externalAccess revokePartnerAccess <json>

catocli mutation externalAccess revokePartnerAccess --json-file mutation.externalAccess.revokePartnerAccess.json

catocli mutation externalAccess revokePartnerAccess '{"revokePartnerAccessInput":{"invitationId":"id","reason":"string"}}'

catocli mutation externalAccess revokePartnerAccess '{
    "revokePartnerAccessInput": {
        "invitationId": "id",
        "reason": "string"
    }
}'
```

#### Operation Arguments for mutation.externalAccess.revokePartnerAccess ####

`accountId` [ID] - (required) ID of the account in which to manage external access requests.
`revokePartnerAccessInput` [RevokePartnerAccessInput] - (required) Access request to revoke and the reason for revoking access.
