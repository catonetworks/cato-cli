
## CATO-CLI - mutation.site.addSecondaryAwsVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.addSecondaryAwsVSocket) for documentation on this operation.

### Usage for mutation.site.addSecondaryAwsVSocket:

```bash
catocli mutation site addSecondaryAwsVSocket -h

catocli mutation site addSecondaryAwsVSocket <json>

catocli mutation site addSecondaryAwsVSocket --json-file mutation.site.addSecondaryAwsVSocket.json

catocli mutation site addSecondaryAwsVSocket '{"addSecondaryAwsVSocketInput":{"eniIpAddress":"192.0.2.1","eniIpSubnet":"192.0.2.0/24","routeTableId":"string","site":{"by":"ID","input":"string"}}}'

catocli mutation site addSecondaryAwsVSocket '{
    "addSecondaryAwsVSocketInput": {
        "eniIpAddress": "192.0.2.1",
        "eniIpSubnet": "192.0.2.0/24",
        "routeTableId": "string",
        "site": {
            "by": "ID",
            "input": "string"
        }
    }
}'
```

#### Operation Arguments for mutation.site.addSecondaryAwsVSocket ####

`accountId` [ID] - (required) N/A
`addSecondaryAwsVSocketInput` [AddSecondaryAwsVSocketInput] - (required) N/A
