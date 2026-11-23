
## CATO-CLI - mutation.networkConfig.dhcp.updateRelayGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dhcp.updateRelayGroup) for documentation on this operation.

### Usage for mutation.networkConfig.dhcp.updateRelayGroup:

```bash
catocli mutation networkConfig dhcp updateRelayGroup -h

catocli mutation networkConfig dhcp updateRelayGroup <json>

catocli mutation networkConfig dhcp updateRelayGroup --json-file mutation.networkConfig.dhcp.updateRelayGroup.json

catocli mutation networkConfig dhcp updateRelayGroup '{"networkConfigDhcpUpdateRelayGroupInput":{"relayGroup":[{"id":"id","name":"string","server":["192.0.2.1"]}]}}'

catocli mutation networkConfig dhcp updateRelayGroup '{
    "networkConfigDhcpUpdateRelayGroupInput": {
        "relayGroup": [
            {
                "id": "id",
                "name": "string",
                "server": [
                    "192.0.2.1"
                ]
            }
        ]
    }
}'
```

#### Operation Arguments for mutation.networkConfig.dhcp.updateRelayGroup ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigDhcpUpdateRelayGroupInput` [NetworkConfigDhcpUpdateRelayGroupInput] - (required) Input for updating existing DHCP relay groups, addressed by id.
