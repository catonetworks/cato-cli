
## CATO-CLI - mutation.site.updateWifiRadioProfile:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateWifiRadioProfile) for documentation on this operation.

### Usage for mutation.site.updateWifiRadioProfile:

```bash
catocli mutation site updateWifiRadioProfile -h

catocli mutation site updateWifiRadioProfile <json>

catocli mutation site updateWifiRadioProfile --json-file mutation.site.updateWifiRadioProfile.json

catocli mutation site updateWifiRadioProfile '{"updateWifiRadioProfileInput":{"id":"id","wifiBandProfileInput":{"band":"BAND_2P4G","channel":1,"channelWidth":"AUTO","dfsEnabled":true,"standard":"AUTO"}}}'

catocli mutation site updateWifiRadioProfile '{
    "updateWifiRadioProfileInput": {
        "id": "id",
        "wifiBandProfileInput": {
            "band": "BAND_2P4G",
            "channel": 1,
            "channelWidth": "AUTO",
            "dfsEnabled": true,
            "standard": "AUTO"
        }
    }
}'
```

#### Operation Arguments for mutation.site.updateWifiRadioProfile ####

`accountId` [ID] - (required) N/A    
`updateWifiRadioProfileInput` [UpdateWifiRadioProfileInput] - (required) N/A    
