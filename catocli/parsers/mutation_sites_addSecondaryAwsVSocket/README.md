
## CATO-CLI - mutation.sites.addSecondaryAwsVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.addSecondaryAwsVSocket) for documentation on this operation.

### Usage for mutation.sites.addSecondaryAwsVSocket:

```bash
catocli mutation sites addSecondaryAwsVSocket -h

catocli mutation sites addSecondaryAwsVSocket <json>

catocli mutation sites addSecondaryAwsVSocket --json-file mutation.sites.addSecondaryAwsVSocket.json

catocli mutation sites addSecondaryAwsVSocket '{"addSecondaryAwsVSocketInput":{"eniIpAddress":"192.0.2.1","eniIpSubnet":"192.0.2.0/24","routeTableId":"string","site":{"by":"ID","input":"string"}}}'

catocli mutation sites addSecondaryAwsVSocket '{
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

#### Operation Arguments for mutation.sites.addSecondaryAwsVSocket ####

`accountId` [ID] - (required) N/A
`addSecondaryAwsVSocketInput` [AddSecondaryAwsVSocketInput] - (required) N/A
