
## CATO-CLI - mutation.sites.updateWifiRadioProfile:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateWifiRadioProfile) for documentation on this operation.

### Usage for mutation.sites.updateWifiRadioProfile:

```bash
catocli mutation sites updateWifiRadioProfile -h

catocli mutation sites updateWifiRadioProfile <json>

catocli mutation sites updateWifiRadioProfile --json-file mutation.sites.updateWifiRadioProfile.json

catocli mutation sites updateWifiRadioProfile '{"updateWifiRadioProfileInput":{"band24":{"band":"BAND_2P4G","channel":1,"channelWidth":"AUTO","dfsEnabled":true,"standard":"AUTO"},"band5":{"band":"BAND_2P4G","channel":1,"channelWidth":"AUTO","dfsEnabled":true,"standard":"AUTO"},"id":"id"}}'

catocli mutation sites updateWifiRadioProfile '{
    "updateWifiRadioProfileInput": {
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
        },
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.sites.updateWifiRadioProfile ####

`accountId` [ID] - (required) N/A    
`updateWifiRadioProfileInput` [UpdateWifiRadioProfileInput] - (required) N/A    
