
## CATO-CLI - mutation.site.updateStaticHost:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateStaticHost) for documentation on this operation.

### Usage for mutation.site.updateStaticHost:

`catocli mutation site updateStaticHost -h`

`catocli mutation site updateStaticHost <accountID> <json>`

`catocli mutation site updateStaticHost 12345 "$(cat < updateStaticHost.json)"`

`catocli mutation site updateStaticHost 12345 '{"UpdateStaticHostInput": {"ip": {"ip": "IPAddress"}, "macAddress": {"macAddress": "String"}, "name": {"name": "String"}}, "hostId": "ID"}'`

#### Operation Arguments for mutation.site.updateStaticHost ####
`UpdateStaticHostInput` [UpdateStaticHostInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
`hostId` [ID] - (required) N/A 
