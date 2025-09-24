
## CATO-CLI - mutation.policy.internetFirewall.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.internetFirewall.updatePolicy) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.updatePolicy:

`catocli mutation policy internetFirewall updatePolicy -h`

`catocli mutation policy internetFirewall updatePolicy <json>`

`catocli mutation policy internetFirewall updatePolicy "$(cat < mutation.policy.internetFirewall.updatePolicy.json)"`

`catocli mutation policy internetFirewall updatePolicy '{"internetFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"internetFirewallPolicyUpdateInput":{"state":"ENABLED"}}'`

`catocli mutation policy internetFirewall updatePolicy -p '{
    "internetFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "internetFirewallPolicyUpdateInput": {
        "state": "ENABLED"
    }
}'`


#### Operation Arguments for mutation.policy.internetFirewall.updatePolicy ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (required) N/A    
`internetFirewallPolicyUpdateInput` [InternetFirewallPolicyUpdateInput] - (required) N/A    
