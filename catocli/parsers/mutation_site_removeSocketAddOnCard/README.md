
## CATO-CLI - mutation.site.removeSocketAddOnCard:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.removeSocketAddOnCard) for documentation on this operation.

### Usage for mutation.site.removeSocketAddOnCard:

`catocli mutation site removeSocketAddOnCard -h`

`catocli mutation site removeSocketAddOnCard <json>`

`catocli mutation site removeSocketAddOnCard "$(cat < mutation.site.removeSocketAddOnCard.json)"`

`catocli mutation site removeSocketAddOnCard '{"removeSocketAddOnCardInput":{"expansionSlotNumbers":"SLOT_1","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation site removeSocketAddOnCard -p '{
    "removeSocketAddOnCardInput": {
        "expansionSlotNumbers": "SLOT_1",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for mutation.site.removeSocketAddOnCard ####

`accountId` [ID] - (required) N/A    
`removeSocketAddOnCardInput` [RemoveSocketAddOnCardInput] - (required) N/A    
