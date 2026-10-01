
## CATO-CLI - mutation.site.updateSecondaryAwsVSocket:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.site.updateSecondaryAwsVSocket) for documentation on this operation.

### Usage for mutation.site.updateSecondaryAwsVSocket:

```bash
catocli mutation site updateSecondaryAwsVSocket -h

catocli mutation site updateSecondaryAwsVSocket <json>

catocli mutation site updateSecondaryAwsVSocket --json-file mutation.site.updateSecondaryAwsVSocket.json

catocli mutation site updateSecondaryAwsVSocket '{"updateSecondaryAwsVSocketInput":{"id":"id","ipAddress":"192.0.2.1","routeTableId":"string","subnet":"192.0.2.0/24"}}'

catocli mutation site updateSecondaryAwsVSocket '{
    "updateSecondaryAwsVSocketInput": {
        "id": "id",
        "ipAddress": "192.0.2.1",
        "routeTableId": "string",
        "subnet": "192.0.2.0/24"
    }
}'
```

#### Operation Arguments for mutation.site.updateSecondaryAwsVSocket ####

`accountId` [ID] - (required) N/A
`updateSecondaryAwsVSocketInput` [UpdateSecondaryAwsVSocketInput] - (required) N/A
