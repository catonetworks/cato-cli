
## CATO-CLI - query.site.retrieveUsedVlanIDs:
[Click here](https://api.catonetworks.com/documentation/#query-query.site.retrieveUsedVlanIDs) for documentation on this operation.

### Usage for query.site.retrieveUsedVlanIDs:

```bash
catocli query site retrieveUsedVlanIDs -h

catocli query site retrieveUsedVlanIDs <json>

catocli query site retrieveUsedVlanIDs --json-file query.site.retrieveUsedVlanIDs.json

catocli query site retrieveUsedVlanIDs '{"retrieveUsedVlanIDsInput":{"encapsulationMethod":"DOT1Q","popLocationRefInput":{"by":"ID","input":"string"},"serviceProviderName":"string"}}'

catocli query site retrieveUsedVlanIDs '{
    "retrieveUsedVlanIDsInput": {
        "encapsulationMethod": "DOT1Q",
        "popLocationRefInput": {
            "by": "ID",
            "input": "string"
        },
        "serviceProviderName": "string"
    }
}'
```

#### Operation Arguments for query.site.retrieveUsedVlanIDs ####

`accountId` [ID] - (required) N/A    
`retrieveUsedVlanIDsInput` [RetrieveUsedVlanIDsInput] - (required) N/A    
