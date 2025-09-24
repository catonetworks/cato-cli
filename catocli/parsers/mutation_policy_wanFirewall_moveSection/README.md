
## CATO-CLI - mutation.policy.wanFirewall.moveSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-mutation.policy.wanFirewall.moveSection) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.moveSection:

`catocli mutation policy wanFirewall moveSection -h`

`catocli mutation policy wanFirewall moveSection <json>`

`catocli mutation policy wanFirewall moveSection "$(cat < mutation.policy.wanFirewall.moveSection.json)"`

`catocli mutation policy wanFirewall moveSection '{"policyMoveSectionInput":{"id":"id","policySectionPositionInput":{"position":"AFTER_SECTION","ref":"id"}},"wanFirewallPolicyMutationInput":{"policyMutationRevisionInput":{"id":"id"}}}'`

`catocli mutation policy wanFirewall moveSection -p '{
    "policyMoveSectionInput": {
        "id": "id",
        "policySectionPositionInput": {
            "position": "AFTER_SECTION",
            "ref": "id"
        }
    },
    "wanFirewallPolicyMutationInput": {
        "policyMutationRevisionInput": {
            "id": "id"
        }
    }
}'`


#### Operation Arguments for mutation.policy.wanFirewall.moveSection ####

`accountId` [ID] - (required) N/A    
`policyMoveSectionInput` [PolicyMoveSectionInput] - (required) N/A    
`wanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (required) N/A    
