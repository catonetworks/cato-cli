
## CATO-CLI - mutation.policy.wanNetwork.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanNetwork.moveSection) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.moveSection:

`catocli mutation policy wanNetwork moveSection -h`

`catocli mutation policy wanNetwork moveSection <json>`

`catocli mutation policy wanNetwork moveSection "$(cat < mutation.policy.wanNetwork.moveSection.json)"`

`catocli mutation policy wanNetwork moveSection '{"policyMoveSectionInput":{"id":"id","policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"wanNetworkPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanNetwork moveSection -p '{
    "policyMoveSectionInput": {
        "id": "id",
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


#### Operation Arguments for mutation.policy.wanNetwork.moveSection ####

`accountId` [ID] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (required) N/A    
