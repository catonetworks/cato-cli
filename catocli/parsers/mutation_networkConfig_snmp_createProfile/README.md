
## CATO-CLI - mutation.networkConfig.snmp.createProfile:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.snmp.createProfile) for documentation on this operation.

### Usage for mutation.networkConfig.snmp.createProfile:

```bash
catocli mutation networkConfig snmp createProfile -h

catocli mutation networkConfig snmp createProfile <json>

catocli mutation networkConfig snmp createProfile --json-file mutation.networkConfig.snmp.createProfile.json

catocli mutation networkConfig snmp createProfile '{"networkConfigSnmpCreateProfileInput":{"snmpProfile":{"authPassphrase":"replace-with-your-secret","authProtocol":"SHA_256","description":"string","name":"string","privacyPassphrase":"replace-with-your-secret","privacyProtocol":"AES_128","securityLevel":"AUTH_PRIV","username":"string"}}}'

catocli mutation networkConfig snmp createProfile '{
    "networkConfigSnmpCreateProfileInput": {
        "snmpProfile": {
            "authPassphrase": "replace-with-your-secret",
            "authProtocol": "SHA_256",
            "description": "string",
            "name": "string",
            "privacyPassphrase": "replace-with-your-secret",
            "privacyProtocol": "AES_128",
            "securityLevel": "AUTH_PRIV",
            "username": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.networkConfig.snmp.createProfile ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigSnmpCreateProfileInput` [NetworkConfigSnmpCreateProfileInput] - (required) N/A
