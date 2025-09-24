
## CATO-CLI - mutation.sites.addSecondaryAzureVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addSecondaryAzureVSocket) for documentation on this operation.

### Usage for mutation.sites.addSecondaryAzureVSocket:

`catocli mutation sites addSecondaryAzureVSocket -h`

`catocli mutation sites addSecondaryAzureVSocket <json>`

`catocli mutation sites addSecondaryAzureVSocket "$(cat < mutation.sites.addSecondaryAzureVSocket.json)"`

`catocli mutation sites addSecondaryAzureVSocket '{"addSecondaryAzureVSocketInput":{"floatingIp":"example_value","interfaceIp":"example_value","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation sites addSecondaryAzureVSocket -p '{
    "addSecondaryAzureVSocketInput": {
        "floatingIp": "example_value",
        "interfaceIp": "example_value",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for mutation.sites.addSecondaryAzureVSocket ####

`accountId` [ID] - (required) N/A    
`addSecondaryAzureVSocketInput` [AddSecondaryAzureVSocketInput] - (required) N/A    
