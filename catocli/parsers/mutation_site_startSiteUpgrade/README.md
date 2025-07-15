
## CATO-CLI - mutation.site.startSiteUpgrade:
[Click here](https://api.catonetworks.com/documentation/#mutation-startSiteUpgrade) for documentation on this operation.

### Usage for mutation.site.startSiteUpgrade:

`catocli mutation site startSiteUpgrade -h`

`catocli mutation site startSiteUpgrade <json>`

`catocli mutation site startSiteUpgrade "$(cat < startSiteUpgrade.json)"`

`catocli mutation site startSiteUpgrade '{"startSiteUpgradeInput": {"siteUpgradeRequest": {"site": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "targetVersion": {"targetVersion": "String"}}}}'`

#### Operation Arguments for mutation.site.startSiteUpgrade ####
`accountId` [ID] - (required) N/A 
`startSiteUpgradeInput` [StartSiteUpgradeInput] - (required) N/A 
