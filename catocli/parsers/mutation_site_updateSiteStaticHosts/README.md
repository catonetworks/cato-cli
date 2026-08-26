
## CATO-CLI - mutation.site.updateSiteStaticHosts:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSiteStaticHosts) for documentation on this operation.

### Usage for mutation.site.updateSiteStaticHosts:

```bash
catocli mutation site updateSiteStaticHosts -h

catocli mutation site updateSiteStaticHosts <json>

catocli mutation site updateSiteStaticHosts --json-file mutation.site.updateSiteStaticHosts.json

catocli mutation site updateSiteStaticHosts '{"updateSiteStaticHostsInput":{"host":{"ip":"example_value","macAddress":"example_value","name":"string"},"hostToAdd":{"ip":"example_value","macAddress":"example_value","name":"string"},"hostToRemove":{"hostId":"id"},"site":{"by":"ID","input":"string"}}}'

catocli mutation site updateSiteStaticHosts '{
    "updateSiteStaticHostsInput": {
        "host": {
            "ip": "example_value",
            "macAddress": "example_value",
            "name": "string"
        },
        "hostToAdd": {
            "ip": "example_value",
            "macAddress": "example_value",
            "name": "string"
        },
        "hostToRemove": {
            "hostId": "id"
        },
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.updateSiteStaticHosts ####

`accountId` [ID] - (required) N/A    
`updateSiteStaticHostsInput` [UpdateSiteStaticHostsInput] - (required) N/A    
