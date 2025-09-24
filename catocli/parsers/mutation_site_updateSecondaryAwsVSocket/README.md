
## CATO-CLI - mutation.site.updateSecondaryAwsVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSecondaryAwsVSocket) for documentation on this operation.

### Usage for mutation.site.updateSecondaryAwsVSocket:

`catocli mutation site updateSecondaryAwsVSocket -h`

`catocli mutation site updateSecondaryAwsVSocket <json>`

`catocli mutation site updateSecondaryAwsVSocket "$(cat < mutation.site.updateSecondaryAwsVSocket.json)"`

`catocli mutation site updateSecondaryAwsVSocket '{"updateSecondaryAwsVSocketInput":{"id":"id","ipAddress":"example_value","routeTableId":"string","subnet":"example_value"}}'`

`catocli mutation site updateSecondaryAwsVSocket -p '{
    "updateSecondaryAwsVSocketInput": {
        "id": "id",
        "ipAddress": "example_value",
        "routeTableId": "string",
        "subnet": "example_value"
    }
}'`


#### Operation Arguments for mutation.site.updateSecondaryAwsVSocket ####

`accountId` [ID] - (required) N/A    
`updateSecondaryAwsVSocketInput` [UpdateSecondaryAwsVSocketInput] - (required) N/A    
