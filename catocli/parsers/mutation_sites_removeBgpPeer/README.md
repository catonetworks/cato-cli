
## CATO-CLI - mutation.sites.removeBgpPeer:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.sites.removeBgpPeer) for documentation on this operation.

### Usage for mutation.sites.removeBgpPeer:

```bash
catocli mutation sites removeBgpPeer -h

catocli mutation sites removeBgpPeer <json>

catocli mutation sites removeBgpPeer "$(cat < mutation.sites.removeBgpPeer.json)"

catocli mutation sites removeBgpPeer '{"removeBgpPeerInput":{"id":"id"}}'

catocli mutation sites removeBgpPeer '{
    "removeBgpPeerInput": {
        "id": "id"
    }
}'
```

#### Operation Arguments for mutation.sites.removeBgpPeer ####

`accountId` [ID] - (required) N/A    
`removeBgpPeerInput` [RemoveBgpPeerInput] - (required) N/A    
