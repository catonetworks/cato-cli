
## CATO-CLI - mutation.sites.updateWifiSsid:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateWifiSsid) for documentation on this operation.

### Usage for mutation.sites.updateWifiSsid:

```bash
catocli mutation sites updateWifiSsid -h

catocli mutation sites updateWifiSsid <json>

catocli mutation sites updateWifiSsid --json-file mutation.sites.updateWifiSsid.json

catocli mutation sites updateWifiSsid '{"updateWifiSsidInput":{"band":"BAND_2P4G","category":"GUEST","dhcp":{"dhcpSubnet":"192.0.2.0/24"},"enabled":true,"id":"id","internetOnly":true,"localIp":"192.0.2.1","mdnsEnabled":true,"microsegmentationEnabled":true,"name":"string","security":{"authProtocol":"WPA2","mode":"OPEN","psk":{"passkey":"replace-with-your-secret"},"trackAuthentication":true},"subnet":"192.0.2.0/24","visible":true}}'

catocli mutation sites updateWifiSsid '{
    "updateWifiSsidInput": {
        "band": "BAND_2P4G",
        "category": "GUEST",
        "dhcp": {
            "dhcpSubnet": "192.0.2.0/24"
        },
        "enabled": true,
        "id": "id",
        "internetOnly": true,
        "localIp": "192.0.2.1",
        "mdnsEnabled": true,
        "microsegmentationEnabled": true,
        "name": "string",
        "security": {
            "authProtocol": "WPA2",
            "mode": "OPEN",
            "psk": {
                "passkey": "replace-with-your-secret"
            },
            "trackAuthentication": true
        },
        "subnet": "192.0.2.0/24",
        "visible": true
    }
}'
```

#### Operation Arguments for mutation.sites.updateWifiSsid ####

`accountId` [ID] - (required) N/A
`updateWifiSsidInput` [UpdateWifiSsidInput] - (required) N/A
