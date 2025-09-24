
## CATO-CLI - mutation.policy.internetFirewall.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.internetFirewall.moveSection) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.moveSection:

`catocli mutation policy internetFirewall moveSection -h`

`catocli mutation policy internetFirewall moveSection <json>`

`catocli mutation policy internetFirewall moveSection "$(cat < mutation.policy.internetFirewall.moveSection.json)"`

`catocli mutation policy internetFirewall moveSection '{"internetFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}},"policyMoveSectionInput":{"id":"id","policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}}}'`

`catocli mutation policy internetFirewall moveSection -p '{
    "internetFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    },
    "policyMoveSectionInput": {
        "id": "id",
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.internetFirewall.moveSection ####

`accountId` [ID] - (required) N/A    
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
