
## CATO-CLI - mutation.policy.wanNetwork.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-removeRule) for documentation on this operation.

### Usage for mutation.policy.wanNetwork.removeRule:

`catocli mutation policy wanNetwork removeRule -h`

`catocli mutation policy wanNetwork removeRule <json>`

`catocli mutation policy wanNetwork removeRule "$(cat < removeRule.json)"`

`catocli mutation policy wanNetwork removeRule '{"wanNetworkPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "wanNetworkRemoveRuleInput": {"id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.wanNetwork.removeRule ####
`accountId` [ID] - (required) N/A 
`wanNetworkPolicyMutationInput` [WanNetworkPolicyMutationInput] - (optional) N/A 
`wanNetworkRemoveRuleInput` [WanNetworkRemoveRuleInput] - (required) N/A 
