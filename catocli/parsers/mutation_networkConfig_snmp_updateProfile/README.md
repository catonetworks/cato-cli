
## CATO-CLI - mutation.networkConfig.snmp.updateProfile:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.snmp.updateProfile) for documentation on this operation.

### Usage for mutation.networkConfig.snmp.updateProfile:

```bash
catocli mutation networkConfig snmp updateProfile -h

catocli mutation networkConfig snmp updateProfile <json>

catocli mutation networkConfig snmp updateProfile --json-file mutation.networkConfig.snmp.updateProfile.json

catocli mutation networkConfig snmp updateProfile '{"networkConfigSnmpUpdateProfileInput":{"snmpProfile":{"authPassphrase":"replace-with-your-secret","authProtocol":"SHA_256","description":"string","id":"id","name":"string","privacyPassphrase":"replace-with-your-secret","privacyProtocol":"AES_128","securityLevel":"AUTH_PRIV","username":"string"}}}'

catocli mutation networkConfig snmp updateProfile '{
    "networkConfigSnmpUpdateProfileInput": {
        "snmpProfile": {
            "authPassphrase": "replace-with-your-secret",
            "authProtocol": "SHA_256",
            "description": "string",
            "id": "id",
            "name": "string",
            "privacyPassphrase": "replace-with-your-secret",
            "privacyProtocol": "AES_128",
            "securityLevel": "AUTH_PRIV",
            "username": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.snmp.updateProfile ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigSnmpUpdateProfileInput` [NetworkConfigSnmpUpdateProfileInput] - (required) N/A
