
## CATO-CLI - mutation.policy.wanNetwork.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanNetwork.createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.createPolicyRevision:

`catocli mutation policy wanNetwork createPolicyRevision -h`

`catocli mutation policy wanNetwork createPolicyRevision <json>`

`catocli mutation policy wanNetwork createPolicyRevision "$(cat < mutation.policy.wanNetwork.createPolicyRevision.json)"`

`catocli mutation policy wanNetwork createPolicyRevision '{"policyCreateRevisionInput":{"description":"string","name":"string"},"wanNetworkPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanNetwork createPolicyRevision -p '{
    "policyCreateRevisionInput": {
        "description": "string",
        "name": "string"
    },
    "wanNetworkPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanNetwork.createPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A    
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (required) N/A    
