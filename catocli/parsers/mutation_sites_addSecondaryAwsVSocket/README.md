
## CATO-CLI - mutation.sites.addSecondaryAwsVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSecondaryAwsVSocket) for documentation on this operation.

### Usage for mutation.sites.addSecondaryAwsVSocket:

`catocli mutation sites addSecondaryAwsVSocket -h`

`catocli mutation sites addSecondaryAwsVSocket <json>`

`catocli mutation sites addSecondaryAwsVSocket "$(cat < addSecondaryAwsVSocket.json)"`

`catocli mutation sites addSecondaryAwsVSocket '{"addSecondaryAwsVSocketInput": {"eniIpAddress": {"eniIpAddress": "IPAddress"}, "eniIpSubnet": {"eniIpSubnet": "NetworkSubnet"}, "routeTableId": {"routeTableId": "String"}, "siteRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}}'`

#### Operation Arguments for mutation.sites.addSecondaryAwsVSocket ####
`accountId` [ID] - (required) N/A 
`addSecondaryAwsVSocketInput` [AddSecondaryAwsVSocketInput] - (required) N/A 
