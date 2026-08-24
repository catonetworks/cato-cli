
## CATO-CLI - mutation.sites.createWifiRadioProfile:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.createWifiRadioProfile) for documentation on this operation.

### Usage for mutation.sites.createWifiRadioProfile:

```bash
catocli mutation sites createWifiRadioProfile -h

catocli mutation sites createWifiRadioProfile <json>

catocli mutation sites createWifiRadioProfile --json-file mutation.sites.createWifiRadioProfile.json

catocli mutation sites createWifiRadioProfile '{"createWifiRadioProfileInput":{"siteRefInput":{"by":"ID","input":"string"},"wifiBandProfileInput":{"band":"BAND_2P4G","channel":1,"channelWidth":"AUTO","dfsEnabled":true,"standard":"AUTO"}}}'

catocli mutation sites createWifiRadioProfile '{
    "createWifiRadioProfileInput": {
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        },
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

#### Operation Arguments for mutation.sites.createWifiRadioProfile ####

`accountId` [ID] - (required) N/A    
`createWifiRadioProfileInput` [CreateWifiRadioProfileInput] - (required) N/A    
