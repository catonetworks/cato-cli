
## CATO-CLI - query.site.availableVersionList:
[Click here](https://api.catonetworks.com/documentation/#query-query.site.availableVersionList) for documentation on this operation.

### Usage for query.site.availableVersionList:

`catocli query site availableVersionList -h`

`catocli query site availableVersionList <json>`

`catocli query site availableVersionList "$(cat < query.site.availableVersionList.json)"`

`catocli query site availableVersionList '{"availableVersionListInput":{"platforms":["string1","string2"]}}'`

`catocli query site availableVersionList -p '{
    "availableVersionListInput": {
        "platforms": [
            "string1",
            "string2"
        ]
    }
}'`


#### Operation Arguments for query.site.availableVersionList ####

`accountId` [ID] - (required) N/A    
`availableVersionListInput` [AvailableVersionListInput] - (required) N/A    
