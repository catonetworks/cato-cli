
## CATO-CLI - mutation.site.addSocketAddOnCard:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addSocketAddOnCard) for documentation on this operation.

### Usage for mutation.site.addSocketAddOnCard:

```bash
catocli mutation site addSocketAddOnCard -h

catocli mutation site addSocketAddOnCard <json>

catocli mutation site addSocketAddOnCard --json-file mutation.site.addSocketAddOnCard.json

catocli mutation site addSocketAddOnCard '{"addSocketAddOnCardInput":{"addOns":{"expansionSlotNumber":"SLOT_1","type":"FOUR_1G_COPPER"},"site":{"by":"ID","input":"string"}}}'

catocli mutation site addSocketAddOnCard '{
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

#### Operation Arguments for mutation.site.addSocketAddOnCard ####

`accountId` [ID] - (required) N/A    
`addSocketAddOnCardInput` [AddSocketAddOnCardInput] - (required) N/A    
