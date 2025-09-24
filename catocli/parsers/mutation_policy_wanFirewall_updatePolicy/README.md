
## CATO-CLI - mutation.policy.wanFirewall.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanFirewall.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.updatePolicy:

`catocli mutation policy wanFirewall updatePolicy -h`

`catocli mutation policy wanFirewall updatePolicy <json>`

`catocli mutation policy wanFirewall updatePolicy "$(cat < mutation.policy.wanFirewall.updatePolicy.json)"`

`catocli mutation policy wanFirewall updatePolicy '{"wanFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"wanFirewallPolicyUpdateInput":{"state":"ENABLED"}}'`

`catocli mutation policy wanFirewall updatePolicy -p '{
    "wanFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "wanFirewallPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'`


#### Operation Arguments for mutation.policy.wanFirewall.updatePolicy ####

`accountId` [ID] - (required) N/A    
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (required) N/A    
`wanFirewallPolicyUpdateInput` [WanFirewallPolicyUpdateInput] - (required) N/A    
