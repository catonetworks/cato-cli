
## CATO-CLI - mutation.sites.updateWifiSsid:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateWifiSsid) for documentation on this operation.

### Usage for mutation.sites.updateWifiSsid:

```bash
catocli mutation sites updateWifiSsid -h

catocli mutation sites updateWifiSsid <json>

catocli mutation sites updateWifiSsid --json-file mutation.sites.updateWifiSsid.json

catocli mutation sites updateWifiSsid '{"updateWifiSsidInput":{"band":"BAND_2P4G","category":"GUEST","enabled":true,"id":"id","internetOnly":true,"localIp":"example_value","mdnsEnabled":true,"microsegmentationEnabled":true,"name":"string","securityConfigInput":{"authProtocol":"WPA2","mode":"OPEN","psk":{"passkey":"example_value"},"trackAuthentication":true},"subnet":"example_value","visible":true,"wifiSsidDhcpSettingsInput":{"dhcpSubnet":"example_value"}}}'

catocli mutation sites updateWifiSsid '{
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

#### Operation Arguments for mutation.sites.updateWifiSsid ####

`accountId` [ID] - (required) N/A    
`updateWifiSsidInput` [UpdateWifiSsidInput] - (required) N/A    
