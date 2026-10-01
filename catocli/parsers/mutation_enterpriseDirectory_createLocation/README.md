
## CATO-CLI - mutation.enterpriseDirectory.createLocation:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.enterpriseDirectory.createLocation) for documentation on this operation.

### Usage for mutation.enterpriseDirectory.createLocation:

```bash
catocli mutation enterpriseDirectory createLocation -h

catocli mutation enterpriseDirectory createLocation <json>

catocli mutation enterpriseDirectory createLocation --json-file mutation.enterpriseDirectory.createLocation.json

catocli mutation enterpriseDirectory createLocation '{"enterpriseDirectoryCreateLocationInput":{"businessUnit":"string","description":"string","details":{"companyName":"string","contact":{"email":"user@example.com","name":"string","phone":"+15053334070"},"postalAddress":{"address1":"string","address2":"string","cityName":"string","country":{"by":"ID","input":"string"},"stateName":"string","zipCode":"string"},"vatId":"string"},"name":"string","type":"BRANCH"}}'

catocli mutation enterpriseDirectory createLocation '{
    "enterpriseDirectoryCreateLocationInput": {
        "businessUnit": "string",
        "description": "string",
        "details": {
            "companyName": "string",
            "contact": {
                "email": "user@example.com",
                "name": "string",
                "phone": "+15053334070"
            },
            "postalAddress": {
                "address1": "string",
                "address2": "string",
                "cityName": "string",
                "country": {
                    "by": "ID",
                    "input": "string"
                },
                "stateName": "string",
                "zipCode": "string"
            },
            "vatId": "string"
        },
        "name": "string",
        "type": "BRANCH"
    }
}'
```

#### Operation Arguments for mutation.enterpriseDirectory.createLocation ####

`accountId` [ID] - (required) N/A
`enterpriseDirectoryCreateLocationInput` [EnterpriseDirectoryCreateLocationInput] - (required) N/A
