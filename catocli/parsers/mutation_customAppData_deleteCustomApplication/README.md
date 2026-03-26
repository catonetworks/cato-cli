
## CATO-CLI - mutation.customAppData.deleteCustomApplication:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.customAppData.deleteCustomApplication) for documentation on this operation.

### Usage for mutation.customAppData.deleteCustomApplication:

```bash
catocli mutation customAppData deleteCustomApplication -h

catocli mutation customAppData deleteCustomApplication <json>

catocli mutation customAppData deleteCustomApplication --json-file mutation.customAppData.deleteCustomApplication.json

catocli mutation customAppData deleteCustomApplication '{"deleteCustomApplicationInput":{"customApplicationRefInput":{"by":"ID","input":"string"}}}'

catocli mutation customAppData deleteCustomApplication '{
    "deleteCustomApplicationInput": {
        "customApplicationRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.customAppData.deleteCustomApplication ####

`accountId` [ID] - (required) N/A    
`deleteCustomApplicationInput` [DeleteCustomApplicationInput] - (required) N/A    
