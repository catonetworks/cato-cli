
## CATO-CLI - mutation.externalAccess.addPartnerAccessRequest:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.externalAccess.addPartnerAccessRequest) for documentation on this operation.

### Usage for mutation.externalAccess.addPartnerAccessRequest:

```bash
catocli mutation externalAccess addPartnerAccessRequest -h

catocli mutation externalAccess addPartnerAccessRequest <json>

catocli mutation externalAccess addPartnerAccessRequest --json-file mutation.externalAccess.addPartnerAccessRequest.json

catocli mutation externalAccess addPartnerAccessRequest '{"addPartnerAccessRequestInput":{"accountRefInput":{"by":"ID","input":"string"},"adminRefInput":{"by":"ID","input":"string"},"expirationDate":"example_value","isAppliedOnAllFullyManagedAccounts":true,"partnerNote":"string","rBACRoleRefInput":{"by":"ID","input":"string"},"reason":"string","supportLink":"string","usersGroupRefInput":{"by":"ID","input":"string"}}}'

catocli mutation externalAccess addPartnerAccessRequest '{
    "addPartnerAccessRequestInput": {
        "accountRefInput": {
            "by": "ID",
            "input": "string"
        },
        "adminRefInput": {
            "by": "ID",
            "input": "string"
        },
        "expirationDate": "example_value",
        "isAppliedOnAllFullyManagedAccounts": true,
        "partnerNote": "string",
        "rBACRoleRefInput": {
            "by": "ID",
            "input": "string"
        },
        "reason": "string",
        "supportLink": "string",
        "usersGroupRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.externalAccess.addPartnerAccessRequest ####

`accountId` [ID] - (required) N/A    
`addPartnerAccessRequestInput` [AddPartnerAccessRequestInput] - (required) N/A    
