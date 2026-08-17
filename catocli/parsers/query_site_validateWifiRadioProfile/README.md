
## CATO-CLI - query.site.validateWifiRadioProfile:
[Click here](https://api.catonetworks.com/documentation/#query-query.site.validateWifiRadioProfile) for documentation on this operation.

### Usage for query.site.validateWifiRadioProfile:

```bash
catocli query site validateWifiRadioProfile -h

catocli query site validateWifiRadioProfile <json>

catocli query site validateWifiRadioProfile --json-file query.site.validateWifiRadioProfile.json

catocli query site validateWifiRadioProfile '{"validateWifiRadioProfileInput":{"siteRefInput":{"by":"ID","input":"string"},"wifiRadioProfileInput":{"band24":{"band":"BAND_2P4G","channel":1,"channelWidth":"AUTO","dfsEnabled":true,"standard":"AUTO"},"band5":{"band":"BAND_2P4G","channel":1,"channelWidth":"AUTO","dfsEnabled":true,"standard":"AUTO"}}}}'

catocli query site validateWifiRadioProfile '{
    "validateWifiRadioProfileInput": {
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        },
        "wifiRadioProfileInput": {
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

#### Operation Arguments for query.site.validateWifiRadioProfile ####

`accountId` [ID] - (required) N/A    
`validateWifiRadioProfileInput` [ValidateWifiRadioProfileInput] - (required) N/A    
