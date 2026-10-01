
## CATO-CLI - mutation.sites.updateSiteStaticHosts:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSiteStaticHosts) for documentation on this operation.

### Usage for mutation.sites.updateSiteStaticHosts:

```bash
catocli mutation sites updateSiteStaticHosts -h

catocli mutation sites updateSiteStaticHosts <json>

catocli mutation sites updateSiteStaticHosts --json-file mutation.sites.updateSiteStaticHosts.json

catocli mutation sites updateSiteStaticHosts '{"updateSiteStaticHostsInput":{"host":[{"ip":"192.0.2.1","macAddress":"02:00:00:00:00:01","name":"string"}],"hostToAdd":[{"ip":"192.0.2.1","macAddress":"02:00:00:00:00:01","name":"string"}],"hostToRemove":[{"hostId":"id"}],"site":{"by":"ID","input":"string"}}}'

catocli mutation sites updateSiteStaticHosts '{
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

#### Operation Arguments for mutation.sites.updateSiteStaticHosts ####

`accountId` [ID] - (required) N/A
`updateSiteStaticHostsInput` [UpdateSiteStaticHostsInput] - (required) N/A
