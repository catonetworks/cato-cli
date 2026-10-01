
## CATO-CLI - mutation.customAppData.addCustomApplication:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.customAppData.addCustomApplication) for documentation on this operation.

### Usage for mutation.customAppData.addCustomApplication:

```bash
catocli mutation customAppData addCustomApplication -h

catocli mutation customAppData addCustomApplication <json>

catocli mutation customAppData addCustomApplication --json-file mutation.customAppData.addCustomApplication.json

catocli mutation customAppData addCustomApplication '{"addCustomApplicationInput":{"category":[{"by":"ID","input":"string"}],"criteria":[{"destination":{"destinationIp":{"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"subnet":["192.0.2.0/24"]},"domain":["internal.example.com"],"fqdn":["host.example.com"]},"port":[443],"portRange":[{"from":443,"to":443}],"protocol":"ANY"}],"description":"string","name":"string"}}'

catocli mutation customAppData addCustomApplication '{
    "addCustomApplicationInput": {
        "category": [
            {
                "by": "ID",
                "input": "string"
            }
        ],
        "criteria": [
            {
                "destination": {
                    "destinationIp": {
                        "ip": [
                            "192.0.2.1"
                        ],
                        "ipRange": [
                            {
                                "from": "192.0.2.1",
                                "to": "192.0.2.1"
                            }
                        ],
                        "subnet": [
                            "192.0.2.0/24"
                        ]
                    },
                    "domain": [
                        "internal.example.com"
                    ],
                    "fqdn": [
                        "host.example.com"
                    ]
                },
                "port": [
                    443
                ],
                "portRange": [
                    {
                        "from": 443,
                        "to": 443
                    }
                ],
                "protocol": "ANY"
            }
        ],
        "description": "string",
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.customAppData.addCustomApplication ####

`accountId` [ID] - (required) N/A
`addCustomApplicationInput` [AddCustomApplicationInput] - (required) N/A
