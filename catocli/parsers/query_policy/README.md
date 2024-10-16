
## CATO-CLI - query.policy:
[Click here](https://api.catonetworks.com/documentation/#query-policy) for documentation on this operation.

### Usage for query.policy:

`catocli query policy -h`

`catocli query policy <json>`

`catocli query policy "$(cat < policy.json)"`

`catocli query policy '{"InternetFirewallPolicyInput": {"PolicyRevisionInput": {"id": {"id": "ID"}, "type": {"type": "enum(PolicyRevisionType)"}}}, "WanFirewallPolicyInput": {"PolicyRevisionInput": {"id": {"id": "ID"}, "type": {"type": "enum(PolicyRevisionType)"}}}}'`

#### Operation Arguments for query.policy ####
`InternetFirewallPolicyInput` [InternetFirewallPolicyInput] - (optional) N/A 
`WanFirewallPolicyInput` [WanFirewallPolicyInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
