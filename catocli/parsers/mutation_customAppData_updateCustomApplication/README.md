
## CATO-CLI - mutation.customAppData.updateCustomApplication:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.customAppData.updateCustomApplication) for documentation on this operation.

### Usage for mutation.customAppData.updateCustomApplication:

```bash
catocli mutation customAppData updateCustomApplication -h

catocli mutation customAppData updateCustomApplication <json>

catocli mutation customAppData updateCustomApplication --json-file mutation.customAppData.updateCustomApplication.json

catocli mutation customAppData updateCustomApplication '{"updateCustomApplicationInput":{"applicationCategoryRefInput":{"by":"ID","input":"string"},"customApplicationCriteriaInput":{"destination":{"destinationIp":{"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"subnet":["example1","example2"]},"domain":["example1","example2"],"fqdn":["example1","example2"]},"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"description":"string","id":"id","name":"string"}}'

catocli mutation customAppData updateCustomApplication '{
    "updateCustomApplicationInput": {
        "applicationCategoryRefInput": {
            "by": "ID",
            "input": "string"
        },
        "customApplicationCriteriaInput": {
            "destination": {
                "destinationIp": {
                    "ip": [
                        "example1",
                        "example2"
                    ],
                    "ipRange": {
                        "from": "example_value",
                        "to": "example_value"
                    },
                    "subnet": [
                        "example1",
                        "example2"
                    ]
                },
                "domain": [
                    "example1",
                    "example2"
                ],
                "fqdn": [
                    "example1",
                    "example2"
                ]
            },
            "port": [
                "example1",
                "example2"
            ],
            "portRange": {
                "from": "example_value",
                "to": "example_value"
            },
            "protocol": "ANY"
        },
        "description": "string",
        "id": "id",
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.customAppData.updateCustomApplication ####

`accountId` [ID] - (required) N/A    
`updateCustomApplicationInput` [UpdateCustomApplicationInput] - (required) N/A    
