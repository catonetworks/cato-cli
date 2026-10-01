
## CATO-CLI - mutation.externalAccess.addPartnerAccessRequest:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.externalAccess.addPartnerAccessRequest) for documentation on this operation.

### Usage for mutation.externalAccess.addPartnerAccessRequest:

```bash
catocli mutation externalAccess addPartnerAccessRequest -h

catocli mutation externalAccess addPartnerAccessRequest <json>

catocli mutation externalAccess addPartnerAccessRequest --json-file mutation.externalAccess.addPartnerAccessRequest.json

catocli mutation externalAccess addPartnerAccessRequest '{"addPartnerAccessRequestInput":{"accounts":[{"by":"ID","input":"string"}],"admins":[{"by":"ID","input":"string"}],"expirationDate":"2026-01-02T15:04:05Z","groups":[{"by":"ID","input":"string"}],"isAppliedOnAllFullyManagedAccounts":true,"partner":{"by":"ID","input":"string"},"partnerNote":"string","reason":"string","roles":[{"by":"ID","input":"string"}],"supportLink":"string"}}'

catocli mutation externalAccess addPartnerAccessRequest '{
    "addPartnerAccessRequestInput": {
        "accounts": [
            {
                "by": "ID",
                "input": "string"
            }
        ],
        "admins": [
            {
                "by": "ID",
                "input": "string"
            }
        ],
        "expirationDate": "2026-01-02T15:04:05Z",
        "groups": [
            {
                "by": "ID",
                "input": "string"
            }
        ],
        "isAppliedOnAllFullyManagedAccounts": true,
        "partner": {
            "by": "ID",
            "input": "string"
        },
        "partnerNote": "string",
        "reason": "string",
        "roles": [
            {
                "by": "ID",
                "input": "string"
            }
        ],
        "supportLink": "string"
    }
}'
```

#### Operation Arguments for mutation.externalAccess.addPartnerAccessRequest ####

`accountId` [ID] - (required) N/A
`addPartnerAccessRequestInput` [AddPartnerAccessRequestInput] - (required) N/A
