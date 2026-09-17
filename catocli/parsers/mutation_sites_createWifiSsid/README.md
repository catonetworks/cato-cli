
## CATO-CLI - mutation.sites.createWifiSsid:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.createWifiSsid) for documentation on this operation.

### Usage for mutation.sites.createWifiSsid:

```bash
catocli mutation sites createWifiSsid -h

catocli mutation sites createWifiSsid <json>

catocli mutation sites createWifiSsid --json-file mutation.sites.createWifiSsid.json

catocli mutation sites createWifiSsid '{"createWifiSsidInput":{"band":"BAND_2P4G","category":"GUEST","dhcp":{"dhcpSubnet":"example_value"},"enabled":true,"internetOnly":true,"localIp":"example_value","mdnsEnabled":true,"microsegmentationEnabled":true,"name":"string","networkInterfaceId":"id","security":{"authProtocol":"WPA2","mode":"OPEN","psk":{"passkey":"example_value"},"trackAuthentication":true},"site":{"by":"ID","input":"string"},"subnet":"example_value","visible":true}}'

catocli mutation sites createWifiSsid '{
    "createWifiSsidInput": {
        "band": "BAND_2P4G",
        "category": "GUEST",
        "dhcp": {
            "dhcpSubnet": "example_value"
        },
        "enabled": true,
        "internetOnly": true,
        "localIp": "example_value",
        "mdnsEnabled": true,
        "microsegmentationEnabled": true,
        "name": "string",
        "networkInterfaceId": "id",
        "security": {
            "authProtocol": "WPA2",
            "mode": "OPEN",
            "psk": {
                "passkey": "example_value"
            },
            "trackAuthentication": true
        },
        "site": {
            "by": "ID",
            "input": "string"
        },
        "subnet": "example_value",
        "visible": true
    }
}'
```

#### Operation Arguments for mutation.sites.createWifiSsid ####

`accountId` [ID] - (required) N/A    
`createWifiSsidInput` [CreateWifiSsidInput] - (required) N/A    
