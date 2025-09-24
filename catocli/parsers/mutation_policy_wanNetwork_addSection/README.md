
## CATO-CLI - mutation.policy.wanNetwork.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanNetwork.addSection) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.addSection:

`catocli mutation policy wanNetwork addSection -h`

`catocli mutation policy wanNetwork addSection <json>`

`catocli mutation policy wanNetwork addSection "$(cat < mutation.policy.wanNetwork.addSection.json)"`

`catocli mutation policy wanNetwork addSection '{"policyAddSectionInput":{"policyAddSectionInfoInput":{"name":"string"},"policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"wanNetworkPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanNetwork addSection -p '{
    "policyAddSectionInput": {
        "policyAddSectionInfoInput": {
            "name": "string"
        },
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    },
    "wanNetworkPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanNetwork.addSection ####

`accountId` [ID] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (required) N/A    
