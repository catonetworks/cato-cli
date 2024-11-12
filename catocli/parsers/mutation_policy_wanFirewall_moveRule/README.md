
## CATO-CLI - mutation.policy.wanFirewall.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveRule) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.moveRule:

`catocli mutation policy wanFirewall moveRule -h`

`catocli mutation policy wanFirewall moveRule <json>`

`catocli mutation policy wanFirewall moveRule "$(cat < moveRule.json)"`

`catocli mutation policy wanFirewall moveRule '{"policyMoveRuleInput": {"id": {"id": "ID"}, "policyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}}, "wanFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.moveRule ####
`accountId` [ID] - (required) N/A 
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A 
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
