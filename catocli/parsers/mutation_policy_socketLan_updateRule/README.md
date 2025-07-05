
## CATO-CLI - mutation.policy.socketLan.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateRule) for documentation on this operation.

### Usage for mutation.policy.socketLan.updateRule:

`catocli mutation policy socketLan updateRule -h`

`catocli mutation policy socketLan updateRule <json>`

`catocli mutation policy socketLan updateRule "$(cat < updateRule.json)"`

`catocli mutation policy socketLan updateRule '{"socketLanPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "socketLanUpdateRuleInput": {"id": {"id": "ID"}, "socketLanUpdateRuleDataInput": {"description": {"description": "String"}, "destination": {"floatingSubnet": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "globalIpRange": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "group": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "host": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "ip": {"ip": ["IPAddress"]}, "ipRange": {"from": {"from": "IPAddress"}, "to": {"to": "IPAddress"}}, "networkInterface": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "siteNetworkSubnet": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "subnet": {"subnet": ["NetworkSubnet"]}, "systemGroup": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "vlan": {"vlan": ["Vlan"]}}, "direction": {"direction": "enum(SocketLanDirection)"}, "enabled": {"enabled": "Boolean"}, "name": {"name": "String"}, "nat": {"enabled": {"enabled": "Boolean"}, "natType": {"natType": "enum(SocketLanNatType)"}}, "service": {"custom": {"port": {"port": ["Port"]}, "portRange": {"from": {"from": "Port"}, "to": {"to": "Port"}}, "protocol": {"protocol": "enum(IpProtocol)"}}, "simple": {"name": {"name": "enum(SimpleServiceType)"}}}, "site": {"group": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "site": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}, "source": {"floatingSubnet": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "globalIpRange": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "group": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "host": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "ip": {"ip": ["IPAddress"]}, "ipRange": {"from": {"from": "IPAddress"}, "to": {"to": "IPAddress"}}, "networkInterface": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "siteNetworkSubnet": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "subnet": {"subnet": ["NetworkSubnet"]}, "systemGroup": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "vlan": {"vlan": ["Vlan"]}}, "transport": {"transport": "enum(SocketLanTransportType)"}}}}'`

#### Operation Arguments for mutation.policy.socketLan.updateRule ####
`accountId` [ID] - (required) N/A 
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (optional) N/A 
`socketLanUpdateRuleInput` [SocketLanUpdateRuleInput] - (required) N/A 
