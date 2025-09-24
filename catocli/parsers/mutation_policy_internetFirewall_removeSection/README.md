
## CATO-CLI - mutation.policy.internetFirewall.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.internetFirewall.removeSection) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.removeSection:

`catocli mutation policy internetFirewall removeSection -h`

`catocli mutation policy internetFirewall removeSection <json>`

`catocli mutation policy internetFirewall removeSection "$(cat < mutation.policy.internetFirewall.removeSection.json)"`

`catocli mutation policy internetFirewall removeSection '{"internetFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyRemoveSectionInput":{"id":"id"}}'`

`catocli mutation policy internetFirewall removeSection -p '{
    "internetFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyRemoveSectionInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.internetFirewall.removeSection ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
