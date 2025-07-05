
## CATO-CLI - mutation.policy.wanNetwork.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveRule) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.moveRule:

`catocli mutation policy wanNetwork moveRule -h`

`catocli mutation policy wanNetwork moveRule <json>`

`catocli mutation policy wanNetwork moveRule "$(cat < moveRule.json)"`

`catocli mutation policy wanNetwork moveRule '{"policyMoveRuleInput": {"id": {"id": "ID"}, "policyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}}, "wanNetworkPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanNetwork.moveRule ####
`accountId` [ID] - (required) N/A 
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A 
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (optional) N/A 
