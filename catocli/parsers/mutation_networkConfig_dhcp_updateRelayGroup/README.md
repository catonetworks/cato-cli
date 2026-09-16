
## CATO-CLI - mutation.networkConfig.dhcp.updateRelayGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dhcp.updateRelayGroup) for documentation on this operation.

### Usage for mutation.networkConfig.dhcp.updateRelayGroup:

```bash
catocli mutation networkConfig dhcp updateRelayGroup -h

catocli mutation networkConfig dhcp updateRelayGroup <json>

catocli mutation networkConfig dhcp updateRelayGroup --json-file mutation.networkConfig.dhcp.updateRelayGroup.json

catocli mutation networkConfig dhcp updateRelayGroup '{"networkConfigDhcpUpdateRelayGroupInput":{"relayGroup":{"id":"id","name":"string","server":["example1","example2"]}}}'

catocli mutation networkConfig dhcp updateRelayGroup '{
    "networkConfigDhcpUpdateRelayGroupInput": {
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

#### Operation Arguments for mutation.networkConfig.dhcp.updateRelayGroup ####

`accountId` [ID] - (required) N/A    
`networkConfigDhcpUpdateRelayGroupInput` [NetworkConfigDhcpUpdateRelayGroupInput] - (required) N/A    
