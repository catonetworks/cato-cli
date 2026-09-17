
## CATO-CLI - mutation.externalAccess.cancelPartnerAccess:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.externalAccess.cancelPartnerAccess) for documentation on this operation.

### Usage for mutation.externalAccess.cancelPartnerAccess:

```bash
catocli mutation externalAccess cancelPartnerAccess -h

catocli mutation externalAccess cancelPartnerAccess <json>

catocli mutation externalAccess cancelPartnerAccess --json-file mutation.externalAccess.cancelPartnerAccess.json

catocli mutation externalAccess cancelPartnerAccess '{"cancelPartnerAccessInput":{"invitationId":"id","reason":"string"}}'

catocli mutation externalAccess cancelPartnerAccess '{
    "cancelPartnerAccessInput": {
        "invitationId": "id",
        "reason": "string"
    }
}'
```

#### Operation Arguments for mutation.externalAccess.cancelPartnerAccess ####

`accountId` [ID] - (required) N/A    
`cancelPartnerAccessInput` [CancelPartnerAccessInput] - (required) N/A    
