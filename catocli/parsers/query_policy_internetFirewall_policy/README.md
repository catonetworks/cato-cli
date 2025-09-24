
## CATO-CLI - query.policy.internetFirewall.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.internetFirewall.policy) for documentation on this operation.

### Usage for query.policy.internetFirewall.policy:

`catocli query policy internetFirewall policy -h`

`catocli query policy internetFirewall policy <json>`

`catocli query policy internetFirewall policy "$(cat < query.policy.internetFirewall.policy.json)"`

`catocli query policy internetFirewall policy '{"internetFirewallPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'`

`catocli query policy internetFirewall policy -p '{
    "internetFirewallPolicyInput": {
        "policyRevisionInput": {
            "id": "id",
            "type": "PRIVATE"
        }
    }
}'`


#### Operation Arguments for query.policy.internetFirewall.policy ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyInput` [InternetFirewallPolicyInput] - (required) N/A    
