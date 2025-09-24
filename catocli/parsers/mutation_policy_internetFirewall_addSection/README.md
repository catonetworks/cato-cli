
## CATO-CLI - mutation.policy.internetFirewall.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.internetFirewall.addSection) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.addSection:

`catocli mutation policy internetFirewall addSection -h`

`catocli mutation policy internetFirewall addSection <json>`

`catocli mutation policy internetFirewall addSection "$(cat < mutation.policy.internetFirewall.addSection.json)"`

`catocli mutation policy internetFirewall addSection '{"internetFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyAddSectionInput":{"policyAddSectionInfoInput":{"name":"string"},"policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}}}'`

`catocli mutation policy internetFirewall addSection -p '{
    "internetFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyAddSectionInput": {
        "policyAddSectionInfoInput": {
            "name": "string"
        },
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.internetFirewall.addSection ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (required) N/A    
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A    
