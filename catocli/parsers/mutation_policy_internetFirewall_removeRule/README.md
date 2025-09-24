
## CATO-CLI - mutation.policy.internetFirewall.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.internetFirewall.removeRule) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.removeRule:

`catocli mutation policy internetFirewall removeRule -h`

`catocli mutation policy internetFirewall removeRule <json>`

`catocli mutation policy internetFirewall removeRule "$(cat < mutation.policy.internetFirewall.removeRule.json)"`

`catocli mutation policy internetFirewall removeRule '{"internetFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"internetFirewallRemoveRuleInput":{"id":"id"}}'`

`catocli mutation policy internetFirewall removeRule -p '{
    "internetFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "internetFirewallRemoveRuleInput": {
        "id": "id"
    }
}'`


#### Operation Arguments for mutation.policy.internetFirewall.removeRule ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (required) N/A    
`internetFirewallRemoveRuleInput` [InternetFirewallRemoveRuleInput] - (required) N/A    
