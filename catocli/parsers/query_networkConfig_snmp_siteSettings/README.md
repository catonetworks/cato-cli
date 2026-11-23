
## CATO-CLI - query.networkConfig.snmp.siteSettings:
[Click here](https://api.catonetworks.com/documentation/#query-query.networkConfig.snmp.siteSettings) for documentation on this operation.

### Usage for query.networkConfig.snmp.siteSettings:

```bash
catocli query networkConfig snmp siteSettings -h

catocli query networkConfig snmp siteSettings <json>

catocli query networkConfig snmp siteSettings --json-file query.networkConfig.snmp.siteSettings.json

catocli query networkConfig snmp siteSettings '{"siteRefInput":{"by":"ID","input":"string"}}'

catocli query networkConfig snmp siteSettings '{
    "siteRefInput": {
        "by": "ID",
        "input": "string"
    }
}'
```

#### Operation Arguments for query.networkConfig.snmp.siteSettings ####

`accountId` [ID] - (required) ID of the account whose network configuration is requested.
`siteRefInput` [SiteRefInput] - (required) N/A
