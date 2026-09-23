
## CATO-CLI - mutation.networkConfig.dhcp.setRelayGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dhcp.setRelayGroup) for documentation on this operation.

### Usage for mutation.networkConfig.dhcp.setRelayGroup:

```bash
catocli mutation networkConfig dhcp setRelayGroup -h

catocli mutation networkConfig dhcp setRelayGroup <json>

catocli mutation networkConfig dhcp setRelayGroup --json-file mutation.networkConfig.dhcp.setRelayGroup.json

catocli mutation networkConfig dhcp setRelayGroup '{"accountId":"id","networkConfigDhcpSetRelayGroupInput":{"relayGroup":{"id":"id","name":"string","server":["example1","example2"]}}}'

catocli mutation networkConfig dhcp setRelayGroup '{
    "accountId": "id",
    "networkConfigDhcpSetRelayGroupInput": {
        "relayGroup": {
            "id": "id",
            "name": "string",
            "server": [
                "example1",
                "example2"
            ]
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dhcp.setRelayGroup ####

`accountId` [ID] - (required) N/A    
`networkConfigDhcpSetRelayGroupInput` [NetworkConfigDhcpSetRelayGroupInput] - (required) N/A    
