
## CATO-CLI - mutation.sites.addSocketAddOnCard:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addSocketAddOnCard) for documentation on this operation.

### Usage for mutation.sites.addSocketAddOnCard:

```bash
catocli mutation sites addSocketAddOnCard -h

catocli mutation sites addSocketAddOnCard <json>

catocli mutation sites addSocketAddOnCard --json-file mutation.sites.addSocketAddOnCard.json

catocli mutation sites addSocketAddOnCard '{"addSocketAddOnCardInput":{"addOns":{"expansionSlotNumber":"SLOT_1","type":"FOUR_1G_COPPER"},"site":{"by":"ID","input":"string"}}}'

catocli mutation sites addSocketAddOnCard '{
    "addSocketAddOnCardInput": {
        "addOns": {
            "expansionSlotNumber": "SLOT_1",
            "type": "FOUR_1G_COPPER"
        },
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.addSocketAddOnCard ####

`accountId` [ID] - (required) N/A    
`addSocketAddOnCardInput` [AddSocketAddOnCardInput] - (required) N/A    
