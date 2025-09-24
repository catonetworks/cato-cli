
## CATO-CLI - mutation.enterpriseDirectory.createLocation:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.enterpriseDirectory.createLocation) for documentation on this operation.

### Usage for mutation.enterpriseDirectory.createLocation:

`catocli mutation enterpriseDirectory createLocation -h`

`catocli mutation enterpriseDirectory createLocation <json>`

`catocli mutation enterpriseDirectory createLocation "$(cat < mutation.enterpriseDirectory.createLocation.json)"`

`catocli mutation enterpriseDirectory createLocation '{"enterpriseDirectoryCreateLocationInput":{"businessUnit":"string","createLocationDetailsInput":{"companyName":"string","contact":{"email":"example_value","name":"string","phone":"example_value"},"postalAddress":{"cityName":"string","country":{"by":"ID","input":"string"},"stateName":"string","street":"string","zipCode":"string"},"vatId":"string"},"description":"string","name":"string","type":"BRANCH"}}'`

`catocli mutation enterpriseDirectory createLocation -p '{
    "enterpriseDirectoryCreateLocationInput": {
        "businessUnit": "string",
        "createLocationDetailsInput": {
            "companyName": "string",
            "contact": {
                "email": "example_value",
                "name": "string",
                "phone": "example_value"
            },
            "postalAddress": {
                "cityName": "string",
                "country": {
                    "by": "ID",
                    "input": "string"
                },
                "stateName": "string",
                "street": "string",
                "zipCode": "string"
            },
            "vatId": "string"
        },
        "description": "string",
        "name": "string",
        "type": "BRANCH"
    }
}'`


#### Operation Arguments for mutation.enterpriseDirectory.createLocation ####

`accountId` [ID] - (required) N/A    
`enterpriseDirectoryCreateLocationInput` [EnterpriseDirectoryCreateLocationInput] - (required) N/A    
