
## CATO-CLI - mutation.policy.socketLan.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveRule) for documentation on this operation.

### Usage for mutation.policy.socketLan.moveRule:

`catocli mutation policy socketLan moveRule -h`

`catocli mutation policy socketLan moveRule <json>`

`catocli mutation policy socketLan moveRule "$(cat < moveRule.json)"`

`catocli mutation policy socketLan moveRule '{"policyMoveRuleInput": {"id": {"id": "ID"}, "policyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}}, "socketLanPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.socketLan.moveRule ####
`accountId` [ID] - (required) N/A 
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A 
`socketLanPolicyMutationInput` [SocketLanPolicyMutationInput] - (optional) N/A 
