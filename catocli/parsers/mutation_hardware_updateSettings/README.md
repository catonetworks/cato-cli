
## CATO-CLI - mutation.hardware.updateSettings:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.hardware.updateSettings) for documentation on this operation.

### Usage for mutation.hardware.updateSettings:

```bash
catocli mutation hardware updateSettings -h

catocli mutation hardware updateSettings <json>

catocli mutation hardware updateSettings --json-file mutation.hardware.updateSettings.json

catocli mutation hardware updateSettings '{"hardwareShippingSettingsUpdateSettingsInput":{"allowEditing":"INHERIT","incotermRestrictionIncludeSelf":true,"restrictedIncoterm":["EXW"],"shippingCostVisibility":"INHERIT"}}'

catocli mutation hardware updateSettings '{
    "hardwareShippingSettingsUpdateSettingsInput": {
        "allowEditing": "INHERIT",
        "incotermRestrictionIncludeSelf": true,
        "restrictedIncoterm": [
            "EXW"
        ],
        "shippingCostVisibility": "INHERIT"
    }
}'
```

#### Operation Arguments for mutation.hardware.updateSettings ####

`accountId` [ID] - (required) N/A
`hardwareShippingSettingsUpdateSettingsInput` [HardwareShippingSettingsUpdateSettingsInput] - (required) N/A
