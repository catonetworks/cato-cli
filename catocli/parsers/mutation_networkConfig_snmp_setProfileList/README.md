
## CATO-CLI - mutation.networkConfig.snmp.setProfileList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.snmp.setProfileList) for documentation on this operation.

### Usage for mutation.networkConfig.snmp.setProfileList:

```bash
catocli mutation networkConfig snmp setProfileList -h

catocli mutation networkConfig snmp setProfileList <json>

catocli mutation networkConfig snmp setProfileList --json-file mutation.networkConfig.snmp.setProfileList.json

catocli mutation networkConfig snmp setProfileList '{"networkConfigSnmpSetProfileListInput":{"snmpProfile":[{"authPassphrase":"replace-with-your-secret","authProtocol":"SHA_256","description":"string","name":"string","privacyPassphrase":"replace-with-your-secret","privacyProtocol":"AES_128","securityLevel":"AUTH_PRIV","username":"string"}]}}'

catocli mutation networkConfig snmp setProfileList '{
    "networkConfigSnmpSetProfileListInput": {
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

#### Operation Arguments for mutation.networkConfig.snmp.setProfileList ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigSnmpSetProfileListInput` [NetworkConfigSnmpSetProfileListInput] - (required) N/A
