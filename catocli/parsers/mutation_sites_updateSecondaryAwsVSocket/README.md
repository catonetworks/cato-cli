
## CATO-CLI - mutation.sites.updateSecondaryAwsVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSecondaryAwsVSocket) for documentation on this operation.

### Usage for mutation.sites.updateSecondaryAwsVSocket:

`catocli mutation sites updateSecondaryAwsVSocket -h`

`catocli mutation sites updateSecondaryAwsVSocket <json>`

`catocli mutation sites updateSecondaryAwsVSocket "$(cat < mutation.sites.updateSecondaryAwsVSocket.json)"`

`catocli mutation sites updateSecondaryAwsVSocket '{"updateSecondaryAwsVSocketInput":{"id":"id","ipAddress":"example_value","routeTableId":"string","subnet":"example_value"}}'`

`catocli mutation sites updateSecondaryAwsVSocket -p '{
    "updateSecondaryAwsVSocketInput": {
        "id": "id",
        "ipAddress": "example_value",
        "routeTableId": "string",
        "subnet": "example_value"
    }
}'`


#### Operation Arguments for mutation.sites.updateSecondaryAwsVSocket ####

`accountId` [ID] - (required) N/A    
`updateSecondaryAwsVSocketInput` [UpdateSecondaryAwsVSocketInput] - (required) N/A    
