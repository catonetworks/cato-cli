
## CATO-CLI - mutation.site.updateBgpPeer:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateBgpPeer) for documentation on this operation.

### Usage for mutation.site.updateBgpPeer:

`catocli mutation site updateBgpPeer -h`

`catocli mutation site updateBgpPeer <json>`

`catocli mutation site updateBgpPeer "$(cat < updateBgpPeer.json)"`

`catocli mutation site updateBgpPeer '{"updateBgpPeerInput": {"advertiseAllRoutes": {"advertiseAllRoutes": "Boolean"}, "advertiseDefaultRoute": {"advertiseDefaultRoute": "Boolean"}, "advertiseSummaryRoutes": {"advertiseSummaryRoutes": "Boolean"}, "bfdEnabled": {"bfdEnabled": "Boolean"}, "bfdSettingsInput": {"multiplier": {"multiplier": "Int"}, "receiveInterval": {"receiveInterval": "Int"}, "transmitInterval": {"transmitInterval": "Int"}}, "bgpSummaryRouteInput": {"community": {"from": {"from": "Asn16"}, "to": {"to": "Asn16"}}, "route": {"route": "NetworkSubnet"}}, "bgpTrackingInput": {"alertFrequency": {"alertFrequency": "enum(PolicyRuleTrackingFrequencyEnum)"}, "enabled": {"enabled": "Boolean"}, "subscriptionId": {"subscriptionId": "ID"}}, "catoAsn": {"catoAsn": "Asn16"}, "defaultAction": {"defaultAction": "enum(BgpDefaultAction)"}, "holdTime": {"holdTime": "Int"}, "id": {"id": "ID"}, "keepaliveInterval": {"keepaliveInterval": "Int"}, "md5AuthKey": {"md5AuthKey": "String"}, "metric": {"metric": "Int"}, "name": {"name": "String"}, "peerAsn": {"peerAsn": "Asn32"}, "peerIp": {"peerIp": "IPAddress"}, "performNat": {"performNat": "Boolean"}}}'`

#### Operation Arguments for mutation.site.updateBgpPeer ####
`accountId` [ID] - (required) N/A 
`updateBgpPeerInput` [UpdateBgpPeerInput] - (required) N/A 
