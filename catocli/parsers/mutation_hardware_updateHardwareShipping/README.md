
## CATO-CLI - mutation.hardware.updateHardwareShipping:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.hardware.updateHardwareShipping) for documentation on this operation.

### Usage for mutation.hardware.updateHardwareShipping:

`catocli mutation hardware updateHardwareShipping -h`

`catocli mutation hardware updateHardwareShipping <json>`

`catocli mutation hardware updateHardwareShipping "$(cat < mutation.hardware.updateHardwareShipping.json)"`

`catocli mutation hardware updateHardwareShipping '{"updateHardwareShippingInput":{"hardwareShippingDetailsInput":{"details":{"address":{"cityName":"string","companyName":"string","countryName":"string","stateName":"string","street":"string","zipCode":"string"},"comment":"string","contact":{"email":"example_value","name":"string","phone":"example_value"},"incoterms":"string","instruction":"string","vatId":"string"},"powerCable":"string"},"ids":["id1","id2"]}}'`

`catocli mutation hardware updateHardwareShipping -p '{
    "updateHardwareShippingInput": {
        "hardwareShippingDetailsInput": {
            "details": {
                "address": {
                    "cityName": "string",
                    "companyName": "string",
                    "countryName": "string",
                    "stateName": "string",
                    "street": "string",
                    "zipCode": "string"
                },
                "comment": "string",
                "contact": {
                    "email": "example_value",
                    "name": "string",
                    "phone": "example_value"
                },
                "incoterms": "string",
                "instruction": "string",
                "vatId": "string"
            },
            "powerCable": "string"
        },
        "ids": [
            "id1",
            "id2"
        ]
    }
}'`


#### Operation Arguments for mutation.hardware.updateHardwareShipping ####

`accountId` [ID] - (required) N/A    
`updateHardwareShippingInput` [UpdateHardwareShippingInput] - (required) N/A    
