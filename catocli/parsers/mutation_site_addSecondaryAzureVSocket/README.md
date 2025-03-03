
## CATO-CLI - mutation.site.addSecondaryAzureVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSecondaryAzureVSocket) for documentation on this operation.

### Usage for mutation.site.addSecondaryAzureVSocket:

`catocli mutation site addSecondaryAzureVSocket -h`

`catocli mutation site addSecondaryAzureVSocket <json>`

`catocli mutation site addSecondaryAzureVSocket "$(cat < addSecondaryAzureVSocket.json)"`

`catocli mutation site addSecondaryAzureVSocket '{"addSecondaryAzureVSocketInput": {"floatingIp": {"floatingIp": "IPAddress"}, "interfaceIp": {"interfaceIp": "IPAddress"}, "siteRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}}'`

#### Operation Arguments for mutation.site.addSecondaryAzureVSocket ####
`accountId` [ID] - (required) N/A 
`addSecondaryAzureVSocketInput` [AddSecondaryAzureVSocketInput] - (required) N/A 
