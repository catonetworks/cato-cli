
## CATO-CLI - mutation.site.startSiteUpgrade:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.startSiteUpgrade) for documentation on this operation.

### Usage for mutation.site.startSiteUpgrade:

`catocli mutation site startSiteUpgrade -h`

`catocli mutation site startSiteUpgrade <json>`

`catocli mutation site startSiteUpgrade "$(cat < mutation.site.startSiteUpgrade.json)"`

`catocli mutation site startSiteUpgrade '{"startSiteUpgradeInput":{"siteUpgradeRequest":{"site":{"by":"ID","input":"string"},"targetVersion":"string"}}}'`

`catocli mutation site startSiteUpgrade -p '{
    "startSiteUpgradeInput": {
        "siteUpgradeRequest": {
            "site": {
                "by": "ID",
                "input": "string"
            },
            "targetVersion": "string"
        }
    }
}'`


#### Operation Arguments for mutation.site.startSiteUpgrade ####

`accountId` [ID] - (required) N/A    
`startSiteUpgradeInput` [StartSiteUpgradeInput] - (required) N/A    
