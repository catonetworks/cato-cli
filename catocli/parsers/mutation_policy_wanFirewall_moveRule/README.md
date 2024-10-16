
## CATO-CLI - mutation.policy.wanFirewall.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveRule) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.moveRule:

`catocli mutation policy wanFirewall moveRule -h`

`catocli mutation policy wanFirewall moveRule <json>`

`catocli mutation policy wanFirewall moveRule "$(cat < moveRule.json)"`

`catocli mutation policy wanFirewall moveRule '{"PolicyMoveRuleInput": {"PolicyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}, "id": {"id": "ID"}}, "WanFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.moveRule ####
`PolicyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A 
`WanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
