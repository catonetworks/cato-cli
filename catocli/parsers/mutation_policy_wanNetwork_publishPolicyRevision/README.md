
## CATO-CLI - mutation.policy.wanNetwork.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanNetwork.publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.publishPolicyRevision:

`catocli mutation policy wanNetwork publishPolicyRevision -h`

`catocli mutation policy wanNetwork publishPolicyRevision <json>`

`catocli mutation policy wanNetwork publishPolicyRevision "$(cat < mutation.policy.wanNetwork.publishPolicyRevision.json)"`

`catocli mutation policy wanNetwork publishPolicyRevision '{"policyPublishRevisionInput":{"description":"string","name":"string"},"wanNetworkPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanNetwork publishPolicyRevision -p '{
    "policyPublishRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "wanNetworkPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanNetwork.publishPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (required) N/A    
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (required) N/A    
