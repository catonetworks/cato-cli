
## CATO-CLI - mutation.policy.dynamicIpAllocation.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.dynamicIpAllocation.moveSection) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.moveSection:

`catocli mutation policy dynamicIpAllocation moveSection -h`

`catocli mutation policy dynamicIpAllocation moveSection <json>`

`catocli mutation policy dynamicIpAllocation moveSection "$(cat < mutation.policy.dynamicIpAllocation.moveSection.json)"`

`catocli mutation policy dynamicIpAllocation moveSection '{"dynamicIpAllocationPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyMoveSectionInput":{"id":"id","policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}}}'`

`catocli mutation policy dynamicIpAllocation moveSection -p '{
    "dynamicIpAllocationPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyMoveSectionInput": {
        "id": "id",
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.dynamicIpAllocation.moveSection ####

`accountId` [ID] - (required) N/A    
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
