
## CATO-CLI - mutation.sites.addSecondaryAzureVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSecondaryAzureVSocket) for documentation on this operation.

### Usage for mutation.sites.addSecondaryAzureVSocket:

`catocli mutation sites addSecondaryAzureVSocket -h`

`catocli mutation sites addSecondaryAzureVSocket <json>`

`catocli mutation sites addSecondaryAzureVSocket "$(cat < addSecondaryAzureVSocket.json)"`

`catocli mutation sites addSecondaryAzureVSocket '{"addSecondaryAzureVSocketInput": {"floatingIp": {"floatingIp": "IPAddress"}, "interfaceIp": {"interfaceIp": "IPAddress"}, "siteRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}}'`

#### Operation Arguments for mutation.sites.addSecondaryAzureVSocket ####
`accountId` [ID] - (required) N/A 
`addSecondaryAzureVSocketInput` [AddSecondaryAzureVSocketInput] - (required) N/A 
