
## CATO-CLI - query.site.validWifiRadioSettingsByCountry:
[Click here](https://api.catonetworks.com/documentation/#query-query.site.validWifiRadioSettingsByCountry) for documentation on this operation.

### Usage for query.site.validWifiRadioSettingsByCountry:

```bash
catocli query site validWifiRadioSettingsByCountry -h

catocli query site validWifiRadioSettingsByCountry <json>

catocli query site validWifiRadioSettingsByCountry --json-file query.site.validWifiRadioSettingsByCountry.json

catocli query site validWifiRadioSettingsByCountry '{"validWifiRadioSettingsByCountryInput":{"band24":{"channelWidth":"AUTO","dfsEnabled":true,"standard":"AUTO"},"band5":{"channelWidth":"AUTO","dfsEnabled":true,"standard":"AUTO"},"countryCode":"string"}}'

catocli query site validWifiRadioSettingsByCountry '{
    "validWifiRadioSettingsByCountryInput": {
        "band24": {
            "channelWidth": "AUTO",
            "dfsEnabled": true,
            "standard": "AUTO"
        },
        "band5": {
            "channelWidth": "AUTO",
            "dfsEnabled": true,
            "standard": "AUTO"
        },
        "countryCode": "string"
    }
}'
```

#### Operation Arguments for query.site.validWifiRadioSettingsByCountry ####

`accountId` [ID] - (required) N/A    
`validWifiRadioSettingsByCountryInput` [ValidWifiRadioSettingsByCountryInput] - (required) N/A    
