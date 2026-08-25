
## CATO-CLI - mutation.privateApplication.deletePrivateApplication:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.privateApplication.deletePrivateApplication) for documentation on this operation.

### Usage for mutation.privateApplication.deletePrivateApplication:

```bash
catocli mutation privateApplication deletePrivateApplication -h

catocli mutation privateApplication deletePrivateApplication <json>

catocli mutation privateApplication deletePrivateApplication --json-file mutation.privateApplication.deletePrivateApplication.json

catocli mutation privateApplication deletePrivateApplication '{"deletePrivateApplicationInput":{"privateApplicationRefInput":{"by":"ID","input":"string"}}}'

catocli mutation privateApplication deletePrivateApplication '{
    "deletePrivateApplicationInput": {
        "privateApplicationRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.privateApplication.deletePrivateApplication ####

`accountId` [ID] - (required) N/A    
`deletePrivateApplicationInput` [DeletePrivateApplicationInput] - (required) N/A    
