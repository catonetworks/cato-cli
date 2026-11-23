
## CATO-CLI - query.networkConfig.snmp.profile:
[Click here](https://api.catonetworks.com/documentation/#query-query.networkConfig.snmp.profile) for documentation on this operation.

### Usage for query.networkConfig.snmp.profile:

```bash
catocli query networkConfig snmp profile -h

catocli query networkConfig snmp profile <json>

catocli query networkConfig snmp profile --json-file query.networkConfig.snmp.profile.json

catocli query networkConfig snmp profile '{"networkConfigSnmpProfileRefInput":{"by":"ID","input":"string"}}'

catocli query networkConfig snmp profile '{
    "networkConfigSnmpProfileRefInput": {
        "by": "ID",
        "input": "string"
    }
}'
```

#### Operation Arguments for query.networkConfig.snmp.profile ####

`accountId` [ID] - (required) ID of the account whose network configuration is requested.
`networkConfigSnmpProfileRefInput` [NetworkConfigSnmpProfileRefInput] - (required) N/A
