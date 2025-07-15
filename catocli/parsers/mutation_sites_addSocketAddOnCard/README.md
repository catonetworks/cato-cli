
## CATO-CLI - mutation.sites.addSocketAddOnCard:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSocketAddOnCard) for documentation on this operation.

### Usage for mutation.sites.addSocketAddOnCard:

`catocli mutation sites addSocketAddOnCard -h`

`catocli mutation sites addSocketAddOnCard <json>`

`catocli mutation sites addSocketAddOnCard "$(cat < addSocketAddOnCard.json)"`

`catocli mutation sites addSocketAddOnCard '{"addSocketAddOnCardInput": {"siteRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "socketAddOnCardInput": {"expansionSlotNumber": {"expansionSlotNumber": "enum(SocketAddOnExpansionSlotNumber)"}, "type": {"type": "enum(SocketAddOnType)"}}}}'`

#### Operation Arguments for mutation.sites.addSocketAddOnCard ####
`accountId` [ID] - (required) N/A 
`addSocketAddOnCardInput` [AddSocketAddOnCardInput] - (required) N/A 
