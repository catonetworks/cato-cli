
## CATO-CLI - mutation.policy.wanFirewall.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanFirewall.removeRule) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.removeRule:

`catocli mutation policy wanFirewall removeRule -h`

`catocli mutation policy wanFirewall removeRule <json>`

`catocli mutation policy wanFirewall removeRule "$(cat < mutation.policy.wanFirewall.removeRule.json)"`

`catocli mutation policy wanFirewall removeRule '{"wanFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"wanFirewallRemoveRuleInput":{"id":"id"}}'`

`catocli mutation policy wanFirewall removeRule -p '{
    "wanFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "wanFirewallRemoveRuleInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.wanFirewall.removeRule ####

`accountId` [ID] - (required) N/A    
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (required) N/A    
`wanFirewallRemoveRuleInput` [WanFirewallRemoveRuleInput] - (required) N/A    
