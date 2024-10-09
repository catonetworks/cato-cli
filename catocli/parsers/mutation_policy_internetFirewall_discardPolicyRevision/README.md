
## CATO-CLI - mutation.policy.internetFirewall.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.discardPolicyRevision:

`catocli mutation policy internetFirewall discardPolicyRevision -h`

`catocli mutation policy internetFirewall discardPolicyRevision <accountID> <json>`

`catocli mutation policy internetFirewall discardPolicyRevision 12345 "$(cat < discardPolicyRevision.json)"`

`catocli mutation policy internetFirewall discardPolicyRevision 12345 '{"InternetFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}, "PolicyDiscardRevisionInput": {"id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.discardPolicyRevision ####
`InternetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`PolicyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 