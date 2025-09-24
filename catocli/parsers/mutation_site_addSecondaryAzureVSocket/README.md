
## CATO-CLI - mutation.site.addSecondaryAzureVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addSecondaryAzureVSocket) for documentation on this operation.

### Usage for mutation.site.addSecondaryAzureVSocket:

`catocli mutation site addSecondaryAzureVSocket -h`

`catocli mutation site addSecondaryAzureVSocket <json>`

`catocli mutation site addSecondaryAzureVSocket "$(cat < mutation.site.addSecondaryAzureVSocket.json)"`

`catocli mutation site addSecondaryAzureVSocket '{"addSecondaryAzureVSocketInput":{"floatingIp":"example_value","interfaceIp":"example_value","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation site addSecondaryAzureVSocket -p '{
    "addSecondaryAzureVSocketInput": {
        "floatingIp": "example_value",
        "interfaceIp": "example_value",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for mutation.site.addSecondaryAzureVSocket ####

`accountId` [ID] - (required) N/A    
`addSecondaryAzureVSocketInput` [AddSecondaryAzureVSocketInput] - (required) N/A    
