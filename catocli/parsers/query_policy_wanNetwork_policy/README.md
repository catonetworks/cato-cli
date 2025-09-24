
## CATO-CLI - query.policy.wanNetwork.policy:
[Click here](https://api.catonetworks.com/documentation/#query-query.policy.wanNetwork.policy) for documentation on this operation.

### Usage for query.policy.wanNetwork.policy:

`catocli query policy wanNetwork policy -h`

`catocli query policy wanNetwork policy <json>`

`catocli query policy wanNetwork policy "$(cat < query.policy.wanNetwork.policy.json)"`

`catocli query policy wanNetwork policy '{"wanNetworkPolicyInput":{"policyRevisionInput":{"id":"id","type":"PRIVATE"}}}'`

`catocli query policy wanNetwork policy -p '{
    "wanNetworkPolicyInput": {
        "policyRevisionInput": {
            "id": "id",
            "type": "PRIVATE"
        }
    }
}'`


#### Operation Arguments for query.policy.wanNetwork.policy ####

`accountId` [ID] - (required) N/A    
`wanNetworkPolicyInput` [WanNetworkPolicyInput] - (required) N/A    
