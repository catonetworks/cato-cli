
## CATO-CLI - mutation.site.addSocketAddOnCard:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSocketAddOnCard) for documentation on this operation.

### Usage for mutation.site.addSocketAddOnCard:

`catocli mutation site addSocketAddOnCard -h`

`catocli mutation site addSocketAddOnCard <json>`

`catocli mutation site addSocketAddOnCard "$(cat < addSocketAddOnCard.json)"`

`catocli mutation site addSocketAddOnCard '{"addSocketAddOnCardInput": {"siteRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "socketAddOnCardInput": {"expansionSlotNumber": {"expansionSlotNumber": "enum(SocketAddOnExpansionSlotNumber)"}, "type": {"type": "enum(SocketAddOnType)"}}}}'`

#### Operation Arguments for mutation.site.addSocketAddOnCard ####
`accountId` [ID] - (required) N/A 
`addSocketAddOnCardInput` [AddSocketAddOnCardInput] - (required) N/A 
