
## CATO-CLI - mutation.site.updateSiteStaticHosts:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSiteStaticHosts) for documentation on this operation.

### Usage for mutation.site.updateSiteStaticHosts:

```bash
catocli mutation site updateSiteStaticHosts -h

catocli mutation site updateSiteStaticHosts <json>

catocli mutation site updateSiteStaticHosts --json-file mutation.site.updateSiteStaticHosts.json

catocli mutation site updateSiteStaticHosts '{"updateSiteStaticHostsInput":{"host":[{"ip":"192.0.2.1","macAddress":"02:00:00:00:00:01","name":"string"}],"hostToAdd":[{"ip":"192.0.2.1","macAddress":"02:00:00:00:00:01","name":"string"}],"hostToRemove":[{"hostId":"id"}],"site":{"by":"ID","input":"string"}}}'

catocli mutation site updateSiteStaticHosts '{
    "updateSiteStaticHostsInput": {
        "host": [
            {
                "ip": "192.0.2.1",
                "macAddress": "02:00:00:00:00:01",
                "name": "string"
            }
        ],
        "hostToAdd": [
            {
                "ip": "192.0.2.1",
                "macAddress": "02:00:00:00:00:01",
                "name": "string"
            }
        ],
        "hostToRemove": [
            {
                "hostId": "id"
            }
        ],
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
