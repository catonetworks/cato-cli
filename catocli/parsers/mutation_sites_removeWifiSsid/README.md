
## CATO-CLI - mutation.sites.removeWifiSsid:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.removeWifiSsid) for documentation on this operation.

### Usage for mutation.sites.removeWifiSsid:

```bash
catocli mutation sites removeWifiSsid -h

catocli mutation sites removeWifiSsid <json>

catocli mutation sites removeWifiSsid --json-file mutation.sites.removeWifiSsid.json

catocli mutation sites removeWifiSsid '{"removeWifiSsidInput":{"wifiSsid":{"by":"ID","input":"string"}}}'

catocli mutation sites removeWifiSsid '{
    "removeWifiSsidInput": {
        "wifiSsid": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.removeWifiSsid ####

`accountId` [ID] - (required) N/A    
`removeWifiSsidInput` [RemoveWifiSsidInput] - (required) N/A    
