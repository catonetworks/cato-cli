
## CATO-CLI - mutation.policy.wanNetwork.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanNetwork.removeRule) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.removeRule:

`catocli mutation policy wanNetwork removeRule -h`

`catocli mutation policy wanNetwork removeRule <json>`

`catocli mutation policy wanNetwork removeRule "$(cat < mutation.policy.wanNetwork.removeRule.json)"`

`catocli mutation policy wanNetwork removeRule '{"wanNetworkPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"wanNetworkRemoveRuleInput":{"id":"id"}}'`

`catocli mutation policy wanNetwork removeRule -p '{
    "wanNetworkPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "wanNetworkRemoveRuleInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.wanNetwork.removeRule ####

`accountId` [ID] - (required) N/A    
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (required) N/A    
`wanNetworkRemoveRuleInput` [WanNetworkRemoveRuleInput] - (required) N/A    
