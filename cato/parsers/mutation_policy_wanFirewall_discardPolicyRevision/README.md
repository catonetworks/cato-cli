
## CATO-CLI - mutation.policy.wanFirewall.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.discardPolicyRevision:

`cato mutation policy wanFirewall discardPolicyRevision -h`

`cato mutation policy wanFirewall discardPolicyRevision <accountID> <json>`

`cato mutation policy wanFirewall discardPolicyRevision 12345 "$(cat < discardPolicyRevision.json)"`

`cato mutation policy wanFirewall discardPolicyRevision 12345 '{"PolicyDiscardRevisionInput": {"id": {"id": "ID"}}, "WanFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.discardPolicyRevision ####
`PolicyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (optional) N/A 
`WanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
