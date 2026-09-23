
## CATO-CLI - mutation.networkConfig.dhcp.createRelayGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dhcp.createRelayGroup) for documentation on this operation.

### Usage for mutation.networkConfig.dhcp.createRelayGroup:

```bash
catocli mutation networkConfig dhcp createRelayGroup -h

catocli mutation networkConfig dhcp createRelayGroup <json>

catocli mutation networkConfig dhcp createRelayGroup --json-file mutation.networkConfig.dhcp.createRelayGroup.json

catocli mutation networkConfig dhcp createRelayGroup '{"accountId":"id","networkConfigDhcpCreateRelayGroupInput":{"relayGroup":{"name":"string","server":["example1","example2"]}}}'

catocli mutation networkConfig dhcp createRelayGroup '{
    "accountId": "id",
    "networkConfigDhcpCreateRelayGroupInput": {
        "relayGroup": {
            "name": "string",
            "server": [
                "example1",
                "example2"
            ]
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dhcp.createRelayGroup ####

`accountId` [ID] - (required) N/A    
`networkConfigDhcpCreateRelayGroupInput` [NetworkConfigDhcpCreateRelayGroupInput] - (required) N/A    
