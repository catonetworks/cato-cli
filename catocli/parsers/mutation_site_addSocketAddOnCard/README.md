
## CATO-CLI - mutation.site.addSocketAddOnCard:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addSocketAddOnCard) for documentation on this operation.

### Usage for mutation.site.addSocketAddOnCard:

`catocli mutation site addSocketAddOnCard -h`

`catocli mutation site addSocketAddOnCard <json>`

`catocli mutation site addSocketAddOnCard "$(cat < mutation.site.addSocketAddOnCard.json)"`

`catocli mutation site addSocketAddOnCard '{"addSocketAddOnCardInput":{"siteRefInput":{"by":"ID","input":"string"},"socketAddOnCardInput":{"expansionSlotNumber":"SLOT_1","type":"FOUR_1G_COPPER"}}}'`

`catocli mutation site addSocketAddOnCard -p '{
    "addSocketAddOnCardInput": {
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        },
        "socketAddOnCardInput": {
            "expansionSlotNumber": "SLOT_1",
            "type": "FOUR_1G_COPPER"
        }
    }
}'`


#### Operation Arguments for mutation.site.addSocketAddOnCard ####

`accountId` [ID] - (required) N/A    
`addSocketAddOnCardInput` [AddSocketAddOnCardInput] - (required) N/A    
