
## CATO-CLI - mutation.sites.startSiteUpgrade:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.startSiteUpgrade) for documentation on this operation.

### Usage for mutation.sites.startSiteUpgrade:

`catocli mutation sites startSiteUpgrade -h`

`catocli mutation sites startSiteUpgrade <json>`

`catocli mutation sites startSiteUpgrade "$(cat < mutation.sites.startSiteUpgrade.json)"`

`catocli mutation sites startSiteUpgrade '{"startSiteUpgradeInput":{"siteUpgradeRequest":{"site":{"by":"ID","input":"string"},"targetVersion":"string"}}}'`

`catocli mutation sites startSiteUpgrade -p '{
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


#### Operation Arguments for mutation.sites.startSiteUpgrade ####

`accountId` [ID] - (required) N/A    
`startSiteUpgradeInput` [StartSiteUpgradeInput] - (required) N/A    
