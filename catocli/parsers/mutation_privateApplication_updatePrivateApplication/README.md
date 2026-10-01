
## CATO-CLI - mutation.privateApplication.updatePrivateApplication:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.privateApplication.updatePrivateApplication) for documentation on this operation.

### Usage for mutation.privateApplication.updatePrivateApplication:

```bash
catocli mutation privateApplication updatePrivateApplication -h

catocli mutation privateApplication updatePrivateApplication <json>

catocli mutation privateApplication updatePrivateApplication --json-file mutation.privateApplication.updatePrivateApplication.json

catocli mutation privateApplication updatePrivateApplication '{"updatePrivateApplicationInput":{"allowIcmpProtocol":true,"description":"string","id":"id","internalAppAddress":"host.example.com","name":"string","privateAppProbing":{"faultThresholdDown":1,"id":"id","interval":1,"type":"string"},"probingEnabled":true,"protocolPorts":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"published":true,"publishedAppDomain":{"catoIp":"192.0.2.1","connectorGroupName":"string","creationTime":"2026-01-02T15:04:05Z","id":"id","publishedAppDomain":"string"}}}'

catocli mutation privateApplication updatePrivateApplication '{
    "updatePrivateApplicationInput": {
        "allowIcmpProtocol": true,
        "description": "string",
        "id": "id",
        "internalAppAddress": "host.example.com",
        "name": "string",
        "privateAppProbing": {
            "faultThresholdDown": 1,
            "id": "id",
            "interval": 1,
            "type": "string"
        },
        "probingEnabled": true,
        "protocolPorts": [
            {
                "port": [
                    443
                ],
                "portRange": {
                    "from": 443,
                    "to": 443
                },
                "protocol": "ANY"
            }
        ],
        "published": true,
        "publishedAppDomain": {
            "catoIp": "192.0.2.1",
            "connectorGroupName": "string",
            "creationTime": "2026-01-02T15:04:05Z",
            "id": "id",
            "publishedAppDomain": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.privateApplication.updatePrivateApplication ####

`accountId` [ID] - (required) N/A
`updatePrivateApplicationInput` [UpdatePrivateApplicationInput] - (required) N/A
