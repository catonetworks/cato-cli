
## CATO-CLI - mutation.sites.updateStaticHost:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateStaticHost) for documentation on this operation.

### Usage for mutation.sites.updateStaticHost:

`catocli mutation sites updateStaticHost -h`

`catocli mutation sites updateStaticHost <accountID> <json>`

`catocli mutation sites updateStaticHost 12345 "$(cat < updateStaticHost.json)"`

`catocli mutation sites updateStaticHost 12345 '{"UpdateStaticHostInput": {"ip": {"ip": "IPAddress"}, "macAddress": {"macAddress": "String"}, "name": {"name": "String"}}, "hostId": "ID"}'`

#### Operation Arguments for mutation.sites.updateStaticHost ####
`UpdateStaticHostInput` [UpdateStaticHostInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`hostId` [ID] - (required) N/A 