
## CATO-CLI - mutation.networkConfig.snmp.deleteProfileList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.snmp.deleteProfileList) for documentation on this operation.

### Usage for mutation.networkConfig.snmp.deleteProfileList:

```bash
catocli mutation networkConfig snmp deleteProfileList -h

catocli mutation networkConfig snmp deleteProfileList <json>

catocli mutation networkConfig snmp deleteProfileList --json-file mutation.networkConfig.snmp.deleteProfileList.json

catocli mutation networkConfig snmp deleteProfileList '{"networkConfigSnmpDeleteProfileListInput":{"id":["id1","id2"]}}'

catocli mutation networkConfig snmp deleteProfileList '{
    "networkConfigSnmpDeleteProfileListInput": {
        "id": [
            "id1",
            "id2"
        ]
    }
}'
```

#### Operation Arguments for mutation.networkConfig.snmp.deleteProfileList ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigSnmpDeleteProfileListInput` [NetworkConfigSnmpDeleteProfileListInput] - (required) N/A
