
## CATO-CLI - mutation.site.createWifiRadioProfile:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.createWifiRadioProfile) for documentation on this operation.

### Usage for mutation.site.createWifiRadioProfile:

```bash
catocli mutation site createWifiRadioProfile -h

catocli mutation site createWifiRadioProfile <json>

catocli mutation site createWifiRadioProfile --json-file mutation.site.createWifiRadioProfile.json

catocli mutation site createWifiRadioProfile '{"createWifiRadioProfileInput":{"band24":{"band":"BAND_2P4G","channel":1,"channelWidth":"AUTO","dfsEnabled":true,"standard":"AUTO"},"band5":{"band":"BAND_2P4G","channel":1,"channelWidth":"AUTO","dfsEnabled":true,"standard":"AUTO"},"site":{"by":"ID","input":"string"}}}'

catocli mutation site createWifiRadioProfile '{
    "createWifiRadioProfileInput": {
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
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.createWifiRadioProfile ####

`accountId` [ID] - (required) N/A    
`createWifiRadioProfileInput` [CreateWifiRadioProfileInput] - (required) N/A    
