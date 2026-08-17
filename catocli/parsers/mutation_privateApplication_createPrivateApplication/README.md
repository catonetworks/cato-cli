
## CATO-CLI - mutation.privateApplication.createPrivateApplication:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.privateApplication.createPrivateApplication) for documentation on this operation.

### Usage for mutation.privateApplication.createPrivateApplication:

```bash
catocli mutation privateApplication createPrivateApplication -h

catocli mutation privateApplication createPrivateApplication <json>

catocli mutation privateApplication createPrivateApplication --json-file mutation.privateApplication.createPrivateApplication.json

catocli mutation privateApplication createPrivateApplication '{"createPrivateApplicationInput":{"allowIcmpProtocol":true,"customServiceInput":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"description":"string","internalAppAddress":"example_value","name":"string","privateAppProbingInput":{"faultThresholdDown":1,"id":"id","interval":1,"type":"string"},"probingEnabled":true,"published":true,"publishedAppDomainInput":{"catoIp":"example_value","connectorGroupName":"string","creationTime":"example_value","id":"id","publishedAppDomain":"string"}}}'

catocli mutation privateApplication createPrivateApplication '{
    "createPrivateApplicationInput": {
        "allowIcmpProtocol": true,
        "customServiceInput": {
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
        "internalAppAddress": "example_value",
        "name": "string",
        "privateAppProbingInput": {
            "faultThresholdDown": 1,
            "id": "id",
            "interval": 1,
            "type": "string"
        },
        "probingEnabled": true,
        "published": true,
        "publishedAppDomainInput": {
            "catoIp": "example_value",
            "connectorGroupName": "string",
            "creationTime": "example_value",
            "id": "id",
            "publishedAppDomain": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.privateApplication.createPrivateApplication ####

`accountId` [ID] - (required) N/A    
`createPrivateApplicationInput` [CreatePrivateApplicationInput] - (required) N/A    
