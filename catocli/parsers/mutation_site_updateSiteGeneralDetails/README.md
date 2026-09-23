
## CATO-CLI - mutation.site.updateSiteGeneralDetails:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSiteGeneralDetails) for documentation on this operation.

### Usage for mutation.site.updateSiteGeneralDetails:

```bash
catocli mutation site updateSiteGeneralDetails -h

catocli mutation site updateSiteGeneralDetails <json>

catocli mutation site updateSiteGeneralDetails --json-file mutation.site.updateSiteGeneralDetails.json

catocli mutation site updateSiteGeneralDetails '{"siteId":"id","updateSiteGeneralDetailsInput":{"description":"string","disableAclForSip":true,"name":"string","preferredPopLocation":{"preferredOnly":true,"primary":{"by":"ID","input":"string"},"secondary":{"by":"ID","input":"string"}},"siteLocation":{"address":"string","cityName":"string","countryCode":"string","stateCode":"string","timezone":"string"},"siteType":"BRANCH","workingHours":{"fromTimeMinuteOffset":1,"override":true,"toTimeMinuteOffset":1,"workingDays":"SUNDAY"}}}'

catocli mutation site updateSiteGeneralDetails '{
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

#### Operation Arguments for mutation.site.updateSiteGeneralDetails ####

`accountId` [ID] - (required) N/A    
`siteId` [ID] - (required) N/A    
`updateSiteGeneralDetailsInput` [UpdateSiteGeneralDetailsInput] - (required) N/A    
