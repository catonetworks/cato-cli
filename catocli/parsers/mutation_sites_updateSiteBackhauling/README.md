
## CATO-CLI - mutation.sites.updateSiteBackhauling:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSiteBackhauling) for documentation on this operation.

### Usage for mutation.sites.updateSiteBackhauling:

```bash
catocli mutation sites updateSiteBackhauling -h

catocli mutation sites updateSiteBackhauling <json>

catocli mutation sites updateSiteBackhauling --json-file mutation.sites.updateSiteBackhauling.json

catocli mutation sites updateSiteBackhauling '{"updateSiteBackhaulingInput":{"destination":"LOCAL_GATEWAY_IP","nextHopIP":"example_value","preferredSocketPort":"string","siteRefInput":{"by":"ID","input":"string"},"useAsBackhaulingGW":true}}'

catocli mutation sites updateSiteBackhauling '{
    "updateSiteBackhaulingInput": {
        "destination": "LOCAL_GATEWAY_IP",
        "nextHopIP": "example_value",
        "preferredSocketPort": "string",
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        },
        "useAsBackhaulingGW": true
    }
}'
```

#### Operation Arguments for mutation.sites.updateSiteBackhauling ####

`accountId` [ID] - (required) N/A    
`updateSiteBackhaulingInput` [UpdateSiteBackhaulingInput] - (required) N/A    
