
## CATO-CLI - mutation.sites.addSocketAddOnCard:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addSocketAddOnCard) for documentation on this operation.

### Usage for mutation.sites.addSocketAddOnCard:

`catocli mutation sites addSocketAddOnCard -h`

`catocli mutation sites addSocketAddOnCard <json>`

`catocli mutation sites addSocketAddOnCard "$(cat < mutation.sites.addSocketAddOnCard.json)"`

`catocli mutation sites addSocketAddOnCard '{"addSocketAddOnCardInput":{"siteRefInput":{"by":"ID","input":"string"},"socketAddOnCardInput":{"expansionSlotNumber":"SLOT_1","type":"FOUR_1G_COPPER"}}}'`

`catocli mutation sites addSocketAddOnCard -p '{
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


#### Operation Arguments for mutation.sites.addSocketAddOnCard ####

`accountId` [ID] - (required) N/A    
`addSocketAddOnCardInput` [AddSocketAddOnCardInput] - (required) N/A    
