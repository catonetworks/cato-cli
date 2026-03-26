
## CATO-CLI - mutation.site.updateSiteBackhauling:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSiteBackhauling) for documentation on this operation.

### Usage for mutation.site.updateSiteBackhauling:

```bash
catocli mutation site updateSiteBackhauling -h

catocli mutation site updateSiteBackhauling <json>

catocli mutation site updateSiteBackhauling --json-file mutation.site.updateSiteBackhauling.json

catocli mutation site updateSiteBackhauling '{"updateSiteBackhaulingInput":{"destination":"LOCAL_GATEWAY_IP","nextHopIP":"example_value","preferredSocketPort":"string","siteRefInput":{"by":"ID","input":"string"},"useAsBackhaulingGW":true}}'

catocli mutation site updateSiteBackhauling '{
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

#### Operation Arguments for mutation.site.updateSiteBackhauling ####

`accountId` [ID] - (required) N/A    
`updateSiteBackhaulingInput` [UpdateSiteBackhaulingInput] - (required) N/A    
