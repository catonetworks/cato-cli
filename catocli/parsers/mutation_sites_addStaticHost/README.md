
## CATO-CLI - mutation.sites.addStaticHost:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addStaticHost) for documentation on this operation.

### Usage for mutation.sites.addStaticHost:

`catocli mutation sites addStaticHost -h`

`catocli mutation sites addStaticHost <json>`

`catocli mutation sites addStaticHost "$(cat < mutation.sites.addStaticHost.json)"`

`catocli mutation sites addStaticHost '{"addStaticHostInput":{"ip":"example_value","macAddress":"string","name":"string"},"siteId":"id"}'`

`catocli mutation sites addStaticHost -p '{
    "addStaticHostInput": {
        "ip": "example_value",
        "macAddress": "string",
        "name": "string"
    },
    "siteId": "id"
}'`


#### Operation Arguments for mutation.sites.addStaticHost ####

`accountId` [ID] - (required) N/A    
`addStaticHostInput` [AddStaticHostInput] - (required) N/A    
`siteId` [ID] - (required) N/A    
