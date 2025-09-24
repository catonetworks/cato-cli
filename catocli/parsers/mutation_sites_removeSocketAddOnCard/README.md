
## CATO-CLI - mutation.sites.removeSocketAddOnCard:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.removeSocketAddOnCard) for documentation on this operation.

### Usage for mutation.sites.removeSocketAddOnCard:

`catocli mutation sites removeSocketAddOnCard -h`

`catocli mutation sites removeSocketAddOnCard <json>`

`catocli mutation sites removeSocketAddOnCard "$(cat < mutation.sites.removeSocketAddOnCard.json)"`

`catocli mutation sites removeSocketAddOnCard '{"removeSocketAddOnCardInput":{"expansionSlotNumbers":"SLOT_1","siteRefInput":{"by":"ID","input":"string"}}}'`

`catocli mutation sites removeSocketAddOnCard -p '{
    "removeSocketAddOnCardInput": {
        "expansionSlotNumbers": "SLOT_1",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        }
    }
}'`


#### Operation Arguments for mutation.sites.removeSocketAddOnCard ####

`accountId` [ID] - (required) N/A    
`removeSocketAddOnCardInput` [RemoveSocketAddOnCardInput] - (required) N/A    
