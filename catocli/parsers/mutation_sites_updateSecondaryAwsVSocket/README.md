
## CATO-CLI - mutation.sites.updateSecondaryAwsVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.updateSecondaryAwsVSocket) for documentation on this operation.

### Usage for mutation.sites.updateSecondaryAwsVSocket:

```bash
catocli mutation sites updateSecondaryAwsVSocket -h

catocli mutation sites updateSecondaryAwsVSocket <json>

catocli mutation sites updateSecondaryAwsVSocket --json-file mutation.sites.updateSecondaryAwsVSocket.json

catocli mutation sites updateSecondaryAwsVSocket '{"updateSecondaryAwsVSocketInput":{"id":"id","ipAddress":"192.0.2.1","routeTableId":"string","subnet":"192.0.2.0/24"}}'

catocli mutation sites updateSecondaryAwsVSocket '{
    "updateSecondaryAwsVSocketInput": {
        "id": "id",
        "ipAddress": "192.0.2.1",
        "routeTableId": "string",
        "subnet": "192.0.2.0/24"
    }
}'
```

#### Operation Arguments for mutation.sites.updateSecondaryAwsVSocket ####

`accountId` [ID] - (required) N/A
`updateSecondaryAwsVSocketInput` [UpdateSecondaryAwsVSocketInput] - (required) N/A
