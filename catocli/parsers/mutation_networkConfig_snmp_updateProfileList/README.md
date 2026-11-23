
## CATO-CLI - mutation.networkConfig.snmp.updateProfileList:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.networkConfig.snmp.updateProfileList) for documentation on this operation.

### Usage for mutation.networkConfig.snmp.updateProfileList:

```bash
catocli mutation networkConfig snmp updateProfileList -h

catocli mutation networkConfig snmp updateProfileList <json>

catocli mutation networkConfig snmp updateProfileList --json-file mutation.networkConfig.snmp.updateProfileList.json

catocli mutation networkConfig snmp updateProfileList '{"networkConfigSnmpUpdateProfileListInput":{"snmpProfile":[{"authPassphrase":"replace-with-your-secret","authProtocol":"SHA_256","description":"string","id":"id","name":"string","privacyPassphrase":"replace-with-your-secret","privacyProtocol":"AES_128","securityLevel":"AUTH_PRIV","username":"string"}]}}'

catocli mutation networkConfig snmp updateProfileList '{
    "networkConfigSnmpUpdateProfileListInput": {
        "snmpProfile": [
            {
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
        ]
    }
}'
```

#### Operation Arguments for mutation.networkConfig.snmp.updateProfileList ####

`accountId` [ID] - (required) ID of the account whose network configuration is modified.
`networkConfigSnmpUpdateProfileListInput` [NetworkConfigSnmpUpdateProfileListInput] - (required) N/A
