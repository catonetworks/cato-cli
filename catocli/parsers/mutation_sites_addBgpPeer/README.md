
## CATO-CLI - mutation.sites.addBgpPeer:
[Click here](https://api.catonetworks.com/documentation/#mutation-addBgpPeer) for documentation on this operation.

### Usage for mutation.sites.addBgpPeer:

`catocli mutation sites addBgpPeer -h`

`catocli mutation sites addBgpPeer <json>`

`catocli mutation sites addBgpPeer "$(cat < addBgpPeer.json)"`

`catocli mutation sites addBgpPeer '{"addBgpPeerInput": {"advertiseAllRoutes": {"advertiseAllRoutes": "Boolean"}, "advertiseDefaultRoute": {"advertiseDefaultRoute": "Boolean"}, "advertiseSummaryRoutes": {"advertiseSummaryRoutes": "Boolean"}, "bfdEnabled": {"bfdEnabled": "Boolean"}, "bfdSettingsInput": {"multiplier": {"multiplier": "Int"}, "receiveInterval": {"receiveInterval": "Int"}, "transmitInterval": {"transmitInterval": "Int"}}, "bgpSummaryRouteInput": {"community": {"from": {"from": "Asn16"}, "to": {"to": "Asn16"}}, "route": {"route": "NetworkSubnet"}}, "bgpTrackingInput": {"alertFrequency": {"alertFrequency": "enum(PolicyRuleTrackingFrequencyEnum)"}, "enabled": {"enabled": "Boolean"}, "subscriptionId": {"subscriptionId": "ID"}}, "catoAsn": {"catoAsn": "Asn16"}, "defaultAction": {"defaultAction": "enum(BgpDefaultAction)"}, "holdTime": {"holdTime": "Int"}, "keepaliveInterval": {"keepaliveInterval": "Int"}, "md5AuthKey": {"md5AuthKey": "String"}, "metric": {"metric": "Int"}, "name": {"name": "String"}, "peerAsn": {"peerAsn": "Asn32"}, "peerIp": {"peerIp": "IPAddress"}, "performNat": {"performNat": "Boolean"}, "siteRefInput": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}}'`

#### Operation Arguments for mutation.sites.addBgpPeer ####
`accountId` [ID] - (required) N/A 
`addBgpPeerInput` [AddBgpPeerInput] - (required) N/A 
