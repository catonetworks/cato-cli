
## CATO-CLI - mutation.site.updateWifiSsid:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateWifiSsid) for documentation on this operation.

### Usage for mutation.site.updateWifiSsid:

```bash
catocli mutation site updateWifiSsid -h

catocli mutation site updateWifiSsid <json>

catocli mutation site updateWifiSsid --json-file mutation.site.updateWifiSsid.json

catocli mutation site updateWifiSsid '{"updateWifiSsidInput":{"band":"BAND_2P4G","category":"GUEST","enabled":true,"id":"id","internetOnly":true,"localIp":"example_value","mdnsEnabled":true,"microsegmentationEnabled":true,"name":"string","securityConfigInput":{"authProtocol":"WPA2","mode":"OPEN","psk":{"passkey":"example_value"},"trackAuthentication":true},"subnet":"example_value","visible":true,"wifiSsidDhcpSettingsInput":{"dhcpSubnet":"example_value"}}}'

catocli mutation site updateWifiSsid '{
    "updateWifiSsidInput": {
        "band": "BAND_2P4G",
        "category": "GUEST",
        "enabled": true,
        "id": "id",
        "internetOnly": true,
        "localIp": "example_value",
        "mdnsEnabled": true,
        "microsegmentationEnabled": true,
        "name": "string",
        "securityConfigInput": {
            "authProtocol": "WPA2",
            "mode": "OPEN",
            "psk": {
                "passkey": "example_value"
            },
            "trackAuthentication": true
        },
        "subnet": "example_value",
        "visible": true,
        "wifiSsidDhcpSettingsInput": {
            "dhcpSubnet": "example_value"
        }
    }
}'
```

#### Operation Arguments for mutation.site.updateWifiSsid ####

`accountId` [ID] - (required) N/A    
`updateWifiSsidInput` [UpdateWifiSsidInput] - (required) N/A    
