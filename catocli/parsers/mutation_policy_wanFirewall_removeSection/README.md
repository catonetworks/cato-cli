
## CATO-CLI - mutation.policy.wanFirewall.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanFirewall.removeSection) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.removeSection:

`catocli mutation policy wanFirewall removeSection -h`

`catocli mutation policy wanFirewall removeSection <json>`

`catocli mutation policy wanFirewall removeSection "$(cat < mutation.policy.wanFirewall.removeSection.json)"`

`catocli mutation policy wanFirewall removeSection '{"policyRemoveSectionInput":{"id":"id"},"wanFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanFirewall removeSection -p '{
    "policyRemoveSectionInput": {
        "id": "id"
    },
    "wanFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanFirewall.removeSection ####

`accountId` [ID] - (required) N/A    
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A    
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (required) N/A    
