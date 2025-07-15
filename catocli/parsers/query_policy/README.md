
## CATO-CLI - query.policy:
[Click here](https://api.catonetworks.com/documentation/#query-policy) for documentation on this operation.

### Usage for query.policy:

`catocli query policy -h`

`catocli query policy <json>`

`catocli query policy "$(cat < policy.json)"`

`catocli query policy '{"appTenantRestrictionPolicyInput": {"policyRevisionInput": {"id": {"id": "ID"}, "type": {"type": "enum(PolicyRevisionType)"}}}, "dynamicIpAllocationPolicyInput": {"policyRevisionInput": {"id": {"id": "ID"}, "type": {"type": "enum(PolicyRevisionType)"}}}, "internetFirewallPolicyInput": {"policyRevisionInput": {"id": {"id": "ID"}, "type": {"type": "enum(PolicyRevisionType)"}}}, "remotePortFwdPolicyInput": {"policyRevisionInput": {"id": {"id": "ID"}, "type": {"type": "enum(PolicyRevisionType)"}}}, "socketLanPolicyInput": {"policyRevisionInput": {"id": {"id": "ID"}, "type": {"type": "enum(PolicyRevisionType)"}}}, "terminalServerPolicyInput": {"policyRevisionInput": {"id": {"id": "ID"}, "type": {"type": "enum(PolicyRevisionType)"}}}, "wanFirewallPolicyInput": {"policyRevisionInput": {"id": {"id": "ID"}, "type": {"type": "enum(PolicyRevisionType)"}}}, "wanNetworkPolicyInput": {"policyRevisionInput": {"id": {"id": "ID"}, "type": {"type": "enum(PolicyRevisionType)"}}}}'`

#### Operation Arguments for query.policy ####
`accountId` [ID] - (required) N/A 
`appTenantRestrictionPolicyInput` [AppTenantRestrictionPolicyInput] - (optional) N/A 
`dynamicIpAllocationPolicyInput` [DynamicIpAllocationPolicyInput] - (optional) N/A 
`internetFirewallPolicyInput` [InternetFirewallPolicyInput] - (optional) N/A 
`remotePortFwdPolicyInput` [RemotePortFwdPolicyInput] - (optional) N/A 
`socketLanPolicyInput` [SocketLanPolicyInput] - (optional) N/A 
`terminalServerPolicyInput` [TerminalServerPolicyInput] - (optional) N/A 
`wanFirewallPolicyInput` [WanFirewallPolicyInput] - (optional) N/A 
`wanNetworkPolicyInput` [WanNetworkPolicyInput] - (optional) N/A 
