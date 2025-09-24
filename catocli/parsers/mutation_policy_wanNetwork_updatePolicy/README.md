
## CATO-CLI - mutation.policy.wanNetwork.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanNetwork.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.updatePolicy:

`catocli mutation policy wanNetwork updatePolicy -h`

`catocli mutation policy wanNetwork updatePolicy <json>`

`catocli mutation policy wanNetwork updatePolicy "$(cat < mutation.policy.wanNetwork.updatePolicy.json)"`

`catocli mutation policy wanNetwork updatePolicy '{"wanNetworkPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"wanNetworkPolicyUpdateInput":{"state":"ENABLED"}}'`

`catocli mutation policy wanNetwork updatePolicy -p '{
    "wanNetworkPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "wanNetworkPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'`


#### Operation Arguments for mutation.policy.wanNetwork.updatePolicy ####

`accountId` [ID] - (required) N/A    
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (required) N/A    
`wanNetworkPolicyUpdateInput` [WanNetworkPolicyUpdateInput] - (required) N/A    
