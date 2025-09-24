
## CATO-CLI - mutation.site.addStaticHost:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addStaticHost) for documentation on this operation.

### Usage for mutation.site.addStaticHost:

`catocli mutation site addStaticHost -h`

`catocli mutation site addStaticHost <json>`

`catocli mutation site addStaticHost "$(cat < mutation.site.addStaticHost.json)"`

`catocli mutation site addStaticHost '{"addStaticHostInput":{"ip":"example_value","macAddress":"string","name":"string"},"siteId":"id"}'`

`catocli mutation site addStaticHost -p '{
    "addStaticHostInput": {
        "ip": "example_value",
        "macAddress": "string",
        "name": "string"
    },
    "siteId": "id"
}'`


#### Operation Arguments for mutation.site.addStaticHost ####

`accountId` [ID] - (required) N/A    
`addStaticHostInput` [AddStaticHostInput] - (required) N/A    
`siteId` [ID] - (required) N/A    
