
## CATO-CLI - mutation.policy.wanFirewall.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanFirewall.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.discardPolicyRevision:

`catocli mutation policy wanFirewall discardPolicyRevision -h`

`catocli mutation policy wanFirewall discardPolicyRevision <json>`

`catocli mutation policy wanFirewall discardPolicyRevision "$(cat < mutation.policy.wanFirewall.discardPolicyRevision.json)"`

`catocli mutation policy wanFirewall discardPolicyRevision '{"policyDiscardRevisionInput":{"id":"id"},"wanFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanFirewall discardPolicyRevision -p '{
    "policyDiscardRevisionInput": {
        "id": "id"
    },
    "wanFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanFirewall.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (required) N/A    
