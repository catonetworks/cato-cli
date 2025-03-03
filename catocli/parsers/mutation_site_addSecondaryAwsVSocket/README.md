
## CATO-CLI - mutation.site.addSecondaryAwsVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSecondaryAwsVSocket) for documentation on this operation.

### Usage for mutation.site.addSecondaryAwsVSocket:

`catocli mutation site addSecondaryAwsVSocket -h`

`catocli mutation site addSecondaryAwsVSocket <json>`

`catocli mutation site addSecondaryAwsVSocket "$(cat < addSecondaryAwsVSocket.json)"`

`catocli mutation site addSecondaryAwsVSocket '{"addSecondaryAwsVSocketInput": {"eniIpAddress": {"eniIpAddress": "IPAddress"}, "eniIpSubnet": {"eniIpSubnet": "NetworkSubnet"}, "routeTableId": {"routeTableId": "String"}, "siteRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}}'`

#### Operation Arguments for mutation.site.addSecondaryAwsVSocket ####
`accountId` [ID] - (required) N/A 
`addSecondaryAwsVSocketInput` [AddSecondaryAwsVSocketInput] - (required) N/A 
