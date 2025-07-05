
## CATO-CLI - mutation.hardware.updateHardwareShipping:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateHardwareShipping) for documentation on this operation.

### Usage for mutation.hardware.updateHardwareShipping:

`catocli mutation hardware updateHardwareShipping -h`

`catocli mutation hardware updateHardwareShipping <json>`

`catocli mutation hardware updateHardwareShipping "$(cat < updateHardwareShipping.json)"`

`catocli mutation hardware updateHardwareShipping '{"updateHardwareShippingInput": {"hardwareShippingDetailsInput": {"details": {"address": {"cityName": {"cityName": "String"}, "companyName": {"companyName": "String"}, "countryName": {"countryName": "String"}, "stateName": {"stateName": "String"}, "street": {"street": "String"}, "zipCode": {"zipCode": "String"}}, "comment": {"comment": "String"}, "contact": {"email": {"email": "Email"}, "name": {"name": "String"}, "phone": {"phone": "Phone"}}, "incoterms": {"incoterms": "String"}, "instruction": {"instruction": "String"}, "vatId": {"vatId": "String"}}, "powerCable": {"powerCable": "String"}}, "ids": {"ids": ["ID"]}}}'`

#### Operation Arguments for mutation.hardware.updateHardwareShipping ####
`accountId` [ID] - (required) N/A 
`updateHardwareShippingInput` [UpdateHardwareShippingInput] - (required) N/A 
