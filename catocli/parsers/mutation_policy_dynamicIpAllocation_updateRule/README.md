
## CATO-CLI - mutation.policy.dynamicIpAllocation.updateRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateRule) for documentation on this operation.

### Usage for mutation.policy.dynamicIpAllocation.updateRule:

`catocli mutation policy dynamicIpAllocation updateRule -h`

`catocli mutation policy dynamicIpAllocation updateRule <json>`

`catocli mutation policy dynamicIpAllocation updateRule "$(cat < updateRule.json)"`

`catocli mutation policy dynamicIpAllocation updateRule '{"dynamicIpAllocationPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "dynamicIpAllocationUpdateRuleInput": {"dynamicIpAllocationUpdateRuleDataInput": {"country": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "description": {"description": "String"}, "enabled": {"enabled": "Boolean"}, "name": {"name": "String"}, "platform": {"platform": "enum(OperatingSystem)"}, "range": {"globalIpRange": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}, "source": {"user": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}, "usersGroup": {"by": {"by": "enum(ObjectRefBy)"}, "input": {"input": "String"}}}}, "id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.dynamicIpAllocation.updateRule ####
`accountId` [ID] - (required) N/A 
`dynamicIpAllocationPolicyMutationInput` [DynamicIpAllocationPolicyMutationInput] - (optional) N/A 
`dynamicIpAllocationUpdateRuleInput` [DynamicIpAllocationUpdateRuleInput] - (required) N/A 
