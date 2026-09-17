
## CATO-CLI - mutation.sites.updateSiteStaticHosts:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSiteStaticHosts) for documentation on this operation.

### Usage for mutation.sites.updateSiteStaticHosts:

```bash
catocli mutation sites updateSiteStaticHosts -h

catocli mutation sites updateSiteStaticHosts <json>

catocli mutation sites updateSiteStaticHosts --json-file mutation.sites.updateSiteStaticHosts.json

catocli mutation sites updateSiteStaticHosts '{"updateSiteStaticHostsInput":{"host":{"ip":"example_value","macAddress":"example_value","name":"string"},"hostToAdd":{"ip":"example_value","macAddress":"example_value","name":"string"},"hostToRemove":{"hostId":"id"},"site":{"by":"ID","input":"string"}}}'

catocli mutation sites updateSiteStaticHosts '{
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

#### Operation Arguments for mutation.sites.updateSiteStaticHosts ####

`accountId` [ID] - (required) N/A    
`updateSiteStaticHostsInput` [UpdateSiteStaticHostsInput] - (required) N/A    
