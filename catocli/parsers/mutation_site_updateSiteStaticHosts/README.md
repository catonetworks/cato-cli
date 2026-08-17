
## CATO-CLI - mutation.site.updateSiteStaticHosts:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSiteStaticHosts) for documentation on this operation.

### Usage for mutation.site.updateSiteStaticHosts:

```bash
catocli mutation site updateSiteStaticHosts -h

catocli mutation site updateSiteStaticHosts <json>

catocli mutation site updateSiteStaticHosts --json-file mutation.site.updateSiteStaticHosts.json

catocli mutation site updateSiteStaticHosts '{"updateSiteStaticHostsInput":{"siteAddStaticHostInput":{"ip":"example_value","macAddress":"example_value","name":"string"},"siteRefInput":{"by":"ID","input":"string"},"siteStaticHostConfigurationInput":{"ip":"example_value","macAddress":"example_value","name":"string"},"siteStaticHostRefInput":{"hostId":"id"}}}'

catocli mutation site updateSiteStaticHosts '{
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

#### Operation Arguments for mutation.site.updateSiteStaticHosts ####

`accountId` [ID] - (required) N/A    
`updateSiteStaticHostsInput` [UpdateSiteStaticHostsInput] - (required) N/A    
