
## CATO-CLI - mutation.networkConfig.snmp.createProfileList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.snmp.createProfileList) for documentation on this operation.

### Usage for mutation.networkConfig.snmp.createProfileList:

```bash
catocli mutation networkConfig snmp createProfileList -h

catocli mutation networkConfig snmp createProfileList <json>

catocli mutation networkConfig snmp createProfileList --json-file mutation.networkConfig.snmp.createProfileList.json

catocli mutation networkConfig snmp createProfileList '{"networkConfigSnmpCreateProfileListInput":{"snmpProfile":[{"authPassphrase":"replace-with-your-secret","authProtocol":"SHA_256","description":"string","name":"string","privacyPassphrase":"replace-with-your-secret","privacyProtocol":"AES_128","securityLevel":"AUTH_PRIV","username":"string"}]}}'

catocli mutation networkConfig snmp createProfileList '{
    "networkConfigSnmpCreateProfileListInput": {
        "snmpProfile": [
            {
                "authPassphrase": "replace-with-your-secret",
                "authProtocol": "SHA_256",
                "description": "string",
                "name": "string",
                "privacyPassphrase": "replace-with-your-secret",
                "privacyProtocol": "AES_128",
                "securityLevel": "AUTH_PRIV",
                "username": "string"
            }
        ]
    }
}'
```

#### Operation Arguments for mutation.networkConfig.snmp.createProfileList ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigSnmpCreateProfileListInput` [NetworkConfigSnmpCreateProfileListInput] - (required) N/A
