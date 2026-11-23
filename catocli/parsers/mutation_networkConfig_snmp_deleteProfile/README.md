
## CATO-CLI - mutation.networkConfig.snmp.deleteProfile:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.snmp.deleteProfile) for documentation on this operation.

### Usage for mutation.networkConfig.snmp.deleteProfile:

```bash
catocli mutation networkConfig snmp deleteProfile -h

catocli mutation networkConfig snmp deleteProfile <json>

catocli mutation networkConfig snmp deleteProfile --json-file mutation.networkConfig.snmp.deleteProfile.json

catocli mutation networkConfig snmp deleteProfile '{"networkConfigSnmpDeleteProfileInput":{"id":"id"}}'

catocli mutation networkConfig snmp deleteProfile '{
    "networkConfigSnmpDeleteProfileInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.networkConfig.snmp.deleteProfile ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigSnmpDeleteProfileInput` [NetworkConfigSnmpDeleteProfileInput] - (required) N/A
