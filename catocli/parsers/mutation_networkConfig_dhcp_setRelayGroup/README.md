
## CATO-CLI - mutation.networkConfig.dhcp.setRelayGroup:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.dhcp.setRelayGroup) for documentation on this operation.

### Usage for mutation.networkConfig.dhcp.setRelayGroup:

```bash
catocli mutation networkConfig dhcp setRelayGroup -h

catocli mutation networkConfig dhcp setRelayGroup <json>

catocli mutation networkConfig dhcp setRelayGroup --json-file mutation.networkConfig.dhcp.setRelayGroup.json

catocli mutation networkConfig dhcp setRelayGroup '{"networkConfigDhcpSetRelayGroupInput":{"relayGroup":[{"id":"id","name":"string","server":["192.0.2.1"]}]}}'

catocli mutation networkConfig dhcp setRelayGroup '{
    "networkConfigDhcpSetRelayGroupInput": {
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

#### Operation Arguments for mutation.networkConfig.dhcp.setRelayGroup ####

`accountId` [ID] - (required) N/A
`networkConfigDhcpSetRelayGroupInput` [NetworkConfigDhcpSetRelayGroupInput] - (required) N/A
