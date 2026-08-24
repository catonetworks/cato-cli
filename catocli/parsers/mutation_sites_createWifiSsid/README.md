
## CATO-CLI - mutation.sites.createWifiSsid:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.createWifiSsid) for documentation on this operation.

### Usage for mutation.sites.createWifiSsid:

```bash
catocli mutation sites createWifiSsid -h

catocli mutation sites createWifiSsid <json>

catocli mutation sites createWifiSsid --json-file mutation.sites.createWifiSsid.json

catocli mutation sites createWifiSsid '{"createWifiSsidInput":{"band":"BAND_2P4G","category":"GUEST","enabled":true,"internetOnly":true,"localIp":"example_value","mdnsEnabled":true,"microsegmentationEnabled":true,"name":"string","networkInterfaceId":"id","securityConfigInput":{"authProtocol":"WPA2","mode":"OPEN","psk":{"passkey":"example_value"},"trackAuthentication":true},"siteRefInput":{"by":"ID","input":"string"},"subnet":"example_value","visible":true,"wifiSsidDhcpSettingsInput":{"dhcpSubnet":"example_value"}}}'

catocli mutation sites createWifiSsid '{
    "createWifiSsidInput": {
        "band": "BAND_2P4G",
        "category": "GUEST",
        "enabled": true,
        "internetOnly": true,
        "localIp": "example_value",
        "mdnsEnabled": true,
        "microsegmentationEnabled": true,
        "name": "string",
        "networkInterfaceId": "id",
        "securityConfigInput": {
            "authProtocol": "WPA2",
            "mode": "OPEN",
            "psk": {
                "passkey": "example_value"
            },
            "trackAuthentication": true
        },
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        },
        "subnet": "example_value",
        "visible": true,
        "wifiSsidDhcpSettingsInput": {
            "dhcpSubnet": "example_value"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.createWifiSsid ####

`accountId` [ID] - (required) N/A    
`createWifiSsidInput` [CreateWifiSsidInput] - (required) N/A    
