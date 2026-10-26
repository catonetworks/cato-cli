
## CATO-CLI - mutation.access:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.access) for documentation on this operation.

### Usage for mutation.access:

```bash
catocli mutation access -h

catocli mutation access <json>

catocli mutation access --json-file mutation.access.json

catocli mutation access '{"accessRemoteAccessSetEligibilityListInput":{"allocationType":"ALL","items":[{"user":{"by":"ID","input":"string"},"userGroup":{"by":"ID","input":"string"}}]}}'

catocli mutation access '{
    "accessRemoteAccessSetEligibilityListInput": {
        "allocationType": "ALL",
        "items": [
            {
                "user": {
                    "by": "ID",
                    "input": "string"
                },
                "userGroup": {
                    "by": "ID",
                    "input": "string"
                }
            }
        ]
    }
}'
```

#### Operation Arguments for mutation.access ####

`accessRemoteAccessSetEligibilityListInput` [AccessRemoteAccessSetEligibilityListInput] - (optional) N/A
`accountId` [ID] - (required) Unique identifier of the Cato account.
