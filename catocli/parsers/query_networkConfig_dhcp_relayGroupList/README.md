
## CATO-CLI - query.networkConfig.dhcp.relayGroupList:
[Click here](https://api.catonetworks.com/documentation/#query-query.networkConfig.dhcp.relayGroupList) for documentation on this operation.

### Usage for query.networkConfig.dhcp.relayGroupList:

```bash
catocli query networkConfig dhcp relayGroupList -h

catocli query networkConfig dhcp relayGroupList <json>

catocli query networkConfig dhcp relayGroupList --json-file query.networkConfig.dhcp.relayGroupList.json

catocli query networkConfig dhcp relayGroupList '{"networkConfigDhcpRelayGroupListInput":{"filter":{"name":{"eq":"string","in":["string1","string2"],"neq":"string","nin":["string1","string2"],"regex":"string"}},"paging":{"from":1,"limit":1},"sort":{"name":{"direction":"ASC","priority":1}}}}'

catocli query networkConfig dhcp relayGroupList '{
    "networkConfigDhcpRelayGroupListInput": {
        "filter": {
            "name": {
                "eq": "string",
                "in": [
                    "string1",
                    "string2"
                ],
                "neq": "string",
                "nin": [
                    "string1",
                    "string2"
                ],
                "regex": "string"
            }
        },
        "paging": {
            "from": 1,
            "limit": 1
        },
        "sort": {
            "name": {
                "direction": "ASC",
                "priority": 1
            }
        }
    }
}'
```

#### Operation Arguments for query.networkConfig.dhcp.relayGroupList ####

`accountId` [ID] - (required) N/A    
`networkConfigDhcpRelayGroupListInput` [NetworkConfigDhcpRelayGroupListInput] - (required) N/A    
