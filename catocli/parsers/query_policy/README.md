
## CATO-CLI - query.policy:
[Click here](https://api.catonetworks.com/documentation/#query-policy) for documentation on this operation.

### Usage for query.policy:

`catocli query policy -h`

`catocli query policy <json>`

`catocli query policy "$(cat < policy.json)"`

`catocli query policy '{"internetFirewallPolicyInput": {"policyRevisionInput": {"id": {"id": "ID"}, "type": {"type": "enum(PolicyRevisionType)"}}}, "wanFirewallPolicyInput": {"policyRevisionInput": {"id": {"id": "ID"}, "type": {"type": "enum(PolicyRevisionType)"}}}}'`

#### Operation Arguments for query.policy ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyInput` [InternetFirewallPolicyInput] - (optional) N/A 
`wanFirewallPolicyInput` [WanFirewallPolicyInput] - (optional) N/A 
