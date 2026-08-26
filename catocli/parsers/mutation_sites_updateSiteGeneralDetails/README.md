
## CATO-CLI - mutation.sites.updateSiteGeneralDetails:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSiteGeneralDetails) for documentation on this operation.

### Usage for mutation.sites.updateSiteGeneralDetails:

```bash
catocli mutation sites updateSiteGeneralDetails -h

catocli mutation sites updateSiteGeneralDetails <json>

catocli mutation sites updateSiteGeneralDetails --json-file mutation.sites.updateSiteGeneralDetails.json

catocli mutation sites updateSiteGeneralDetails '{"siteId":"id","updateSiteGeneralDetailsInput":{"description":"string","disableAclForSip":true,"name":"string","preferredPopLocation":{"preferredOnly":true,"primary":{"by":"ID","input":"string"},"secondary":{"by":"ID","input":"string"}},"siteLocation":{"address":"string","cityName":"string","countryCode":"string","stateCode":"string","timezone":"string"},"siteType":"BRANCH","workingHours":{"fromTimeMinuteOffset":1,"override":true,"toTimeMinuteOffset":1,"workingDays":"SUNDAY"}}}'

catocli mutation sites updateSiteGeneralDetails '{
    "siteId": "id",
    "updateSiteGeneralDetailsInput": {
        "description": "string",
        "disableAclForSip": true,
        "name": "string",
        "preferredPopLocation": {
            "preferredOnly": true,
            "primary": {
                "by": "ID",
                "input": "string"
            },
            "secondary": {
                "by": "ID",
                "input": "string"
            }
        },
        "siteLocation": {
            "address": "string",
            "cityName": "string",
            "countryCode": "string",
            "stateCode": "string",
            "timezone": "string"
        },
        "siteType": "BRANCH",
        "workingHours": {
            "fromTimeMinuteOffset": 1,
            "override": true,
            "toTimeMinuteOffset": 1,
            "workingDays": "SUNDAY"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.updateSiteGeneralDetails ####

`accountId` [ID] - (required) N/A    
`siteId` [ID] - (required) N/A    
`updateSiteGeneralDetailsInput` [UpdateSiteGeneralDetailsInput] - (required) N/A    
