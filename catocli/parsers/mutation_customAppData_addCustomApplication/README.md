
## CATO-CLI - mutation.customAppData.addCustomApplication:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.customAppData.addCustomApplication) for documentation on this operation.

### Usage for mutation.customAppData.addCustomApplication:

```bash
catocli mutation customAppData addCustomApplication -h

catocli mutation customAppData addCustomApplication <json>

catocli mutation customAppData addCustomApplication --json-file mutation.customAppData.addCustomApplication.json

catocli mutation customAppData addCustomApplication '{"addCustomApplicationInput":{"applicationCategoryRefInput":{"by":"ID","input":"string"},"customApplicationCriteriaInput":{"destination":{"destinationIp":{"ip":["example1","example2"],"ipRange":{"from":"example_value","to":"example_value"},"subnet":["example1","example2"]},"domain":["example1","example2"],"fqdn":["example1","example2"]},"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"description":"string","name":"string"}}'

catocli mutation customAppData addCustomApplication '{
    "addCustomApplicationInput": {
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
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.customAppData.addCustomApplication ####

`accountId` [ID] - (required) N/A    
`addCustomApplicationInput` [AddCustomApplicationInput] - (required) N/A    
