
## CATO-CLI - mutation.policy.internetFirewall.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSection) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.addSection:

`catocli mutation policy internetFirewall addSection -h`

`catocli mutation policy internetFirewall addSection <json>`

`catocli mutation policy internetFirewall addSection "$(cat < addSection.json)"`

`catocli mutation policy internetFirewall addSection '{"internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyAddSectionInput": {"policyAddSectionInfoInput": {"name": {"name": "String"}}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.addSection ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A 
