
## CATO-CLI - mutation.customAppData.updateCustomApplication:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.customAppData.updateCustomApplication) for documentation on this operation.

### Usage for mutation.customAppData.updateCustomApplication:

```bash
catocli mutation customAppData updateCustomApplication -h

catocli mutation customAppData updateCustomApplication <json>

catocli mutation customAppData updateCustomApplication --json-file mutation.customAppData.updateCustomApplication.json

catocli mutation customAppData updateCustomApplication '{"updateCustomApplicationInput":{"category":[{"by":"ID","input":"string"}],"criteria":[{"destination":{"destinationIp":{"ip":["192.0.2.1"],"ipRange":[{"from":"192.0.2.1","to":"192.0.2.1"}],"subnet":["192.0.2.0/24"]},"domain":["internal.example.com"],"fqdn":["host.example.com"]},"port":[443],"portRange":[{"from":443,"to":443}],"protocol":"ANY"}],"description":"string","id":"id","name":"string"}}'

catocli mutation customAppData updateCustomApplication '{
    "updateCustomApplicationInput": {
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
        "id": "id",
        "name": "string"
    }
}'
```

#### Operation Arguments for mutation.customAppData.updateCustomApplication ####

`accountId` [ID] - (required) N/A
`updateCustomApplicationInput` [UpdateCustomApplicationInput] - (required) N/A
