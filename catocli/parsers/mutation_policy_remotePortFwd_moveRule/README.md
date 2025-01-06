
## CATO-CLI - mutation.policy.remotePortFwd.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveRule) for documentation on this operation.

### Usage for mutation.policy.remotePortFwd.moveRule:

`catocli mutation policy remotePortFwd moveRule -h`

`catocli mutation policy remotePortFwd moveRule <json>`

`catocli mutation policy remotePortFwd moveRule "$(cat < moveRule.json)"`

`catocli mutation policy remotePortFwd moveRule '{"policyMoveRuleInput": {"id": {"id": "ID"}, "policyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}}, "remotePortFwdPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.remotePortFwd.moveRule ####
`accountId` [ID] - (required) N/A 
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A 
`remotePortFwdPolicyMutationInput` [RemotePortFwdPolicyMutationInput] - (optional) N/A 
