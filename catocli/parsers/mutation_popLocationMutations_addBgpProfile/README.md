
## CATO-CLI - mutation.popLocationMutations.addBgpProfile:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.popLocationMutations.addBgpProfile) for documentation on this operation.

### Usage for mutation.popLocationMutations.addBgpProfile:

```bash
catocli mutation popLocationMutations addBgpProfile -h

catocli mutation popLocationMutations addBgpProfile <json>

catocli mutation popLocationMutations addBgpProfile --json-file mutation.popLocationMutations.addBgpProfile.json

catocli mutation popLocationMutations addBgpProfile '{"popLocationAddBgpProfileInput":{"communities":[{"from":64512,"to":64512}],"description":"string","name":"string"}}'

catocli mutation popLocationMutations addBgpProfile '{
    "popLocationAddBgpProfileInput": {
        "communities": [
            {
                "from": 64512,
                "to": 64512
            }
        ],
        "description": "string",
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.popLocationMutations.addBgpProfile ####

`accountId` [ID] - (required) N/A
`popLocationAddBgpProfileInput` [PopLocationAddBgpProfileInput] - (required) N/A
