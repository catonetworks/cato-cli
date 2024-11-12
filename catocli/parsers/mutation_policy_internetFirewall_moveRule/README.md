
## CATO-CLI - mutation.policy.internetFirewall.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveRule) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.moveRule:

`catocli mutation policy internetFirewall moveRule -h`

`catocli mutation policy internetFirewall moveRule <json>`

`catocli mutation policy internetFirewall moveRule "$(cat < moveRule.json)"`

`catocli mutation policy internetFirewall moveRule '{"internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyMoveRuleInput": {"id": {"id": "ID"}, "policyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.moveRule ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A 
