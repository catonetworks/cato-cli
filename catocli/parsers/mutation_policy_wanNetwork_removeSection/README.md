
## CATO-CLI - mutation.policy.wanNetwork.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanNetwork.removeSection) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.removeSection:

`catocli mutation policy wanNetwork removeSection -h`

`catocli mutation policy wanNetwork removeSection <json>`

`catocli mutation policy wanNetwork removeSection "$(cat < mutation.policy.wanNetwork.removeSection.json)"`

`catocli mutation policy wanNetwork removeSection '{"policyRemoveSectionInput":{"id":"id"},"wanNetworkPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanNetwork removeSection -p '{
    "policyRemoveSectionInput": {
        "id": "id"
    },
    "wanNetworkPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanNetwork.removeSection ####

`accountId` [ID] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (required) N/A    
