
## CATO-CLI - mutation.policy.dynamicIpAllocation.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveRule) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.moveRule:

`catocli mutation policy dynamicIpAllocation moveRule -h`

`catocli mutation policy dynamicIpAllocation moveRule <json>`

`catocli mutation policy dynamicIpAllocation moveRule "$(cat < moveRule.json)"`

`catocli mutation policy dynamicIpAllocation moveRule '{"dynamicIpAllocationPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyMoveRuleInput": {"id": {"id": "ID"}, "policyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}}}'`

#### Operation Arguments for mutation.policy.dynamicIpAllocation.moveRule ####
`accountId` [ID] - (required) N/A 
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (optional) N/A 
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A 
