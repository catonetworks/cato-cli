
## CATO-CLI - query.policy.wanFirewall.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.wanFirewall.policy) for documentation on this operation.

### Usage for query.policy.wanFirewall.policy:

`catocli query policy wanFirewall policy -h`

`catocli query policy wanFirewall policy <json>`

`catocli query policy wanFirewall policy "$(cat < query.policy.wanFirewall.policy.json)"`

`catocli query policy wanFirewall policy '{"wanFirewallPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'`

`catocli query policy wanFirewall policy -p '{
    "wanFirewallPolicyInput": {
        "policyRevisionInput": {
            "id": "id",
            "type": "PRIVATE"
        }
    }
}'`


#### Operation Arguments for query.policy.wanFirewall.policy ####

`accountId` [ID] - (required) N/A    
`wanFirewallPolicyInput` [WanFirewallPolicyInput] - (required) N/A    
