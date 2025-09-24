
## CATO-CLI - mutation.policy.internetFirewall.updateSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.internetFirewall.updateSection) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.updateSection:

`catocli mutation policy internetFirewall updateSection -h`

`catocli mutation policy internetFirewall updateSection <json>`

`catocli mutation policy internetFirewall updateSection "$(cat < mutation.policy.internetFirewall.updateSection.json)"`

`catocli mutation policy internetFirewall updateSection '{"internetFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyUpdateSectionInput":{"id":"id","policyUpdateSectionInfoInput":{"name":"string"}}}'`

`catocli mutation policy internetFirewall updateSection -p '{
    "internetFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyUpdateSectionInput": {
        "id": "id",
        "policyUpdateSectionInfoInput": {
            "name": "string"
        }
    }
}'`


#### Operation Arguments for mutation.policy.internetFirewall.updateSection ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (required) N/A    
`policyUpdateSectionInput` [PolicyUpdateSectionInput] - (required) N/A    
