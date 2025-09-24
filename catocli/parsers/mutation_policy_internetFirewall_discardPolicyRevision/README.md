
## CATO-CLI - mutation.policy.internetFirewall.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.internetFirewall.discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.discardPolicyRevision:

`catocli mutation policy internetFirewall discardPolicyRevision -h`

`catocli mutation policy internetFirewall discardPolicyRevision <json>`

`catocli mutation policy internetFirewall discardPolicyRevision "$(cat < mutation.policy.internetFirewall.discardPolicyRevision.json)"`

`catocli mutation policy internetFirewall discardPolicyRevision '{"internetFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyDiscardRevisionInput":{"id":"id"}}'`

`catocli mutation policy internetFirewall discardPolicyRevision -p '{
    "internetFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyDiscardRevisionInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.internetFirewall.discardPolicyRevision ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (required) N/A    
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (required) N/A    
