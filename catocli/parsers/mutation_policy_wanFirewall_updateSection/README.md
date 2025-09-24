
## CATO-CLI - mutation.policy.wanFirewall.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanFirewall.updateSection) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.updateSection:

`catocli mutation policy wanFirewall updateSection -h`

`catocli mutation policy wanFirewall updateSection <json>`

`catocli mutation policy wanFirewall updateSection "$(cat < mutation.policy.wanFirewall.updateSection.json)"`

`catocli mutation policy wanFirewall updateSection '{"policyUpdateSectionInput":{"id":"id","policyUpdateSectionInfoInput":{"name":"string"}},"wanFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanFirewall updateSection -p '{
    "policyUpdateSectionInput": {
        "id": "id",
        "policyUpdateSectionInfoInput": {
            "name": "string"
        }
    },
    "wanFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanFirewall.updateSection ####

`accountId` [ID] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (required) N/A    
