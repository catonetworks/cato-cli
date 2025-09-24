
## CATO-CLI - mutation.policy.dynamicIpAllocation.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.dynamicIpAllocation.addSection) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.addSection:

`catocli mutation policy dynamicIpAllocation addSection -h`

`catocli mutation policy dynamicIpAllocation addSection <json>`

`catocli mutation policy dynamicIpAllocation addSection "$(cat < mutation.policy.dynamicIpAllocation.addSection.json)"`

`catocli mutation policy dynamicIpAllocation addSection '{"dynamicIpAllocationPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyAddSectionInput":{"policyAddSectionInfoInput":{"name":"string"},"policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}}}'`

`catocli mutation policy dynamicIpAllocation addSection -p '{
    "dynamicIpAllocationPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyAddSectionInput": {
        "policyAddSectionInfoInput": {
            "name": "string"
        },
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.dynamicIpAllocation.addSection ####

`accountId` [ID] - (required) N/A    
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
