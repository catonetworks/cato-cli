
## CATO-CLI - mutation.site.updateStaticHost:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateStaticHost) for documentation on this operation.

### Usage for mutation.site.updateStaticHost:

`catocli mutation site updateStaticHost -h`

`catocli mutation site updateStaticHost <json>`

`catocli mutation site updateStaticHost "$(cat < mutation.site.updateStaticHost.json)"`

`catocli mutation site updateStaticHost '{"hostId":"id","updateStaticHostInput":{"ip":"example_value","macAddress":"string","name":"string"}}'`

`catocli mutation site updateStaticHost -p '{
    "hostId": "id",
    "updateStaticHostInput": {
        "ip": "example_value",
        "macAddress": "string",
        "name": "string"
    }
}'`


#### Operation Arguments for mutation.site.updateStaticHost ####

`accountId` [ID] - (required) N/A    
`hostId` [ID] - (required) N/A    
`updateStaticHostInput` [UpdateStaticHostInput] - (required) N/A    
