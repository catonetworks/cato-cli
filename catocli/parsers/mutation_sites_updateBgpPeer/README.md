
## CATO-CLI - mutation.sites.updateBgpPeer:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateBgpPeer) for documentation on this operation.

### Usage for mutation.sites.updateBgpPeer:

`catocli mutation sites updateBgpPeer -h`

`catocli mutation sites updateBgpPeer <json>`

`catocli mutation sites updateBgpPeer "$(cat < updateBgpPeer.json)"`

`catocli mutation sites updateBgpPeer '{"updateBgpPeerInput": {"advertiseAllRoutes": {"advertiseAllRoutes": "Boolean"}, "advertiseDefaultRoute": {"advertiseDefaultRoute": "Boolean"}, "advertiseSummaryRoutes": {"advertiseSummaryRoutes": "Boolean"}, "bfdEnabled": {"bfdEnabled": "Boolean"}, "bfdSettingsInput": {"multiplier": {"multiplier": "Int"}, "receiveInterval": {"receiveInterval": "Int"}, "transmitInterval": {"transmitInterval": "Int"}}, "bgpSummaryRouteInput": {"community": {"from": {"from": "Asn16"}, "to": {"to": "Asn16"}}, "route": {"route": "NetworkSubnet"}}, "bgpTrackingInput": {"alertFrequency": {"alertFrequency": "enum(PolicyRuleTrackingFrequencyEnum)"}, "enabled": {"enabled": "Boolean"}, "subscriptionId": {"subscriptionId": "ID"}}, "catoAsn": {"catoAsn": "Asn16"}, "defaultAction": {"defaultAction": "enum(BgpDefaultAction)"}, "holdTime": {"holdTime": "Int"}, "id": {"id": "ID"}, "keepaliveInterval": {"keepaliveInterval": "Int"}, "md5AuthKey": {"md5AuthKey": "String"}, "metric": {"metric": "Int"}, "name": {"name": "String"}, "peerAsn": {"peerAsn": "Asn32"}, "peerIp": {"peerIp": "IPAddress"}, "performNat": {"performNat": "Boolean"}}}'`

#### Operation Arguments for mutation.sites.updateBgpPeer ####
`accountId` [ID] - (required) N/A 
`updateBgpPeerInput` [UpdateBgpPeerInput] - (required) N/A 
