
## CATO-CLI - query.site.validateWifiRadioProfileByCountry:
[Click here](https://api.catonetworks.com/documentation/#query-query.site.validateWifiRadioProfileByCountry) for documentation on this operation.

### Usage for query.site.validateWifiRadioProfileByCountry:

```bash
catocli query site validateWifiRadioProfileByCountry -h

catocli query site validateWifiRadioProfileByCountry <json>

catocli query site validateWifiRadioProfileByCountry --json-file query.site.validateWifiRadioProfileByCountry.json

catocli query site validateWifiRadioProfileByCountry '{"validateWifiRadioProfileByCountryInput":{"countryCode":"string","radioProfile":{"band24":{"band":"BAND_2P4G","channel":1,"channelWidth":"AUTO","dfsEnabled":true,"standard":"AUTO"},"band5":{"band":"BAND_2P4G","channel":1,"channelWidth":"AUTO","dfsEnabled":true,"standard":"AUTO"}}}}'

catocli query site validateWifiRadioProfileByCountry '{
    "validateWifiRadioProfileByCountryInput": {
        "countryCode": "string",
        "radioProfile": {
            "band24": {
                "band": "BAND_2P4G",
                "channel": 1,
                "channelWidth": "AUTO",
                "dfsEnabled": true,
                "standard": "AUTO"
            },
            "band5": {
                "band": "BAND_2P4G",
                "channel": 1,
                "channelWidth": "AUTO",
                "dfsEnabled": true,
                "standard": "AUTO"
            }
        }
    }
}'
```

#### Operation Arguments for query.site.validateWifiRadioProfileByCountry ####

`accountId` [ID] - (required) N/A    
`validateWifiRadioProfileByCountryInput` [ValidateWifiRadioProfileByCountryInput] - (required) N/A    
