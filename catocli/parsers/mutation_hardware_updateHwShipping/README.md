
## CATO-CLI - mutation.hardware.updateHwShipping:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.hardware.updateHwShipping) for documentation on this operation.

### Usage for mutation.hardware.updateHwShipping:

```bash
catocli mutation hardware updateHwShipping -h

catocli mutation hardware updateHwShipping <json>

catocli mutation hardware updateHwShipping --json-file mutation.hardware.updateHwShipping.json

catocli mutation hardware updateHwShipping '{"updateHwShippingInput":{"hwShippingDetailsInput":{"details":{"address":"id","comment":"string","incoterms":"string","instruction":"string"},"powerCable":"string"},"ids":["id1","id2"]}}'

catocli mutation hardware updateHwShipping '{
    "updateHwShippingInput": {
        "hwShippingDetailsInput": {
            "details": {
                "address": "id",
                "comment": "string",
                "incoterms": "string",
                "instruction": "string"
            },
            "powerCable": "string"
        },
        "ids": [
            "id1",
            "id2"
        ]
    }
}'
```

#### Operation Arguments for mutation.hardware.updateHwShipping ####

`accountId` [ID] - (required) N/A    
`updateHwShippingInput` [UpdateHwShippingInput] - (required) N/A    
