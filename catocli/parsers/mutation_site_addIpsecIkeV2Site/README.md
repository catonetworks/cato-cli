
## CATO-CLI - mutation.site.addIpsecIkeV2Site:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addIpsecIkeV2Site) for documentation on this operation.

### Usage for mutation.site.addIpsecIkeV2Site:

```bash
catocli mutation site addIpsecIkeV2Site -h

catocli mutation site addIpsecIkeV2Site <json>

catocli mutation site addIpsecIkeV2Site --json-file mutation.site.addIpsecIkeV2Site.json

catocli mutation site addIpsecIkeV2Site '{"addIpsecIkeV2SiteInput":{"description":"string","name":"string","nativeNetworkRange":"192.0.2.0/24","siteLocation":{"address":"string","city":"string","countryCode":"string","stateCode":"string","timezone":"string"},"siteType":"BRANCH","vlan":100}}'

catocli mutation site addIpsecIkeV2Site '{
    "addIpsecIkeV2SiteInput": {
        "description": "string",
        "name": "string",
        "nativeNetworkRange": "192.0.2.0/24",
        "siteLocation": {
            "address": "string",
            "city": "string",
            "countryCode": "string",
            "stateCode": "string",
            "timezone": "string"
        },
        "siteType": "BRANCH",
        "vlan": 100
    }
}'
```

#### Operation Arguments for mutation.site.addIpsecIkeV2Site ####

`accountId` [ID] - (required) N/A
`addIpsecIkeV2SiteInput` [AddIpsecIkeV2SiteInput] - (required) N/A
