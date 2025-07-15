
## CATO-CLI - mutation.sites.startSiteUpgrade:
[Click here](https://api.catonetworks.com/documentation/#mutation-startSiteUpgrade) for documentation on this operation.

### Usage for mutation.sites.startSiteUpgrade:

`catocli mutation sites startSiteUpgrade -h`

`catocli mutation sites startSiteUpgrade <json>`

`catocli mutation sites startSiteUpgrade "$(cat < startSiteUpgrade.json)"`

`catocli mutation sites startSiteUpgrade '{"startSiteUpgradeInput": {"siteUpgradeRequest": {"site": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "targetVersion": {"targetVersion": "String"}}}}'`

#### Operation Arguments for mutation.sites.startSiteUpgrade ####
`accountId` [ID] - (required) N/A 
`startSiteUpgradeInput` [StartSiteUpgradeInput] - (required) N/A 
