
## CATO-CLI - mutation.sites.updateSiteStaticHosts:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSiteStaticHosts) for documentation on this operation.

### Usage for mutation.sites.updateSiteStaticHosts:

```bash
catocli mutation sites updateSiteStaticHosts -h

catocli mutation sites updateSiteStaticHosts <json>

catocli mutation sites updateSiteStaticHosts --json-file mutation.sites.updateSiteStaticHosts.json

catocli mutation sites updateSiteStaticHosts '{"updateSiteStaticHostsInput":{"siteAddStaticHostInput":{"ip":"example_value","macAddress":"example_value","name":"string"},"siteRefInput":{"by":"ID","input":"string"},"siteStaticHostConfigurationInput":{"ip":"example_value","macAddress":"example_value","name":"string"},"siteStaticHostRefInput":{"hostId":"id"}}}'

catocli mutation sites updateSiteStaticHosts '{
    "updateSiteStaticHostsInput": {
        "siteAddStaticHostInput": {
            "ip": "example_value",
            "macAddress": "example_value",
            "name": "string"
        },
        "siteRefInput": {
            "by": "ID",
            "input": "string"
        },
        "siteStaticHostConfigurationInput": {
            "ip": "example_value",
            "macAddress": "example_value",
            "name": "string"
        },
        "siteStaticHostRefInput": {
            "hostId": "id"
        }
    }
}'
```

#### Operation Arguments for mutation.sites.updateSiteStaticHosts ####

`accountId` [ID] - (required) N/A    
`updateSiteStaticHostsInput` [UpdateSiteStaticHostsInput] - (required) N/A    
