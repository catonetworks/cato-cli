
## CATO-CLI - mutation.sites.addSecondaryAwsVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addSecondaryAwsVSocket) for documentation on this operation.

### Usage for mutation.sites.addSecondaryAwsVSocket:

`catocli mutation sites addSecondaryAwsVSocket -h`

`catocli mutation sites addSecondaryAwsVSocket <json>`

`catocli mutation sites addSecondaryAwsVSocket "$(cat < mutation.sites.addSecondaryAwsVSocket.json)"`

`catocli mutation sites addSecondaryAwsVSocket '{"addSecondaryAwsVSocketInput":{"eniIpAddress":"example_value","eniIpSubnet":"example_value","routeTableId":"string","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation sites addSecondaryAwsVSocket -p '{
    "addSecondaryAwsVSocketInput": {
        "eniIpAddress": "example_value",
        "eniIpSubnet": "example_value",
        "routeTableId": "string",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for mutation.sites.addSecondaryAwsVSocket ####

`accountId` [ID] - (required) N/A    
`addSecondaryAwsVSocketInput` [AddSecondaryAwsVSocketInput] - (required) N/A    
