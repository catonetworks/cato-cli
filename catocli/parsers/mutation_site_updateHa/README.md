
## CATO-CLI - mutation.site.updateHa:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateHa) for documentation on this operation.

### Usage for mutation.site.updateHa:

`catocli mutation site updateHa -h`

`catocli mutation site updateHa <json>`

`catocli mutation site updateHa "$(cat < mutation.site.updateHa.json)"`

`catocli mutation site updateHa '{"siteId":"id","updateHaInput":{"primaryManagementIp":"example_value","secondaryManagementIp":"example_value","vrid":1}}'`

`catocli mutation site updateHa -p '{
    "siteId": "id",
    "updateHaInput": {
        "primaryManagementIp": "example_value",
        "secondaryManagementIp": "example_value",
        "vrid": 1
    }
}'`


#### Operation Arguments for mutation.site.updateHa ####

`accountId` [ID] - (required) N/A    
`siteId` [ID] - (required) N/A    
`updateHaInput` [UpdateHaInput] - (required) N/A    
