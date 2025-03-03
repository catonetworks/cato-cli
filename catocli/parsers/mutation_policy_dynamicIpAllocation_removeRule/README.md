
## CATO-CLI - mutation.policy.dynamicIpAllocation.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-removeRule) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.removeRule:

`catocli mutation policy dynamicIpAllocation removeRule -h`

`catocli mutation policy dynamicIpAllocation removeRule <json>`

`catocli mutation policy dynamicIpAllocation removeRule "$(cat < removeRule.json)"`

`catocli mutation policy dynamicIpAllocation removeRule '{"dynamicIpAllocationPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "dynamicIpAllocationRemoveRuleInput": {"id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.dynamicIpAllocation.removeRule ####
`accountId` [ID] - (required) N/A 
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (optional) N/A 
`dynamicIpAllocationRemoveRuleInput` [DynamicIpAllocationRemoveRuleInput] - (required) N/A 
