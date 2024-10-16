
## CATO-CLI - mutation.policy.internetFirewall.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveRule) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.moveRule:

`catocli mutation policy internetFirewall moveRule -h`

`catocli mutation policy internetFirewall moveRule <json>`

`catocli mutation policy internetFirewall moveRule "$(cat < moveRule.json)"`

`catocli mutation policy internetFirewall moveRule '{"InternetFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}, "PolicyMoveRuleInput": {"PolicyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}, "id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.moveRule ####
`InternetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`PolicyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
