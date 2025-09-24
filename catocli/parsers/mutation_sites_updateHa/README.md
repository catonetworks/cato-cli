
## CATO-CLI - mutation.sites.updateHa:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateHa) for documentation on this operation.

### Usage for mutation.sites.updateHa:

`catocli mutation sites updateHa -h`

`catocli mutation sites updateHa <json>`

`catocli mutation sites updateHa "$(cat < mutation.sites.updateHa.json)"`

`catocli mutation sites updateHa '{"siteId":"id","updateHaInput":{"primaryManagementIp":"example_value","secondaryManagementIp":"example_value","vrid":1}}'`

`catocli mutation sites updateHa -p '{
    "siteId": "id",
    "updateHaInput": {
        "primaryManagementIp": "example_value",
        "secondaryManagementIp": "example_value",
        "vrid": 1
    }
}'`


#### Operation Arguments for mutation.sites.updateHa ####

`accountId` [ID] - (required) N/A    
`siteId` [ID] - (required) N/A    
`updateHaInput` [UpdateHaInput] - (required) N/A    
