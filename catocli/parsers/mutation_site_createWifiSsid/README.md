
## CATO-CLI - mutation.site.createWifiSsid:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.createWifiSsid) for documentation on this operation.

### Usage for mutation.site.createWifiSsid:

```bash
catocli mutation site createWifiSsid -h

catocli mutation site createWifiSsid <json>

catocli mutation site createWifiSsid --json-file mutation.site.createWifiSsid.json

catocli mutation site createWifiSsid '{"createWifiSsidInput":{"band":"BAND_2P4G","category":"GUEST","dhcp":{"dhcpSubnet":"192.0.2.0/24"},"enabled":true,"internetOnly":true,"localIp":"192.0.2.1","mdnsEnabled":true,"microsegmentationEnabled":true,"name":"string","networkInterfaceId":"id","security":{"authProtocol":"WPA2","mode":"OPEN","psk":{"passkey":"replace-with-your-secret"},"trackAuthentication":true},"site":{"by":"ID","input":"string"},"subnet":"192.0.2.0/24","visible":true}}'

catocli mutation site createWifiSsid '{
    "createWifiSsidInput": {
        "band": "BAND_2P4G",
        "category": "GUEST",
        "dhcp": {
            "dhcpSubnet": "192.0.2.0/24"
        },
        "enabled": true,
        "internetOnly": true,
        "localIp": "192.0.2.1",
        "mdnsEnabled": true,
        "microsegmentationEnabled": true,
        "name": "string",
        "networkInterfaceId": "id",
        "security": {
            "authProtocol": "WPA2",
            "mode": "OPEN",
            "psk": {
                "passkey": "replace-with-your-secret"
            },
            "trackAuthentication": true
        },
        "site": {
            "by": "ID",
            "input": "string"
        },
        "subnet": "192.0.2.0/24",
        "visible": true
    }
}'
```

#### Operation Arguments for mutation.site.createWifiSsid ####

`accountId` [ID] - (required) N/A
`createWifiSsidInput` [CreateWifiSsidInput] - (required) N/A
