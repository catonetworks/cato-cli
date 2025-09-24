
## CATO-CLI - mutation.enterpriseDirectory.updateLocation:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.enterpriseDirectory.updateLocation) for documentation on this operation.

### Usage for mutation.enterpriseDirectory.updateLocation:

`catocli mutation enterpriseDirectory updateLocation -h`

`catocli mutation enterpriseDirectory updateLocation <json>`

`catocli mutation enterpriseDirectory updateLocation "$(cat < mutation.enterpriseDirectory.updateLocation.json)"`

`catocli mutation enterpriseDirectory updateLocation '{"enterpriseDirectoryUpdateLocationInput":{"businessUnit":"string","description":"string","id":"id","name":"string","type":"BRANCH","updateLocationDetailsInput":{"companyName":"string","contact":{"email":"example_value","name":"string","phone":"example_value"},"postalAddress":{"cityName":"string","country":{"by":"ID","input":"string"},"stateName":"string","street":"string","zipCode":"string"},"vatId":"string"}}}'`

`catocli mutation enterpriseDirectory updateLocation -p '{
    "enterpriseDirectoryUpdateLocationInput": {
        "businessUnit": "string",
        "description": "string",
        "id": "id",
        "name": "string",
        "type": "BRANCH",
        "updateLocationDetailsInput": {
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
        }
    }
}'`


#### Operation Arguments for mutation.enterpriseDirectory.updateLocation ####

`accountId` [ID] - (required) N/A    
`enterpriseDirectoryUpdateLocationInput` [EnterpriseDirectoryUpdateLocationInput] - (required) N/A    
