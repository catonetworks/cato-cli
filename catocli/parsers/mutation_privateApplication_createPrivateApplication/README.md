
## CATO-CLI - mutation.privateApplication.createPrivateApplication:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.privateApplication.createPrivateApplication) for documentation on this operation.

### Usage for mutation.privateApplication.createPrivateApplication:

```bash
catocli mutation privateApplication createPrivateApplication -h

catocli mutation privateApplication createPrivateApplication <json>

catocli mutation privateApplication createPrivateApplication --json-file mutation.privateApplication.createPrivateApplication.json

catocli mutation privateApplication createPrivateApplication '{"createPrivateApplicationInput":{"allowIcmpProtocol":true,"description":"string","internalAppAddress":"host.example.com","name":"string","privateAppProbing":{"faultThresholdDown":1,"id":"id","interval":1,"port":1,"probingType":"ICMP_PING","type":"string"},"probingEnabled":true,"protocolPorts":[{"port":[443],"portRange":{"from":443,"to":443},"protocol":"ANY"}],"published":true,"publishedAppDomain":{"catoIp":"192.0.2.1","connectorGroupName":"string","creationTime":"2026-01-02T15:04:05Z","id":"id","publishedAppDomain":"string"}}}'

catocli mutation privateApplication createPrivateApplication '{
    "createPrivateApplicationInput": {
        "allowIcmpProtocol": true,
        "description": "string",
        "internalAppAddress": "host.example.com",
        "name": "string",
        "privateAppProbing": {
            "faultThresholdDown": 1,
            "id": "id",
            "interval": 1,
            "port": 1,
            "probingType": "ICMP_PING",
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

#### Operation Arguments for mutation.privateApplication.createPrivateApplication ####

`accountId` [ID] - (required) Account containing the private applications.
`createPrivateApplicationInput` [CreatePrivateApplicationInput] - (required) Parameters for the private application operation.
