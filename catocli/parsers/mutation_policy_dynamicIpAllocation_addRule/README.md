
## CATO-CLI - mutation.policy.dynamicIpAllocation.addRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-addRule) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.addRule:

`catocli mutation policy dynamicIpAllocation addRule -h`

`catocli mutation policy dynamicIpAllocation addRule <json>`

`catocli mutation policy dynamicIpAllocation addRule "$(cat < addRule.json)"`

`catocli mutation policy dynamicIpAllocation addRule '{"dynamicIpAllocationAddRuleInput": {"dynamicIpAllocationAddRuleDataInput": {"country": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "description": {"description": "String"}, "enabled": {"enabled": "Boolean"}, "name": {"name": "String"}, "platform": {"platform": "enum(OperatingSystem)"}, "range": {"globalIpRange": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}, "source": {"user": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "usersGroup": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}}, "policyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}}, "dynamicIpAllocationPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.dynamicIpAllocation.addRule ####
`accountId` [ID] - (required) N/A 
`dynamicIpAllocationAddRuleInput` [DynamicIpAllocationAddRuleInput] - (required) N/A 
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (optional) N/A 
