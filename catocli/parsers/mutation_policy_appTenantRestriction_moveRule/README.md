
## CATO-CLI - mutation.policy.appTenantRestriction.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveRule) for documentation on this operation.

### Usage for mutation.policy.appTenantRestriction.moveRule:

`catocli mutation policy appTenantRestriction moveRule -h`

`catocli mutation policy appTenantRestriction moveRule <json>`

`catocli mutation policy appTenantRestriction moveRule "$(cat < moveRule.json)"`

`catocli mutation policy appTenantRestriction moveRule '{"appTenantRestrictionPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyMoveRuleInput": {"id": {"id": "ID"}, "policyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}}}'`

#### Operation Arguments for mutation.policy.appTenantRestriction.moveRule ####
`accountId` [ID] - (required) N/A 
`appTenantRestrictionPolicyMutationInput` [AppTenantRestrictionPolicyMutationInput] - (optional) N/A 
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A 
