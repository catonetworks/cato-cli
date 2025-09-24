
## CATO-CLI - mutation.policy.wanNetwork.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanNetwork.updateSection) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.updateSection:

`catocli mutation policy wanNetwork updateSection -h`

`catocli mutation policy wanNetwork updateSection <json>`

`catocli mutation policy wanNetwork updateSection "$(cat < mutation.policy.wanNetwork.updateSection.json)"`

`catocli mutation policy wanNetwork updateSection '{"policyUpdateSectionInput":{"id":"id","policyUpdateSectionInfoInput":{"name":"string"}},"wanNetworkPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanNetwork updateSection -p '{
    "policyUpdateSectionInput": {
        "id": "id",
        "policyUpdateSectionInfoInput": {
            "name": "string"
        }
    },
    "wanNetworkPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanNetwork.updateSection ####

`accountId` [ID] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (required) N/A    
