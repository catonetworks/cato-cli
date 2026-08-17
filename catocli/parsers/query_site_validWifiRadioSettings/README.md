
## CATO-CLI - query.site.validWifiRadioSettings:
[Click here](https://api.catonetworks.com/documentation/#query-query.site.validWifiRadioSettings) for documentation on this operation.

### Usage for query.site.validWifiRadioSettings:

```bash
catocli query site validWifiRadioSettings -h

catocli query site validWifiRadioSettings <json>

catocli query site validWifiRadioSettings --json-file query.site.validWifiRadioSettings.json

catocli query site validWifiRadioSettings '{"validWifiRadioSettingsInput":{"siteRefInput":{"by":"ID","input":"string"},"wifiBandSettingsFilterInput":{"channelWidth":"AUTO","dfsEnabled":true,"standard":"AUTO"}}}'

catocli query site validWifiRadioSettings '{
    "validWifiRadioSettingsInput": {
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        },
        "wifiBandSettingsFilterInput": {
            "channelWidth": "AUTO",
            "dfsEnabled": true,
            "standard": "AUTO"
        }
    }
}'
```

#### Operation Arguments for query.site.validWifiRadioSettings ####

`accountId` [ID] - (required) N/A    
`validWifiRadioSettingsInput` [ValidWifiRadioSettingsInput] - (required) N/A    
