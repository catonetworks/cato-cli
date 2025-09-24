
## CATO-CLI - mutation.policy.wanNetwork.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanNetwork.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.discardPolicyRevision:

`catocli mutation policy wanNetwork discardPolicyRevision -h`

`catocli mutation policy wanNetwork discardPolicyRevision <json>`

`catocli mutation policy wanNetwork discardPolicyRevision "$(cat < mutation.policy.wanNetwork.discardPolicyRevision.json)"`

`catocli mutation policy wanNetwork discardPolicyRevision '{"policyDiscardRevisionInput":{"id":"id"},"wanNetworkPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanNetwork discardPolicyRevision -p '{
    "policyDiscardRevisionInput": {
        "id": "id"
    },
    "wanNetworkPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanNetwork.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (required) N/A    
