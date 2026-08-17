
## CATO-CLI - mutation.site.createWifiSsid:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.createWifiSsid) for documentation on this operation.

### Usage for mutation.site.createWifiSsid:

```bash
catocli mutation site createWifiSsid -h

catocli mutation site createWifiSsid <json>

catocli mutation site createWifiSsid --json-file mutation.site.createWifiSsid.json

catocli mutation site createWifiSsid '{"createWifiSsidInput":{"band":"BAND_2P4G","category":"GUEST","enabled":true,"internetOnly":true,"localIp":"example_value","mdnsEnabled":true,"microsegmentationEnabled":true,"name":"string","networkInterfaceId":"id","securityConfigInput":{"authProtocol":"WPA2","mode":"OPEN","psk":{"passkey":"example_value"},"trackAuthentication":true},"siteRefInput":{"by":"ID","input":"string"},"subnet":"example_value","visible":true,"wifiSsidDhcpSettingsInput":{"dhcpSubnet":"example_value"}}}'

catocli mutation site createWifiSsid '{
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

#### Operation Arguments for mutation.site.createWifiSsid ####

`accountId` [ID] - (required) N/A    
`createWifiSsidInput` [CreateWifiSsidInput] - (required) N/A    
