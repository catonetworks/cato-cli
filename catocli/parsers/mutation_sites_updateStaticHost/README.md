
## CATO-CLI - mutation.sites.updateStaticHost:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateStaticHost) for documentation on this operation.

### Usage for mutation.sites.updateStaticHost:

`catocli mutation sites updateStaticHost -h`

`catocli mutation sites updateStaticHost <json>`

`catocli mutation sites updateStaticHost "$(cat < mutation.sites.updateStaticHost.json)"`

`catocli mutation sites updateStaticHost '{"hostId":"id","updateStaticHostInput":{"ip":"example_value","macAddress":"string","name":"string"}}'`

`catocli mutation sites updateStaticHost -p '{
    "hostId": "id",
    "updateStaticHostInput": {
        "ip": "example_value",
        "macAddress": "string",
        "name": "string"
    }
}'`


#### Operation Arguments for mutation.sites.updateStaticHost ####

`accountId` [ID] - (required) N/A    
`hostId` [ID] - (required) N/A    
`updateStaticHostInput` [UpdateStaticHostInput] - (required) N/A    
