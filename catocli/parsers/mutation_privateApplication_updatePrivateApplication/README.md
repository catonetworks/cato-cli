
## CATO-CLI - mutation.privateApplication.updatePrivateApplication:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.privateApplication.updatePrivateApplication) for documentation on this operation.

### Usage for mutation.privateApplication.updatePrivateApplication:

```bash
catocli mutation privateApplication updatePrivateApplication -h

catocli mutation privateApplication updatePrivateApplication <json>

catocli mutation privateApplication updatePrivateApplication --json-file mutation.privateApplication.updatePrivateApplication.json

catocli mutation privateApplication updatePrivateApplication '{"updatePrivateApplicationInput":{"allowIcmpProtocol":true,"customServiceInput":{"port":["example1","example2"],"portRange":{"from":"example_value","to":"example_value"},"protocol":"ANY"},"description":"string","id":"id","internalAppAddress":"example_value","name":"string","privateAppProbingInput":{"faultThresholdDown":1,"id":"id","interval":1,"type":"string"},"probingEnabled":true,"published":true,"publishedAppDomainInput":{"catoIp":"example_value","connectorGroupName":"string","creationTime":"example_value","id":"id","publishedAppDomain":"string"}}}'

catocli mutation privateApplication updatePrivateApplication '{
    "updatePrivateApplicationInput": {
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
        "id": "id",
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

#### Operation Arguments for mutation.privateApplication.updatePrivateApplication ####

`accountId` [ID] - (required) N/A    
`updatePrivateApplicationInput` [UpdatePrivateApplicationInput] - (required) N/A    
