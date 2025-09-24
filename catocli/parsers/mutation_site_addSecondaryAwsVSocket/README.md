
## CATO-CLI - mutation.site.addSecondaryAwsVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addSecondaryAwsVSocket) for documentation on this operation.

### Usage for mutation.site.addSecondaryAwsVSocket:

`catocli mutation site addSecondaryAwsVSocket -h`

`catocli mutation site addSecondaryAwsVSocket <json>`

`catocli mutation site addSecondaryAwsVSocket "$(cat < mutation.site.addSecondaryAwsVSocket.json)"`

`catocli mutation site addSecondaryAwsVSocket '{"addSecondaryAwsVSocketInput":{"eniIpAddress":"example_value","eniIpSubnet":"example_value","routeTableId":"string","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation site addSecondaryAwsVSocket -p '{
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


#### Operation Arguments for mutation.site.addSecondaryAwsVSocket ####

`accountId` [ID] - (required) N/A    
`addSecondaryAwsVSocketInput` [AddSecondaryAwsVSocketInput] - (required) N/A    
