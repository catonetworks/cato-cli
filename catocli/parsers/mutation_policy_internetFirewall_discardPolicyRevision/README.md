
## CATO-CLI - mutation.policy.internetFirewall.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.discardPolicyRevision:

`catocli mutation policy internetFirewall discardPolicyRevision -h`

`catocli mutation policy internetFirewall discardPolicyRevision <json>`

`catocli mutation policy internetFirewall discardPolicyRevision "$(cat < discardPolicyRevision.json)"`

`catocli mutation policy internetFirewall discardPolicyRevision '{"internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyDiscardRevisionInput": {"id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.discardPolicyRevision ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (optional) N/A 
